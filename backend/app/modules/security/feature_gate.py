class SecurityFeatureGate:

    def allows(
        self,
        feature: str,
        licensed_features: set[str],
    ):
        if "*" in licensed_features:
            return True

        return (
            feature
            in licensed_features
        )


security_feature_gate = (
    SecurityFeatureGate()
)
