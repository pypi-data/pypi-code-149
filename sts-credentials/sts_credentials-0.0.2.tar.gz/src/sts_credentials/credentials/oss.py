import json
from alibabacloud_sts20150401.client import Client as StsClient
from alibabacloud_sts20150401.models import AssumeRoleRequest
from alibabacloud_tea_openapi.models import Config as ClientConfig
from pydantic import BaseModel

# https://pypi.org/project/alibabacloud-sts20150401/
# https://www.npmjs.com/package/ali-oss


class OssCredentials(BaseModel):
    AccessKeyId: str
    AccessKeySecret: str
    SecurityToken: str
    Expiration: str
    Domain: str
    Bucket: str
    Region: str
    Endpoint: str


def get_credential_oss(
    bucket: str,
    region: str,  # https://help.aliyun.com/document_detail/31837.html
    role_arn: str,  # https://help.aliyun.com/document_detail/100624.html
    access_key_id: str,
    access_key_secret: str,
    sts_endpoint: str = "sts.cn-hangzhou.aliyuncs.com",
    role_session_name: str = "sts",
    duration_seconds: int = 3600,
):
    config = ClientConfig(
        access_key_id=access_key_id,
        access_key_secret=access_key_secret,
        endpoint=sts_endpoint,
    )
    client = StsClient(config)
    policy = {
        "Version": "1",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": ["oss:Put*"],
                "Resource": [
                    f"acs:oss:*:*:{bucket}",
                    f"acs:oss:*:*:{bucket}/*",
                ],
            },
        ],
    }
    assume_role_request = AssumeRoleRequest(
        duration_seconds=duration_seconds,
        role_arn=role_arn,
        role_session_name=role_session_name,
        policy=json.dumps(policy),
    )
    response = client.assume_role(assume_role_request)
    data = response.body.credentials.to_map()
    data["Bucket"] = bucket
    data["Region"] = region
    data["Endpoint"] = f"{region}.aliyuncs.com"
    data["Domain"] = f"{bucket}.{region}.aliyuncs.com"

    credentials = OssCredentials.parse_obj(data)
    return credentials
