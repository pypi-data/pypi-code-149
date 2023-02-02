from toolkit.code_status_tkt import CodesStatusTkt
from toolkit.connection_setting import ConnectionSettings
from toolkit.utility import is_true
from toolkit.utility import to_string, request_post, request_get


def workstation_sign_in(connection_settings: ConnectionSettings,
                        content_dict: dict):
    """
    Logs into the workstation. Username of the operator should be set in ConnectionSettings. This generates the
    necessary. Authentication token for all sessions. Token will be stored in provided connection_settings.

    :param connection_settings: (ConnectionSettings) Contains the hostname, port, and username of the operator.
    :param content_dict: Dictionary containing username, workstation ApiKey, and credentials.

        .. code-block:: json

            {
                "UserName": "administrator",
                "Password": "mypass123",
                "ApiKey": "be5df8f2-524e-463e-8901-baa82eff1f88"
            }
    :return: Dictionary. The "content" key dictionary value will contain a token if successful. ConnectionSettings
        token will also be updated if successfully logged in.

        **Success**

        .. code-block:: json

            {
                "isLogin": true,
                "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6IiIsImdpdm"
            }

        **Failed**

        .. code-block:: json

            {
                "response": [
                    "Invalid login attempt."
                ]
            }
    """
    connection_url = "https://" + connection_settings.hostname + ":" + str(connection_settings.port) + \
                     "/shopfloorapi/auth/signin"

    logger = connection_settings.comm_logger

    result_dict = {
        "result": True,
        "status_code": 0,
        "content": []
    }

    status_code = [0]
    result = request_post(status_code=status_code,
                          logger=logger,
                          connection_url=connection_url,
                          content_dict=content_dict,
                          verify=False)

    if status_code[0] == 200:
        try:
            result_dict["content"] = result.json()

            # Storing Token into connection_settings
            if "token" in result_dict["content"].keys():
                connection_settings.token = result_dict["content"]["token"]

                logger.info(f"url={connection_url} content={content_dict}")
            else:
                logger.error(f"Failed login. url={connection_url} content={content_dict} "
                             f"response={result_dict}")

        except ValueError:  # If conversion causes an error
            result_dict["content"] = to_string(result.content)
            logger.info(f"Failed to convert response content to String. '{result.content}'")

        result_dict["status_code"] = result.status_code

    else:
        result_dict["result"] = False
        result_dict["status_code"] = status_code[0]

    return result_dict


def validate_user(connection_settings: ConnectionSettings,
                  content_dict: dict):
    """
    Checks if the specified user is a valid user - active and have proper access privilege

    .. warning::

        * Login is required, bearer token from login is needed for Authorization
        * If the username has been provided, then the password should also be provided (or other credentials like \
            RFID, etc).
        * If multiple credentials are provided, the validation will only return true if all values matches with the \
            username

    :param connection_settings: (ConnectionSettings) Contains the hostname, port, and token of the operator.
    :param content_dict: Dictionary (JSON), containing username, and credentials.

        .. code-block:: json

            {
                "UserName": "[username]",
                "Password": "[password]",
                "RFID":"[rfid_string]",
                "Voice": "[voice_string]",
                "Fingerprint": "[fingerprint_string]",
                "Iris": "[iris_string]"
            }
    :return: Dictionary. Value of "content" is  True if it's a valid username and credential(s)
    """
    result_dict = {
        "result": True,
        "status_code": 0,
        "content": []
    }

    logger = connection_settings.comm_logger

    connection_url = "https://" + connection_settings.hostname + ":" + str(connection_settings.port) + \
        "/shopfloorapi/auth/validateuser"

    if not connection_settings.token:
        logger.info("Token is empty. Try logging in first.")
        result_dict["result"] = False
        result_dict["status_code"] = CodesStatusTkt.ERR_CODE_NO_TOKEN.value
        return result_dict

    header = \
        {
            "content-type": "application/json",
            "Authorization": f"Bearer {connection_settings.token}",
        }

    status_code = [0]
    result = request_post(status_code=status_code,
                          logger=logger,
                          connection_url=connection_url,
                          content_dict=content_dict,
                          header=header,
                          verify=False)

    if status_code[0] == 200:
        result_dict["content"] = is_true(result.content)
        result_dict["status_code"] = result.status_code

        logger.info(f"url={connection_url} content={content_dict}"
                    f" response={result_dict}")
    else:
        result_dict["result"] = False
        result_dict["status_code"] = status_code[0]

    return result_dict


