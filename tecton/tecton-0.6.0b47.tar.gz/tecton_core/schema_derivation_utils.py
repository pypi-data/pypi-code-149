from tecton_core import data_types as tecton_types
from tecton_proto.common import column_type_pb2
from tecton_proto.common import schema_pb2


# Keep in sync with DataTypeUtils.kt. Use "simple strings" as the keys so that fields like "nullable" are ignored.
TECTON_TYPE_TO_COLUMN_TYPE = {
    str(tecton_types.StringType()): schema_pb2.Column(
        raw_spark_type="string",
        feature_server_type=column_type_pb2.COLUMN_TYPE_STRING,
        offline_data_type=tecton_types.StringType().proto,
        feature_server_data_type=tecton_types.StringType().proto,
    ),
    str(tecton_types.Int64Type()): schema_pb2.Column(
        raw_spark_type="long",
        feature_server_type=column_type_pb2.COLUMN_TYPE_INT64,
        offline_data_type=tecton_types.Int64Type().proto,
        feature_server_data_type=tecton_types.Int64Type().proto,
    ),
    str(tecton_types.Float64Type()): schema_pb2.Column(
        raw_spark_type="double",
        feature_server_type=column_type_pb2.COLUMN_TYPE_DOUBLE,
        offline_data_type=tecton_types.Float64Type().proto,
        feature_server_data_type=tecton_types.Float64Type().proto,
    ),
    str(tecton_types.BoolType()): schema_pb2.Column(
        raw_spark_type="boolean",
        feature_server_type=column_type_pb2.COLUMN_TYPE_BOOL,
        offline_data_type=tecton_types.BoolType().proto,
        feature_server_data_type=tecton_types.BoolType().proto,
    ),
    # Int32 has a different offline and feature server data type.
    str(tecton_types.Int32Type()): schema_pb2.Column(
        raw_spark_type="integer",
        feature_server_type=column_type_pb2.COLUMN_TYPE_INT64,
        offline_data_type=tecton_types.Int32Type().proto,
        feature_server_data_type=tecton_types.Int64Type().proto,
    ),
    # Timestamp type is special since it does not have a ColumnType.
    str(tecton_types.TimestampType()): schema_pb2.Column(
        raw_spark_type="timestamp",
        feature_server_type=column_type_pb2.COLUMN_TYPE_DERIVE_FROM_DATA_TYPE,
        offline_data_type=tecton_types.TimestampType().proto,
        feature_server_data_type=tecton_types.TimestampType().proto,
    ),
    # Array types.
    str(tecton_types.ArrayType(tecton_types.Int64Type())): schema_pb2.Column(
        raw_spark_type="long_array",
        feature_server_type=column_type_pb2.COLUMN_TYPE_INT64_ARRAY,
        offline_data_type=tecton_types.ArrayType(tecton_types.Int64Type()).proto,
        feature_server_data_type=tecton_types.ArrayType(tecton_types.Int64Type()).proto,
    ),
    str(tecton_types.ArrayType(tecton_types.Float32Type())): schema_pb2.Column(
        raw_spark_type="float_array",
        feature_server_type=column_type_pb2.COLUMN_TYPE_FLOAT_ARRAY,
        offline_data_type=tecton_types.ArrayType(tecton_types.Float32Type()).proto,
        feature_server_data_type=tecton_types.ArrayType(tecton_types.Float32Type()).proto,
    ),
    str(tecton_types.ArrayType(tecton_types.Float64Type())): schema_pb2.Column(
        raw_spark_type="double_array",
        feature_server_type=column_type_pb2.COLUMN_TYPE_DOUBLE_ARRAY,
        offline_data_type=tecton_types.ArrayType(tecton_types.Float64Type()).proto,
        feature_server_data_type=tecton_types.ArrayType(tecton_types.Float64Type()).proto,
    ),
    str(tecton_types.ArrayType(tecton_types.StringType())): schema_pb2.Column(
        raw_spark_type="string_array",
        feature_server_type=column_type_pb2.COLUMN_TYPE_STRING_ARRAY,
        offline_data_type=tecton_types.ArrayType(tecton_types.StringType()).proto,
        feature_server_data_type=tecton_types.ArrayType(tecton_types.StringType()).proto,
    ),
}
