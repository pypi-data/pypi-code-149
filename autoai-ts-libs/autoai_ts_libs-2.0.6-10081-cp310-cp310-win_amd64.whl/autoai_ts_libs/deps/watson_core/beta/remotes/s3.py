# *****************************************************************#
# (C) Copyright IBM Corporation 2021.                             #
#                                                                 #
# The source code for this program is not published or otherwise  #
# divested of its trade secrets, irrespective of what has been    #
# deposited with the U.S. Copyright Office.                       #
# *****************************************************************#
"""IBM cloud object storage client"""
import os
import threading
from typing import List
import botocore
import boto3
from botocore.client import Config as BotoClientConfig
from tqdm import tqdm
from autoai_ts_libs.deps.watson_core.toolkit import alog, error_handler
from . import base


log = alog.use_channel("S3REMOTE")
error = error_handler.get(log)


class S3Remote(base.RemoteClient):
    """An implementation of a RemoteClient for S3 storage."""

    def __init__(
        self,
        bucket,
        access_key_id,
        secret_access_key,
        endpoints,
        read_timeout=120,
        connect_timeout=10,
        max_attempts=0,
    ):
        """Initialize a S3 client

        Args:
            bucket: str
                S3 bucket name
            access_key_id: str
                access key used for authentication
            secret_access_key: str
                secret key used for authentication
            endpoints: str
                endpoint URL e.g. s3-api.sjc-us-geo.objectstorage.softlayer.net
            read_timeout: int
                read time out in seconds
            connect_timeout: int
                connect time out in seconds
            max_attempts: int
                max attempts to reconnect to storage
        """
        error.type_check("<COR00859207E>", str, bucket=bucket)
        error.type_check("<COR67757676E>", str, access_key_id=access_key_id)
        error.type_check("<COR38256218E>", str, secret_access_key=secret_access_key)
        error.type_check("<COR02124016E>", str, endpoints=endpoints)
        error.type_check("<COR36997701E>", int, read_timeout=read_timeout)
        error.type_check("<COR17541074E>", int, connect_timeout=connect_timeout)
        error.type_check("<COR98188577E>", int, max_attempts=max_attempts)

        self.bucket = bucket
        s3 = boto3.resource(
            "s3",
            config=BotoClientConfig(
                read_timeout=float(read_timeout),
                connect_timeout=float(connect_timeout),
                retries={"max_attempts": int(max_attempts)},
            ),
            aws_access_key_id=access_key_id,
            aws_secret_access_key=secret_access_key,
            endpoint_url=endpoints,
        )
        self.client = s3.meta.client

    def list(self, prefix) -> List[str]:
        """Return a list of files in prefix.

        Args:
            prefix: str
                Limits the response to keys that begin with the specified prefix (folder name)

        Returns:
            List[str]
                List of the files in the prefix
        """
        error.type_check("<COR11286273E>", str, prefix=prefix)
        try:
            results = self.client.list_objects_v2(Bucket=self.bucket, Prefix=prefix)
        except botocore.exceptions.ClientError as err:
            error(
                "<COR27484357E>",
                Exception("Failed to list files in folder {}.".format(prefix)),
                err,
            )

        files_list = []
        if "Contents" in results:
            # Filter out folders since we are only interested in files.
            files_list = [
                os.path.basename(obj["Key"])
                for obj in results["Contents"]
                if obj["Key"][-1:] != "/"
            ]

        return files_list

    def upload(self, source_file, destination_path) -> None:
        """Push a single source file to a remote destination.

        Args:
            source_file: str
                File to upload e.g. test.zip
            destination_path: str
                Path in the s3 storage file to be upload to
                e.g. blocks/categories/test.zip
        """
        error.type_check("<COR84770267E>", str, source_file=source_file)
        error.type_check("<COR67235207E>", str, destination_path=destination_path)

        try:
            self.client.upload_file(
                Filename=source_file,
                Bucket=self.bucket,
                Key=destination_path,
                Callback=ProgressPercentage(
                    self.client, self.bucket, source_file, download=False
                ),
            )
        except botocore.exceptions.ClientError as err:
            error(
                "<COR85263832E>",
                Exception("Failed to upload file {}.".format(source_file)),
                err,
            )

    def download(self, source_path, destination_path) -> None:
        """Pull a single file from a remote destination to a local path.

        Args:
            source_path: str
                Path to the file that will be downloaded from s3 storage
                e.g. blocks/categories/test.zip
            destination_path: str
                Path to download file to e.g. blocks/categories/test.zip
        """
        error.type_check("<COR35880262E>", str, source_path=source_path)
        error.type_check("<COR75081224E>", str, destination_path=destination_path)
        try:
            self.client.download_file(
                Bucket=self.bucket,
                Key=source_path,
                Filename=destination_path,
                Callback=ProgressPercentage(
                    self.client, self.bucket, source_path, download=True
                ),
            )
        except botocore.exceptions.ClientError as err:
            error(
                "<COR32359221E>",
                Exception("Failed to download file {}.".format(source_path)),
                err,
            )


class ProgressPercentage:
    """Log file transfer progress."""

    def __init__(self, client, bucket, filename, download):
        """Initialize the ProgressPercentage object.

        Args:
            client: s3.meta.client
                S3 client
            bucket: str
                S3 bucket name
            filename: str
                name of the file being copied
            download: boolean
                whether this is a download action
        """
        self._filename = filename
        # Download will fetch the file size from Object Storage
        # Upload simply gets the file size from file in local workspace
        if download:
            self._size = client.head_object(Bucket=bucket, Key=filename).get(
                "ContentLength"
            )
        else:
            self._size = float(os.path.getsize(filename))
        self._seen_so_far = 0
        # Configure the progress bar
        self.progress_bar = tqdm(total=self._size)
        self.progress_bar.set_description(
            "Transfer progress for file: {}".format(self._filename)
        )
        # Shorten the progress bar length
        self.progress_bar.bar_format = "{l_bar}{bar:20}{r_bar}"

        self._lock = threading.Lock()

    def __call__(self, bytes_amount):
        """Compute byte transfer progress and display/log results."""
        with self._lock:
            self._seen_so_far += bytes_amount
            percentage = (self._seen_so_far / self._size) * 100
            self.progress_bar.update(bytes_amount)
            log.info(
                "File transfer progress: {} {} / {}  {:2.2f}".format(
                    self._filename, self._seen_so_far, self._size, percentage
                )
            )