def validate_user_qualifications(connection_settings: ConnectionSettings,
                                 content_dict: dict):
    """
    Validates the specified user qualifications against the user qualifications set on the specified workflow step.

    .. warning::

        * Login is required, bearer token from login is needed for Authorization
        * If multiple credentials have been provided, all credentials should match the same user. For example if \
            the UserName provided is User1 then the RFID should also be User1's RFID, however Password is optional.

    :param connection_settings: (ConnectionSettings) Contains the hostname, port, and token of the operator.
    :param content_dict: Dictionary (JSON), containing username, credentials, and Transaction ID.

        .. code-block:: json

            {
                "UserName": "[username]",
                "Password": "[password]",
                "RFID":"[rfid_string]",
                "Voice": "[voice_string]",
                "Fingerprint": "[fingerprint_string]",
                "Iris": "[iris_string]",
                "TransactionId": "[transaction_id]"
            }
    :return: Dictionary. Value of "content" is True if user qualification matches on the specified transaction.
    """
    result_dict = {
        "result": True,
        "status_code": 0,
        "content": []
    }

    logger = connection_settings.comm_logger

    connection_url = "https://" + connection_settings.hostname + ":" + str(connection_settings.port) + \
                     "/shopfloorapi/auth/validateuserqualifications"

    if not connection_settings.token:
        logger.info("Token is empty. Try logging in first.")
        result_dict["result"] = False
        result_dict["status_code"] = CodesStatusTkt.ERR_CODE_NO_TOKEN.value
        return result_dict

    header = \
        {
            "content-type": "application/json",
            "Authorization": f"Bearer {connection_settings.token}",
        }

    status_code = [0]
    result = request_post(status_code=status_code,
                          logger=logger,
                          connection_url=connection_url,
                          content_dict=content_dict,
                          header=header,
                          verify=False)

    if status_code[0] == 200:
        result_dict["content"] = is_true(result.content)
        result_dict["status_code"] = result.status_code

        logger.info(f"url={connection_url} content={content_dict}"
                    f" response={result_dict}")
    else:
        result_dict["result"] = False
        result_dict["status_code"] = status_code[0]

    return result_dict


def create_transaction(connection_settings: ConnectionSettings,
                       content_dict: dict):
    """
    Creates a transaction that validates the current inventory quantity of the components used and the quantity of \
    the work order. Checks if the quantity of the origin bin is still enough and for a serialised product it would \
    check if the transaction has already been processed.

    The API returns a transaction token that will be used for the get spec, post transaction and other endpoints that \
    requires a transaction token.

    * BarCode could either be a work order or a serial number that will be processed.
    * WorkflowStep is required if there are multiple steps in a workflow that uses the same workstation.
    * Qty is the number of quantity to be processed in the transaction.
    * OperatorUserName is the username of the operator when transacting a containment transaction.
    * WorkStation is the work station identifier that will be used when transacting a containment transaction.

    :param connection_settings: (ConnectionSettings) Contains the hostname, port, and token of the operator.
    :param content_dict: Dictionary (JSON), containing username, credentials, and Transaction ID.

        .. code-block:: json

            {
                "BarCode":"JN00001SIM",
                "WorkflowStep":"WFS-278",
                "Qty": 1,
                "OperatorUserName" :"user1",
                "WorkStation":"WST-37"
            }

    :return: Dictionary. Value of "content" is True if user qualification matches on the specified transaction.

        .. code-block:: json

            {
                "isSuccess":true,
                "message":"",
                "data":"1cce7ba7-6aba-4fcb-8c6d-47283424fcf6"
            }
    """
    result_dict = {
        "result": True,
        "status_code": 0,
        "content": []
    }

    logger = connection_settings.comm_logger

    connection_url = "https://" + connection_settings.hostname + ":" + str(connection_settings.port) + \
                     "/api/shopfloor/transaction"

    if not connection_settings.token:
        logger.info("Token is empty. Try logging in first.")
        result_dict["result"] = False
        result_dict["status_code"] = CodesStatusTkt.ERR_CODE_NO_TOKEN.value
        return result_dict

    header = \
        {
            "content-type": "application/json",
            "Authorization": f"Bearer {connection_settings.token}",
        }

    status_code = [0]
    result = request_post(status_code=status_code,
                          logger=logger,
                          connection_url=connection_url,
                          content_dict=content_dict,
                          header=header,
                          verify=False)

    if status_code[0] == 200:
        try:
            result_dict["content"] = result.json()
            result_dict["status_code"] = result.status_code
        except ValueError:  # If conversion causes an error
            result_dict["content"] = to_string(result.content)
            logger.info(f"Failed to convert response content to String. '{result.content}'")

        logger.info(f"url={connection_url} content={content_dict}"
                    f" response={result_dict}")
    else:
        result_dict["result"] = False
        result_dict["status_code"] = status_code[0]

    return result_dict


