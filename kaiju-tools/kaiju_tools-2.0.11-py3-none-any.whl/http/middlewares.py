from aiohttp.web import middleware, json_response, Request
from aiohttp.web_exceptions import HTTPException

from kaiju_tools.exceptions import APIException
from kaiju_tools.serialization import dumps

__all__ = ['error_middleware']


@middleware
async def error_middleware(request: Request, handler):
    """Wrap an error in RPC exception."""
    try:
        response = await handler(request)
    except Exception as exc:
        request.app.logger.error('Request error.', exc_info=exc)
        if isinstance(exc, APIException):
            error = exc
        elif isinstance(exc, HTTPException):
            error = APIException(message=str(exc), base_exc=exc)
            error.status_code = exc.status
        else:
            error = APIException(message=str(exc), base_exc=exc)
        response = json_response({'jsonrpc': '2.0', 'id': None, 'error': error.repr()}, dumps=dumps)
    return response
