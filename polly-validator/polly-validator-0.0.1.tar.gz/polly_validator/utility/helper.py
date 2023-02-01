import base64
import json
import os
import sys
import traceback as tb
from datetime import datetime as dt
from functools import wraps

import requests as rq
from pydantic import StrictFloat, StrictInt, StrictStr, conlist, create_model
from requests import Session

from polly_validator.utility.errors import error_handler, invalidApiResponseException

DATATYPE_MAP = {'string': StrictStr,
                'bigint': StrictInt,
                'integer': StrictInt,
                'float': StrictFloat,
                'double': StrictFloat,
                'object': dict,
                'boolean': bool,
                'array<string>': conlist(StrictStr, min_items=1),
                'array<int>': conlist(StrictInt, min_items=1),
                'array<object>': conlist(dict, min_items=1),
                'array<boolean>': conlist(bool, min_items=1)}


class UnauthorizedException(Exception):
    def __str__(self):
        return f"Authorization failed"


class PollySession(Session):
    """
    This class contain function to create session for
    polly.
    """

    def __init__(self, TOKEN, env="polly"):
        Session.__init__(self)
        try:
            # for python version >= python3.8
            from importlib.metadata import version

            version = version("polly-python")
        except ImportError:
            # for python version < python3.8
            import pkg_resources

            version = pkg_resources.get_distribution("polly-python").version
        client = os.getenv("POLLY_SERVICE")
        if client is not None:
            version = version + "/" + client
        else:
            version = version + "/local"

        try:
            json.loads(base64.b64decode(TOKEN.split(".")[0].encode("ascii") + b"=="))
            self.headers = {
                "Content-Type": "application/vnd.api+json",
                "Cookie": f"refreshToken={TOKEN}",
                "User-Agent": "polly-python/" + version,
            }
        except Exception:
            self.headers = {
                "Content-Type": "application/vnd.api+json",
                "x-api-key": f"{TOKEN}",
                "User-Agent": "polly-python/" + version,
            }
        self.env = env


class Polly:
    default_session = None

    @classmethod
    def auth(cls, token):
        cls.default_session = PollySession(token)

    @classmethod
    def get_session(cls, token=None):
        if not token:
            if not cls.default_session:
                raise UnauthorizedException
            else:
                return cls.default_session
        else:
            return PollySession(token)


def get_schema_from_api(repo, schema_level, env, token, file_type=None):
    """
    Given a repo name and schema level, get the schema from the API
    Args:
        repo:
        schema_level:
        env:
        token:
        file_type:
    Returns:

    """
    try:
        url_discover = f"https://api.discover.{env}.elucidata.io"
        session = Polly.get_session(token)
        if schema_level == 'dataset':
            files_api_endpoint = f'{url_discover}/repositories/{repo}/schemas/files'
            response = session.get(files_api_endpoint)
            error_handler(response)
            # making `schema_type` from the API response
            # as the key of resp_dict
            api_resp_dict = response.json()
            if "data" in api_resp_dict:
                if "attributes" in api_resp_dict["data"]:
                    if "schema" in api_resp_dict["data"]["attributes"]:
                        if 'all' in api_resp_dict["data"]["attributes"]["schema"]:
                            if 'all' in api_resp_dict["data"]["attributes"]["schema"]['all']:
                                schema_dict = api_resp_dict["data"]["attributes"]["schema"]['all']['all']
                                return schema_dict
                            else:
                                raise invalidApiResponseException(
                                    title="all key not present",
                                    detail="all not present in the repository schema", )
                        else:
                            raise invalidApiResponseException(
                                title="all key not present",
                                detail="all key not present in the repository schema", )
                    else:
                        raise invalidApiResponseException(
                            title="schema not present",
                            detail="schema not present in the repository schema", )
                else:
                    raise invalidApiResponseException(
                        title="attributes not present",
                        detail="attributes not present in the repository schema", )
            else:
                raise invalidApiResponseException(
                    title="data key not present",
                    detail="data key not present in the repository schema", )
        elif schema_level == 'sample':
            if file_type is None:
                raise Exception(f'"file_type" parameter not passed.')
            files_api_endpoint = f'{url_discover}/repositories/{repo}/schemas/{file_type}_metadata'
            response = session.get(files_api_endpoint)
            error_handler(response)
            # making `schema_type` from the API response
            # as the key of resp_dict
            api_resp_dict = response.json()
            if "data" in api_resp_dict:
                if "attributes" in api_resp_dict["data"]:
                    if "schema" in api_resp_dict["data"]["attributes"]:
                        if 'all' in api_resp_dict["data"]["attributes"]["schema"]:
                            if 'all' in api_resp_dict["data"]["attributes"]["schema"]['all']:
                                schema_dict = api_resp_dict["data"]["attributes"]["schema"]['all']['all']
                                return schema_dict
                            else:
                                raise invalidApiResponseException(
                                    title="all key not present",
                                    detail="all not present in the repository schema", )
                        else:
                            raise invalidApiResponseException(
                                title="all key not present",
                                detail="all key not present in the repository schema", )
                    else:
                        raise invalidApiResponseException(
                            title="schema not present",
                            detail="schema not present in the repository schema", )
                else:
                    raise invalidApiResponseException(
                        title="attributes not present",
                        detail="attributes not present in the repository schema", )
            else:
                raise invalidApiResponseException(
                    title="data key not present",
                    detail="data key not present in the repository schema", )
        else:
            raise Exception(f'Invalid value for schema_level: {schema_level}')
    except Exception:
        print(tb.format_exc())
        print_exception()
        return None


