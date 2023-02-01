import os
import re
import subprocess

import pandas as pd

from auto_od.core.logger import logger
from auto_od.core.settings import Settings
from auto_od.training.stop.early_stopping import EarlyStopping
from auto_od.utils.info_messages import file_created, folder_exist
from typing import List


class StopAlgo:
    def __init__(self, config_path: str):
        self.settings = Settings(config_path=config_path)
        self.additional_dir: str = os.path.join(self.settings.path_to_work_dir, self.settings.additional_folder)
        self.models_dir: str = os.path.join(self.additional_dir, self.settings.models_folder)

        self.logs_dir = os.path.join(self.models_dir, "logs")
        self.path_to_work_dir = self.settings.path_to_work_dir
        self.loss_log_path = os.path.join(self.logs_dir, "loss.log")
        self.train_loss_path = os.path.join(self.logs_dir, "train.csv")
        self.val_loss_path = os.path.join(self.logs_dir, "val.csv")
        self.val_log_path = os.path.join(self.logs_dir, "val_loss.log")
        self.best_ckpt_dir = os.path.join(self.models_dir, "best_ckpt")
        self.step_val_path = os.path.join(self.best_ckpt_dir, "step_val.txt")
        self.es = EarlyStopping(config_path=config_path, models_dir=self.models_dir,
                                best_ckpt_dir=self.best_ckpt_dir,
                                val_loss_path=self.val_loss_path)
        self.init()

    def init(self) -> None:
        """!
        Initialize all folders.
        @return:
        """
        df_loss = pd.DataFrame({"step": [], "classification_loss": [],
                                "localization_loss": [], "regularization_loss": [],
                                "total_loss": [], "learning_rate": []})
        df_val_loss = pd.DataFrame({"step": [], "classification_loss": [],
                                    "localization_loss": [], "regularization_loss": [],
                                    "total_loss": [], 'ckpt': []})

        try:
            os.makedirs(self.logs_dir)
            logger.info(file_created.format(self.logs_dir))
        except FileExistsError:
            logger.info(folder_exist.format(self.logs_dir))

        try:
            os.makedirs(self.best_ckpt_dir)
            logger.info(file_created.format(self.best_ckpt_dir))
        except FileExistsError:
            logger.info(folder_exist.format(self.best_ckpt_dir))

        if not os.path.exists(self.train_loss_path):
            df_loss.to_csv(self.train_loss_path, index=False)
            logger.info(file_created.format(self.train_loss_path))

        with open(self.step_val_path, mode='w') as f:
            f.write('0')

        if not os.path.exists(self.val_loss_path):
            df_val_loss.to_csv(self.val_loss_path, index=False)
            logger.info(file_created.format(self.val_loss_path))

        if not os.path.exists(self.val_log_path):
            with open(self.val_log_path, mode='w'):
                logger.info(file_created.format(self.val_log_path))

        if not os.path.exists(self.loss_log_path):
            with open(self.loss_log_path, mode='w'):
                logger.info(file_created.format(self.loss_log_path))

    def select_logs(self, log: str) -> bool:
        """!
        Read logs from stdout during training.
        @param str log:
        @return
        """
        allowed_str = [' Step ', 'Loss/classification_loss']
        allowed_logs = [item for item in allowed_str if log.find(item) != -1]

        if allowed_logs:
            with open(self.loss_log_path, 'a+') as f:
                f.write(log)
            return True
        return False

    def extract_train_loss(self, data: List[str]) -> None:
        """!
        Extract loss values from loss.log file.
        @param list data: List of loss.log file parts.
        @return
        """
        learning_rate = data[data.index("learning_rate") - 1]
        total_loss = data[data.index("total_loss") - 1]
        regularization_loss = data[data.index("regularization_loss") - 1]
        localization_loss = data[data.index("localization_loss") - 1]
        classification_loss = data[data.index("classification_loss") - 1]
        step = data[data.index("Step") - 1]

        df = pd.read_csv(self.train_loss_path, dtype=str)
        row = {
            'step': step,
            'classification_loss': classification_loss,
            'localization_loss': localization_loss,
            'regularization_loss': regularization_loss,
            'total_loss': total_loss,
            'learning_rate': learning_rate
        }
        if not df.step.str.contains(step).any():
            ind = len(df.index)
            df.loc[ind] = row
            df.to_csv(self.train_loss_path, index=False)
            logger.info('New row in train.csv')

    def extract_val_loss(self, item: List[str]) -> None:
        """!
        Extract loss values from val_loss.log file.
        @param list item: List of val_loss.log file parts.
        @return
        """
        localization_loss = item[item.index("Loss/localization_loss") + 1]
        classification_loss = item[item.index("Loss/classification_loss") + 1]
        regularization_loss = item[item.index("Loss/regularization_loss") + 1]
        total_loss = item[item.index("Loss/total_loss") + 1]
        step = item[item.index('INFO:tensorflow:Eval') + 4]
        ckpt = item[item.index('Found') + 4]
        df = pd.read_csv(self.val_loss_path, dtype=str)
        row = {
            'step': step,
            'localization_loss': localization_loss,
            'classification_loss': classification_loss,
            'regularization_loss': regularization_loss,
            'total_loss': total_loss,
            'ckpt': ckpt
        }

        if not df.step.str.contains(step).any():
            with open(self.step_val_path, mode='r') as f:
                step_val = int(f.read()) + 1
            with open(self.step_val_path, mode='w') as f:
                f.write(str(step_val))

            ind = len(df.index)
            df.loc[ind] = row
            df.to_csv(self.val_loss_path, index=False)
            logger.info('New row in val.csv')

    def read_train_loss(self, flag: bool = False) -> None:
        """!
        Add new rows to the train.csv with losses.
        @param bool flag: if False, function will be skipped.
        @return
        """

        if flag is False:
            return
        with open(self.loss_log_path, 'r') as file:
            data = file.read()

        data = list(filter(None, re.split("{|: |,|}|\n |'|/| |\n", data)))[::-1]
        if data[1] == 'time':
            return
        try:
            self.extract_train_loss(data)
        except ValueError as _:
            pass
        except Exception as e:
            logger.warning('Extract training losses. Warning ' + str(e))

    def eval(self, command: List[str]) -> None:
        """!
        Write logs to the validation file
        @param list command:
        @return
        """
        filename = self.val_log_path
        with open(filename, "a+") as f:
            _ = subprocess.Popen(command, stdout=f, stderr=f)

    def read_val_loss(self) -> None:
        """!
        Read logs' validation file.
        @return
        """
        with open(self.val_log_path, 'r') as file:
            data = file.read()
        logs = data.split('INFO:tensorflow:Waiting')

        for log in logs:
            item = list(filter(None, re.split("{|: |,|}|\n |'| |\n", log)))
            try:
                self.extract_val_loss(item)
            except ValueError:
                pass
            except Exception as e:
                logger.warning('Extract training losses. Warning ' + str(e))

    def run_stop_algo(self, size: int) -> int:
        """!
        Run Early Stopping algorithm.
        @param int size: row's number validation result
        @return
        """
        if size == 0:
            df = pd.read_csv(self.val_loss_path, dtype=str)
            size = df.shape[0]
        self.read_val_loss()

        if size != 0:
            logger.info('Starting Early Stopping...')
            self.es()
        return size

