from netsuite import swagger_client


class RestClient:
    def __init__(self, netsuite):
        self.netsuite = netsuite
        self.configuration = swagger_client.Configuration()
        self.configuration.app_name = netsuite.netsuite_app_name
        self.configuration.host = f"https://{self.configuration.app_name}.suitetalk.api.netsuite.com/services/rest/record/v1"
        self.configuration.access_token = netsuite.storage.get_token(netsuite.app_name).access_token
        self.api_client = swagger_client.ApiClient(configuration=self.configuration)
        self.contact_api = swagger_client.ContactApi(api_client=self.api_client)
        self.customer_api = swagger_client.CustomerApi(api_client=self.api_client)
