# General imports
import numbers
from typing import Any

class AbstractSimulation:
    def __init__(self) -> None:

        # Model Informations
        self._inputs: dict = {}
        self._outputs: dict = {}
        self._parameters: dict = {}
        self._components: dict = {}

        # Simulation Informations
        self._start_time: float = None
        self._stop_time: float = None
        self._step_size: float = None

    # -------------
    # Properties
    # -------------
    @property
    def inputs(self) -> dict:
        return self._inputs

    @property
    def outputs(self) -> dict:
        return self._outputs

    @property
    def parameters(self) -> dict:
        return self._parameters

    @property
    def components(self) -> dict:
        return self._components

    @property
    def start_time(self) -> numbers.Number:
        return self._start_time

    @start_time.setter
    def start_time(self, new_start_time: numbers.Number) -> None:
        if AbstractSimulation.is_valid_start_time(new_start_time) and new_start_time != self._start_time:
            self._start_time = new_start_time

    @property
    def stop_time(self) -> numbers.Number:
        return self._stop_time

    @stop_time.setter
    def stop_time(self, new_stop_time: numbers.Number) -> None:
        if AbstractSimulation.is_valid_stop_time(new_stop_time) and new_stop_time != self._stop_time:
            self._stop_time = new_stop_time

    @property
    def step_size(self) -> numbers.Number:
        return self._step_size

    @step_size.setter
    def step_size(self, new_step_size: numbers.Number) -> None:
        if AbstractSimulation.is_valid_step_size(new_step_size) and new_step_size != self._step_size:
            self._step_size = new_step_size

    # -------------
    # Methods
    # -------------
    def run_simulation(self):
        raise(NotImplementedError(f"{type(self).__name__}.run_simulation() not implemented yet"))

    def set_simulation_options(self, start_time: float, stop_time: float, step_size:float):
        if AbstractSimulation.is_valid_start_time(start_time):
            self._start_time = start_time

        if  AbstractSimulation.is_valid_stop_time(stop_time):
            self._stop_time = stop_time

        if  AbstractSimulation.is_valid_step_size(step_size):
            self._step_size = step_size

    # --------------
    # Static Methods
    # --------------
    @staticmethod
    def is_valid_start_time(start_time: Any):
        return start_time is not None and isinstance(start_time, numbers.Number)

    @staticmethod
    def is_valid_stop_time(stop_time: Any):
        return stop_time is not None and isinstance(stop_time, numbers.Number)

    @staticmethod
    def is_valid_step_size(step_size: Any):
        return step_size is not None and isinstance(step_size, numbers.Number)
