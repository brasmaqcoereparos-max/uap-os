class DeviceLogic:

    def equals(
        self,
        value,
        expected,
    ):

        return value == expected

    def greater(
        self,
        value,
        limit,
    ):

        return value > limit

    def less(
        self,
        value,
        limit,
    ):

        return value < limit

    def greater_or_equal(
        self,
        value,
        limit,
    ):

        return value >= limit

    def less_or_equal(
        self,
        value,
        limit,
    ):

        return value <= limit

    def and_(
        self,
        *values,
    ):

        return all(values)

    def or_(
        self,
        *values,
    ):

        return any(values)

    def not_(
        self,
        value,
    ):

        return not value


device_logic = DeviceLogic()
