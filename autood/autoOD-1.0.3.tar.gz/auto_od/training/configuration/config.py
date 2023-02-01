from typing import List, Tuple

from auto_od.core.logger import logger
from auto_od.training.configuration.augmentation import Augmentation


class PipelineConfig(Augmentation):
    def __init__(self, config_path: str):
        super().__init__(config_path=config_path)

        self.training_methods = {
            'is_custom_settings': self.settings.is_custom_settings,
            'is_prevent_overfitting': self.settings.is_prevent_overfitting,
            'is_loss_function': self.settings.is_loss_function,
        }
        self.augmentation_methods = {
            'normalize_image': self.settings.normalize_image,
            'horizontal_flip': self.settings.horizontal_flip,
            'vertical_flip': self.settings.vertical_flip,
            'rotation90': self.settings.rotation90,
            'pixel_value_scale': self.settings.pixel_value_scale,
            'entire_rgb_to_grey': self.settings.entire_rgb_to_grey,
            'adjust_brightness': self.settings.adjust_brightness,
            'adjust_contrast': self.settings.adjust_contrast,
            'adjust_hue': self.settings.adjust_hue,
            'adjust_saturation': self.settings.adjust_saturation,
            'distort_color': self.settings.distort_color,
            'crop_image': self.settings.crop_image,
            'pad_image': self.settings.pad_image,
            'crop_pad_image': self.settings.crop_pad_image,
            'crop_to_aspect_ratio': self.settings.crop_to_aspect_ratio,
            'black_patches': self.settings.black_patches,
            'rgb_to_grey': self.settings.rgb_to_grey,
            'drop_label_probabilistically': self.settings.drop_label_probabilistically,
            'jpeg_quality': self.settings.jpeg_quality,
            'patch_gaussian': self.settings.patch_gaussian
        }

    def default_settings(self, pipeline_dir: str, new_pipeline_dir: str, test_record: str, train_record: str,
                         fine_tune_checkpoint: str,
                         label_map_dir: str, annotations: List[str]) -> None:
        """!
        Necessary default settings to start training.
        @param pipeline_dir: File pipeline.config.
        @param new_pipeline_dir: New pipeline.config file.
        @param test_record: test_record path.
        @param train_record: train_record path.
        @param fine_tune_checkpoint: Pretrained model checkpoint.
        @param label_map_dir: Label Map path.
        @param annotations: Objects' list.
        @return
        """
        configuration = self.read_pipeline(pipeline_dir)
        configuration.train_input_reader.tf_record_input_reader.input_path[0] = train_record
        configuration.train_input_reader.label_map_path = label_map_dir

        configuration.eval_input_reader[0].tf_record_input_reader.input_path[0] = test_record
        configuration.eval_input_reader[0].label_map_path = label_map_dir

        configuration.train_config.fine_tune_checkpoint = fine_tune_checkpoint
        configuration.train_config.fine_tune_checkpoint_type = 'detection'

        if configuration.model.HasField('ssd'):
            configuration.model.ssd.num_classes = len(annotations)
        elif configuration.model.HasField('center_net'):
            configuration.model.center_net.num_classes = len(annotations)
        else:
            configuration.model.faster_rcnn.num_classes = len(annotations)
        self.write_pipeline(configuration, new_pipeline_dir)
        logger.info("Default settings has been changed: train_record, test_record, label_map_path, "
                    "fine_tune_checkpoint, fine_tune_checkpoint_type, num_classes. "
                    "See changes: {0}".format(new_pipeline_dir))

    def custom_settings(self, new_pipeline_dir: str) -> None:
        """!
        Custom parameters (is_custom_settings parameter). Changed values: model_id, batch_size, num_steps.
        @param new_pipeline_dir: New pipeline.config file.
        @return
        """
        FLAG = True
        configuration = self.read_pipeline(new_pipeline_dir)

        configuration.train_config.num_steps = self.settings.num_steps
        configuration.train_config.batch_size = self.settings.batch_size

        current_optimizer = configuration.train_config.optimizer
        if current_optimizer.HasField('adam_optimizer') and current_optimizer.adam_optimizer.learning_rate.HasField(
                'cosine_decay_learning_rate'):
            current_optimizer.adam_optimizer.learning_rate.cosine_decay_learning_rate.total_steps = \
                self.settings.num_steps
        elif current_optimizer.HasField('momentum_optimizer') and \
                current_optimizer.momentum_optimizer.learning_rate.HasField('cosine_decay_learning_rate'):
            current_optimizer.momentum_optimizer.learning_rate.cosine_decay_learning_rate.total_steps = \
                self.settings.num_steps
        else:
            FLAG = False
            logger.info('Optimizer is not adam_optimizer or momentum_optimizer, or manual learning_rate used.')
        self.write_pipeline(configuration, new_pipeline_dir)
        if FLAG:
            logger.info("Custom settings has been changed: num_steps - {0}, batch_size - {1}, optimizer's "
                        "total_steps - {0}. See changes: {2}".format(self.settings.num_steps,
                                                                     self.settings.batch_size, new_pipeline_dir))

    def prevent_overfitting(self, new_pipeline_dir: str) -> None:
        """!
        Use dropout and score threshold (non-maximum suppression) to prevent model's overfitting.
        @param new_pipeline_dir: New pipeline.config file.
        @return
        """
        configuration = self.read_pipeline(new_pipeline_dir)
        if configuration.model.HasField('ssd'):
            if self.settings.use_score_threshold:
                configuration.model.ssd.post_processing.batch_non_max_suppression.score_threshold = 0.2
                logger.info("Score threshold has been changed. New value: 0.2.")

        if configuration.model.HasField('faster_rcnn'):
            if self.settings.use_score_threshold:
                configuration.model.faster_rcnn.second_stage_post_processing.batch_non_max_suppression.\
                    score_threshold = 0.2
                logger.info("Score threshold has been changed. New value: 0.2.")
            if self.settings.use_dropout:
                configuration.model.faster_rcnn.second_stage_box_predictor.mask_rcnn_box_predictor.use_dropout = True
                configuration.model.faster_rcnn.second_stage_box_predictor.\
                    mask_rcnn_box_predictor.dropout_keep_probability = 0.8
                logger.info("Pipeline.config has been changed. Dropout will be used. Probability: 0.2.")

            max_total_detections = configuration.model.faster_rcnn.\
                second_stage_box_predictor.batch_non_max_suppression.max_detections_per_class
            configuration.model.faster_rcnn. \
                second_stage_box_predictor.batch_non_max_suppression.max_total_detections = max_total_detections

        self.write_pipeline(configuration, new_pipeline_dir)

    def learning_rate(self, s: str) -> str:
        pass

    def loss_function(self, new_pipeline_dir: str) -> None:
        """!
        Change classification_weight and localization_weight by the specified value.
        If trained model has a normal classification quality, but not a localization quality,
        it is necessary to increase localization_weight.
        @param new_pipeline_dir: New pipeline.config file.
        @return
        """
        configuration = self.read_pipeline(new_pipeline_dir)
        if configuration.model.HasField('ssd'):
            configuration.model.ssd.loss.classification_weight = self.settings.classification_weight
            logger.info("The classification weight's value have been changed. "
                        "New value: {0}".format(self.settings.classification_weight))

            configuration.model.ssd.loss.localization_weight = self.settings.localization_weight
            logger.info("The localization weight's value have been changed."
                        "New value: {0}".format(self.settings.localization_weight))
        self.write_pipeline(configuration, new_pipeline_dir)

    def select_methods(self, augment_methods: dict, train_methods: dict) -> Tuple[List[str], List[str]]:
        """!
        Select methods with True value from object_detection.ini.
        @param augment_methods: Augmentation methods.
        @param train_methods: Overfitting, Loss and Custom params.
        @return Lists with required config settings.
        """
        selected_augment = []
        if self.settings.is_augmentation:
            selected_augment = [key for key, value in augment_methods.items() if value]
        if self.settings.is_auto_augmentation:
            selected_augment.append('auto_augmentation')
        selected_train = [key for key, value in train_methods.items() if value]
        return selected_augment, selected_train

    def run_additional_settings(self, new_pipeline_dir: str, selected_train: list) -> None:
        """!
        Run selected settings: overfitting, loss and custom (value==True).
        @param new_pipeline_dir: New pipeline.config path.
        @param selected_train: Selected overfitting, loss and custom params.
        @return
        """
        methods = {
            'is_custom_settings': self.custom_settings,
            'is_prevent_overfitting': self.prevent_overfitting,
            'is_loss_function': self.loss_function
        }
        for key in methods.keys():
            if key in selected_train:
                methods[key](new_pipeline_dir=new_pipeline_dir)

    def generate_config(self, pipeline_dir: str, new_pipeline_dir: str, test_record: str, train_record: str,
                        fine_tune_checkpoint: str, label_map_dir: str, annotations: List[str]) -> None:
        """!
        Generate pipeline.config.
        @param pipeline_dir: File pipeline.config.
        @param new_pipeline_dir: New file pipeline.config.
        @param test_record: File test_data.record.
        @param train_record: File train_data.record.
        @param fine_tune_checkpoint: File fine_tune_checkpoint.ckpt-0.
        @param label_map_dir: File label_map.pbtxt.
        @param annotations: Objects to detect.
        @return
        """
        selected_augment, selected_train = self.select_methods(self.augmentation_methods, self.training_methods)
        self.default_settings(pipeline_dir, new_pipeline_dir, test_record, train_record,
                              fine_tune_checkpoint, label_map_dir, annotations)
        self.run_additional_settings(new_pipeline_dir=new_pipeline_dir, selected_train=selected_train)
        self.run_augment(pipeline_dir=new_pipeline_dir, selected_methods=selected_augment)



