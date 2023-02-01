import requests


class BillingClient:
    def __init__(self, api_key, base_url="https://api.lumaserv.com/billing"):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({
            'Authorization': 'Bearer ' + api_key,
            'Content-Type': 'application/json'
        })


    def request(self, method, path, params={}, body={}):
        r = self.session.request(method, self.base_url + path, data=body, params=params)
        if r.status_code < 200 or (r.status_code >= 300 and r.status_code < 400):
            raise Exception("Status code is " + r.status_code + "!")
        return r.json()


    def create_debit_mandate(self, body, query_params={}):
        return self.request("POST", "/debit-mandates", query_params, body)


    def get_debit_mandates(self, query_params={}):
        return self.request("GET", "/debit-mandates", query_params)


    def get_invoice_file(self, id, query_params={}):
        return self.request("GET", "/invoices/{id}/file".format(id=id), query_params)


    def create_invoice_position(self, id, body, query_params={}):
        return self.request("POST", "/invoices/{id}/positions".format(id=id), query_params, body)


    def get_invoice_positions(self, id, query_params={}):
        return self.request("GET", "/invoices/{id}/positions".format(id=id), query_params)


    def get_billing_position(self, id, query_params={}):
        return self.request("GET", "/billing-positions/{id}".format(id=id), query_params)


    def delete_billing_position(self, id, query_params={}):
        return self.request("DELETE", "/billing-positions/{id}".format(id=id), query_params)


    def update_billing_position(self, id, body, query_params={}):
        return self.request("PUT", "/billing-positions/{id}".format(id=id), query_params, body)


    def get_debit_mandate(self, id, query_params={}):
        return self.request("GET", "/debit-mandates/{id}".format(id=id), query_params)


    def create_billing_position(self, body, query_params={}):
        return self.request("POST", "/billing-positions", query_params, body)


    def get_billing_positions(self, query_params={}):
        return self.request("GET", "/billing-positions", query_params)


    def create_customer(self, body, query_params={}):
        return self.request("POST", "/customers", query_params, body)


    def get_customers(self, query_params={}):
        return self.request("GET", "/customers", query_params)


    def get_invoice_position(self, invoice_id, id, query_params={}):
        return self.request("GET", "/invoices/{invoice_id}/positions/{id}".format(invoice_id=invoice_id, id=id), query_params)


    def delete_invoice_position(self, invoice_id, id, query_params={}):
        return self.request("DELETE", "/invoices/{invoice_id}/positions/{id}".format(invoice_id=invoice_id, id=id), query_params)


    def update_invoice_position(self, invoice_id, id, body, query_params={}):
        return self.request("PUT", "/invoices/{invoice_id}/positions/{id}".format(invoice_id=invoice_id, id=id), query_params, body)


    def create_service_contract(self, body, query_params={}):
        return self.request("POST", "/service-contracts", query_params, body)


    def get_service_contracts(self, query_params={}):
        return self.request("GET", "/service-contracts", query_params)


    def get_debits(self, query_params={}):
        return self.request("GET", "/debits", query_params)


    def get_customer(self, id, query_params={}):
        return self.request("GET", "/customers/{id}".format(id=id), query_params)


    def update_customer(self, id, body, query_params={}):
        return self.request("PUT", "/customers/{id}".format(id=id), query_params, body)


    def get_invoice(self, id, query_params={}):
        return self.request("GET", "/invoices/{id}".format(id=id), query_params)


    def delete_invoice(self, id, query_params={}):
        return self.request("DELETE", "/invoices/{id}".format(id=id), query_params)


    def update_invoice(self, id, body, query_params={}):
        return self.request("PUT", "/invoices/{id}".format(id=id), query_params, body)


    def get_service_contract_position(self, contract_id, id, query_params={}):
        return self.request("GET", "/service-contracts/{contract_id}/positions/{id}".format(contract_id=contract_id, id=id), query_params)


    def delete_service_contract_position(self, contract_id, id, query_params={}):
        return self.request("DELETE", "/service-contracts/{contract_id}/positions/{id}".format(contract_id=contract_id, id=id), query_params)


    def update_service_contract_position(self, contract_id, id, body, query_params={}):
        return self.request("PUT", "/service-contracts/{contract_id}/positions/{id}".format(contract_id=contract_id, id=id), query_params, body)


    def create_invoice(self, body, query_params={}):
        return self.request("POST", "/invoices", query_params, body)


    def get_invoices(self, query_params={}):
        return self.request("GET", "/invoices", query_params)


    def get_debit(self, id, query_params={}):
        return self.request("GET", "/debits/{id}".format(id=id), query_params)


    def create_service_contract_position(self, contract_id, body, query_params={}):
        return self.request("POST", "/service-contracts/{contract_id}/positions".format(contract_id=contract_id), query_params, body)


    def get_service_contract_positions(self, contract_id, query_params={}):
        return self.request("GET", "/service-contracts/{contract_id}/positions".format(contract_id=contract_id), query_params)


    def get_service_contract(self, id, query_params={}):
        return self.request("GET", "/service-contracts/{id}".format(id=id), query_params)


    def delete_service_contract(self, id, query_params={}):
        return self.request("DELETE", "/service-contracts/{id}".format(id=id), query_params)


    def update_service_contract(self, id, body, query_params={}):
        return self.request("PUT", "/service-contracts/{id}".format(id=id), query_params, body)


