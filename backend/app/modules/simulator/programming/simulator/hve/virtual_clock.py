"""
Relógio virtual do Hardware Virtual Engine (HVE).

O VirtualClock representa tempo lógico determinístico dentro
do mundo virtual do UAP.

O contrato original é preservado:

    clock.tick
    clock.next()
    clock.reset()

Além do contador simples, agora suporta:
- passos configuráveis;
- tempo virtual;
- pause/resume;
- escala temporal;
- limites opcionais;
- snapshots;
- restauração de estado.
"""


class VirtualClock:

    def __init__(
        self,
        tick=0,
        step=1,
        tick_duration=1.0,
        time_scale=1.0,
    ):
        self.tick = int(tick)

        self.step = max(
            1,
            int(step),
        )

        self.tick_duration = max(
            0.0,
            float(tick_duration),
        )

        self.time_scale = max(
            0.0,
            float(time_scale),
        )

        self.enabled = True
        self.paused = False

        self.max_tick = None

        self.advance_count = 0

    def next(
        self,
        steps=None,
    ):
        if (
            not self.enabled
            or self.paused
        ):
            return self.tick

        amount = (
            self.step
            if steps is None
            else max(
                0,
                int(steps),
            )
        )

        target = (
            self.tick
            + amount
        )

        if self.max_tick is not None:
            target = min(
                target,
                self.max_tick,
            )

        delta = (
            target
            - self.tick
        )

        self.tick = target

        if delta > 0:
            self.advance_count += 1

        return self.tick

    def advance(
        self,
        steps=1,
    ):
        return self.next(
            steps
        )

    def reset(self):
        self.tick = 0

        self.paused = False

        self.advance_count = 0

        return self.tick

    def set(
        self,
        tick,
    ):
        tick = max(
            0,
            int(tick),
        )

        if self.max_tick is not None:
            tick = min(
                tick,
                self.max_tick,
            )

        self.tick = tick

        return self.tick

    def set_step(
        self,
        step,
    ):
        self.step = max(
            1,
            int(step),
        )

        return self.step

    def set_tick_duration(
        self,
        duration,
    ):
        duration = float(
            duration
        )

        if duration < 0:
            raise ValueError(
                "tick_duration não pode "
                "ser negativo."
            )

        self.tick_duration = duration

        return self.tick_duration

    def set_time_scale(
        self,
        scale,
    ):
        scale = float(
            scale
        )

        if scale < 0:
            raise ValueError(
                "time_scale não pode "
                "ser negativo."
            )

        self.time_scale = scale

        return self.time_scale

    def set_max_tick(
        self,
        max_tick=None,
    ):
        if max_tick is None:
            self.max_tick = None

            return None

        self.max_tick = max(
            0,
            int(max_tick),
        )

        if self.tick > self.max_tick:
            self.tick = self.max_tick

        return self.max_tick

    def pause(self):
        self.paused = True

        return True

    def resume(self):
        self.paused = False

        return True

    def enable(self):
        self.enabled = True

        return True

    def disable(self):
        self.enabled = False

        return True

    def is_paused(self):
        return self.paused

    def is_enabled(self):
        return self.enabled

    def time(self):
        return (
            self.tick
            * self.tick_duration
            * self.time_scale
        )

    def milliseconds(self):
        return (
            self.time()
            * 1000.0
        )

    def snapshot(self):
        return {
            "tick": self.tick,
            "step": self.step,
            "tick_duration": (
                self.tick_duration
            ),
            "time_scale": (
                self.time_scale
            ),
            "enabled": self.enabled,
            "paused": self.paused,
            "max_tick": self.max_tick,
            "advance_count": (
                self.advance_count
            ),
        }

    def restore(
        self,
        snapshot,
    ):
        if not isinstance(
            snapshot,
            dict,
        ):
            raise TypeError(
                "Snapshot do relógio "
                "precisa ser um dicionário."
            )

        self.tick = max(
            0,
            int(
                snapshot.get(
                    "tick",
                    0,
                )
            ),
        )

        self.step = max(
            1,
            int(
                snapshot.get(
                    "step",
                    1,
                )
            ),
        )

        self.tick_duration = max(
            0.0,
            float(
                snapshot.get(
                    "tick_duration",
                    1.0,
                )
            ),
        )

        self.time_scale = max(
            0.0,
            float(
                snapshot.get(
                    "time_scale",
                    1.0,
                )
            ),
        )

        self.enabled = bool(
            snapshot.get(
                "enabled",
                True,
            )
        )

        self.paused = bool(
            snapshot.get(
                "paused",
                False,
            )
        )

        self.max_tick = (
            snapshot.get(
                "max_tick"
            )
        )

        self.advance_count = max(
            0,
            int(
                snapshot.get(
                    "advance_count",
                    0,
                )
            ),
        )

        return self.tick

    def status(self):
        return {
            **self.snapshot(),
            "time": self.time(),
            "milliseconds": (
                self.milliseconds()
            ),
        }

    def to_dict(self):
        return self.status()


virtual_clock = VirtualClock()
