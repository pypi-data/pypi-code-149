import requests
import json
import logging
from cryptography.fernet import Fernet
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