def get_spec_no_transaction(connection_settings: ConnectionSettings,
                            content_dict: dict):
    """
    Any DBL attribute or test has to a ValueHEX and Value field. ValueHEX allows the raw unformulated number to be \
    sent to the platform, the platform then converts to DBL to store in the  database. The Value is a formatted \
    value from the machine that is human readable. The reason for sending up the raw unformulated value is that \
    it provides traceability  back to the number that the test was performed on.

    * BarCode can either be a work order number or a serial number, the platform is intelligent enough and return \
    the required data.
    * DataCollectionVersion is the spec version on which the user can specify, The default version is 0.01 and \
    the version number has increments of .01
    * WorkflowStep is required if there are multiple steps in a workflow that uses the same workstation.

    :param connection_settings: (ConnectionSettings) Contains the hostname, port, and token of the operator.
    :param content_dict: Dictionary (JSON), containing BarCode, DataCollectionVersion, and WorkflowStep.

        .. code-block:: json

            {
                "BarCode": "string",
                "WorkflowStep": "string",
                "VersionNumber": "string"
            }

    :return: Dictionary. Value of "content" is True if user qualification matches on the specified transaction.

        .. code-block:: json

            {
                "isSuccess": true,
                "message": "",
                "data": {
                    "id": None,
                    "workflowStepDataCollectionSpecId": None,
                    "checkSum": "56AA74AE2A562EB20B1A630117F34D7B",
                    "description": None,
                    "title": "sample file",
                    "accountId": "localhost;stage.medulla.net",
                    "workstationName": "Ascalon",
                    "workstationRefId": "WS-289",
                    "workstationId": 289,
                    "workstationAlias": "Diessa",
                    "stepName": "Step A",
                    "stepRefId": "WFS-1505",
                    "stepId": 1505,
                    "workflowName": "API_DOCUMENTATION",
                    "workflowRefId": "WF-516",
                    "workflowId": 516,
                    "workflowVer": "WF-516-1",
                    "location": "Ascalon1",
                    "loginUser": "amedrano",
                    "loginUserId": 268,
                    "getSpecTime": "2021-10-06T11:01:06.4851137Z",
                    "postSpecTime": None,
                    "barcode": "API DOCUMENTATION",
                    "barcodeUser": None,
                    "partNumber": " FP1006-NB-2",
                    "partNumberId": 587,
                    "partNumberRev": "1",
                    "partNumberRevId": 617,
                    "quantity": 1000,
                    "batchTestQuantity": None,
                    "comment": None,
                    "commentUser": None,
                    "abortReason": None,
                    "abortUser": None,
                    "status": None,
                    "firstFail": None,
                    "failCode": None,
                    "workstationLocation": "Ascalon1",
                    "workstationTimeZone": None,
                    "transactionApiValue": None,
                    "dataCollectionId": 920,
                    "dataCollectionVersion": "1",
                    "dataCollectionVersionId": 218,
                    "grade": None,
                    "events": [],
                    "attributes": [],
                    "tests": [
                        {
                            "id": 751,
                            "name": "boolean test 1",
                            "dataType": "Boolean",
                            "value": None,
                            "valueDim": 0,
                            "displayFormat": None,
                            "units": None,
                            "dependantItem": None,
                            "procedure": None,
                            "parameters": None,
                            "schema": None,
                            "timeAcquired": None,
                            "status": None,
                            "valueRange": None,
                            "valueOperator": None,
                            "valueCompare": true,
                            "failCode": "Fail 1",
                            "contOnFail": true,
                            "user": None,
                            "comment": None,
                            "isPass": false,
                            "defaultValue": None
                        }
                    ],
                    "components": [],
                    "constants": [],
                    "gradingSequence": [],
                    "sequence": [],
                    "webform": [
                        {
                            "id": 265,
                            "item": "boolean test 1",
                            "label": "Is it valid",
                            "enableDefault": false,
                            "defaultValue": None,
                            "retain": true,
                            "buttonLabel": "Test"
                        }
                    ]
                }
            }
    """
    result_dict = {
        "result": True,
        "status_code": 0,
        "content": []
    }

    logger = connection_settings.comm_logger

    connection_url = "https://" + connection_settings.hostname + ":" + str(connection_settings.port) + \
                     "/api/shopfloor/specnotransact"

    if not connection_settings.token:
        logger.info("Token is empty. Try logging in first.")
        result_dict["result"] = False
        result_dict["status_code"] = CodesStatusTkt.ERR_CODE_NO_TOKEN.value
        return result_dict

    header = \
        {
            "content-type": "application/json",
            "Authorization": f"Bearer {connection_settings.token}",
        }

    status_code = [0]
    result = request_get(status_code=status_code,
                         logger=logger,
                         connection_url=connection_url,
                         content_dict=content_dict,
                         header=header,
                         verify=False)

    if status_code[0] == 200:
        try:
            result_dict["content"] = result.json()
        except ValueError:  # If conversion causes an error
            result_dict["content"] = to_string(result.content)
            logger.info(f"Failed to convert response content to String. '{result.content}'")

        result_dict["status_code"] = result.status_code
        logger.info(f"url={connection_url} content={content_dict}"
                    f" response={result_dict}")
    else:
        result_dict["result"] = False
        result_dict["status_code"] = status_code[0]

    return result_dict


