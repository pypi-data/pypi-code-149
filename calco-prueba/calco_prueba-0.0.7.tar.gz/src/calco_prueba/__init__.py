import requests
import json
import logging
from cryptography.fernet import Fernet
from smbclient import (listdir, open_file, register_session, scandir)
import configparser
import smtplib
import logging
import ssl
import os
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formatdate
from os.path import basename
from email.mime.application import MIMEApplication
from hdbcli import dbapi
import mariadb
import msal


def calco_logger():
    """
    Función que sirve para inicializar el log en el archivo debug.log
    """
    logging.basicConfig(filename='debug.log', level=logging.DEBUG,
                        filemode='w',
                        format='%(asctime)s - %(name)s - %(message)s')


class conectar_MariaDB():
    """
        Contextmanager para conectar a MariaDB. Esta clase se encarga de
        iniciar las conexiones y cerrarlas de forma automatica.
    """

    def __init__(self, host: str, user: str, password: str, database: str,
                 port: int = 3306):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.port = port

    def __enter__(self):
        self.conn = self.conectarMariaDB(host=self.host, user=self.user,
                                    password=self.password, db=self.database,
                                    port=self.port)
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()

# Conexiones a bases de datos Mariadb y MySQL
    def conectarMariaDB(self, host: str, user: str, password: str, db: str,
                        port: int = 3306):
        """
        Establecemos una conexion a mariadb

        :param host: ip del host
        :param user: usuario
        :param password: contraseña
        :param db: nombre de la base de datos
        :param port: puerto de conexion. Por defecto 3306
        :return: conexión a la base de datos
        """

        conexion = mariadb.connect(
            user=user,
            password=password,
            host=host,
            port=port,
            database=db
        )
        return conexion


class conectar_HanaDB():
    """
    ContextManager de las conexiones de HanaDB
    """

    def __init__(self, host: str, user: str, password: str, port: int = 3306):
        self.host = host
        self.user = user
        self.password = password
        self.port = port

    def __enter__(self):
        self.conn = self.hanaConnection()
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()

    def hanaConnection(self):
        """
        Establecemos una conexion a hanadb

        :param host: ip del host
        :param port: puerto de conexion
        :param user: usuario
        :param passwd: contraseña
        :return: conexión a la base de datos
        """
        conexion = dbapi.connect(
            address=self.host,
            port=self.port,
            user=self.user,
            password=self.password
        )
        return conexion


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


class CodeDecode():
    def parserReader(self, section, parser):
        """
        Reads the parameters from the configuration file
        """
        data = {}
        if parser.has_section(section):
            params = parser.items(section)
            for param in params:
                data[param[0]] = (self.desencriptar_items(param[1],
                                self.cargar_clave()).decode("utf-8"))

        return data

    def cargar_clave(self):
        """
        Carga la clave del archivo clave.key
        """
        return open('clave.key', "rb").read()

    # Encriptar items del .ini
    def encriptar_items(self, config, clave):
        """
        Encripta los items del .ini
        :param config: ConfigParser en el que se ha leido el .ini
        :param clave: Clave para encriptar
        """
        for sections in config.sections():
            print("\n\n["+sections+"]\n")
            f = Fernet(clave)
            for items in list(config[sections]):
                mensaje = config[sections][items].encode("latin1", "strict")
                encriptado = f.encrypt(mensaje).decode("utf-8", "strict")
                print(items + " = " + encriptado)

    # Desencriptar un item determinado
    def desencriptar_items(self, item: str, clave):
        """
        Desencripta un item determinado

        :param item: Item a desencriptar
        :param clave: Clave para desencriptar
        :return: Item desencriptado
        """
        f = Fernet(clave)
        decrypted = f.decrypt(item.encode())
        return decrypted

    def genera_clave(self):
        clave = Fernet.generate_key()
        with open("clave.key", "wb") as archivo_clave:
            archivo_clave.write(clave)


