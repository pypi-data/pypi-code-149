from abc import ABC, abstractmethod
from enum import Enum
from typing import List

from PIL import Image

from functional_cat.data_types import (
    Detection,
    DetectionWithKeypoints,
    ImageInput,
    InstanceSegmentation,
)

__all__ = ["ObjectDetector", "InstanceSegmentationModel", "KeyPointDetector"]


class Task(Enum):
    OBJECT_DETECTION = "Object Detection"
    INSTANCE_SEGMENTATION = "Instance Segmentation"
    KEYPOINT_DETECTION = "KeyPoint Detection"


class ObjectDetector(ABC):
    """Base class for object detectors. These objects are all callable and take in
    a list of `PIL.Image` objects and output a list of bounding box detections.
    """

    task = Task.OBJECT_DETECTION

    @property
    @abstractmethod
    def class_labels(self) -> List[str]:
        pass

    @abstractmethod
    def __call__(
        self, imgs: ImageInput, score_thres: float
    ) -> List[List[Detection]]:
        pass

    @staticmethod
    def draw_output_on_img(
        img: Image.Image, dets: List[Detection]
    ) -> Image.Image:
        for i, det in enumerate(dets):
            img = det.draw_on_image(img, inplace=i != 0)
        return img


class InstanceSegmentationModel(ObjectDetector):
    task = Task.INSTANCE_SEGMENTATION

    @abstractmethod
    def __call__(self, imgs: ImageInput) -> List[List[InstanceSegmentation]]:
        pass

    @staticmethod
    def draw_output_on_img(
        img: Image.Image, dets: List[InstanceSegmentation]
    ) -> Image.Image:
        for i, det in enumerate(dets):
            img = det.draw_on_image(
                img, inplace=i != 0, draw_mask=True, draw_bbox=False
            )
        for i, det in enumerate(dets):
            img = det.draw_on_image(
                img, inplace=i != 0, draw_mask=False, draw_bbox=True
            )

        return img


class KeyPointDetector(ObjectDetector):
    task = Task.KEYPOINT_DETECTION

    @abstractmethod
    def __call__(self, imgs: ImageInput) -> List[List[DetectionWithKeypoints]]:
        pass

    @property
    @abstractmethod
    def key_point_labels(self) -> List[str]:
        pass
