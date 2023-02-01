import os
import shutil
import subprocess

import pandas as pd

from auto_od.core.logger import logger
from auto_od.core.settings import Settings
from auto_od.notify.send import send_message


class EarlyStopping:
    def __init__(self, config_path: str, models_dir: str, val_loss_path: str, best_ckpt_dir: str):
        self.settings = Settings(config_path=config_path)

        self.patience = self.settings.patience
        self.val_loss_path = val_loss_path
        self.path_to_work_dir = self.settings.path_to_work_dir
        self.models_dir = models_dir
        self.min_delta = self.settings.min_delta
        self.best_ckpt_dir = best_ckpt_dir
        self.save_step = self.settings.save_step
        self.step_val_path = os.path.join(self.best_ckpt_dir, "step_val.txt")
        self.best_ckpt_path = os.path.join(self.best_ckpt_dir, "best_ckpt.txt")

    def algorithm(self, losses: list[float], ckpt: list[str], step: list[int]):
        """!
        Find the best checkpoint and step.
        @param list losses: List of validation losses.
        @param list ckpt: List of checkpoints.
        @param list step: List of steps.
        @return
        """
        f = lambda x, max_val: -1 if x - max_val > self.min_delta else 0
        min_value = min(losses)
        min_val_ind = losses.index(min_value)
        best_ckpt = ckpt[min_val_ind]
        best_step = step[min_val_ind]
        ids = [f(loss, min_value) for loss in losses[min_val_ind + 1:]]
        if sum(ids) <= -self.patience:
            send_message('Required to stop training. best_checkpoint is: {0}'.format(best_ckpt))
        return best_ckpt, best_step

    def froze_model(self):
        """!
        Froze model with the best checkpoint.
        @return:
        """
        save_dir = os.path.join(self.best_ckpt_dir, 'frozen')
        pipeline_dir = os.path.join(self.models_dir, 'pipeline.config')
        em_tf2_path = os.path.join(self.path_to_work_dir, "models/research/object_detection/exporter_main_v2.py")
        command = f"python {em_tf2_path} --input_type image_tensor --trained_checkpoint_dir={self.best_ckpt_dir} " \
                  f"--pipeline_config_path={pipeline_dir} --output_directory={save_dir}"
        _ = subprocess.Popen(command.split())

    def save_best_ckpt(self, best_ckpt: str, step: str):
        """!
        Save best checkpoint.
        @param str best_ckpt: Best checkpoint path.
        @param str step: Best checkpoint step.
        @return
        """
        if not os.path.exists(self.best_ckpt_path):
            with open(self.best_ckpt_path, mode='w'): pass
        with open(self.best_ckpt_path, mode='r') as f:
            ckpt = f.read()

        if str(ckpt) != step:
            with open(self.best_ckpt_path, mode='w') as f:
                f.write(step)
            with open(os.path.join(self.best_ckpt_dir, "checkpoint"), "w") as checkpoint_file:
                checkpoint_file.write("model_checkpoint_path: \"{}\"".format(best_ckpt.split('/')[-1]))

            dir = '/'.join(best_ckpt.split('/')[:-1])
            ckpt_files = os.listdir(dir)
            ckpt_files_now = [os.path.join(dir, file) for file in ckpt_files]
            ckpt_files_future = [os.path.join(self.best_ckpt_dir, file) for file in ckpt_files]
            ckpt_delete = [os.path.join(self.best_ckpt_dir, i) for i in os.listdir(self.best_ckpt_dir)]

            for ckpt_del in ckpt_delete:
                if 'ckpt-' in ckpt_del:
                    logger.info('Deleting old checkpoint {0}...'.format(ckpt_del))
                    os.remove(ckpt_del)

            for i in range(len(ckpt_files)):
                if ckpt_files_now[i].startswith(best_ckpt):
                    shutil.copyfile(ckpt_files_now[i], ckpt_files_future[i])

            with open(self.step_val_path, mode='r') as f:
                step_val = int(f.read())
            if step_val % self.save_step == 2:
                logger.info('Start saving best checkpoint {0}...'.format(best_ckpt))
                self.froze_model()

    def __call__(self):
        df = pd.read_csv(self.val_loss_path)
        loss = df['total_loss'].to_list()
        ckpt = df['ckpt'].to_list()
        step = df['step'].to_list()

        best_ckpt, best_step = self.algorithm(loss, ckpt, step)
        self.save_best_ckpt(best_ckpt, str(best_step))


