import requests
import json
import configparser
import logging


class SAPContextManager():
    def __init__(self, ip, CompanyDB, UserName, password):
        self.ip = ip
        self.CompanyDB = CompanyDB
        self.UserName = UserName
        self.password = password
        self.alertConf = {}

    def __enter__(self):
        self.session, self.routeID = self.SAPlogin(self.ip, self.CompanyDB,
                                                   self.UserName,
                                                   self.password)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.SAPlogout(self.CompanyDB, self.ip, self.routeID)

    def SAPlogin(self, ip, CompanyDB, UserName, password):
        """
        Se conecta a SAP.

        :param ip: Direccion IP de SAP
        :param CompanyDB: Nombre de la base de datos de SAP
        :param UserName: Nombre de usuario de SAP
        :param password: Contraseña de usuario de SAP
        """
        url = ip+"/b1s/v1/Login"
        payload = "{\r\n  \"CompanyDB\": "\
            f"\"{CompanyDB}\",\r\n\"UserName\": \"{UserName}\",\r\n "\
            f"\"Password\": \"{password}\"\r"\
            "\n}"

        headers = {
            'Content-Type': 'text/plain',
            'Cookie': f'CompanyDB={CompanyDB};ROUTEID=.node1'
        }
        response = self.peticionSAP("POST", url, msg="Ha ocurrido un error"
                                    " comunicandose con SAP en "
                                    "DetectorErroresTraspasoComerzziaSAP al"
                                    " hacer login",  headers=headers,
                                    data=payload, verify=False)
        val = json.loads(response.text)
        routeID = ".node1"

        session_Key = val['SessionId']
        return session_Key, routeID

    def peticionSAP(self, method, url, headers, data, msg, verify=False):
        try:
            response = requests.request(method, url, headers=headers,
                                        data=data, verify=verify)
        except Exception as e:
            print(e)
            raise Exception("Error en la peticion a SAP")
        return response

    def SAPlogout(self, CompanyDB, ip, routeID=".node0"):
        """
        Se desconecta de SAP.

        :param CompanyDB: Nombre de la base de datos de SAP
        :param UserName: Nombre de usuario de SAP
        :param password: Contraseña de usuario de SAP
        :param ip: Direccion IP de SAP
        """

        url = ip+"/b1s/v1/Logout"
        payload = "{\r\n"+f"    \"CompanyDB\": \"{CompanyDB}\",\r\n "
        "   \"UserName\": \"{UserName}\",\r\n    \"Password\":"
        " \"{password}\"\r\n"+"}"
        headers = {
            'Content-Type': 'text/plain',
            'Cookie': f'ROUTEID={routeID}'
        }

        response = self.peticionSAP("POST", url, msg="Ha ocurrido un error"
                                    " comunicandose con SAP en "
                                    "DetectorErroresTraspasoComerzziaSAP al"
                                    " hacer logout", headers=headers,
                                    data=payload,
                                    verify=False)
