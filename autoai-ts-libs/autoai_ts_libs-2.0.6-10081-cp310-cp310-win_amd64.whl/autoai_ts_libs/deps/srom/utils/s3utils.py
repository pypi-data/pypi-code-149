# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""A collection of Amazon s3 related utilities."""

import logging
import os
import json
from io import StringIO

import pandas as pd
import requests

import ibm_boto3
from ibm_boto3.s3.transfer import S3Transfer
from ibm_botocore.client import Config
from ibm_botocore.exceptions import ClientError

LOGGER = logging.getLogger(__name__)


def ibm_cos_s3_transfer_agent(
    credentials, resiliency="cross-region", region="us", public=True, location="us-geo"
):
    """Based on credentials returns S3Transfer instance"""
    return (
        _ibm_cos_s3_transfer_agent_internal(credentials)
        if credentials.get("ENDPOINT")
        else _ibm_cos_s3_transfer_agent_external(credentials)
    )


def _ibm_cos_s3_transfer_agent_internal(
    credentials, resiliency="cross-region", region="us", public=True, location="us-geo"
):
    client = ibm_boto3.client(
        service_name="s3",
        ibm_api_key_id=credentials["IBM_API_KEY_ID"],
        ibm_service_instance_id=credentials["IAM_SERVICE_ID"],
        ibm_auth_endpoint=credentials["IBM_AUTH_ENDPOINT"],
        config=Config(signature_version="oauth"),
        region_name=location,
        endpoint_url=credentials["ENDPOINT"],
    )
    return S3Transfer(client)


def _ibm_cos_s3_transfer_agent_external(
    credentials, resiliency="cross-region", region="us", public=True, location="us-geo"
):
    """returns an ibm cloud s3 compatible transfer agent"""
    return S3Transfer(boto3client(credentials, resiliency, region, public, location))


def creds_details(credentials):
    """Resolves endpoint and host configuration for given credentials"""
    endpoints = requests.get(credentials.get("endpoints")).json()

    # Obtain iam and cos host from the the detailed endpoints
    iam_host = endpoints["identity-endpoints"]["iam-token"]
    cos_host = endpoints["service-endpoints"]["cross-region"]["us"]["public"]["us-geo"]

    api_key = credentials.get("apikey")
    service_instance_id = credentials.get("resource_instance_id")

    # Construct auth and cos endpoint
    endpoint = "https://" + iam_host + "/oidc/token"
    service_endpoint = "https://" + cos_host

    answer = dict(
        api_key=api_key,
        service_instance_id=service_instance_id,
        auth_endpoint=endpoint,
        service_endpoint=service_endpoint,
    )
    return answer


def boto3client(
    credentials, resiliency="cross-region", region="us", public=True, location="us-geo"
):
    """returns an ibm boto3 client"""

    # Request detailed endpoint list
    endpoints = requests.get(credentials.get("endpoints")).json()

    # Obtain iam and cos host from the the detailed endpoints
    iam_host = endpoints["identity-endpoints"]["iam-token"]
    cos_host = ""
    pub_string = "public" if public is True else "private"
    if location in endpoints["service-endpoints"][resiliency][region][pub_string]:
        cos_host = endpoints["service-endpoints"][resiliency][region][pub_string][
            location
        ]
    else:
        regions_handle = os.path.join(os.path.dirname(__file__), "cos_regions.json")
        with open(regions_handle) as json_file:
            regions = json.load(json_file)
        resiliency = regions[pub_string][location]["resiliency"]
        region = regions[pub_string][location]["region"]
        cos_host = endpoints["service-endpoints"][resiliency][region][pub_string][
            location
        ]

    api_key = credentials.get("apikey")
    service_instance_id = credentials.get("resource_instance_id")

    # Construct auth and cos endpoint
    endpoint = "https://" + iam_host + "/oidc/token"
    service_endpoint = "https://" + cos_host

    LOGGER.info("Creating client...")
    # Get bucket list
    cos = ibm_boto3.client(
        "s3",
        ibm_api_key_id=api_key,
        ibm_service_instance_id=service_instance_id,
        ibm_auth_endpoint=endpoint,
        config=Config(signature_version="oauth"),
        region_name=location,
        endpoint_url=service_endpoint,
    )

    return cos


def boto3resource(
    credentials, resiliency="cross-region", region="us", public=True, location="us-geo"
):
    """returns an ibm boto3 client"""

    # Request detailed endpoint list
    endpoints = requests.get(credentials.get("endpoints")).json()

    # Obtain iam and cos host from the the detailed endpoints
    iam_host = endpoints["identity-endpoints"]["iam-token"]
    cos_host = ""
    pub_string = "public" if public is True else "private"
    if location in endpoints["service-endpoints"][resiliency][region][pub_string]:
        cos_host = endpoints["service-endpoints"][resiliency][region][pub_string][
            location
        ]
    else:
        regions_handle = os.path.join(os.path.dirname(__file__), "cos_regions.json")
        with open(regions_handle) as json_file:
            regions = json.load(json_file)
        resiliency = regions[pub_string][location]["resiliency"]
        region = regions[pub_string][location]["region"]
        cos_host = endpoints["service-endpoints"][resiliency][region][pub_string][
            location
        ]

    api_key = credentials.get("apikey")
    service_instance_id = credentials.get("resource_instance_id")

    # Construct auth and cos endpoint
    endpoint = "https://" + iam_host + "/oidc/token"
    service_endpoint = "https://" + cos_host

    LOGGER.info("Creating resources...")
    # Get bucket list
    resource = ibm_boto3.resource(
        "s3",
        ibm_api_key_id=api_key,
        ibm_service_instance_id=service_instance_id,
        ibm_auth_endpoint=endpoint,
        config=Config(signature_version="oauth"),
        region_name=location,
        endpoint_url=service_endpoint,
    )

    return resource


def csv_to_pandasdf(
    credentials,
    object_name,
    resiliency="cross-region",
    region="us",
    public=True,
    location="us-geo",
    **kwargs
):
    """
    Method to fetch data from cos and convert it to dataframe.
    Returns:
        Pandas dataframe
    """

    if "BUCKET" in credentials and "bucket" not in credentials:
        LOGGER.warning(
            'please use lower case "bucket" instead of "BUCKET",\
            fixing for backward compatibility'
        )
        credentials["bucket"] = credentials.pop("BUCKET")
    if not "bucket" in credentials:
        raise Exception("credentials must bucket key")

    try:
        botoc = boto3client(credentials, resiliency, region, public, location)
        encoding = kwargs.get("encoding", "UTF-8")
        obj = botoc.get_object(Bucket=credentials["bucket"], Key=object_name)
        sio = StringIO(obj["Body"].read().decode(encoding))
        return pd.read_csv(sio, **kwargs)
    except ClientError as ex:
        if ex.response["Error"]["Code"] == "NoSuchKey":
            LOGGER.error("Please provide correct location and object key")
            raise Exception("Please provide correct location and object key") from None
        else:
            LOGGER.error("boto3 client error: {}".format(ex))
            raise Exception("Error in boto3 client") from None
    except KeyError as ex:
        msg = "Please provide correct location. resiliency and region are optional"
        msg2 = " but you can try to skip them if you are not sure of correct values."
        LOGGER.error(msg + msg2)
        raise Exception("Please provide correct location and object key") from None
    finally:
        botoc = None

