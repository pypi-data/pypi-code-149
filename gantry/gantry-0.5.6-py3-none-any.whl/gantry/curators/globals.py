from gantry.exceptions import ClientNotInitialized


# circualr imports here, so need to figure out the typing...
# from typing import Optional
# from gantry.curators.curators import CuratorClient
# _CURATOR_CLIENT: Optional["CuratorClient"] = None


# api calls like like "list all curators" live on the curator client
_CURATOR_CLIENT = None

# instantions of curators don't need all of the curator client's methods
# but also need to be able to make api calls (and we don't want to initialize
# a new client for each curator)
_API_CLIENT = None


def validate_init():
    if _CURATOR_CLIENT is None:
        raise ClientNotInitialized()
