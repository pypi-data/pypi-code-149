import shutil
import subprocess
from pathlib import Path
from typing import List

from . import exceptions, helpers
from .configs import Config


class Step:
    def __init__(self):
        pass

    def run(self, config: Config, simulate: bool = False):
        raise NotImplementedError()


class StepCreatDir(Step):
    def __init__(self, path: str):
        self.path = path

    def run(self, config: Config, simulate: bool = False):
        print(f'+ Creating {self.path} directory')
        if not Path(self.path).exists():
            Path(self.path).mkdir(parents=True, exist_ok=True)


class StepDeleteDir(Step):
    def __init__(self, path: str):
        self.path = path

    def run(self, config: Config, simulate: bool = False):
        if not Path(self.path).exists():
            return None
        print(f'+ Deleting {self.path} directory')
        shutil.rmtree(self.path)


class StepCommand(Step):
    def __init__(self, command: List[str], **kwargs):
        self.command = command
        self.work_dir = kwargs.get('work_dir')

    def run(self, config: Config, simulate: bool = False):
        print('+ Run command:')
        print(" ".join(self.command))
        if not simulate:
            p = subprocess.run(self.command, stdout=subprocess.PIPE, cwd=self.work_dir)
            if p.returncode != 0:
                raise exceptions.CommandError('command not success')


class StepCopyFileContent(Step):
    def __init__(self, file_a_path: str, file_b_path: str):
        self.file_a_path = file_a_path
        self.file_b_path = file_b_path

    def run(self, config: Config, simulate: bool = False):
        print(f'+ Copy {self.file_a_path} to {self.file_b_path}')
        with open(self.file_a_path) as fr:
            with open(self.file_b_path, "w") as fw:
                fw.write(fr.read())


class StepCopyDir(Step):
    def __init__(self, path_a: str, path_b: str):
        self.path_a = path_a
        self.path_b = path_b

    def run(self, config: Config, simulate: bool = False):
        print(f'+ Copy {self.path_a} to {self.path_b}')
        shutil.copytree(self.path_a, self.path_b)


class StepCommand(Step):
    def __init__(self, command: List[str], **kwargs):
        self.command = command
        self.work_dir = kwargs.get('work_dir')

    def run(self, config: Config, simulate: bool = False):
        print('+ Run command:')
        print(" ".join(self.command))
        if not simulate:
            p = subprocess.run(self.command, stdout=subprocess.PIPE, cwd=self.work_dir)
            if p.returncode != 0:
                raise exceptions.CommandError('command not success')


class Manager:
    def __init__(self, config: Config, steps: list, **kwargs):
        self.config = config
        self.steps = steps
        self.simulate = kwargs.get('simulate', False)

    def run(self) -> int:
        if self.simulate:
            print(helpers.bcolors.WARNING + '+ Simulate' + helpers.bcolors.ENDC)
        for step in self.steps:
            try:
                step.run(self.config, self.simulate)
            except Exception as e:
                print(helpers.bcolors.FAIL + f'ERROR: {e}' + helpers.bcolors.ENDC)
                return 1
        return 0
