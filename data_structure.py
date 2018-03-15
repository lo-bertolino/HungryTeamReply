services = list()
countries = list()
providers = list()
projects = list()

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


class Project:
    def __init__(self, penalty: int, county: str, services_project: list):
        self.penalty = penalty
        self.county = county
        self.services = services_project
