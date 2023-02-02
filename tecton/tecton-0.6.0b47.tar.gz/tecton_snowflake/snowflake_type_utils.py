from tecton_core import data_types as tecton_types
from tecton_core import errors


# Keep in sync with DataTypeUtils.kt
def snowflake_type_to_tecton_type(snowflake_type: str, column_name: str) -> tecton_types.DataType:
    if snowflake_type == "VARCHAR":
        return tecton_types.StringType()
    elif snowflake_type == "NUMBER":
        return tecton_types.Int64Type()
    elif snowflake_type == "FLOAT":
        return tecton_types.Float64Type()
    elif snowflake_type == "BOOLEAN":
        return tecton_types.BoolType()
    elif snowflake_type == "TIMESTAMP_NTZ":
        return tecton_types.TimestampType()
    elif snowflake_type == "TIMESTAMP_TZ" or snowflake_type == "TIMESTAMP_LTZ":
        raise errors.TectonValidationError(
            f"Timestamp type {snowflake_type} for column {column_name} is not supported because it contains a timezone.Please use TIMESTAMP_NTZ instead."
        )
    else:
        raise errors.TectonValidationError(f"Unsupported Snowflake type {snowflake_type} for column {column_name}.")
