"""
Dispositivo Wi-Fi simulado do UAP.
"""

import ipaddress

from app.modules.simulator.programming.simulator.device.device_base import (
    DeviceBase,
)


class WiFiDevice(DeviceBase):

    def __init__(
        self,
        name,
    ):
        super().__init__(
            name=name,
            category="communication",
            description="Interface Wi-Fi simulada",
            icon="wifi",
        )

        self.connected = False

        self.ssid = None
        self.ip = None
        self.gateway = None
        self.dns = None

        self.signal_strength = None
        self.channel = None

        self.available_networks = []

        self.connection_count = 0
        self.last_error = None

    def scan(self):
        return [
            dict(network)
            for network
            in self.available_networks
        ]

    def add_network(
        self,
        ssid,
        signal_strength=-50,
        channel=None,
        secure=True,
    ):
        network = {
            "ssid": str(ssid),
            "signal_strength": int(
                signal_strength
            ),
            "channel": (
                int(channel)
                if channel is not None
                else None
            ),
            "secure": bool(secure),
        }

        self.available_networks = [
            item
            for item
            in self.available_networks
            if item.get("ssid")
            != network["ssid"]
        ]

        self.available_networks.append(
            network
        )

        return network

    def remove_network(
        self,
        ssid,
    ):
        ssid = str(ssid)

        before = len(
            self.available_networks
        )

        self.available_networks = [
            item
            for item
            in self.available_networks
            if item.get("ssid") != ssid
        ]

        return (
            len(self.available_networks)
            != before
        )

    def connect(
        self,
        ssid,
        ip=None,
        gateway=None,
        dns=None,
    ):
        if not self.enabled:
            self.last_error = (
                "device_disabled"
            )

            return False

        ssid = str(
            ssid or ""
        ).strip()

        if not ssid:
            self.last_error = (
                "ssid_required"
            )

            return False

        if ip is not None:
            self._validate_ip(ip)

        if gateway is not None:
            self._validate_ip(
                gateway
            )

        if dns is not None:
            self._validate_ip(dns)

        self.ssid = ssid

        self.ip = (
            str(ip)
            if ip is not None
            else "192.168.1.100"
        )

        self.gateway = (
            str(gateway)
            if gateway is not None
            else None
        )

        self.dns = (
            str(dns)
            if dns is not None
            else None
        )

        network = self._find_network(
            ssid
        )

        if network is not None:
            self.signal_strength = (
                network.get(
                    "signal_strength"
                )
            )

            self.channel = (
                network.get(
                    "channel"
                )
            )

        self.connected = True
        self.connection_count += 1
        self.last_error = None

        return True

    def disconnect(self):
        self.connected = False

        self.ssid = None
        self.ip = None
        self.gateway = None
        self.dns = None

        self.signal_strength = None
        self.channel = None

        return True

    def is_connected(self):
        return self.connected

    def set_signal_strength(
        self,
        strength,
    ):
        strength = int(strength)

        strength = max(
            -120,
            min(
                0,
                strength,
            ),
        )

        self.signal_strength = (
            strength
        )

        return strength

    def status(self):
        return {
            "connected": (
                self.connected
            ),
            "ssid": self.ssid,
            "ip": self.ip,
            "gateway": (
                self.gateway
            ),
            "dns": self.dns,
            "signal_strength": (
                self.signal_strength
            ),
            "channel": self.channel,
            "last_error": (
                self.last_error
            ),
        }

    def update(self):
        return self.status()

    def reset(self):
        self.disconnect()

        self.connection_count = 0
        self.last_error = None

        return True

    def _find_network(
        self,
        ssid,
    ):
        for network in (
            self.available_networks
        ):
            if (
                network.get("ssid")
                == str(ssid)
            ):
                return network

        return None

    @staticmethod
    def _validate_ip(value):
        try:
            ipaddress.ip_address(
                str(value)
            )

        except ValueError as exc:
            raise ValueError(
                f"Endereço IP inválido: {value}"
            ) from exc

        return True

    def to_dict(self):
        data = super().to_dict()

        data.update({
            "connected": (
                self.connected
            ),
            "ssid": self.ssid,
            "ip": self.ip,
            "gateway": (
                self.gateway
            ),
            "dns": self.dns,
            "signal_strength": (
                self.signal_strength
            ),
            "channel": self.channel,
            "available_networks": (
                self.scan()
            ),
            "connection_count": (
                self.connection_count
            ),
            "last_error": (
                self.last_error
            ),
        })

        return data