def abort_transaction(connection_settings: ConnectionSettings,
                      content_dict: dict):
    """
    Aborts the transaction specified by the transaction API key

    :param connection_settings: (ConnectionSettings) Contains the hostname, port, and token of the operator.
    :param content_dict: Dictionary (JSON), containing username, credentials, and Transaction ID.

        .. code-block:: json

            {
                "TransactionID": "63aa0b5f-a724-4408-b45d-8bf9aa4bcec5"
            }

    :return: Dictionary. Value of "content" is a directory shown below.

        **SUCCESS**

        .. code-block:: json

            {
                "isSuccess": true,
                "message": "Transaction successfully aborted."
            }

        **FAILED**

        .. code-block:: json

            {
                "isSuccess": false,
                "message": "",
                "errors": [
                    {
                        "code": "AbortTransactionFail",
                        "description": "Cannot abort an already aborted transaction."
                    }
                ]
            }
    """
    result_dict = {
        "result": True,
        "status_code": 0,
        "content": []
    }

    logger = connection_settings.comm_logger

    connection_url = "https://" + connection_settings.hostname + ":" + str(connection_settings.port) + \
                     "/api/shopfloor/aborttransaction"

    if not connection_settings.token:
        logger.info("Token is empty. Try logging in first.")
        result_dict["result"] = False
        result_dict["status_code"] = CodesStatusTkt.ERR_CODE_NO_TOKEN.value
        return result_dict

    header = \
        {
            "content-type": "application/json",
            "Authorization": f"Bearer {connection_settings.token}",
        }

    status_code = [0]
    result = request_post(status_code=status_code,
                          logger=logger,
                          connection_url=connection_url,
                          content_dict=content_dict,
                          header=header,
                          verify=False)

    if status_code[0] == 200:
        try:
            result_dict["content"] = result.json()
            result_dict["status_code"] = result.status_code
        except ValueError:  # If conversion causes an error
            result_dict["content"] = to_string(result.content)
            logger.info(f"Failed to convert response content to String. '{result.content}'")

        logger.info(f"url={connection_url} content={content_dict}"
                    f" response={result_dict}")
    else:
        result_dict["result"] = False
        result_dict["status_code"] = status_code[0]

    return result_dict


