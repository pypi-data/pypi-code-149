from collections import namedtuple

METARIUM_FUNCTION_CALL_SERVICE_UPDATE_AS_ROOT = "force_update_service_info"
METARIUM_FUNCTION_CALL_SERVICE_REGISTER_AS_SCRIBE = "register_service"
METARIUM_FUNCTION_CALL_SERVICE_UPDATE_AS_SCRIBE = "update_service"
METARIUM_FUNCTION_CALL_SERVICE_DELETE_AS_SCRIBE = "delete_service"
METARIUM_FUNCTION_CALL_SERVICE_UPDATE_AS_SERVICE = "update_service_status"

ServiceStatusObject = namedtuple(
    "ServiceStatusObject",
    "status rff call_function caller call_index",
    defaults=[None, None, None, None, None]
)

ServiceOperation = namedtuple(
    "ServiceOperation",
    "update_as_root create_as_scribe update_as_scribe delete_as_scribe update_as_service",
    defaults=[
        METARIUM_FUNCTION_CALL_SERVICE_UPDATE_AS_ROOT,
        METARIUM_FUNCTION_CALL_SERVICE_REGISTER_AS_SCRIBE,
        METARIUM_FUNCTION_CALL_SERVICE_UPDATE_AS_SCRIBE,
        METARIUM_FUNCTION_CALL_SERVICE_DELETE_AS_SCRIBE,
        METARIUM_FUNCTION_CALL_SERVICE_UPDATE_AS_SERVICE
    ]
)