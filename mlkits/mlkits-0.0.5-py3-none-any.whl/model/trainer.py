from typing import Callable, List, Optional

from tqdm.auto import tqdm

from mlkits.config import C
from mlkits.data.dataset import Dataset
from mlkits.data.dataset.weight import Reweighter

from mlkits.model.base import Model
from mlkits.utils import (
    auto_filter_kwargs,
    init_instance_by_config,
)

class Trainer():
    """
    The trainer can train a list of models.
    There are Trainer and DelayTrainer, which can be distinguished by when it will finish real training.
    """
    def __init__(self, task_config: dict):
        self.model: Model = init_instance_by_config(task_config["model"], accept_types=Model)
        self.dataset: Dataset = init_instance_by_config(task_config["dataset"], accept_types=Dataset)
        self.reweighter: Reweighter = task_config.get("reweighter", None)

    def train(self) -> list:
        auto_filter_kwargs(model.fit)(self.dataset, reweighter=self.reweighter)

