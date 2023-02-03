'''
Connect to Amazon AWS S3 Storage (Kortex) by Assuming IAM Role.

Copyright (C) 2023 Nat Hawkins & Mike Chappelow

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License (version 3 of the License)
as published by the Free Software Foundation.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''


# Imports
import os
import boto3
from plinko.zoltar import zoltar_ask
from plinko.configurations import configure_username


def plinko_s3():
    '''
    Establish needed environment variables and global environment variables
    for connecting and reading/writing data to AWS S3 storage (Kortex) by assuming
    IAM Role

    Parameters
    ----------
    None

    Returns
    -------
    dict
        Dicitonary containing s3BucketName and connection object from boto3.client()
    '''
    # Check for API Key configuration
    if os.getenv("CONNECT_API_KEY") is None: configure_username()

    # Check for existing AWS S3 configuration information
    if os.getenv("AWS_SECRET_ACCESS_KEY") is not None: 
        print("You already have a defined S3 connection configured in your global environment.")
        print("You can only assume one role at a time. You must restart your session to connect to a different S3 storage location.")
        return None

    # Check for hostname
    hostname_ = os.popen('hostname').read().strip()

    # Create placeholder for Session to assume IAM role for
    # Same for PROD and DEV
    session = boto3.Session()
    sts     = session.client('sts')

    # DEV
    if hostname_ in ['usaws3170', 'usaws3171', 'usaws3172', 'usaws3173', 'usaws3174']:
        bucket_name = zoltar_ask("s3BucketName_kortex_DEV")
        response    = sts.assume_role(RoleArn = zoltar_ask("kortex_DEV_IAM"),
                                      RoleSessionName = "rstudio")

    # PROD
    else:
        bucket_name = zoltar_ask("s3BucketName_kortex")
        response    = sts.assume_role(RoleArn = zoltar_ask("kortex_IAM"),
                                      RoleSessionName = "rstudio")

    # Create session with temporary credentials from assuming IAM role
    temporary_credentials = boto3.Session(aws_access_key_id = response['Credentials']['AccessKeyId'],
                                          aws_secret_access_key = response['Credentials']['SecretAccessKey'],
                                          aws_session_token = response['Credentials']['SessionToken'])

    # Return bucket name and session client for accessing data
    return {"s3BucketName": bucket_name, "conn": temporary_credentials.client("s3")}
