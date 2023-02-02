class BaseNotionClass(Exception):
    def __init__(self, message, response) -> None:
        super().__init__(message)

        self.response = response


class InvalidJSON(BaseNotionClass):
    pass


class InvalidRequestUrl(BaseNotionClass):
    pass


class InvalidRequest(BaseNotionClass):
    pass


class ValidationError(BaseNotionClass):
    pass


class MissingVersion(BaseNotionClass):
    pass


class Unauthorized(BaseNotionClass):
    pass


class RestrictedResource(BaseNotionClass):
    pass


class ObjectNotFound(BaseNotionClass):
    pass


class ConflictError(BaseNotionClass):
    pass


class RateLimited(BaseNotionClass):
    pass


class InternalServerError(BaseNotionClass):
    pass


class ServiceUnavailable(BaseNotionClass):
    pass


class DatabaseConnectionUnavailable(BaseNotionClass):
    pass


ERRORS_MAP = {
    "invalid_json": InvalidJSON,
    "invalid_request_url": InvalidRequestUrl,
    "invalid_request": InvalidRequest,
    "validation_error": ValidationError,
    "missing_version": MissingVersion,
    "unauthorized": Unauthorized,
    "restricted_resource": RestrictedResource,
    "object_not_found": ObjectNotFound,
    "conflict_error": ConflictError,
    "rate_limited": RateLimited,
    "internal_server_error": InternalServerError,
    "service_unavailable": ServiceUnavailable,
    "database_connection_unavailable": DatabaseConnectionUnavailable,
}
