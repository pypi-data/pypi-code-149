import os
from dotenv import load_dotenv

load_dotenv()

qcloud_bucket = os.environ.get("qcloud_bucket", "")
qcloud_region = os.environ.get("qcloud_region", "")
qcloud_secret_id = os.environ.get("qcloud_secret_id", "")
qcloud_secret_key = os.environ.get("qcloud_secret_key", "")


aliyun_bucket = os.environ.get("aliyun_bucket", "")
aliyun_region = os.environ.get("aliyun_region", "")
aliyun_access_key_id = os.environ.get("aliyun_access_key_id", "")
aliyun_access_key_secret = os.environ.get("aliyun_access_key_secret", "")
aliyun_role_arn = os.environ.get("aliyun_role_arn", "")
