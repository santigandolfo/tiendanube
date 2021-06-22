class ShippingOptions:
    def __init__(self, options) -> None:
        self.options = options

    def getSortedOptions(self):
        return sorted(self.options, key=lambda x: (x["cost"], x["estimated_days"]))