def build_original_name_to_field_name_mapping(schema_dict):
    """
    Given a schema dict for a repo, create a mapping for original name vs representative name
    Args:
        schema_dict:

    Returns:

    """
    res = {}
    for k, v in schema_dict.items():
        res[v['original_name']] = k
    return res


def build_field_name_to_original_name_mapping(schema_dict):
    """
    Given a schema dict for a repo, create a mapping for representative name vs original name
    Args:
        schema_dict:

    Returns:

    """
    try:
        res = {}
        for k, v in schema_dict.items():
            res[k] = v['original_name']
        return res
    except Exception:
        print(tb.format_exc())
        print_exception()
        return None


def modify_metadata_as_per_mapping(metadata_list, repo, schema_level, env, token, file_type=None):
    """
    Given a metadata list, repo and schema level. Perform the following steps:
    1. Get schema dict from API call
    2. Create mapping for original name vs the representative name
    3. Change the key names in the metadata list to representative names.
    Args:
        metadata_list:
        repo:
        schema_level:
        env:
        token:

    Returns:

    """
    try:
        # Step 1
        schema_dict = get_schema_from_api(repo, schema_level, env, token, file_type)
        if schema_dict is None:
            raise Exception('Error getting schema from API')
        # Step 2
        orig_name_mapping = build_original_name_to_field_name_mapping(schema_dict)
        # Step 3
        for metadata in metadata_list:
            for k, v in orig_name_mapping.items():
                if k in metadata:
                    metadata[v] = metadata.pop(k)
        return metadata_list
    except Exception:
        print(tb.format_exc())
        print_exception()
        return None


def timeit(func):
    """
    Timing function to time error collection.
    Args:
        func:

    Returns:
    """

    @wraps(func)
    def timed(*args, **kw):
        tstart = dt.now()
        output = func(*args, **kw)
        tend = dt.now()
        print('"{}" took {} to execute.\n'.format(func.__name__, (tend - tstart)))
        return output

    return timed


def list_to_set_in_dict(obj):
    """
    Recursively convert list values inside a dic to sets
    Args:
        obj: Current value being checked

    Returns:
        obj: Dict with lists converted to sets.
    """
    if isinstance(obj, list):
        return {list_to_set_in_dict(v) for v in obj}
    elif isinstance(obj, dict):
        return {k: list_to_set_in_dict(v) for k, v in obj.items()}
    return obj


def lower_and_strip(obj):
    """
    Lower and strip all values in a list
    Args:
        obj:

    Returns:

    """
    for key, val in obj.items():
        if isinstance(val, list) or isinstance(val, set):
            obj[key] = [v.lower().strip() for v in val]
        elif isinstance(val, dict):
            obj[key] = lower_and_strip(obj[key])
    return obj


