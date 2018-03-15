class Region:
    """
    --------
    Region
    --------
    """

    def __init__(self, name: str, package_number: int, cost: float, service: dict):
        self.name = name
        self.package_number = package_number
        self.cost = cost
        self.service = service


class Provider:
    """
    -----------------
    Provider
    -----------------
    """

    def __init__(self, name: str):
        self.name = name
        self.region = dict()

    def add_region(self, region_name: str, region: Region):
        self.region[region_name] = region
