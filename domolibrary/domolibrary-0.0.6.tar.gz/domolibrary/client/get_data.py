# AUTOGENERATED! DO NOT EDIT! File to edit: ../../nbs/client/10_get_data.ipynb.

# %% auto 0
__all__ = ['get_data_aiohttp', 'get_data', 'LooperError', 'looper']

# %% ../../nbs/client/10_get_data.ipynb 2
from typing import Optional, Union

from pprint import pprint

import aiohttp
import httpx


import domolibrary.client.DomoAuth as dmda
import domolibrary.client.ResponseGetData as rgd


# %% ../../nbs/client/10_get_data.ipynb 3
async def get_data_aiohttp(
    url: str,
    method: str,
    auth: dmda.DomoAuth,
    content_type: Optional[dict] = None,
    headers: Optional[dict] = None,
    # if no session passed by default will create and close session during execution
    session: Optional[aiohttp.ClientSession] = None,
    body: Union[dict, str, None] = None,
    params: Optional[dict] = None,
    debug_api: bool = False,
    process_stream : bool = False,
    stream_chunks : int = 10
) -> rgd.ResponseGetData:
    """async wrapper for asyncio requests"""

    if auth and not auth.token:
        await auth.get_auth_token()

    if headers is None:
        headers = {}

    is_close_session = False
    if session is None:
        is_close_session = True
        session = session or aiohttp.ClientSession()

    headers = {
        "Content-Type": content_type or "application/json",
        "Connection": "keep-alive",
        "accept": "application/json, text/plain",
        **headers,
    }

    if auth:
        headers.update(**auth.auth_header)

    if debug_api:
        pprint(
            {
                "method": method,
                "url": url,
                "headers": headers,
                "json": body,
                "params": params,
            }
        )

    try:
        if headers.get("Content-Type") == "application/json":
            res = await session.request(
                method=method.upper(),
                url=url,
                headers=headers,
                json=body,
                params=params,
            )

        elif body is not None:
            res = await session.request(
                method=method.upper(),
                url=url,
                headers=headers,
                data=body,
                params=params,
            )

        else:
            res = await session.request(
                method=method.upper(), url=url, headers=headers, params=params
            )

    except Exception as e:
        print(e)

    finally:
        if is_close_session:
            await session.close()
    
    return await rgd.ResponseGetData._from_aiohttp_response(res, auth=auth, debug_api=debug_api, process_stream=process_stream, stream_chunks=stream_chunks)


# %% ../../nbs/client/10_get_data.ipynb 6
async def get_data(
    url: str,
    method: str,
    auth: dmda.DomoAuth,
    content_type: Optional[dict] = None,
    headers: Optional[dict] = None,
    body: Union[dict, str, None] = None,
    params: Optional[dict] = None,
    debug_api: bool = False,
    session : httpx.AsyncClient = None ,
    return_raw : bool = False
    ) -> rgd.ResponseGetData:
    """async wrapper for asyncio requests"""

    if debug_api:
        print( f"🐛 debugging get_data")

    if auth and not auth.token:
        await auth.get_auth_token()

    if headers is None:
        headers = {}

    headers = {
        "Content-Type": content_type or "application/json",
        "Connection": "keep-alive",
        "accept": "application/json, text/plain",
        **headers,
    }

    if auth:
        headers.update(**auth.auth_header)

    if debug_api:
        pprint(
            {
                "method": method,
                "url": url,
                "headers": headers,
                "body": body,
                "params": params,
            }
        )
    
    is_close_session = False if session else True
        
    session = session or httpx.AsyncClient()

    res = None
    try:
        if isinstance(body, dict) or isinstance(body, list):
            if debug_api:
                print("get_data: sending json")
            res = await getattr(session, method.lower())(url=url,
                                                 headers=headers,
                                                 json=body,
                                                 params=params)
        
        elif body:
            if debug_api:
                print("get_data: sending data")

            res = await getattr(session, method.lower())(url=url,
                                                 headers=headers,
                                                 data=body,
                                                 params=params)


        else:
            if debug_api:
                print("get_data: no body")

            res = await getattr(session, method.lower())(
                url=url, headers=headers, params=params)

    except Exception as e:
        print(e)

    finally:
        if debug_api:
            print('get_data_response', res)
        if is_close_session:
            await session.aclose()
    
    if return_raw:
        return res


    return rgd.ResponseGetData._from_httpx_response(res, auth=auth, debug_api=debug_api)


# %% ../../nbs/client/10_get_data.ipynb 8
class LooperError(Exception):
    def __init__(self, loop_stage: str, message ):

        super().__init__(f"{loop_stage} - {message}")

# %% ../../nbs/client/10_get_data.ipynb 9
async def looper(
    auth: dmda.DomoAuth,
    session: aiohttp.ClientSession,
    url,
    offset_params,
    arr_fn: callable,
    loop_until_end: bool = False,
    method="POST",
    body: dict = None,
    fixed_params: dict = None,
    offset_params_in_body: bool = False,
    body_fn=None,
    limit=1000,
    skip = 0,
    maximum=2000,
    debug_api: bool = False,
    debug_loop: bool = False
) -> rgd.ResponseGetData:

    is_close_session = False
    
    if not session:
        session = aiohttp.ClientSession()
        is_close_session = True


    allRows = []
    isLoop = True

    res = None

    if maximum < limit:
        limit = maximum

    while isLoop:
        params = fixed_params or {}

        if offset_params_in_body:
            body[offset_params.get("offset")] = skip
            body[offset_params.get("limit")] = limit

        else:
            params[offset_params.get("offset")] = skip
            params[offset_params.get("limit")] = limit

        if body_fn:
            try:
                body = body_fn(skip, limit)
            
            except Exception as e:
                await session.close()
                raise LooperError(loop_stage = "processing body_fn", message = str(e))
            

        if debug_loop:
            print(
                f"\n🚀 Retrieving records {skip} through {skip + limit} via {url}")
            # pprint(params)

        
        res = await get_data_aiohttp(
            auth=auth,
            url=url,
            method=method,
            params=params,
            session=session,
            body=body,
            debug_api=debug_api,
        )

        if not res.is_success:
            if is_close_session:
                await session.close()
            return res


        try:
            newRecords = arr_fn(res)
        
        except Exception as e:
            await session.close()
            raise LooperError(loop_stage = "processing arr_fn", message = str(e))
        
        allRows += newRecords

        if loop_until_end and len(newRecords) != 0:
            maximum = maximum + limit

        if debug_loop:
            print({"all_rows": len(allRows), "new_records": len(newRecords)})

        if len(allRows) >= maximum or len(newRecords) == 0:
            if debug_loop:
                print(
                    f"\n🎉 Success - {len(allRows)} records retrieved from {url} in query looper\n")

            break

        skip += len(newRecords)
        
        if skip + limit > maximum:
            limit = maximum - len(allRows)

            if debug_loop:
                print(f"skip: {skip}, limit: {limit}")
    
    if is_close_session:
        await session.close()

    return await rgd.ResponseGetData._from_looper(res = res, array = allRows)