def generate_work_order(connection_settings: ConnectionSettings,
                        content_dict: dict):
    """
    Generates a work order through the API.

    .. note::

        The validations of this end point might be outdated since there are new validations that are in place.

        * WorkOrderNumber is the work order number that will be used when generating the work order.
        * Name of the work order.
        * WorkflowIdentifier is the identifier of the process that the work order will go through.
        * WorkFlowRevisionNumber is the specific revision number that will be used in the work order.
        * ProductionType is the classification of the work order may be it be either production, engineering and more.
        * IssueDate is the date and time on which the work order was issued.
        * PurchaseOrder of the work order.
        * Comments or notes for the work order.
        * PartNumber is the product that will be used in the work order
        * ProductVersion is the revision of that product that will be used in the work order.
        * SerialMask is the mask that will be used when auto generating serial numbers.
        * Quantity that will be allocated to the work order.
        * BatchTestQuantity is the quantity that will be used in random testing for the products in the work order.

    :param connection_settings: (ConnectionSettings) Contains the hostname, port, and token of the operator.
    :param content_dict: Dictionary (JSON), containing work order information like Name, WorkflowIdentifier,
    WorkflowVersion, PartNumber, etc.

        .. code-block:: json

            {
                "WorkOrderNumber": "Batch API Generate WO12-ANN",
                "Name":"BATCH NAME API2-ANN",
                "WorkflowIdentifier":"WF-189",
                "WorkflowVersion":1,
                "ProductionType": "approved",
                "IssueDate":"2021-10-06T19:16:12",
                "PurchaseOrder":"PO BATCH API",
                "Comments": "COMMENT TEST API",
                "PartNumber":"Batch API Generate",
                "ProductVersion":"v1",
                "SerialMask":null,
                "Quantity":100,
                "TestBatchQuantity":25
            }

    :return: Dictionary. Value of "content" is a directory shown below.

        **SUCCESS**

        .. code-block:: json

            {
                "isSuccess": true,
                "message": "Work Order generated successfully."
            }
    """
    result_dict = {
        "result": True,
        "status_code": 0,
        "content": []
    }

    logger = connection_settings.comm_logger

    connection_url = "https://" + connection_settings.hostname + ":" + str(connection_settings.port) + \
                     "/shopfloorapi/workorder/api"

    if not connection_settings.token:
        logger.info("Token is empty. Try logging in first.")
        result_dict["result"] = False
        result_dict["status_code"] = CodesStatusTkt.ERR_CODE_NO_TOKEN.value
        return result_dict

    header = \
        {
            "content-type": "application/json",
            "Authorization": f"Bearer {connection_settings.token}",
        }

    status_code = [0]
    result = request_post(status_code=status_code,
                          logger=logger,
                          connection_url=connection_url,
                          content_dict=content_dict,
                          header=header,
                          verify=False)

    if status_code[0] == 200:
        try:
            result_dict["content"] = result.json()
            result_dict["status_code"] = result.status_code
        except ValueError:  # If conversion causes an error
            result_dict["content"] = to_string(result.content)
            logger.info(f"Failed to convert response content to String. '{result.content}'")

        logger.info(f"url={connection_url} content={content_dict}"
                    f" response={result_dict}")
    else:
        result_dict["result"] = False
        result_dict["status_code"] = status_code[0]

    return result_dict


def work_order_query(connection_settings: ConnectionSettings,
                     content_dict: dict):
    """
    Returns the detail of the work order.

    WorkOrderNumber is the unique identifier on which the platform will use to indicate which work order data to return.

    :param connection_settings: (ConnectionSettings) Contains the hostname, port, and token of the operator.
    :param content_dict: Dictionary (JSON), containing work order number.

        .. code-block:: json

            {
                "WorkOrderNumber": "API DOCUMENTATION"
            }

    :return: Dictionary. Value of "content" is a directory shown below.

        **SUCCESS**

        .. code-block:: json

            {
                "isSuccess": true,
                "message": "",
                "data": {
                    "workorderNumber": "API DOCUMENTATION",
                    "testBatchQuantity": null,
                    "quantity": 1000,
                    "partNumber": " FP1006-NB-2"
                }
            }

        ** FAILED **

        .. code-block:: json

            {
                "isSuccess": false,
                "message": "WorkOrderNumber not found."
            }
    """
    result_dict = {
        "result": True,
        "status_code": 0,
        "content": []
    }

    logger = connection_settings.comm_logger

    connection_url = "https://" + connection_settings.hostname + ":" + str(connection_settings.port) + \
                     "/api/shopfloor/workorder"

    if not connection_settings.token:
        logger.info("Token is empty. Try logging in first.")
        result_dict["result"] = False
        result_dict["status_code"] = CodesStatusTkt.ERR_CODE_NO_TOKEN.value
        return result_dict

    header = \
        {
            "content-type": "application/json",
            "Authorization": f"Bearer {connection_settings.token}",
        }

    status_code = [0]

    result = request_get(status_code=status_code,
                         logger=logger,
                         connection_url=connection_url,
                         content_dict=content_dict,
                         header=header,
                         verify=False)

    if status_code[0] == 200:
        try:
            result_dict["content"] = result.json()
            result_dict["status_code"] = result.status_code
        except ValueError:  # If conversion causes an error
            result_dict["content"] = to_string(result.content)
            logger.info(f"Failed to convert response content to String. '{result.content}'")

        logger.info(f"url={connection_url} content={content_dict}"
                    f" response={result_dict}")
    else:
        result_dict["result"] = False
        result_dict["status_code"] = status_code[0]

    return result_dict


