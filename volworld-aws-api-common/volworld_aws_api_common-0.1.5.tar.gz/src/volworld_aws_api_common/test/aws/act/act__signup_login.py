from api.AA import AA
from volworld_aws_api_common.api.enum.HttpStatus import HttpStatus
from volworld_aws_api_common.test.aws.request.post__login import post__login
from volworld_aws_api_common.test.aws.act.act__signup import act__signup
from volworld_aws_api_common.test.aws.ATestRequest import ATestRequest


def act__signup_login(name: str = None, pw: str = None) -> dict:
    signup = act__signup(name, pw)
    req = ATestRequest(True)
    resp = post__login(signup[AA.Name], signup[AA.Password], req)
    assert resp[AA.HttpStatus] == HttpStatus.Ok_200
    return {
        AA.Name: signup[AA.Name],
        AA.Password: signup[AA.Password],
        AA.UserId: signup[AA.UserId],
        AA.Token: resp[AA.Data][AA.Token]
    }
