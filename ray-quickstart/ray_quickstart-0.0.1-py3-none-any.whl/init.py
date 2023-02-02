"""
Utilities for working with Ray.
"""
import os
import shutil
import subprocess
import tempfile

import ray
from ray import logger
from ray.air import session, Checkpoint

from src.ray_quickstart.rsync_syncer import RsyncSyncer
from src.ray_quickstart.util.platform import expand_user_home_path

EXCLUDED_PROJECT_DIRS = ['__pycache__', '.git', '.idea', '.pytest_cache', 'data', 'docs', 'logs', 'models', 'notebooks', 'runs', 'scripts', 'scripts', 'setup', 'tests']


def initialize_ray(config,
                   base_dir,
                   src_dir,
                   driver_computer_username,
                   driver_computer_hostname,
                   ray_cluster_username,
                   ray_cluster_hostname,
                   success_callback=None):
    if not ray.is_initialized() and config.get_run_on_ray_cluster():
        # runtime_env is required for cloudpickle to be able to find modules
        runtime_env = {'working_dir': src_dir}
        try:
            clear_local_trial_results_dir(RsyncSyncer(driver_computer_username,
                                                      driver_computer_hostname,
                                                      ray_cluster_username,
                                                      ray_cluster_hostname,
                                                      'linux'))
            #ray.init(local_mode=True, ignore_reinit_error=True)
            ray.init(address='ray://192.168.2.4:10001', runtime_env=runtime_env, ignore_reinit_error=True)
            if success_callback is not None:
                success_callback()
        except ConnectionError:
            from src.ray_quickstart.util import platform
            if platform.is_windows():
                with subprocess.Popen(f'{base_dir}/scripts/ray_start.bat') as p:
                    p.wait()
                ray.init(address='ray://192.168.2.4:10001', runtime_env=runtime_env, ignore_reinit_error=True)
            else:
                raise


def get_local_trial_results_dir():
    return f'~/ray_results'


def clear_local_trial_results_dir(syncer):
    logger.info('clearing local trial results dir...')
    local_trial_results_dir = os.path.expanduser(get_local_trial_results_dir())
    if os.path.exists(local_trial_results_dir):
        delete_dir_contents(local_trial_results_dir)
    else:
        os.makedirs(local_trial_results_dir, exist_ok=True)
    if syncer is not None:
        trial_results_dir = get_local_trial_results_dir()
        syncer.sync_down(trial_results_dir,
                         expand_user_home_path(trial_results_dir,
                                               syncer.worker_username,
                                               syncer.worker_platform))


def delete_dir_contents(dir_path):
    for filename in os.listdir(dir_path):
        file_path = os.path.join(dir_path, filename)
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path, ignore_errors=True)


def save_checkpoint_as_directory(metrics, model):
    if metrics is None:
        metrics = {}
    temp_dir = tempfile.mkdtemp()
    model.set_models_dir(temp_dir)
    model.save_model()
    model.set_models_dir(None)
    session.report(metrics, checkpoint=Checkpoint.from_directory(temp_dir))
    shutil.rmtree(temp_dir)


def update_model_using_directory_checkpoint(checkpoint, model):
    checkpoint_dir = checkpoint.uri[7:]
    model.load_from_checkpoint(checkpoint_dir)
