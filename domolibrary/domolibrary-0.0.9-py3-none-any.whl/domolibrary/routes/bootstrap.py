# AUTOGENERATED! DO NOT EDIT! File to edit: ../../nbs/routes/bootstrap.ipynb.

# %% auto 0
__all__ = ['GetBootstrap_InvalidAuthMethod', 'get_bootstrap', 'get_bootstrap_features', 'get_bootstrap_pages']

# %% ../../nbs/routes/bootstrap.ipynb 3
import httpx

import domolibrary.client.get_data as gd
import domolibrary.client.ResponseGetData as rgd
import domolibrary.client.DomoAuth as dmda

# %% ../../nbs/routes/bootstrap.ipynb 4
class GetBootstrap_InvalidAuthMethod(Exception):
    def __init__(self, domo_instance):
        message = f"invalid auth method sent to {domo_instance} bootstrap API, use DomoFullAuth (username and password) authentication"
        super().__init__(message)

async def get_bootstrap(
    auth: dmda.DomoFullAuth, ## only works with DomoFullAuth authentication, do not use TokenAuth
    debug_api: bool = False, session: httpx.AsyncClient = None
) -> rgd.ResponseGetData:
    """get bootstrap data"""

    # url = f"https://{auth.domo_instance}.domo.com/api/domoweb/bootstrap?v2Navigation=false"
    url = f"https://{auth.domo_instance}.domo.com/api/domoweb/bootstrap?v2Navigation=true"

    res = await gd.get_data(
        url=url, method="GET", auth=auth, debug_api=debug_api, session=session
    )

    if res.status == 302:
        raise GetBootstrap_InvalidAuthMethod(auth.domo_instance)

    return res


# %% ../../nbs/routes/bootstrap.ipynb 8
async def get_bootstrap_features(   
    auth: dmda.DomoAuth, session: httpx.AsyncClient = None, debug_api: bool = False
) -> rgd.ResponseGetData:
    res = await get_bootstrap(auth=auth, session=session, debug_api=debug_api)

    if not res.is_success:
        return None

    res.response = res.response.get("data").get("features")
    return res

# %% ../../nbs/routes/bootstrap.ipynb 11
async def get_bootstrap_pages(
    auth: dmda.DomoAuth, session: httpx.AsyncClient = None, debug_api: bool = False
) -> rgd.ResponseGetData:
    res = await get_bootstrap(auth=auth, session=session, debug_api=debug_api)

    if not res.is_success:
        return None

    res.response = res.response.get("data").get("pages")
    return res

