import functools

import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
import tensorflow_addons as tfa
from object_detection.core import preprocessor, preprocessor_cache
from tf_image.core.colors import channel_drop, rgb_shift
from tf_image.core.convert_type_decorator import convert_type
from tf_image.core.random import random_function

image = tf.io.read_file("tiger.jpeg")
image = tf.image.decode_jpeg(image)


def visualize(original, augmented, augment_type):
    fig = plt.figure(figsize=(10, 4))
    plt.subplot(1, 2, 1)
    plt.title('Original image')
    plt.imshow(original)

    plt.subplot(1, 2, 2)
    plt.title(f'Augmented: Type {augment_type}')
    plt.imshow(augmented)
    plt.show()


# # horizontal_flip
# hor_flipped = tf.image.flip_left_right(image)
# visualize(image, hor_flipped, 'horizontal_flip')
#
# # vertical_flip
# vert_flipped = tf.image.flip_up_down(image)
# visualize(image, vert_flipped, 'vertical_flip')
#
# # rotation90
# rotated = tf.image.rot90(image)
# visualize(image, rotated, 'rotation90')
#
# # entire_rgb_to_grey
# gray_scaled = tf.image.rgb_to_grayscale(image)
# visualize(image, tf.squeeze(gray_scaled), 'entire_rgb_to_grey')

# # adjust_brightness
# # delta: A scalar. Amount to add to the pixel values. (0, 1)
# bright = tf.image.adjust_brightness(image, 0.3)
# visualize(image, bright, 'adjust_brightness')

# # adjust_contrast
# # contrast_factor (-inf, inf) how much to change the contrast. Contrast will change with a
# #                value between min_delta and max_delta. This value will be
# #                multiplied to the current contrast of the image.
# contrast = tf.image.adjust_contrast(image, -1.)
# visualize(image, contrast, 'adjust_contrast, contrast_factor=-1.')
#
# contrast = tf.image.adjust_contrast(image, 1.5)
# visualize(image, contrast, 'adjust_contrast, contrast_factor=1.5')

# # adjust_hue
# # change hue randomly with a value between 0 and max_delta.
# for i in np.arange(0, 1, 0.2):
#     hue = tf.image.adjust_hue(image, delta=i)
#     visualize(image, hue, f'adjust_hue, delta={i}')


# # adjust_saturation
# # how much to change the saturation. Saturation will change with a
# #                value between min_delta and max_delta. This value will be
# #                multiplied to the current saturation of the image.
# for i in np.arange(0, 1, 0.2):
#     saturation = tf.image.adjust_saturation(image, saturation_factor=i)
#     visualize(image, saturation, f'adjust_saturation, saturation_factor={i}')


# distort_color
# Randomly distorts color.
#   Randomly distorts color using a combination of brightness, hue, contrast and
#   saturation changes. Makes sure the output image is still between 0 and 255.
# color_ordering: Python int, a type of distortion (valid values: 0, 1).
# example:

# distort_color = tf.image.adjust_brightness(image, 32. / 255.)
# distort_color = tf.image.adjust_saturation(distort_color, 0.6)
# distort_color = tf.image.adjust_hue(distort_color, 0.5)
# distort_color = tf.image.adjust_contrast(distort_color, 0.7)
# visualize(image, distort_color, 'distort_color, color_ordering=0')

#
# distort_color = tf.image.adjust_brightness(image, 32. / 255.)
# distort_color = tf.image.adjust_contrast(distort_color, 1.2)
# distort_color = tf.image.adjust_saturation(distort_color, 0.7)
# distort_color = tf.image.adjust_hue(distort_color, 0.6)
# visualize(image, distort_color, 'distort_color, color_ordering=1')

# box = tf.convert_to_tensor([380, 406, 660, 973])
# print(box)
# box = tf.transpose(box)
# print(box[:, 0])
# box = [380, 406, 660, 973]
# ymin, xmin, ymax, xmax
# 380, 406, 660, 973
# print([box[:, i] for i in range(4)])
# ymin, xmin, ymax, xmax = (box[:, i] for i in range(4))
# res = preprocessor.random_jitter_boxes(box)
# print('res', res, box)

preprocessor.random_crop_image(image, tf.convert_to_tensor([1, 1, [380, 406, 660, 973]], dtype=float),
                               tf.convert_to_tensor([1], dtype=float), None)