def get_spec(connection_settings: ConnectionSettings,
             content_dict: dict):
    """
    Gets the test spec that was imported in the platform. The API returns a formatted spec that can be used by the \
    test system to set the values and other parameters. The Spec is a document that instructs a machine regarding \
    tests to perform, attributes to collect and components to capture.

    The spec is basically a document that the machine fills out and then posts back to the platform. The spec is \
    designed to be saved by a machine in an offline mode and to be posted later.

    .. note::

        Any DBL attribute or test has to a ValueHEX and Value field. ValueHEX allows the raw unformulated number to \
        be sent to the platform, the platform then converts to DBL to store in the  database. The Value is a \
        formatted value from the machine that is human readable. The reason for sending up the raw unformulated \
        value is that it provides traceability  back to the number that the test was performed on.

    Components are a list for both batch and serial.
    * VersionNumber is the spec version on which the user can specify, The default version is 0.01 and the version \
    number has increments of .01


    :param connection_settings: (ConnectionSettings) Contains the hostname, port, and token of the operator.
    :param content_dict: Dictionary (JSON),TransactionID, and VersionNumber.

        .. code-block:: json

            {
                "TransactionID": "2df2399e-5896-4472-82e2-915d84f66b31",
                "VersionNumber": null
            }

    :return: Dictionary. Value of "content" is a directory shown below.

        .. code-block:: json

            {
                "isSuccess": true,
                "message": "",
                "data": {
                    "id": None,
                    "workflowStepDataCollectionSpecId": None,
                    "checkSum": "56AA74AE2A562EB20B1A630117F34D7B",
                    "description": None,
                    "title": "sample file",
                    "accountId": "localhost;stage.medulla.net",
                    "workstationName": "Ascalon",
                    "workstationRefId": "WS-289",
                    "workstationId": 289,
                    "workstationAlias": "Diessa",
                    "stepName": "Step A",
                    "stepRefId": "WFS-1505",
                    "stepId": 1505,
                    "workflowName": "API_DOCUMENTATION",
                    "workflowRefId": "WF-516",
                    "workflowId": 516,
                    "workflowVer": "WF-516-1",
                    "location": "Ascalon1",
                    "loginUser": "amedrano",
                    "loginUserId": 268,
                    "getSpecTime": "2021-10-06T11:01:06.4851137Z",
                    "postSpecTime": None,
                    "barcode": "API DOCUMENTATION",
                    "barcodeUser": None,
                    "partNumber": " FP1006-NB-2",
                    "partNumberId": 587,
                    "partNumberRev": "1",
                    "partNumberRevId": 617,
                    "quantity": 1000,
                    "batchTestQuantity": None,
                    "comment": None,
                    "commentUser": None,
                    "abortReason": None,
                    "abortUser": None,
                    "status": None,
                    "firstFail": None,
                    "failCode": None,
                    "workstationLocation": "Ascalon1",
                    "workstationTimeZone": None,
                    "transactionApiValue": None,
                    "dataCollectionId": 920,
                    "dataCollectionVersion": "1",
                    "dataCollectionVersionId": 218,
                    "grade": None,
                    "events": [],
                    "attributes": [],
                    "tests": [
                        {
                            "id": 751,
                            "name": "boolean test 1",
                            "dataType": "Boolean",
                            "value": None,
                            "valueDim": 0,
                            "displayFormat": None,
                            "units": None,
                            "dependantItem": None,
                            "procedure": None,
                            "parameters": None,
                            "schema": None,
                            "timeAcquired": None,
                            "status": None,
                            "valueRange": None,
                            "valueOperator": None,
                            "valueCompare": true,
                            "failCode": "Fail 1",
                            "contOnFail": true,
                            "user": None,
                            "comment": None,
                            "isPass": false,
                            "defaultValue": None
                        }
                    ],
                    "components": [],
                    "constants": [],
                    "gradingSequence": [],
                    "sequence": [],
                    "webform": [
                        {
                            "id": 265,
                            "item": "boolean test 1",
                            "label": "Is it valid",
                            "enableDefault": false,
                            "defaultValue": None,
                            "retain": true,
                            "buttonLabel": "Test"
                        }
                    ]
                }
            }
    """
    result_dict = {
        "result": True,
        "status_code": 0,
        "content": []
    }

    logger = connection_settings.comm_logger

    connection_url = "https://" + connection_settings.hostname + ":" + str(connection_settings.port) + \
                     "/api/shopfloor/spec"

    if not connection_settings.token:
        logger.info("Token is empty. Try logging in first.")
        result_dict["result"] = False
        result_dict["status_code"] = CodesStatusTkt.ERR_CODE_NO_TOKEN.value
        return result_dict

    header = \
        {
            "content-type": "application/json",
            "Authorization": f"Bearer {connection_settings.token}",
        }

    status_code = [0]
    result = request_get(status_code=status_code,
                         logger=logger,
                         connection_url=connection_url,
                         content_dict=content_dict,
                         header=header,
                         verify=False)

    if status_code[0] == 200:
        try:
            result_dict["content"] = result.json()
        except ValueError:  # If conversion causes an error
            result_dict["content"] = to_string(result.content)
            logger.info(f"Failed to convert response content to String. '{result.content}'")

        result_dict["status_code"] = result.status_code
        logger.info(f"url={connection_url} content={content_dict}"
                    f" response={result_dict}")
    else:
        result_dict["result"] = False
        result_dict["status_code"] = status_code[0]

    return result_dict