def enviarCorreo(mensaje, destino, origen, asunto, server, puerto, password,
                 isFile=False, fileName=None):
    """
    Envia un correo con las caracteristicas dadas por parametros

    :param mensaje: mensaje a enviar
    :param destino: correo de destino
    :param origen: correo de origen
    :param asunto: asunto del correo
    :param server: servidor smtp del correo
    :param puerto: puerto del servidor smtp
    :param password: contraseña del correo
    :param isFile: True o False
    :param fileName: ruta local al archivo
    """
    mensaje.encode('utf-8')
    context = ssl.create_default_context()
    try:
        with smtplib.SMTP_SSL(server, puerto, context=context) as server:
            msg = MIMEMultipart()
            msg['From'] = origen
            msg['To'] = destino
            msg['Date'] = formatdate(localtime=True)
            msg['Subject'] = asunto
            msg.attach(MIMEText(mensaje))
            if isFile:
                if 'list' in str(type(fileName)):
                    for file in fileName:
                        if not os.path.exists(file):
                            raise FileNotFoundError
                        with open(file, "rb") as fil:
                            part = MIMEApplication(
                                fil.read(),
                                Name=basename(file)
                            )
                        part['Content-Disposition'] =\
                            'attachment; filename="%s"' % basename(file)
                        msg.attach(part)
                else:
                    if not os.path.exists(fileName):
                        raise FileNotFoundError
                    with open(fileName, "rb") as fil:
                        part = MIMEApplication(
                            fil.read(),
                            Name=basename(fileName)
                        )
                    part['Content-Disposition'] =\
                        'attachment; filename="%s"' % basename(fileName)
                    msg.attach(part)
            server.login(origen, password)
            server.sendmail(origen, destino.split(", "), msg.as_string())
            print("Successfully sent email")
    except FileNotFoundError:
        print(
            f"Error: unable to send email because cannot find file {fileName}"
        )
        logging.error(
            f"Error: unable to send email because cannot find file {fileName}"
        )
        raise Exception(
            f"Error: unable to send email because cannot find file {fileName}"

        )
    except Exception as e:
        print(f"Error: unable to send email: {e}")
        logging.error(f"Error: unable to send email: {e}")
        raise Exception(f"Error: unable to send email: {e}")


def mail_send(mensaje, destino, origen, asunto, server, puerto, password,
              isFile=False, fileName=None, copia=""):
    """
    Envia un correo con las caracteristicas dadas por parametros

    :param mensaje: mensaje a enviar
    :param destino: correo de destino, en una lista si son varios
    :param origen: correo de origen
    :param asunto: asunto del correo
    :param server: servidor smtp del correo
    :param puerto: puerto del servidor smtp
    :param password: contraseña del correo
    :param isFile: True o False
    :param fileName: ruta local al archivo
    :param copia: lista de personas en copia
    """
    try:
        email = EmailMessage()
        mensaje += '\n\n\n'
        email["From"] = origen
        email["To"] = destino
        email["Cc"] = copia
        email["Subject"] = asunto
        email.set_content(mensaje)
        if isFile:
            if 'list' in str(type(fileName)):
                for file in fileName:
                    if not os.path.exists(file):
                        raise FileNotFoundError
                    with open(file, "rb") as fil:
                        email.add_attachment(
                            fil.read(), maintype="application",
                            subtype="octet-stream", filename=basename(file)
                        )
            else:
                if not os.path.exists(fileName):
                    raise FileNotFoundError
                with open(fileName, "rb") as fil:
                    email.add_attachment(
                        fil.read(), maintype="application",
                        subtype="octet-stream", filename=basename(fileName)
                    )

        smtp = smtplib.SMTP(server, port=puerto)
        smtp.starttls()
        smtp.login(origen, password)
        failed_mails = smtp.sendmail(origen, destino, email.as_string())
        if failed_mails:
            print(failed_mails)
            logging.error(f'No se ha podido enviar correo a {destino}')
            smtp.quit()
            return False
        else:
            print(f'El mail a {destino} fue enviado...')
            smtp.quit()
            return True
    except FileNotFoundError:
        print(
            f"Error: unable to send email because cannot find file {fileName}"
        )
        logging.error(
            f"Error: unable to send email because cannot find file {fileName}"
        )
        raise Exception(
            f"Error: unable to send email because cannot find file {fileName}"

        )
    except Exception as e:
        print(f"Error: unable to send email: {e}")
        logging.error(f"Error: unable to send email: {e}")
        raise Exception(f"Error: unable to send email: {e}")


