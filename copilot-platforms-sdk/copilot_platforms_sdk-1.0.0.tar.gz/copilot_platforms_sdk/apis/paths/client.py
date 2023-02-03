from copilot_platforms_sdk.paths.client.get import ApiForget
from copilot_platforms_sdk.paths.client.put import ApiForput
from copilot_platforms_sdk.paths.client.post import ApiForpost


class Client(
    ApiForget,
    ApiForput,
    ApiForpost,
):
    pass
