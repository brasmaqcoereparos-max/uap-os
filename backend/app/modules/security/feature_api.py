from fastapi import APIRouter

from app.modules.security.feature_defaults import (
    install_default_security_features,
)
from app.modules.security.feature_policy_registry import (
    security_feature_policy_registry,
)


router = APIRouter()


@router.get("/features")
def features():
    install_default_security_features()

    return [
        policy.to_dict()
        for policy
        in security_feature_policy_registry
        .list_all()
    ]