class API_microsoft():
    def obtenerAccessToken(self):
        """
        Esta función se encarga de obtener el access_token de Microsoft para poder usarlo en otras funciones.

        v2 - 03/11/2022 - Nueva función para obtener el access_token
        """

        config = json.load(open('parameters.json'))
        app = msal.ConfidentialClientApplication(
            config["client_id"], authority=config["authority"],
            client_credential=config["secret"],
        )

        result = None

        result = app.acquire_token_silent(config["scope"], account=None)

        if not result:
            logging.info(
                "No suitable token exists in cache. Let's get a new one from AAD.")
            result = app.acquire_token_for_client(scopes=config["scope"])

        if "access_token" in result:
            return result['access_token']
        else:
            return 'Error al obtener el accessToken'

    def getIdMicrosoft(self, email):
        """
        Obtenemos el id de Microsoft del correo electrónico pasado por parámetro mediante la api de Microsoft

        v2 - 03/11/2022 - Hemos sacado a otra funcion la obtención del acces_token

        :param email: email del empleado
        :return: id de Microsoft
        """

        accessToken = self.obtenerAccessToken()
        if accessToken:
            # Calling graph using the access token
            url = f"https://graph.microsoft.com/v1.0/users?$filter=startswith(mail,'{email}')"
            payload = {}
            headers = {
                'Authorization': 'Bearer ' + accessToken
            }
            response = requests.request("GET", url, headers=headers, data=payload)
            res = response.json()
            if response.status_code == 200:
                if len(res['value']) > 0:
                    return response.status_code, res['value'][0]['id']
                else:
                    return response.status_code, 'No id_microsoft'
            else:
                print(
                    f"Response: {response.status_code}, {email} -> {res['error']['message']}")
                logging.error(
                    f"Response: {response.status_code}, {email} -> {res['error']['message']}")
                return response.status_code, res['error']['message']
        else:
            print(accessToken)
            return 404, accessToken

    def enableDisableAccount(self, email, desbloquear):
        """
        Esta función se encarga de bloquear o desbloquear una cuenta de Microsoft.

        v2 - 03/11/2022 - Nueva función para bloquear y desbloquear usuarios.

        :param url: url con el correo que se desea atacar
        :param desbloquear: true para desbloquear / false para bloquear
        :return: 1 OK / 0 ERROR
        """

        accessToken = self.obtenerAccessToken()

        url = f"https://graph.microsoft.com/v1.0/users/{email}"
        if accessToken:
            # Calling graph using the access token
            payload = json.dumps({
                "accountEnabled": f"{desbloquear}"
            })
            headers = {
                'Authorization': 'Bearer ' + accessToken,
                'Content-type': 'application/json'
            }
            response = requests.request(
                "PATCH", url, headers=headers, data=payload)
            if response.status_code == 204:
                print(response)
                logging.info(f"Se ha bloqueado/desbloqueado con exito")
                return 1
            else:
                print(f"Response: {response.status_code} {response.content}")
                logging.error(
                    f"Response: {response.status_code} {response.content}")
                return 0
        else:
            logging.error("No se ha conseguido obtener el access_token")
            return 0

    def getRuleID(self, email):
        """
        Esta función se encarga de obtener el id de las reglas creadas por AutoDetox.

        v2 - 03/11/2022 - Función para obtener los IDs de las rules creadas por AutoDetox

        :param url: url con el correo que se desea atacar
        :param desbloquear: true para desbloquear / false para bloquear
        :return: 1 OK / 0 Error
        """
        url = f"https://graph.microsoft.com/v1.0/users/{email}/mailFolders/inbox/messageRules"\
            f"?$filter=displayName eq 'AutoDetox'&$select=id "
        accessToken = self.obtenerAccessToken()
        if accessToken:
            # Calling graph using the access token
            payload = {}
            headers = {
                'Authorization': 'Bearer ' + accessToken,
                'Content-type': 'application/json'
            }
            response = requests.request(
                "GET", url, headers=headers, data=payload)
            if response.status_code <= 210 and response.status_code >= 200:
                res = response.json()
                print(res['value'])
                return res['value']
            else:
                print(f"Response: {response.status_code} {response.content}")
                logging.error(
                    f"Response: {response.status_code} {response.content}")
                return
        else:
            logging.error("No se ha conseguido obtener el access_token")
            return

    def deshabilitar_redireccion(self, email):
        """
        Esta función se encarga de deshabilitar la redirección de una cuenta de Microsoft.
        Borramos una regla creada anteriormente.

        v2 - 03/11/2022 - Nueva función para deshabilitar redireccón

        :param email: email a deshabilitar redirección
        :return: 1 OK / 0 ERROR
        """
        accessToken = self.obtenerAccessToken()
        res = self.getRuleID(email)
        for i in res:
            url = f"https://graph.microsoft.com/v1.0/users/{email}/mailFolders/inbox/messageRules/{i['id']}"
            if accessToken:
                # Calling graph using the access token
                payload = {}
                headers = {
                    'Authorization': 'Bearer ' + accessToken,
                    'Content-type': 'application/json'
                }
                response = requests.request(
                    "DELETE", url, headers=headers, data=payload)
                if response.status_code <= 210 and response.status_code >= 200:
                    print('Borrado')
                    logging.info('Borrada la redirección con exito.')
                else:
                    print(f"Response: {response.status_code} {response.content}")
                    logging.error(
                        f"Response: {response.status_code} {response.content}")
                    return 0
            else:
                logging.error("No se ha conseguido obtener el access_token")
                return 0
        return 1

    def redireccionar(self, email, email_redireccion):
        """
        Esta función se encarga de redireccionar una cuenta de Microsoft.
        Para ello creamos una regla.

        v2 - 03/11/2022 - Nueva función para habilitar redirección

        :param email: email que se desea redireccionar
        :param email_redireccion: email hacia donde se redirecciona
        :return: 1 OK / 0 ERROR
        """
        url = f"https://graph.microsoft.com/v1.0/users/{email}/mailFolders/inbox/messageRules"
        accessToken = self.obtenerAccessToken()
        res = self.getRuleID(email)
        if res:
            logging.info(f'Ya hay una regla existente: {res}')
            return 1
        else:
            if accessToken:
                # Calling graph using the access token
                payload = json.dumps({
                    "displayName": "AutoDetox",
                    "sequence": 2,
                    "isEnabled": 'true',
                    "actions": {
                        "redirectTo": [
                            {
                                "emailAddress": {
                                    "address": f"{email_redireccion}"
                                }
                            }
                        ],
                    }
                })
                headers = {
                    'Authorization': 'Bearer ' + accessToken,
                    'Content-type': 'application/json'
                }
                response = requests.request(
                    "POST", url, headers=headers, data=payload)
                if response.status_code <= 210 and response.status_code >= 200:
                    print(response.content)
                    logging.info(f"Redireccionado de {email} a {email_redireccion}")
                    return 1
                else:
                    print(f"Response: {response.status_code} {response.content}")
                    logging.error(
                        f"Response: {response.status_code} {response.content}")
                    return 0
            else:
                logging.error("No se ha conseguido obtener el access_token")
                return 0


