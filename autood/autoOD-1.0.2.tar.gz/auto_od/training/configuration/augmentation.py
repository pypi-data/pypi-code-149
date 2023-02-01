from typing import Optional

from object_detection.protos import pipeline_pb2, preprocessor_pb2

from auto_od.core.logger import logger
from auto_od.core.settings import Settings
from auto_od.training.configuration.config_parser import Parser
from auto_od.utils.info_messages import data_augmentation


class Augmentation(Parser):
    def __init__(self, config_path: str):
        self.settings = Settings(config_path=config_path)

    def normalize_image(self, configuration: Optional[pipeline_pb2.TrainEvalPipelineConfig]) -> \
            Optional[pipeline_pb2.TrainEvalPipelineConfig]:
        augment = preprocessor_pb2.PreprocessingStep()
        augment.normalize_image.original_minval = 0.0
        augment.normalize_image.original_maxval = 255.0
        augment.normalize_image.target_minval = -1.0
        augment.normalize_image.target_maxval = 1.0
        configuration.train_config.data_augmentation_options.append(augment)
        logger.info(data_augmentation.format("NormalizeImage"))
        return configuration

    def horizontal_flip(self, configuration: Optional[pipeline_pb2.TrainEvalPipelineConfig]) -> \
            Optional[pipeline_pb2.TrainEvalPipelineConfig]:

        augment = preprocessor_pb2.PreprocessingStep()
        augment.random_horizontal_flip.probability = self.settings.probability_horizontal_flip
        configuration.train_config.data_augmentation_options.append(augment)
        logger.info(data_augmentation.format("RandomHorizontalFlip"))
        return configuration

    def vertical_flip(self, configuration: Optional[pipeline_pb2.TrainEvalPipelineConfig]) -> \
            Optional[pipeline_pb2.TrainEvalPipelineConfig]:

        augment = preprocessor_pb2.PreprocessingStep()
        augment.random_vertical_flip.probability = self.settings.probability_vertical_flip
        configuration.train_config.data_augmentation_options.append(augment)
        logger.info(data_augmentation.format("RandomVerticalFlip"))
        return configuration

    def rotation90(self, configuration: Optional[pipeline_pb2.TrainEvalPipelineConfig]) -> \
            Optional[pipeline_pb2.TrainEvalPipelineConfig]:
        augment = preprocessor_pb2.PreprocessingStep()
        augment.random_rotation90.probability = self.settings.probability_rotation90
        configuration.train_config.data_augmentation_options.append(augment)
        logger.info(data_augmentation.format("RandomRotation90"))
        return configuration

    @staticmethod
    def pixel_value_scale(configuration: Optional[pipeline_pb2.TrainEvalPipelineConfig]) -> \
            Optional[pipeline_pb2.TrainEvalPipelineConfig]:
        augment = preprocessor_pb2.PreprocessingStep(random_pixel_value_scale=preprocessor_pb2.RandomPixelValueScale())
        configuration.train_config.data_augmentation_options.append(augment)
        logger.info(data_augmentation.format("RandomPixelValueScale"))
        return configuration

    def entire_rgb_to_grey(self, configuration: Optional[pipeline_pb2.TrainEvalPipelineConfig]) -> \
            Optional[pipeline_pb2.TrainEvalPipelineConfig]:
        augment = preprocessor_pb2.PreprocessingStep()
        augment.random_rgb_to_gray.probability = self.settings.probability_entire_rgb_to_grey
        configuration.train_config.data_augmentation_options.append(augment)
        logger.info(data_augmentation.format("RandomRGBtoGray"))
        return configuration

    def adjust_brightness(self, configuration: Optional[pipeline_pb2.TrainEvalPipelineConfig]) -> \
            Optional[pipeline_pb2.TrainEvalPipelineConfig]:
        augment = preprocessor_pb2.PreprocessingStep()
        augment.random_adjust_brightness.max_delta = self.settings.max_delta_adjust_brightness
        configuration.train_config.data_augmentation_options.append(augment)
        logger.info(data_augmentation.format("RandomAdjustBrightness"))
        return configuration

    def adjust_contrast(self, configuration: Optional[pipeline_pb2.TrainEvalPipelineConfig]) -> \
            Optional[pipeline_pb2.TrainEvalPipelineConfig]:
        augment = preprocessor_pb2.PreprocessingStep()
        augment.random_adjust_contrast.min_delta = self.settings.min_delta_adjust_contrast
        augment.random_adjust_contrast.max_delta = self.settings.max_delta_adjust_contrast
        configuration.train_config.data_augmentation_options.append(augment)
        logger.info(data_augmentation.format("RandomAdjustContrast"))
        return configuration

    def adjust_hue(self, configuration: Optional[pipeline_pb2.TrainEvalPipelineConfig]) -> \
            Optional[pipeline_pb2.TrainEvalPipelineConfig]:
        augment = preprocessor_pb2.PreprocessingStep()
        augment.random_adjust_hue.max_delta = self.settings.max_delta_adjust_hue
        configuration.train_config.data_augmentation_options.append(augment)
        logger.info(data_augmentation.format("RandomAdjustHue"))
        return configuration

    def adjust_saturation(self, configuration: Optional[pipeline_pb2.TrainEvalPipelineConfig]) -> \
            Optional[pipeline_pb2.TrainEvalPipelineConfig]:
        augment = preprocessor_pb2.PreprocessingStep()
        augment.random_adjust_saturation.min_delta = self.settings.min_delta_adjust_saturation
        augment.random_adjust_saturation.max_delta = self.settings.max_delta_adjust_saturation
        configuration.train_config.data_augmentation_options.append(augment)
        logger.info(data_augmentation.format("RandomAdjustSaturation"))
        return configuration

    def distort_color(self, configuration: Optional[pipeline_pb2.TrainEvalPipelineConfig]) -> \
            Optional[pipeline_pb2.TrainEvalPipelineConfig]:
        # color_ordering: 0 or 1
        augment = preprocessor_pb2.PreprocessingStep()
        augment.random_distort_color.color_ordering = self.settings.color_ordering
        configuration.train_config.data_augmentation_options.append(augment)
        logger.info(data_augmentation.format("RandomDistortColor"))
        return configuration

    def crop_image(self, configuration: Optional[pipeline_pb2.TrainEvalPipelineConfig]) -> \
            Optional[pipeline_pb2.TrainEvalPipelineConfig]:
        augment = preprocessor_pb2.PreprocessingStep()
        augment.random_crop_image.min_object_covered = self.settings.min_object_covered_crop_image
        augment.random_crop_image.min_aspect_ratio = self.settings.min_aspect_ratio_crop_image
        augment.random_crop_image.max_aspect_ratio = self.settings.max_aspect_ratio_crop_image
        augment.random_crop_image.min_area = self.settings.min_area_crop_image
        augment.random_crop_image.max_area = self.settings.max_area_crop_image
        augment.random_crop_image.overlap_thresh = self.settings.overlap_thresh_crop_image
        augment.random_crop_image.clip_boxes = self.settings.clip_boxes_crop_image
        augment.random_crop_image.random_coef = self.settings.random_coef_crop_image
        configuration.train_config.data_augmentation_options.append(augment)
        logger.info(data_augmentation.format("RandomCropImage"))
        return configuration

    @staticmethod
    def pad_image(configuration: Optional[pipeline_pb2.TrainEvalPipelineConfig]) -> \
            Optional[pipeline_pb2.TrainEvalPipelineConfig]:
        augment = preprocessor_pb2.PreprocessingStep(random_pad_image=preprocessor_pb2.RandomPadImage())
        configuration.train_config.data_augmentation_options.append(augment)
        logger.info(data_augmentation.format("RandomPadImage"))
        return configuration

    def absolute_pad_image(self):
        pass

    @staticmethod
    def crop_pad_image(configuration: Optional[pipeline_pb2.TrainEvalPipelineConfig]) -> \
            Optional[pipeline_pb2.TrainEvalPipelineConfig]:
        augment = preprocessor_pb2.PreprocessingStep(random_crop_pad_image=preprocessor_pb2.RandomCropPadImage())
        configuration.train_config.data_augmentation_options.append(augment)
        logger.info(data_augmentation.format("RandomCropPadImage"))
        return configuration

    def crop_to_aspect_ratio(self, configuration: Optional[pipeline_pb2.TrainEvalPipelineConfig]) -> \
            Optional[pipeline_pb2.TrainEvalPipelineConfig]:
        augment = preprocessor_pb2.PreprocessingStep()
        augment.random_crop_to_aspect_ratio.aspect_ratio = self.settings.aspect_ratio_car
        augment.random_crop_to_aspect_ratio.overlap_thresh = self.settings.overlap_thresh_car
        augment.random_crop_to_aspect_ratio.clip_boxes = self.settings.clip_boxes_car
        configuration.train_config.data_augmentation_options.append(augment)
        logger.info(data_augmentation.format("RandomCropToAspectRatio"))
        return configuration

    def black_patches(self, configuration: Optional[pipeline_pb2.TrainEvalPipelineConfig]) -> \
            Optional[pipeline_pb2.TrainEvalPipelineConfig]:
        augment = preprocessor_pb2.PreprocessingStep()
        augment.random_black_patches.max_black_patches = self.settings.max_black_patches
        augment.random_black_patches.probability = self.settings.probability_black_patches
        augment.random_black_patches.size_to_image_ratio = self.settings.size_to_image_ratio
        configuration.train_config.data_augmentation_options.append(augment)
        logger.info(data_augmentation.format("RandomBlackPatches"))
        return configuration

    def resize_method(self):
        pass

    @staticmethod
    def rgb_to_grey(configuration: Optional[pipeline_pb2.TrainEvalPipelineConfig]) -> \
            Optional[pipeline_pb2.TrainEvalPipelineConfig]:
        augment = preprocessor_pb2.PreprocessingStep(rgb_to_gray=preprocessor_pb2.RGBtoGray())
        configuration.train_config.data_augmentation_options.append(augment)
        logger.info(data_augmentation.format("RGBtoGray"))
        return configuration

    def scale_boxes_to_pixel_coordinates(self):
        pass

    def subtract_channel_mean(self):
        pass

    def drop_label_probabilistically(self, configuration: Optional[pipeline_pb2.TrainEvalPipelineConfig]) -> \
            Optional[pipeline_pb2.TrainEvalPipelineConfig]:
        augment = preprocessor_pb2.PreprocessingStep()
        augment.drop_label_probabilistically.label = self.settings.label
        augment.drop_label_probabilistically.drop_probability = self.settings.drop_probability
        configuration.train_config.data_augmentation_options.append(augment)
        logger.info(data_augmentation.format("DropLabelProbabilistically"))
        return configuration

    def jpeg_quality(self, configuration: Optional[pipeline_pb2.TrainEvalPipelineConfig]) -> \
            Optional[pipeline_pb2.TrainEvalPipelineConfig]:
        augment = preprocessor_pb2.PreprocessingStep()
        augment.random_jpeg_quality.random_coef = self.settings.random_coef_jpeg_quality
        augment.random_jpeg_quality.min_jpeg_quality = self.settings.min_jpeg_quality
        augment.random_jpeg_quality.max_jpeg_quality = self.settings.max_jpeg_quality
        configuration.train_config.data_augmentation_options.append(augment)
        logger.info(data_augmentation.format("RandomJpegQuality"))
        return configuration

    def downscale_to_target_pixels(self):
        pass

    def patch_gaussian(self, configuration: Optional[pipeline_pb2.TrainEvalPipelineConfig]) -> \
            Optional[pipeline_pb2.TrainEvalPipelineConfig]:
        augment = preprocessor_pb2.PreprocessingStep()
        augment.random_patch_gaussian.random_coef = self.settings.random_coef_patch_gauss
        augment.random_patch_gaussian.min_patch_size = self.settings.min_patch_size
        augment.random_patch_gaussian.max_patch_size = self.settings.max_patch_size
        augment.random_patch_gaussian.min_gaussian_stddev = self.settings.min_gaussian_stddev
        augment.random_patch_gaussian.max_gaussian_stddev = self.settings.max_gaussian_stddev
        configuration.train_config.data_augmentation_options.append(augment)
        logger.info(data_augmentation.format("RandomPatchGaussian"))
        return configuration

    def random_square_crop_by_scale(self):
        pass

    def random_scale_crop_and_pad_to_square(self):
        pass

    def autoaugment_image(self, configuration: Optional[pipeline_pb2.TrainEvalPipelineConfig]) -> \
            Optional[pipeline_pb2.TrainEvalPipelineConfig]:
        augment = preprocessor_pb2.PreprocessingStep()
        augment.autoaugment_image.policy_name = self.settings.policy
        configuration.train_config.data_augmentation_options.append(augment)
        logger.info(data_augmentation.format("AutoAugmentImage"))
        return configuration

    def run_augment(self, pipeline_dir: str, selected_methods: list):
        config = self.read_pipeline(pipeline_dir)
        aug = {
            'auto_augmentation': self.autoaugment_image,
            'normalize_image': self.normalize_image,
            'horizontal_flip': self.horizontal_flip,
            'vertical_flip': self.vertical_flip,
            'rotation90': self.rotation90,
            'pixel_value_scale': self.pixel_value_scale,
            'entire_rgb_to_grey': self.entire_rgb_to_grey,
            'adjust_brightness': self.adjust_brightness,
            'adjust_contrast': self.adjust_contrast,
            'adjust_hue': self.adjust_hue,
            'adjust_saturation': self.adjust_saturation,
            'distort_color': self.distort_color,
            'crop_image': self.crop_image,
            'pad_image': self.pad_image,
            'crop_pad_image': self.crop_pad_image,
            'crop_to_aspect_ratio': self.crop_to_aspect_ratio,
            'black_patches': self.black_patches,
            'rgb_to_grey': self.rgb_to_grey,
            'drop_label_probabilistically': self.drop_label_probabilistically,
            'jpeg_quality': self.jpeg_quality,
            'patch_gaussian': self.patch_gaussian
        }

        for key in aug.keys():
            if key in selected_methods:
                config = aug[key](configuration=config)

        self.write_pipeline(config, pipeline_dir)
