from src.volworld_aws_api_common.api.AA import AA
from src.volworld_aws_api_common.api.url import authUrl
from src.volworld_aws_api_common.test.aws.ATestRequest import ATestRequest
from src.volworld_aws_api_common.test.request import post_request


def post__login(
        name: str, pw: str,
        req: ATestRequest,
        # status_code: int = -1
):
    resp_json, resp = post_request(
        authUrl.doLoginUrl, {
            AA.Name: name,
            AA.Password: pw,
        }, req,
    )

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