class samba_conection():
    def uploadFile(self, ruta_entrada, ruta_salida, smb_conection):
        """
        Módulo que se encarga de subir un archivo a una ruta en una unidad de red.

        :param ruta_entrada: Ruta del archivo que se quiere subir
        :param ruta_salida: Ruta donde se quiere subir el archivo en la unidad de red
        :param smb_conection: Diccionario con los datos de acceso a la unidad de red
        """
        try:
            with open(ruta_entrada, 'rb') as input:
                datos = input.read()
            register_session(smb_conection['server_ip'],
                             username=smb_conection['username'],
                             password=smb_conection['password'])
            with open_file(ruta_salida, 'wb') as output:
                output.write(datos)
            print(f'{ruta_salida} => Upload Success!')
            logging.info(
                f'{ruta_salida} => Upload Success!'
            )

        except Exception as e:
            msg = f'{e}'
            logging.error(msg)
            raise Exception(msg)

    def downloadFile(self, ruta_local, ruta_smb, smb_conection):
        """
        Módulo que descarga un archivo de una unidad de red a una ruta local.

        :param ruta_local: Ruta del archivo que se quiere descargar en una unidad de red 
        :param ruta_smb: Ruta donde se quiere subir el archivo
        :param smb_conection: Diccionario con los datos de acceso a la unidad de red
        """
        try:
            register_session(smb_conection['server_ip'],
                             username=smb_conection['username'],
                             password=smb_conection['password'])
            with open_file(ruta_smb, 'rb') as output:
                datos = output.read()

            with open(ruta_local, "wb") as input:
                input.write(datos)
            print(f'{ruta_local} => Download Success!')
            logging.info(
                f'{ruta_local} => Download Success!'
            )

        except Exception as e:
            msg = f'{e}'
            logging.error(msg)
            raise Exception(msg)

    def readFile(self, ruta_smb, smb_conection):
        """
        Módulo que lee un archivo de una unidad de red

        :param ruta_smb: Ruta donde se quiere subir el archivo
        :param smb_conection: Diccionario con los datos de acceso a la unidad de red
        """
        try:
            register_session(smb_conection['server_ip'],
                             username=smb_conection['username'],
                             password=smb_conection['password'])
            with open_file(ruta_smb, 'r') as output:
                datos = output.read()

            return datos

        except Exception as e:
            msg = f'{e}'
            logging.error(msg)
            raise Exception(msg)

    def readFile_binario(self, ruta_smb, smb_conection):
        """
        Módulo que lee un archivo binario de una unidad de red

        :param ruta_smb: Ruta donde se quiere subir el archivo
        :param smb_conection: Diccionario con los datos de acceso a la unidad de red
        """
        try:
            register_session(smb_conection['server_ip'],
                             username=smb_conection['username'],
                             password=smb_conection['password'])
            with open_file(ruta_smb, 'rb') as output:
                datos = output.read()

            return datos

        except Exception as e:
            msg = f'{e}'
            logging.error(msg)
            raise Exception(msg)

    def listar_dir(self, ruta_smb, smb_conection):
        """
        Módulo que lista los archivos y carpetas de un directorio en una unidad de red

        :param ruta_smb: Ruta donde se quiere listar
        :param smb_conection: Diccionario con los datos de acceso a la unidad de red
        """
        try:
            register_session(smb_conection['server_ip'],
                             username=smb_conection['username'],
                             password=smb_conection['password'])
            archivos_smb = []
            archivos = scandir(ruta_smb)
            archivos_smb = sorted(archivos_smb, key=lambda x: x['fecha_creacion'])
            for archivo in archivos:
                info = archivo.stat()
                # Obtiene la fecha de creación del archivo
                fecha_creacion = info.st_ctime
                archivos_smb.append({'nombre': archivo.name, 'fecha_creacion': fecha_creacion})
            return archivos_smb

        except Exception as e:
            msg = f'{e}'
            logging.error(msg)
            raise Exception(msg)
