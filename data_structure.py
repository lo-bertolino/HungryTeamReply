services = list()
countries = list()
providers = list()


class Region:
    """
    --------
    Region
    --------
    """

    def __init__(self, name: str, package_number: int, cost: float, service: list, latency: list):
        self.name = name
        self.package_number = package_number
        self.cost = cost
        self.service = service
        self.latency = latency


class Provider:
    """
    -----------------
    Provider
    -----------------
    """

    def __init__(self, name: str):
        self.name = name
        self.region = list()

    def add_region(self, region: Region):
        self.region.append(region)
