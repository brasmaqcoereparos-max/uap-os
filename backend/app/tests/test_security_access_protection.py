from app.modules.security.lockout_manager import (
    security_lockout_manager,
)
from app.modules.security.rate_limiter import (
    security_rate_limiter,
)
from app.modules.security.security_access_protection_service import (
    security_access_protection_service,
)


def test_access_allowed_initially():
    principal = (
        "security-test-user"
    )

    security_lockout_manager.clear(
        principal
    )

    security_rate_limiter.reset(
        principal
    )

    result = (
        security_access_protection_service
        .check(
            principal_id=principal
        )
    )

    assert (
        result["allowed"]
        is True
    )


def test_lockout_after_failures():
    principal = (
        "security-lockout-user"
    )

    security_lockout_manager.clear(
        principal
    )

    for _ in range(5):
        security_access_protection_service.record_login(
            principal_id=principal,
            success=False,
        )

    assert (
        security_lockout_manager
        .is_locked(
            principal
        )
        is True
    )


def test_successful_login_clears_lockout():
    principal = (
        "security-clear-user"
    )

    security_lockout_manager.clear(
        principal
    )

    for _ in range(5):
        security_access_protection_service.record_login(
            principal_id=principal,
            success=False,
        )

    result = (
        security_access_protection_service
        .record_login(
            principal_id=principal,
            success=True,
        )
    )

    assert (
        result["locked"]
        is False
    )
