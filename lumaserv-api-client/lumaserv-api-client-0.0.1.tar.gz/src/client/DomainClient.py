import requests


class DomainClient:
    def __init__(self, api_key, base_url="https://api.lumaserv.com/domain"):
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


    def get_domain_handle(self, code, query_params={}):
        return self.request("GET", "/domain-handles/{code}".format(code=code), query_params)


    def delete_domain_handle(self, code, query_params={}):
        return self.request("DELETE", "/domain-handles/{code}".format(code=code), query_params)


    def update_domain_handle(self, code, body, query_params={}):
        return self.request("PUT", "/domain-handles/{code}".format(code=code), query_params, body)


    def unschedule_domain_delete(self, name, query_params={}):
        return self.request("POST", "/domains/{name}/unschedule-delete".format(name=name), query_params)


    def create_dns_zone_record(self, name, body, query_params={}):
        return self.request("POST", "/dns/zones/{name}/records".format(name=name), query_params, body)


    def get_dns_zone_records(self, name, query_params={}):
        return self.request("GET", "/dns/zones/{name}/records".format(name=name), query_params)


    def update_dns_zone_records(self, name, body, query_params={}):
        return self.request("PUT", "/dns/zones/{name}/records".format(name=name), query_params, body)


    def schedule_domain_delete(self, name, body, query_params={}):
        return self.request("POST", "/domains/{name}/schedule-delete".format(name=name), query_params, body)


    def search(self, query_params={}):
        return self.request("GET", "/search", query_params)


    def get_domain_pricing_list(self, query_params={}):
        return self.request("GET", "/pricing/domains", query_params)


    def get_domain_authinfo(self, name, query_params={}):
        return self.request("GET", "/domains/{name}/authinfo".format(name=name), query_params)


    def remove_domain_authinfo(self, name, query_params={}):
        return self.request("DELETE", "/domains/{name}/authinfo".format(name=name), query_params)


    def restore_domain(self, name, query_params={}):
        return self.request("POST", "/domains/{name}/restore".format(name=name), query_params)


    def get_dns_zones(self, query_params={}):
        return self.request("GET", "/dns/zones", query_params)


    def delete_dns_record(self, name, id, query_params={}):
        return self.request("DELETE", "/dns/zones/{name}/records/{id}".format(name=name, id=id), query_params)


    def update_dns_record(self, name, id, body, query_params={}):
        return self.request("PUT", "/dns/zones/{name}/records/{id}".format(name=name, id=id), query_params, body)


    def send_domain_verification(self, name, query_params={}):
        return self.request("POST", "/domains/{name}/verification".format(name=name), query_params)


    def check_domain_verification(self, name, query_params={}):
        return self.request("GET", "/domains/{name}/verification".format(name=name), query_params)


    def get_dns_zone(self, name, query_params={}):
        return self.request("GET", "/dns/zones/{name}".format(name=name), query_params)


    def update_dns_zone(self, name, body, query_params={}):
        return self.request("PUT", "/dns/zones/{name}".format(name=name), query_params, body)


    def get_labels(self, query_params={}):
        return self.request("GET", "/labels", query_params)


    def create_domain_handle(self, body, query_params={}):
        return self.request("POST", "/domain-handles", query_params, body)


    def get_domain_handles(self, query_params={}):
        return self.request("GET", "/domain-handles", query_params)


    def check_domain(self, name, query_params={}):
        return self.request("GET", "/domains/{name}/check".format(name=name), query_params)


    def create_domain(self, body, query_params={}):
        return self.request("POST", "/domains", query_params, body)


    def get_domains(self, query_params={}):
        return self.request("GET", "/domains", query_params)


    def get_domain(self, name, query_params={}):
        return self.request("GET", "/domains/{name}".format(name=name), query_params)


    def delete_domain(self, name, query_params={}):
        return self.request("DELETE", "/domains/{name}".format(name=name), query_params)


    def update_domain(self, name, body, query_params={}):
        return self.request("PUT", "/domains/{name}".format(name=name), query_params, body)


