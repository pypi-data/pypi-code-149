
from volworld_aws_api_common.api.AA import AA
from volworld_aws_api_common.api.enum.HttpStatus import HttpStatus
from volworld_aws_api_common.test.aws.request.post__signup import post__signup
from volworld_aws_api_common.test.aws.ATestRequest import ATestRequest
from volworld_common.util.id_util import new_rand_test_user_name


def act__signup(name: str = None, pw: str = None) -> dict:
    if name is None:
        name = new_rand_test_user_name()
    if pw is None:
        pw = 'password'
    req = ATestRequest(True)
    resp = post__signup(name, pw, req)
    assert resp[AA.HttpStatus] == HttpStatus.Created_201
    uid: str = resp[AA.Data][AA.UserId]
    return {
        AA.Name: name,
        AA.Password: pw,
        AA.UserId: uid
    }
