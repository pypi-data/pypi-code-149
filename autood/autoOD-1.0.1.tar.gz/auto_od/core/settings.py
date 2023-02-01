import configparser
import os
from dataclasses import dataclass, field


def str_to_bool(value: str):
    return True if value.lower() == 'true' else False


@dataclass
class Settings:
    config_path: str
    parser = configparser.ConfigParser()

    dataset_dir: str = field(init=False)
    path_to_work_dir: str = field(init=False)
    image_folder: str = field(init=False)
    test_folder: str = field(init=False)
    train_folder: str = field(init=False)
    all_data_folder: str = field(init=False)
    annotations_folder: str = field(init=False)
    result_folder: str = field(init=False)
    models_folder: str = field(init=False)
    additional_folder: str = field(init=False)

    allowed_extensions: tuple = ('jpg', 'jpeg', 'png', 'JPG')
    extension: str = field(init=False)
    pretrained_model: str = 'zoo_models.csv'
    core_path: str = field(init=False)
    pretrained_model_dir: str = field(init=False)

    train_set_percent: float = field(init=False)
    is_shuffle: bool = field(init=False)

    is_custom_settings: bool = field(init=False)
    model_id: int = field(init=False)
    batch_size: int = field(init=False)
    num_steps: int = field(init=False)

    early_stopping: bool = field(init=False)
    patience: int = field(init=False)
    save_step: int = field(init=False)
    min_delta: float = field(init=False)

    is_prevent_overfitting: bool = field(init=False)
    use_dropout: bool = field(init=False)
    use_score_threshold: bool = field(init=False)

    is_loss_function: bool = field(init=False)
    classification_weight: float = field(init=False)
    localization_weight: float = field(init=False)

    is_auto_augmentation: bool = field(init=False)
    policy: str = field(init=False)

    is_augmentation: bool = field(init=False)
    normalize_image: bool = field(init=False)
    horizontal_flip: bool = field(init=False)
    probability_horizontal_flip: float = field(init=False)

    vertical_flip: bool = field(init=False)
    probability_vertical_flip: float = field(init=False)

    rotation90: bool = field(init=False)
    probability_rotation90: float = field(init=False)

    pixel_value_scale: bool = field(init=False)
    entire_rgb_to_grey: bool = field(init=False)
    probability_entire_rgb_to_grey: float = field(init=False)

    adjust_brightness: bool = field(init=False)
    max_delta_adjust_brightness: float = field(init=False)

    adjust_contrast: bool = field(init=False)
    min_delta_adjust_contrast: float = field(init=False)
    max_delta_adjust_contrast: float = field(init=False)

    adjust_hue: bool = field(init=False)
    max_delta_adjust_hue: float = field(init=False)

    adjust_saturation: bool = field(init=False)
    min_delta_adjust_saturation: float = field(init=False)
    max_delta_adjust_saturation: float = field(init=False)

    distort_color: bool = field(init=False)
    color_ordering: int = field(init=False)

    crop_image: bool = field(init=False)
    min_object_covered_crop_image: float = field(init=False)
    min_aspect_ratio_crop_image: float = field(init=False)
    max_aspect_ratio_crop_image: float = field(init=False)
    min_area_crop_image: float = field(init=False)
    max_area_crop_image: float = field(init=False)
    overlap_thresh_crop_image: float = field(init=False)
    clip_boxes_crop_image: bool = field(init=False)
    random_coef_crop_image: float = field(init=False)

    pad_image: bool = field(init=False)
    crop_pad_image: bool = field(init=False)

    crop_to_aspect_ratio: bool = field(init=False)
    aspect_ratio_car: float = field(init=False)
    overlap_thresh_car: float = field(init=False)
    clip_boxes_car: bool = field(init=False)

    black_patches: bool = field(init=False)
    max_black_patches: int = field(init=False)
    probability_black_patches: float = field(init=False)
    size_to_image_ratio: float = field(init=False)

    rgb_to_grey: bool = field(init=False)

    drop_label_probabilistically: bool = field(init=False)
    label: int = field(init=False)
    drop_probability: float = field(init=False)

    jpeg_quality: bool = field(init=False)
    random_coef_jpeg_quality: float = field(init=False)
    min_jpeg_quality: int = field(init=False)
    max_jpeg_quality: int = field(init=False)

    patch_gaussian: bool = field(init=False)
    random_coef_patch_gauss: float = field(init=False)
    min_patch_size: int = field(init=False)
    max_patch_size: int = field(init=False)
    min_gaussian_stddev: float = field(init=False)
    max_gaussian_stddev: float = field(init=False)

    def __post_init__(self):
        self.parser.read(self.config_path)
        self.dataset_dir: str = self.parser["Environment"]["dataset_dir"]
        self.path_to_work_dir = self.parser["Environment"]["path_to_work_dir"]
        self.image_folder: str = self.parser["Environment"]["image_folder"]
        self.test_folder: str = self.parser["Environment"]["test_folder"]
        self.train_folder: str = self.parser["Environment"]["train_folder"]
        self.all_data_folder: str = self.parser["Environment"]["all_data_folder"]
        self.annotations_folder: str = self.parser["Environment"]["annotations_folder"]
        self.result_folder: str = self.parser["Environment"]["result_folder"]
        self.models_folder: str = self.parser["Environment"]["models_folder"]
        self.additional_folder: str = self.parser["Environment"]["additional_folder"]

        self.core_path: str = os.path.join(self.path_to_work_dir, 'auto_od/core')
        self.pretrained_model_dir: str = os.path.join(self.core_path, 'zoo_models.csv')

        self.extension: str = self.parser["Dataset"]["extension"]

        self.train_set_percent: float = float(self.parser["Dataset.Preparation"]["train_set_percent"])
        self.is_shuffle: bool = str_to_bool(self.parser["Dataset.Preparation"]["is_shuffle"])

        self.is_custom_settings: bool = str_to_bool(self.parser["Training.Params"]["is_custom_settings"])
        self.model_id: int = int(self.parser["Training.Params"]["model_id"])
        self.batch_size: int = int(self.parser["Training.Params"]["batch_size"])
        self.num_steps: int = int(self.parser["Training.Params"]["num_steps"])

        self.early_stopping: bool = str_to_bool(self.parser["Training.EarlyStopping"]["early_stopping"])
        self.patience: int = int(self.parser["Training.EarlyStopping"]["patience"])
        self.min_delta: float = float(self.parser["Training.EarlyStopping"]["min_delta"])
        self.save_step: int = int(self.parser["Training.EarlyStopping"]["save_step"])

        self.is_prevent_overfitting: bool = str_to_bool(self.parser["Training.Overfitting"]["is_prevent_overfitting"])
        self.use_dropout: bool = str_to_bool(self.parser["Training.Overfitting"]["use_dropout"])
        self.use_score_threshold: bool = str_to_bool(self.parser["Training.Overfitting"]["use_score_threshold"])

        self.is_loss_function: bool = bool(self.parser["Training.Loss"]["is_loss_function"])
        self.classification_weight: float = float(self.parser["Training.Loss"]["classification_weight"])
        self.localization_weight: float = float(self.parser["Training.Loss"]["localization_weight"])

        self.is_auto_augmentation: bool = str_to_bool(self.parser["Training.Augmentation"]["is_auto_augmentation"])
        self.policy: str = self.parser["Training.Augmentation"]["policy"]

        self.is_augmentation: bool = str_to_bool(self.parser["Training.Augmentation"]["is_augmentation"])
        self.normalize_image: bool = str_to_bool(self.parser["Training.Augmentation"]["normalize_image"])
        self.horizontal_flip: bool = str_to_bool(self.parser["Training.Augmentation"]["horizontal_flip"])
        self.probability_horizontal_flip: float = float(
            self.parser["Training.Augmentation"]["probability_horizontal_flip"])
        self.vertical_flip: bool = str_to_bool(self.parser["Training.Augmentation"]["vertical_flip"])
        self.probability_vertical_flip: float = float(self.parser["Training.Augmentation"]["probability_vertical_flip"])
        self.rotation90: bool = str_to_bool(self.parser["Training.Augmentation"]["rotation90"])
        self.probability_rotation90: float = float(self.parser["Training.Augmentation"]["probability_rotation90"])
        self.pixel_value_scale: bool = str_to_bool(self.parser["Training.Augmentation"]["pixel_value_scale"])
        self.entire_rgb_to_grey: bool = str_to_bool(self.parser["Training.Augmentation"]["entire_rgb_to_grey"])
        self.probability_entire_rgb_to_grey: float = float(
            self.parser["Training.Augmentation"]["probability_entire_rgb_to_grey"])

        self.adjust_brightness: bool = str_to_bool(self.parser["Training.Augmentation"]["adjust_brightness"])
        self.max_delta_adjust_brightness: float = float(
            self.parser["Training.Augmentation"]["max_delta_adjust_brightness"])

        self.adjust_contrast: bool = str_to_bool(self.parser["Training.Augmentation"]["adjust_contrast"])
        self.min_delta_adjust_contrast: float = float(
            self.parser["Training.Augmentation"]["min_delta_adjust_contrast"])
        self.max_delta_adjust_contrast: float = float(
            self.parser["Training.Augmentation"]["max_delta_adjust_contrast"])

        self.adjust_hue: bool = str_to_bool(self.parser["Training.Augmentation"]["adjust_hue"])
        self.max_delta_adjust_hue: float = float(self.parser["Training.Augmentation"]["max_delta_adjust_hue"])

        self.adjust_saturation: bool = str_to_bool(self.parser["Training.Augmentation"]["adjust_saturation"])
        self.min_delta_adjust_saturation: float = float(
            self.parser["Training.Augmentation"]["min_delta_adjust_saturation"])
        self.max_delta_adjust_saturation: float = float(
            self.parser["Training.Augmentation"]["max_delta_adjust_saturation"])

        self.distort_color: bool = str_to_bool(self.parser["Training.Augmentation"]["distort_color"])
        self.color_ordering: int = int(self.parser["Training.Augmentation"]["color_ordering"])

        self.crop_image: bool = str_to_bool(self.parser["Training.Augmentation"]["crop_image"])
        self.min_object_covered_crop_image: float = float(
            self.parser["Training.Augmentation"]["min_object_covered_crop_image"])
        self.min_aspect_ratio_crop_image: float = float(
            self.parser["Training.Augmentation"]["min_aspect_ratio_crop_image"])
        self.max_aspect_ratio_crop_image: float = float(
            self.parser["Training.Augmentation"]["max_aspect_ratio_crop_image"])
        self.min_area_crop_image: float = float(
            self.parser["Training.Augmentation"]["min_area_crop_image"])
        self.max_area_crop_image: float = float(
            self.parser["Training.Augmentation"]["max_area_crop_image"])
        self.overlap_thresh_crop_image: float = \
            float(self.parser["Training.Augmentation"]["overlap_thresh_crop_image"])
        self.clip_boxes_crop_image: bool = \
            str_to_bool(self.parser["Training.Augmentation"]["clip_boxes_crop_image"])
        self.random_coef_crop_image: float = \
            float(self.parser["Training.Augmentation"]["random_coef_crop_image"])

        self.pad_image: bool = str_to_bool(self.parser["Training.Augmentation"]["pad_image"])
        self.crop_pad_image: bool = str_to_bool(self.parser["Training.Augmentation"]["crop_pad_image"])

        self.crop_to_aspect_ratio: bool = str_to_bool(self.parser["Training.Augmentation"]["crop_to_aspect_ratio"])
        self.aspect_ratio_car: float = float(
            self.parser["Training.Augmentation"]["aspect_ratio_crop_to_aspect_ratio"])
        self.overlap_thresh_car: float = \
            float(self.parser["Training.Augmentation"]["overlap_thresh_crop_to_aspect_ratio"])
        self.clip_boxes_car: str_to_bool = \
            bool(self.parser["Training.Augmentation"]["clip_boxes_crop_to_aspect_ratio"])

        self.black_patches: bool = str_to_bool(self.parser["Training.Augmentation"]["black_patches"])
        self.max_black_patches: int = int(self.parser["Training.Augmentation"]["max_black_patches"])
        self.probability_black_patches: float = float(self.parser["Training.Augmentation"]["probability_black_patches"])
        self.size_to_image_ratio: float = float(self.parser["Training.Augmentation"]["size_to_image_ratio"])

        self.rgb_to_grey: bool = str_to_bool(self.parser["Training.Augmentation"]["rgb_to_grey"])

        self.drop_label_probabilistically: bool = \
            str_to_bool(self.parser["Training.Augmentation"]["drop_label_probabilistically"])
        self.label: int = int(self.parser["Training.Augmentation"]["label"])
        self.drop_probability: float = \
            float(self.parser["Training.Augmentation"]["drop_probability"])

        self.jpeg_quality: bool = str_to_bool(self.parser["Training.Augmentation"]["jpeg_quality"])
        self.random_coef_jpeg_quality: float = float(self.parser["Training.Augmentation"]["random_coef_jpeg_quality"])
        self.min_jpeg_quality: int = int(self.parser["Training.Augmentation"]["min_jpeg_quality"])
        self.max_jpeg_quality: int = int(self.parser["Training.Augmentation"]["max_jpeg_quality"])

        self.patch_gaussian: bool = str_to_bool(self.parser["Training.Augmentation"]["patch_gaussian"])
        self.random_coef_patch_gauss: float = float(self.parser["Training.Augmentation"]["random_coef_patch_gaussian"])
        self.min_patch_size: int = int(self.parser["Training.Augmentation"]["min_patch_size"])
        self.max_patch_size: int = int(self.parser["Training.Augmentation"]["max_patch_size"])
        self.min_gaussian_stddev: float = float(self.parser["Training.Augmentation"]["min_gaussian_stddev"])
        self.max_gaussian_stddev: float = float(self.parser["Training.Augmentation"]["max_gaussian_stddev"])

