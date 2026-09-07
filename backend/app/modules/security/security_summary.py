from app.modules.security.feature_policy_registry import (
    security_feature_policy_registry,
)
from app.modules.security.license_registry import (
    license_registry,
)
from app.modules.security.security_event_log import (
    security_event_log,
)
from app.modules.security.security_session_manager import (
    security_session_manager,
)


class SecuritySummary:

    def snapshot(self):
        return {
            "licenses": len(
                license_registry.list_all()
            ),
            "active_sessions": len(
                security_session_manager
                .active()
            ),
            "security_events": (
                security_event_log.size()
            ),
            "feature_policies": [
                policy.to_dict()
                for policy
                in security_feature_policy_registry
                .list_all()
            ],
        }


security_summary = (
    SecuritySummary()
)