def get_time(connection_settings: ConnectionSettings,
             content_dict: dict):
    """
    Gets the Coordinated Universal Time from the platform with a standard format for all the date related data. The \
    endpoint is usuallly used in the pre-post transaction where the test system populates the time acquired.

    :param connection_settings: (ConnectionSettings) Contains the hostname, port, and token of the operator.
    :param content_dict: Dictionary (JSON), empty content

        .. code-block:: json

            {
            }

    :return: Dictionary. Value of "content" is True if time is successfully retrieved.

        .. code-block:: json

            {
                "isSuccess": true,
                "message": "Successfully fetched current date time.",
                "data": "06/10/2021 10:21:24"
            }
    """
    result_dict = {
        "result": True,
        "status_code": 0,
        "content": []
    }

    logger = connection_settings.comm_logger

    connection_url = "https://" + connection_settings.hostname + ":" + str(connection_settings.port) + \
                     "/api/shopfloor/time"

    if not connection_settings.token:
        logger.info("Token is empty. Try logging in first.")
        result_dict["result"] = False
        result_dict["status_code"] = CodesStatusTkt.ERR_CODE_NO_TOKEN.value
        return result_dict

    header = \
        {
            "content-type": "application/json",
            "Authorization": f"Bearer {connection_settings.token}",
        }

    status_code = [0]
    result = request_get(status_code=status_code,
                         logger=logger,
                         connection_url=connection_url,
                         content_dict=content_dict,
                         header=header,
                         verify=False)

    if status_code[0] == 200:
        try:
            result_dict["content"] = result.json()
        except ValueError:  # If conversion causes an error
            result_dict["content"] = to_string(result.content)
            logger.info(f"Failed to convert response content to String. '{result.content}'")

        result_dict["status_code"] = result.status_code
        logger.info(f"url={connection_url} content={content_dict}"
                    f" response={result_dict}")
    else:
        result_dict["result"] = False
        result_dict["status_code"] = status_code[0]

    return result_dict


