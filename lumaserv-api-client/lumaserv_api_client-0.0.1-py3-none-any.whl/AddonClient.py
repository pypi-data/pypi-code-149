import requests


class AddonClient:
    def __init__(self, api_key, base_url="https://api.lumaserv.com/addon"):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({
            'Authorization': 'Bearer ' + api_key,
            'Content-Type': 'application/json'
        })


    def request(self, method, path, params={}, body={}):
        r = self.session.request(method, self.base_url + path, data=body, params=params)
        if(r.status_code < 200 or (r.status_code >= 300 and r.status_code < 400):
            raise Exception("Status code is " + r.status_code + "!")
        return r.json()


    def create_ssl_certificate(self, body, query_params={}):
        return self.request("POST", "/ssl/certificates", query_params, body)


    def get_ssl_certificates(self, query_params={}):
        return self.request("GET", "/ssl/certificates", query_params)


    def get_plesk_license_types(self, query_params={}):
        return self.request("GET", "/license/plesk-types", query_params)


    def search(self, query_params={}):
        return self.request("GET", "/search", query_params)


    def get_ssl_certificate(self, id, query_params={}):
        return self.request("GET", "/ssl/certificates/{id}".format(id=id), query_params)


    def get_ssl_organisation(self, id, query_params={}):
        return self.request("GET", "/ssl/organisations/{id}".format(id=id), query_params)


    def delete_ssl_organisation(self, id, query_params={}):
        return self.request("DELETE", "/ssl/organisations/{id}".format(id=id), query_params)


    def create_ssl_contact(self, body, query_params={}):
        return self.request("POST", "/ssl/contacts", query_params, body)


    def get_ssl_contacts(self, query_params={}):
        return self.request("GET", "/ssl/contacts", query_params)


    def create_ssl_organisation(self, body, query_params={}):
        return self.request("POST", "/ssl/organisations", query_params, body)


    def get_ssl_organisations(self, query_params={}):
        return self.request("GET", "/ssl/organisations", query_params)


    def get_ssl_type(self, id, query_params={}):
        return self.request("GET", "/ssl/types/{id}".format(id=id), query_params)


    def get_ssl_contact(self, id, query_params={}):
        return self.request("GET", "/ssl/contacts/{id}".format(id=id), query_params)


    def delete_ssl_contact(self, id, query_params={}):
        return self.request("DELETE", "/ssl/contacts/{id}".format(id=id), query_params)


    def create_plesk_license(self, body, query_params={}):
        return self.request("POST", "/licenses/plesk", query_params, body)


    def get_plesk_licenses(self, query_params={}):
        return self.request("GET", "/licenses/plesk", query_params)


    def get_ssl_types(self, query_params={}):
        return self.request("GET", "/ssl/types", query_params)


    def get_plesk_license(self, id, query_params={}):
        return self.request("GET", "/licenses/plesk/{id}".format(id=id), query_params)


    def update_plesk_license(self, id, body, query_params={}):
        return self.request("PUT", "/licenses/plesk/{id}".format(id=id), query_params, body)


    def get_plesk_license_type(self, id, query_params={}):
        return self.request("GET", "/license/plesk-types/{id}".format(id=id), query_params)


