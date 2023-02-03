import time
import unittest
from types import ModuleType
import uuid
import warnings
import oss2
from qcloud_cos import CosConfig, CosS3Client
from qcloud_cos.cos_exception import CosServiceError


class CredentialsTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        warnings.simplefilter("ignore", ResourceWarning)
        warnings.simplefilter("ignore", ImportWarning)

    def test_00_env_import(self):
        print("test_00_env_import")
        try:
            from . import secrets
        except ImportError as e:
            self.fail(f"{e}, no secrets.py")

        self.assertIsInstance(secrets, ModuleType)
        self.assertTrue(getattr(secrets, "qcloud_bucket"), "missing qcloud_bucket")
        self.assertTrue(getattr(secrets, "qcloud_region"), "missing qcloud_region")
        self.assertTrue(getattr(secrets, "qcloud_secret_id"), "missing qcloud_secret_id")
        self.assertTrue(getattr(secrets, "qcloud_secret_key"), "missing qcloud_secret_key")
        self.assertTrue(getattr(secrets, "aliyun_bucket"), "missing aliyun_bucket")
        self.assertTrue(getattr(secrets, "aliyun_region"), "missing aliyun_region")
        self.assertTrue(getattr(secrets, "aliyun_access_key_id"), "missing aliyun_access_key_id")
        self.assertTrue(getattr(secrets, "aliyun_access_key_secret"), "missing aliyun_access_key_secret")
        self.assertTrue(getattr(secrets, "aliyun_role_arn"), "missing aliyun_role_arn")

    def test_01_cos_secrets(self):
        print("test_01_cos_secrets")
        from .secrets import (
            aliyun_access_key_id,
            aliyun_access_key_secret,
            aliyun_bucket,
            aliyun_region,
        )

        auth = oss2.Auth(
            access_key_id=aliyun_access_key_id,
            access_key_secret=aliyun_access_key_secret,
        )

        bucket = oss2.Bucket(
            auth=auth,
            bucket_name=aliyun_bucket,
            endpoint=f"{aliyun_region}.aliyuncs.com",
        )
        info = bucket.get_bucket_info()
        if info.status != 200:
            self.fail(info)

    def test_02_oss_secrets(self):
        print("test_02_oss_secrets")
        from .secrets import (
            qcloud_region,
            qcloud_secret_id,
            qcloud_secret_key,
            qcloud_bucket,
        )

        config = CosConfig(
            Region=qcloud_region,
            SecretId=qcloud_secret_id,
            SecretKey=qcloud_secret_key,
        )
        client = CosS3Client(config)

        try:
            client.head_bucket(Bucket=qcloud_bucket)
        except CosServiceError as e:
            self.fail(e)

    def test_03_oss_upload(self):
        print("test_03_oss_upload")
        import oss2

        from sts_credentials.credentials.oss import get_credential_oss

        from .secrets import (
            aliyun_access_key_id,
            aliyun_access_key_secret,
            aliyun_bucket,
            aliyun_region,
            aliyun_role_arn,
        )

        c = get_credential_oss(
            access_key_id=aliyun_access_key_id,
            access_key_secret=aliyun_access_key_secret,
            bucket=aliyun_bucket,
            region=aliyun_region,
            role_arn=aliyun_role_arn,
        )
        auth = oss2.StsAuth(
            access_key_id=c.AccessKeyId,
            access_key_secret=c.AccessKeySecret,
            security_token=c.SecurityToken,
        )
        bucket = oss2.Bucket(
            auth=auth,
            endpoint=c.Endpoint,
            bucket_name=c.Bucket,
        )
        test_key = f"oss_test_{int(time.time())}.txt"
        test_data = uuid.uuid4().hex
        r = bucket.put_object(key=test_key, data=test_data)
        print("put_object", r.status)
        auth = oss2.Auth(
            access_key_id=aliyun_access_key_id,
            access_key_secret=aliyun_access_key_secret,
        )
        bucket = oss2.Bucket(
            auth=auth,
            endpoint=c.Endpoint,
            bucket_name=c.Bucket,
        )
        self.assertEqual(bucket.get_object(key=test_key).read(), test_data.encode())
        r = bucket.delete_object(key=test_key)
        print("delete_object", r.status)

    def test_04_cos_upload(self):
        print("test_04_cos_upload")
        from qcloud_cos import CosConfig, CosS3Client
        from qcloud_cos.streambody import StreamBody

        from sts_credentials.credentials.cos import get_credential_cos

        from .secrets import (
            qcloud_bucket,
            qcloud_region,
            qcloud_secret_id,
            qcloud_secret_key,
        )

        r = get_credential_cos(
            bucket=qcloud_bucket,
            region=qcloud_region,
            secret_id=qcloud_secret_id,
            secret_key=qcloud_secret_key,
        )
        c = r.credentials
        config = CosConfig(
            Region=c.region,
            SecretId=c.tmpSecretId,
            SecretKey=c.tmpSecretKey,
            Token=c.sessionToken,
        )
        client = CosS3Client(config)
        test_key = f"cos_test_{int(time.time())}.txt"
        test_data = uuid.uuid4().hex
        print("put_object")
        client.put_object(Bucket=c.bucket, Body=test_data, Key=test_key)
        config = CosConfig(
            Region=c.region,
            SecretId=qcloud_secret_id,
            SecretKey=qcloud_secret_key,
        )
        client = CosS3Client(config)
        body: StreamBody = client.get_object(Bucket=c.bucket, Key=test_key)["Body"]
        self.assertEqual(body.read(), test_data.encode())
        print("delete_object")
        client.delete_object(Bucket=c.bucket, Key=test_key)
