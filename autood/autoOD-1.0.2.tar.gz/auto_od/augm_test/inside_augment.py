import functools

import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
from object_detection import inputs
from object_detection.core import preprocessor
from object_detection.core import standard_fields as fields
from PIL import Image


def load_image_into_numpy_array(image):
    (im_width, im_height) = image.size
    return np.array(image.getdata()).reshape(
        (im_height, im_width, 3)).astype(np.float32)  # .astype(np.uint8)


number_of_repeats = 10

image2 = Image.open("tiger.jpeg")
image_np = load_image_into_numpy_array(image2)

preprocessing_list = [
                      # (preprocessor.random_horizontal_flip, {}),
                      # (preprocessor.random_vertical_flip, {}),
                      # (preprocessor.random_rotation90, {}),
                      # (preprocessor.random_pixel_value_scale, {
                      #     'minval': 0.5,
                      #     'maxval': 1.5
                      # }),  ##### slightly changes the values of pixels
                      # (preprocessor.random_image_scale, {
                      #     'min_scale_ratio': 0.5,
                      #     'max_scale_ratio': 4.0}),
                      # (preprocessor.random_rgb_to_gray, {
                      #       'probability': 0.99
                      # }),
                      # (preprocessor.random_adjust_brightness, {
                      #     "max_delta": 0.1
                      # }),
                      # (preprocessor.random_adjust_contrast, {
                      #       "min_delta": 0.5,
                      #       "max_delta": 1.1
                      # }),
                      # (preprocessor.random_adjust_hue, {
                      #     "max_delta": 0.05
                      # }),
                      # (preprocessor.random_adjust_saturation, {
                      #     "min_delta": 0.5,
                      #     "max_delta": 1.5
                      # }),
                      # (preprocessor.random_distort_color, {}),  # very strong augmentation
                      # (preprocessor.random_jitter_boxes, {   #####
                      #       'ratio': 0.9
                      # }),
                      # (preprocessor.random_crop_image, {}), #####
                      # (preprocessor.random_pad_image, {}),  # pad using average color of the input image
                      # (preprocessor.random_crop_pad_image, {}),
                      # (preprocessor.random_pad_to_aspect_ratio, {}),
                      # (preprocessor.random_black_patches, {}),
                      # (preprocessor.random_patch_gaussian, {}),
                      # (preprocessor.convert_class_logits_to_softmax, {}),
                      (preprocessor.autoaugment_image, {
                          "policy_name": "v1"
                      }),
                      ]

for preprocessing_technique in preprocessing_list:
    for i in range(number_of_repeats):
        tf.compat.v1.reset_default_graph()
        if preprocessing_technique is not None:
            data_augmentation_options = [preprocessing_technique]
        else:
            data_augmentation_options = []
        data_augmentation_fn = functools.partial(
            inputs.augment_input_data,
            data_augmentation_options=data_augmentation_options)
        tensor_dict = {
            fields.InputDataFields.image:
                tf.constant(image_np.astype(np.float32)),
            fields.InputDataFields.groundtruth_boxes:
                tf.constant(np.array([[.5, .5, 1., 1.]], np.float32)),
            fields.InputDataFields.groundtruth_classes:
                tf.constant(np.array([1.0], np.float32)),
        }
        augmented_tensor_dict = data_augmentation_fn(tensor_dict=tensor_dict)

        plt.figure()

        plt.imshow(augmented_tensor_dict[fields.InputDataFields.image].numpy().astype("uint8"))
        plt.imsave(f'images/tiger_{str(preprocessing_technique).split(" ")[1]}{i}.jpeg',
                   augmented_tensor_dict[fields.InputDataFields.image].numpy().astype("uint8"))
        plt.show()

