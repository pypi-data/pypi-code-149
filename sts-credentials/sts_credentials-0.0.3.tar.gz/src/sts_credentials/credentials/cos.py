from pydantic import BaseModel
from sts.sts import Sts

# https://pypi.org/project/qcloud-python-sts/
# https://www.npmjs.com/package/cos-js-sdk-v5


class CosCredentials(BaseModel):
    sessionToken: str
    tmpSecretId: str
    tmpSecretKey: str
    domain: str
    bucket: str
    region: str
    endpoint: str


class CosStsModel(BaseModel):
    expiredTime: int
    expiration: str
    credentials: CosCredentials
    requestId: str
    startTime: int


def get_credential_cos(
    bucket: str,
    region: str,  # https://cloud.tencent.com/document/product/436/6224
    secret_id: str,
    secret_key: str,
    duration_seconds: int = 1800,
):
    config = {
        "url": "https://sts.tencentcloudapi.com/",
        # 域名，非必须，默认为 sts.tencentcloudapi.com
        "domain": "sts.tencentcloudapi.com",
        # 临时密钥有效时长，单位是秒
        "duration_seconds": duration_seconds,
        "secret_id": secret_id,
        # 固定密钥
        "secret_key": secret_key,
        # 换成你的 bucket
        "bucket": bucket,
        # 换成 bucket 所在地区
        "region": region,
        # 这里改成允许的路径前缀，可以根据自己网站的用户登录态判断允许上传的具体路径
        # 例子： a.jpg 或者 a/* 或者 * (使用通配符*存在重大安全风险, 请谨慎评估使用)
        "allow_prefix": "*",
        # 密钥的权限列表。简单上传和分片需要以下的权限，其他权限列表请看 https://cloud.tencent.com/document/product/436/31923
        "allow_actions": [
            # 简单上传
            "name/cos:PutObject",
            "name/cos:PostObject",
            # 分片上传
            "name/cos:InitiateMultipartUpload",
            "name/cos:ListMultipartUploads",
            "name/cos:ListParts",
            "name/cos:UploadPart",
            "name/cos:CompleteMultipartUpload",
        ],
    }

    sts = Sts(config)
    data = sts.get_credential()
    data["credentials"]["bucket"] = bucket
    data["credentials"]["region"] = region
    data["credentials"]["domain"] = f"{bucket}.cos.{region}.myqcloud.com"
    data["credentials"]["endpoint"] = f"cos.{region}.myqcloud.com"

    response = CosStsModel.parse_obj(data)
    return response
