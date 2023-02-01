import tensorflow as tf
from google.protobuf import text_format
from object_detection.protos import pipeline_pb2
from typing import Optional


class Parser:
    @staticmethod
    def read_pipeline(pipeline_config_path, config_override=None) -> Optional[pipeline_pb2.TrainEvalPipelineConfig]:
        """!
        Read pipeline.config file.
        @param pipeline_config_path:
        @param config_override:
        @return
        """
        pipeline_config = pipeline_pb2.TrainEvalPipelineConfig()
        with tf.io.gfile.GFile(pipeline_config_path, "r") as f:
            proto_str = f.read()
            text_format.Merge(proto_str, pipeline_config)
        if config_override:
            text_format.Merge(config_override, pipeline_config)
        return pipeline_config

    @staticmethod
    def write_pipeline(pipeline_config, pipeline_config_path) -> None:
        """!
        Write pipeline.config file.
        @param pipeline_config: pipeline.config text.
        @param pipeline_config_path: New pipeline.config path.
        @return
        """
        config_text = text_format.MessageToString(pipeline_config)

        with tf.io.gfile.GFile(pipeline_config_path, "wb") as f:
            f.write(config_text)