def get_transaction_api(connection_settings: ConnectionSettings,
                        content_dict: dict):
    """
    Gets the stats of the scanned barcode. This returns the barcode’s workorder details like name and number. This \
    will also return the current barcode location, the number of times the barcode has been scanned, and the \
    barcode status.

    :param connection_settings: (ConnectionSettings) Contains the hostname, port, and token of the operator.
    :param content_dict: Dictionary (JSON), containing the bar code

        .. code-block:: json

            {
                "BarCode": "CP-00000001-PF"
            }

    :return: Dictionary. Value of "content" is True if Transaction information is found and returned.

        .. code-block:: json

            {
                "isSuccess": true,
                "message": "",
                "data": {
                    "workorderNumber": "WO-COFFEE_PRESS",
                    "wokorkoderName": "WO-COFFEE_PRESS",
                    "barcode": "CP-00000001-PF",
                    "workflowLocation": "WFS-1521",
                    "status": "Work in progress",
                    "transactionApiRecordCount": 7
                }
            }
    """
    result_dict = {
        "result": True,
        "status_code": 0,
        "content": []
    }

    logger = connection_settings.comm_logger

    connection_url = "https://" + connection_settings.hostname + ":" + str(connection_settings.port) + \
                     "/api/shopfloor/gettransactionapi"

    if not connection_settings.token:
        logger.info("Token is empty. Try logging in first.")
        result_dict["result"] = False
        result_dict["status_code"] = CodesStatusTkt.ERR_CODE_NO_TOKEN.value
        return result_dict

    header = \
        {
            "content-type": "application/json",
            "Authorization": f"Bearer {connection_settings.token}",
        }

    status_code = [0]
    result = request_get(status_code=status_code,
                         logger=logger,
                         connection_url=connection_url,
                         content_dict=content_dict,
                         header=header,
                         verify=False)

    if status_code[0] == 200:
        try:
            result_dict["content"] = result.json()
        except ValueError:  # If conversion causes an error
            result_dict["content"] = to_string(result.content)
            logger.info(f"Failed to convert response content to String. '{result.content}'")

        result_dict["status_code"] = result.status_code
        logger.info(f"url={connection_url} content={content_dict}"
                    f" response={result_dict}")
    else:
        result_dict["result"] = False
        result_dict["status_code"] = status_code[0]

    return result_dict


def get_data(connection_settings: ConnectionSettings,
             content_dict: dict):
    """
    Gets the artifact data from the moment of the transaction was made and returns a data collection formatted \
    attribute with the values that were transacted.

    * NameOfAttribute is the name key in the test spec which was imported into the platform. This is a unique \
    identifier that can be used to determine in the dependent item key.
    * WorkflowStepId is the step identifier that can be viewed in the workflow → workflowstep configuration.
    * SerialNumber is the serial number that is used during the transaction. This is optional and can only be \
    used if the product is serialised.

    :param connection_settings: (ConnectionSettings) Contains the hostname, port, and token of the operator.
    :param content_dict: Dictionary (JSON), empty content

        .. code-block:: json

            {
                "BarCode": "API DOCUMENTATION",
                "WorkflowStep": null,
                "VersionNumber": null,
                "Name": null
            }

    :return: Dictionary. Value of "content" is True if data is successfully retrieved.

        .. code-block:: json

            {
                "isSuccess": true,
                "message": "",
                "data": {
                    "attributes": [],
                    "tests": [],
                    "components": [],
                    "constants": [],
                    "gradingSequence": [],
                    "sequence": []
                }
            }
    """
    result_dict = {
        "result": True,
        "status_code": 0,
        "content": []
    }

    logger = connection_settings.comm_logger

    connection_url = "https://" + connection_settings.hostname + ":" + str(connection_settings.port) + \
                     "/api/shopfloor/getdata"

    if not connection_settings.token:
        logger.info("Token is empty. Try logging in first.")
        result_dict["result"] = False
        result_dict["status_code"] = CodesStatusTkt.ERR_CODE_NO_TOKEN.value
        return result_dict

    header = \
        {
            "content-type": "application/json",
            "Authorization": f"Bearer {connection_settings.token}",
        }

    status_code = [0]
    result = request_get(status_code=status_code,
                         logger=logger,
                         connection_url=connection_url,
                         content_dict=content_dict,
                         header=header,
                         verify=False)

    if status_code[0] == 200:
        try:
            result_dict["content"] = result.json()
        except ValueError:  # If conversion causes an error
            result_dict["content"] = to_string(result.content)
            logger.info(f"Failed to convert response content to String. '{result.content}'")

        result_dict["status_code"] = result.status_code
        logger.info(f"url={connection_url} content={content_dict}"
                    f" response={result_dict}")
    else:
        result_dict["result"] = False
        result_dict["status_code"] = status_code[0]

    return result_dict
