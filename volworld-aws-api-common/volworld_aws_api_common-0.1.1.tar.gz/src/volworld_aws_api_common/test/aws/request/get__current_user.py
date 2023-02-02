from src.volworld_aws_api_common.api.AA import AA
from src.volworld_aws_api_common.api.url import authUrl
from src.volworld_aws_api_common.test.aws.ATestRequest import ATestRequest
from src.volworld_aws_api_common.test.request import get_request


def get__current_user(
        req: ATestRequest,
        token: str = None):
    resp_json, resp = get_request(
        authUrl.currentUserUrl, req,
        token=token)

    data = None
    error = None

    if AA.___Error___ in resp_json.keys():
        error = resp_json[AA.___Error___]
    else:
        data = resp_json[AA.Data]

    return {
        AA.Data: data,
        AA.___Error___: error,
        AA.HttpStatus: resp.status_code,
        AA.Response: resp
    }
