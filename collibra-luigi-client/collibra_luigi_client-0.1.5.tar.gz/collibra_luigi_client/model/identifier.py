from model.community import Community
from model.domain import Domain


class Identifier:
    def __init__(self, name: str = None, domain: Domain = None, community: Community = None):
        self.name: str = name
        self.domain: Domain = domain
        self.community: Community = community
