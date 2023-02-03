import typing_extensions

from copilot_platforms_sdk.paths import PathValues
from copilot_platforms_sdk.apis.paths.channel_file import ChannelFile
from copilot_platforms_sdk.apis.paths.client import Client
from copilot_platforms_sdk.apis.paths.client_id import ClientId
from copilot_platforms_sdk.apis.paths.company import Company
from copilot_platforms_sdk.apis.paths.company_id import CompanyId
from copilot_platforms_sdk.apis.paths.custom_fields import CustomFields
from copilot_platforms_sdk.apis.paths.file import File
from copilot_platforms_sdk.apis.paths.form import Form
from copilot_platforms_sdk.apis.paths.form_response import FormResponse
from copilot_platforms_sdk.apis.paths.form_id import FormId

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.CHANNEL_FILE: ChannelFile,
        PathValues.CLIENT: Client,
        PathValues.CLIENT_ID: ClientId,
        PathValues.COMPANY: Company,
        PathValues.COMPANY_ID: CompanyId,
        PathValues.CUSTOMFIELDS: CustomFields,
        PathValues.FILE: File,
        PathValues.FORM: Form,
        PathValues.FORMRESPONSE: FormResponse,
        PathValues.FORM_ID: FormId,
    }
)

path_to_api = PathToApi(
    {
        PathValues.CHANNEL_FILE: ChannelFile,
        PathValues.CLIENT: Client,
        PathValues.CLIENT_ID: ClientId,
        PathValues.COMPANY: Company,
        PathValues.COMPANY_ID: CompanyId,
        PathValues.CUSTOMFIELDS: CustomFields,
        PathValues.FILE: File,
        PathValues.FORM: Form,
        PathValues.FORMRESPONSE: FormResponse,
        PathValues.FORM_ID: FormId,
    }
)
