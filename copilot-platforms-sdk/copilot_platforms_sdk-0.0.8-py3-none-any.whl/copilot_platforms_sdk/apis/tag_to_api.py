import typing_extensions

from copilot_platforms_sdk.apis.tags import TagValues
from copilot_platforms_sdk.apis.tags.copilot_api import CopilotApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.COPILOT: CopilotApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.COPILOT: CopilotApi,
    }
)