def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def build_validation_schema(schema_df, for_level, validators=None):
    """
    Takes a description DF and returns a pydantic class with the values taken from the schema
    Args:
        for_level:
        validators:
        schema_df:

    Returns:

    """
    try:
        if for_level == 'sample':
            curated_fields = schema_df[schema_df['column_name'].str.startswith('curated_')]
            schema_dict = dict(zip(curated_fields['column_name'], curated_fields['column_type']))
        elif for_level == 'dataset':
            schema_dict = dict(zip(schema_df['column_name'], schema_df['column_type']))
        else:
            raise Exception(f'Invalid argument given for argument "for_level": {for_level}')
        for k, v in schema_dict.items():
            schema_dict[k] = (DATATYPE_MAP[v], ...)
        if validators is not None:
            schema = create_model('SchemaWithValidators', **schema_dict, __validators__=validators)
        else:
            schema = create_model('Schema', **schema_dict)
        return schema
    except Exception as e:
        print(tb.format_exc())
        print_exception()
        return None


def split_ontological_fields_by_type(ontological_fields, schema_df):
    """
    Given a list of ontological fields, split them into str fields or list type fields as per description dataframe
    Args:
        ontological_fields:
        schema_df:

    Returns:

    """
    curated_fields = schema_df[schema_df['column_name'].str.startswith('curated_')]
    schema_dict = dict(zip(curated_fields['column_name'], curated_fields['column_type']))
    list_fields = [k for k, v in schema_dict.items() if v == 'array<string>' and k in ontological_fields]
    str_fields = [k for k, v in schema_dict.items() if v == 'string' and k in ontological_fields]
    return str_fields, list_fields


def split_fields_by_type(all_fields, schema_df):
    """
    Given a list of ontological fields, split them into str fields or list type fields as per description dataframe
    Args:
        ontological_fields:
        schema_df:

    Returns:

    """
    curated_fields = schema_df[schema_df['column_name'].str.startswith('curated_')]
    schema_dict = dict(zip(curated_fields['column_name'], curated_fields['column_type']))
    list_fields = [k for k, v in schema_dict.items() if v == 'array<string>']
    str_fields = [k for k, v in schema_dict.items() if v == 'string']
    return str_fields, list_fields


def schema_correction(meta, err):
    """
    Type Modification:
        - If errors are found, collect the errors and perform in-memory modifications of the metadata values.
        This correction can be one of the following:
            If the value should be a list but the incoming value is a string, typecast it into a list
            E.g. ‘Cancer’ will be changed to ['Cancer']

            If the value should be a string, but the incoming value is an integer, typecast it into a string.
            E.g. 2021 will change to ‘2021’.
        - If no errors are found, perform no in-memory modifications.
    Args:
        meta: sample level metadata dict
        err: list of dict of schema errors

    Returns:

    """
    for e in err:
        field = e['loc'][0]
        if e['type'] == 'type_error.list':
            meta[field] = [meta[field]]
        elif e['type'] == 'type_error.str':
            meta[field] = str(meta[field])
    return meta


def print_exception():
    """
    Print exception in detail
    Returns:

    """
    exception_type, exception_object, exception_traceback = sys.exc_info()
    filename = exception_traceback.tb_frame.f_code.co_filename
    line_number = exception_traceback.tb_lineno
    print("Exception type: ", exception_type)
    print("File name: ", filename)
    print("Line number: ", line_number)


def get_data_types_data_sources():
    """Getting Data Type and Data Source values from a separate repo on GitHub"""
    try:
        response_data_types = rq.get(f'https://raw.githubusercontent.com/ElucidataInc/PublicAssets/'
                                     f'master/polly_validator/accepted_data_types.txt')
        if response_data_types.status_code != 200:
            raise Exception(f"Unable to retrieve data type file from GitHub. Status Code: "
                            f"{response_data_types.status_code}")
        valid_data_types = base64.b64decode(response_data_types.content).decode('ascii').split('\n')
        print(f'Retrieved Valid Data Types')

        response_data_sources = rq.get(f'https://raw.githubusercontent.com/ElucidataInc/PublicAssets/'
                                       f'master/polly_validator/accepted_data_sources.txt')
        if response_data_sources.status_code != 200:
            raise Exception(f"Unable to retrieve data source file from GitHub. Status Code: "
                            f"{response_data_sources.status_code}")
        valid_data_sources = base64.b64decode(response_data_sources.content).decode('ascii').split('\n')
        print(f'Retrieved Valid Data Sources')
        return valid_data_types, valid_data_sources
    except Exception as e:
        print(tb.format_exc())
        print_exception()
        return [], []
