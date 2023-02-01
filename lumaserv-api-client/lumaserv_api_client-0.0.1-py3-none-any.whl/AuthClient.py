import requests


class AuthClient:
    def __init__(self, api_key, base_url="https://auth.lumaserv.com"):
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


    def create_project(self, body, query_params={}):
        return self.request("POST", "/projects", query_params, body)


    def get_projects(self, query_params={}):
        return self.request("GET", "/projects", query_params)


    def get_project(self, id, query_params={}):
        return self.request("GET", "/projects/{id}".format(id=id), query_params)


    def delete_project(self, id, query_params={}):
        return self.request("DELETE", "/projects/{id}".format(id=id), query_params)


    def update_project(self, id, body, query_params={}):
        return self.request("PUT", "/projects/{id}".format(id=id), query_params, body)


    def login(self, body, query_params={}):
        return self.request("POST", "/login", query_params, body)


    def create_user(self, body, query_params={}):
        return self.request("POST", "/users", query_params, body)


    def get_users(self, query_params={}):
        return self.request("GET", "/users", query_params)


    def get_user(self, id, query_params={}):
        return self.request("GET", "/users/{id}".format(id=id), query_params)


    def update_user(self, id, body, query_params={}):
        return self.request("PUT", "/users/{id}".format(id=id), query_params, body)


    def request_password_reset(self, body, query_params={}):
        return self.request("POST", "/password-reset", query_params, body)


    def execute_password_reset(self, body, query_params={}):
        return self.request("PUT", "/password-reset", query_params, body)


    def change_email(self, body, query_params={}):
        return self.request("PUT", "/email-change", query_params, body)


    def reject_project_invite(self, id, query_params={}):
        return self.request("POST", "/project-invites/{id}/reject".format(id=id), query_params)


    def insert_audit_log_entry(self, body, query_params={}):
        return self.request("POST", "/audit-log", query_params, body)


    def search_audit_log(self, query_params={}):
        return self.request("GET", "/audit-log", query_params)


    def create_token(self, body, query_params={}):
        return self.request("POST", "/tokens", query_params, body)


    def get_tokens(self, query_params={}):
        return self.request("GET", "/tokens", query_params)


    def get_country(self, code, query_params={}):
        return self.request("GET", "/countries/{code}".format(code=code), query_params)


    def change_password(self, body, query_params={}):
        return self.request("PUT", "/password-change", query_params, body)


    def get_token(self, id, query_params={}):
        return self.request("GET", "/tokens/{id}".format(id=id), query_params)


    def delete_token(self, id, query_params={}):
        return self.request("DELETE", "/tokens/{id}".format(id=id), query_params)


    def delete_project_invite(self, id, query_params={}):
        return self.request("DELETE", "/project-invites/{id}".format(id=id), query_params)


    def validate_token(self, token, query_params={}):
        return self.request("GET", "/validate/{token}".format(token=token), query_params)


    def create_project_invite(self, body, query_params={}):
        return self.request("POST", "/project-invites", query_params, body)


    def get_project_invites(self, query_params={}):
        return self.request("GET", "/project-invites", query_params)


    def add_project_member(self, id, body, query_params={}):
        return self.request("POST", "/projects/{id}/members".format(id=id), query_params, body)


    def get_project_members(self, id, query_params={}):
        return self.request("GET", "/projects/{id}/members".format(id=id), query_params)


    def search_transaction_log(self, body, query_params={}):
        return self.request("POST", "/transaction-log", query_params, body)


    def validate_self(self, query_params={}):
        return self.request("GET", "/validate/self", query_params)


    def accept_project_invite(self, id, query_params={}):
        return self.request("POST", "/project-invites/{id}/accept".format(id=id), query_params)


    def remove_project_member(self, id, user_id, query_params={}):
        return self.request("DELETE", "/projects/{id}/members/{user_id}".format(id=id, user_id=user_id), query_params)


    def get_user_project_memberships(self, id, query_params={}):
        return self.request("GET", "/users/{id}/project_memberships".format(id=id), query_params)


    def get_countries(self, query_params={}):
        return self.request("GET", "/countries", query_params)


