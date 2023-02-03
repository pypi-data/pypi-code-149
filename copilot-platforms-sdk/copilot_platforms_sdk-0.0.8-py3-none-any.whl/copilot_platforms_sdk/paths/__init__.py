# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from copilot_platforms_sdk.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    CHANNEL_FILE = "/channel/file"
    CLIENT = "/client"
    CLIENT_ID = "/client/{id}"
    COMPANY = "/company"
    COMPANY_ID = "/company/{id}"
    CUSTOMFIELDS = "/custom-fields"
    FILE = "/file"
    FORM = "/form"
    FORMRESPONSE = "/form-response"
    FORM_ID = "/form/{id}"
