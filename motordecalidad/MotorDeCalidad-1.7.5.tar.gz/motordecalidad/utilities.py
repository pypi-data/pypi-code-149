from motordecalidad.constants import *
from pyspark.sql import DataFrame
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(receiver_email = "operacionestelefonicabi.hispam@outlook.com"):
    import smtplib, ssl
    port = 587  # For SSL
    smtp_server = "smtp-mail.outlook.com"
    sender_email = "operacionestelefonicabi.hispam@outlook.com"
    password = "Telef0n1ca@2022"
    message = MIMEMultipart("alternative")
    message["Subject"] = "Ejecucion de Motor de Calidad"
    message["From"] = sender_email
    message["To"] = receiver_email

    # Create the plain-text and HTML version of your message
    text = """\
    Hola,
    Su ejecucion en el motorde calidad ha dado resultados erroneos que superan los limites establecidos """
    html = """\
    <html>
    <body>
        <p>Hola,<br>
        Su ejecucion en el motor de calidad ha dado resultados erroneos que superan los limites establecidos.
        </p>
    </body>
    </html>
    """
    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")
    message.attach(part1)
    message.attach(part2)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
#Function to define the dbutils library from Azure Databricks
def get_dbutils(spark):
        try:
            from pyspark.dbutils import DBUtils
            dbutils = DBUtils(spark)
        except ImportError:
            import IPython
            dbutils = IPython.get_ipython().user_ns["dbutils"]
        return dbutils
def applyFilter(object:DataFrame, filtered) :
    try:
        filteredColumn = filtered.get(JsonParts.Fields)
        filterValue = filtered.get(JsonParts.Values)
        print("Extracción de parametros de filtrado finalizada")
        return object.filter(col(filteredColumn)==filterValue)
    except:
        print("Se omite filtro")
        return object