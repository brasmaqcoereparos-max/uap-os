from dataclasses import dataclass


@dataclass
class RuntimeSecurityPolicy:
    require_valid_license: bool = True

    block_on_tamper: bool = True

    audit_denials: bool = True

    audit_success: bool = False

    def to_dict(self):
        return {
            "require_valid_license": (
                self.require_valid_license
            ),
            "block_on_tamper": (
                self.block_on_tamper
            ),
            "audit_denials": (
                self.audit_denials
            ),
            "audit_success": (
                self.audit_success
            ),
        }


runtime_security_policy = (
    RuntimeSecurityPolicy()
)
