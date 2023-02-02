# General Imports
import numbers
import os
import re
from typing import Any
from threading import Thread

# OPCUA connection
from opcua import Client, Node
from opcua.ua.uatypes import LocalizedText

# Open Modelica Libraries Imports
from OMPython import ModelicaSystem

from muphyn.packages.core.simulation.abstract_simulation import AbstractSimulation
from muphyn.packages.core.utils.directory_manager import DirectoryManager
from muphyn.packages.core.utils.log_manager import LogManager


class OpenModelicaSimulationController:
    def __init__(self, url: str):
        # URL
        self._url = url

        # OPC-UA client
        self._client = Client(url)

    # --------------
    # Properties
    # --------------
    @property
    def url(self) -> str:
        return self._url

    @url.setter
    def url(self, new_url) -> None:
        if self._url != new_url:
            self._url = new_url

            # Reset client
            self._client.disconnect()
            self._client = Client(new_url)
        
    # --------------
    # Methods
    # --------------
    def init_connection(self):
        try:
            # Connect to the client
            self._client.connect()

            # Get object nodes
            self._object_nodes = self.get_object_nodes()

            # Get run node
            self._run_node = self.get_node("run")

            # Get step node
            self._step_node = self.get_node("step")

            # Get realTimeScalingFactor node
            self._real_time_scaling_factor = self.get_node("realTimeScalingFactor")

            # Get enableStopTime node
            self._enable_stop_time = self.get_node("enableStopTime")

            # Get time node
            self._time = self.get_node("time")

            # Get terminate node
            self._terminate = self.get_node("terminate")
        except: 
            LogManager().error("Connection not established")

    def disconnect(self):
        self._client.disconnect()

    def get_object_nodes(self) -> dict:
        # Init object node dict
        object_nodes = {}

        # Get root node
        root_node: Node = self._client.get_root_node()
        root_node_display_name: LocalizedText = root_node.get_display_name()

        for child_node in root_node.get_children():
            root_child_display_name: LocalizedText = child_node.get_display_name()
            if root_child_display_name.Text == "Objects":
                for object_node in child_node.get_children():
                    object_node: Node = object_node
                    object_node_display_name = object_node.get_display_name()
                    object_nodes[object_node_display_name.Text] = object_node

        return object_nodes

    def get_node(self, node_name: str) -> Node:
        return self._object_nodes[node_name]

    def get_node_value(self, param_name: str) -> Any:
        # Get Node ID
        node = self.get_node(param_name)

        # Get Value
        return node.get_value()

    def set_node_value(self, param_name: str, value: Any) -> Any:
        # Get Node ID
        node = self.get_node(param_name)

        # Get Value
        return node.set_value(value)

    def make_step(self, is_last_step: bool = False):
        # Make step
        self._step_node.set_value(True)

        if not is_last_step:
            while self._step_node.get_value():
                pass

    def terminate(self):
        # Run the rest of the simulation (terminate command doesn't work)
        self._run_node.set_value(True)

    def get_simulation_time(self):
        return self._time.get_value()

class OpenModelicaSimulation(AbstractSimulation):

    # Default simulation values
    DefaultIsRealTime: bool = True
    DefaultPort: int = 4841
    DefaultSolver: str = "dassl"
    DefaultTolerance: float = 1e-12

    # Component name pattern
    ComponentPattern: str = "^(?P<component_name>\w+)\\.(?P<quantity_name>.+)$"
    
    # Solvers
    AvailableSolvers: list[str] = [
        "cvcode",
        "dassl",
        "euler", 
        "ida",
        "impeuleur",
        "imprungekutta",
        "irksco",
        "heun",
        "optimization",
        "qss",
        "rungekutta",
        "rungekuttaSsc",
        "symSolver",
        "symSolverSsc",
        "trapezoid"
    ]

    def __init__(self, om_file_path: str) -> None:
        super().__init__()

        # Change Directoryif not os.path.isabs(mo_filename):
        om_file_path = os.path.join(os.getcwd(), om_file_path).replace("\\","/")

        if os.path.exists(om_file_path):
            # Extract working directory
            self.working_directory = os.path.dirname(om_file_path)
            self.om_filename = os.path.basename(om_file_path)

            # Change current Directory before starting Open Modelica Processes
            DirectoryManager().set_working_directory(self.working_directory)

            # Init System
            self.om_system = ModelicaSystem(self.om_filename, ".".join(self.om_filename.split(".")[:-1]))

            if self.om_system.xmlFile is not None and self.om_system.tree is not None:
                # Get model informations
                self._inputs = self.om_system.getInputs()
                self._outputs = self.om_system.getOutputs()
                self._parameters = self.om_system.getParameters()
                self._components = self.get_components()

                # Init Simulation options with default values
                self._tolerance = OpenModelicaSimulation.DefaultTolerance
                self._solver = OpenModelicaSimulation.DefaultSolver

                # Port
                self._port = OpenModelicaSimulation.DefaultPort

                # Is real time simulation
                self._is_real_time = OpenModelicaSimulation.DefaultIsRealTime

                # Reset working directory
                DirectoryManager().reset_working_directory()

            else:
                # Reset working directory
                DirectoryManager().reset_working_directory()

                # Raise type error
                raise(TypeError(f"File is not a valid Open Modelica file : {self.om_system.xmlFile} {self.om_system.tree}"))

        else:
            raise(FileNotFoundError(f"Open Modelica file doesn't exists : {om_file_path}"))

    # --------------
    # Properties
    # --------------
    @property
    def tolerance(self) -> numbers.Number:
        return self._tolerance

    @tolerance.setter
    def tolerance(self, new_tolerance: numbers.Number) -> None:
        if OpenModelicaSimulation.is_valid_tolerance(new_tolerance) and new_tolerance != self._tolerance:
            self._tolerance = new_tolerance

    @property
    def solver(self) -> str:
        return self._solver

    @solver.setter
    def solver(self, new_solver: str) -> None:
        if OpenModelicaSimulation.is_valid_solver(new_solver) and new_solver != self._solver:
            self._solver = new_solver

    @property
    def port(self) -> numbers.Number:
        return self._port

    @port.setter
    def port(self, new_port: numbers.Number) -> None:
        if OpenModelicaSimulation.is_valid_port(new_port) and new_port != self._port:
            self._port = new_port

    @property
    def is_real_time(self) -> numbers.Number:
        return self._is_real_time

    @is_real_time.setter
    def is_real_time(self, new_is_real_time: numbers.Number) -> None:
        if OpenModelicaSimulation.is_valid_is_real_time(new_is_real_time) and new_is_real_time != self._is_real_time:
            self._is_real_time = new_is_real_time

    # --------------
    # Methods
    # --------------
    def get_components(self):
        components = {}
        for solution_name in self.om_system.getContinuous():
            continuous_item_value = self.om_system.getContinuous(solution_name)
            OpenModelicaSimulation.extract_continuous_information(components, solution_name, continuous_item_value)
        return components

    def init_simulation(self):
        # Set default value if unexpected values
        # Tolerance
        if not OpenModelicaSimulation.is_valid_tolerance(self._tolerance):
            self._tolerance = OpenModelicaSimulation.DefaultTolerance

        # Solver
        if not OpenModelicaSimulation.is_valid_solver(self._solver):
            self._solver = OpenModelicaSimulation.DefaultSolver

        # Init Simulation
        self.om_system.setSimulationOptions([
            f"startTime={self._start_time}",
            f"stopTime={self._stop_time}",
            f"stepSize={self._step_size}",
            f"tolerance={self._tolerance}",
            f"solver={self._solver}",
        ])

    def run_simulation(self):

        # Set Working Directory
        DirectoryManager().set_working_directory(self.working_directory)

        # Build Model
        self.om_system.buildModel()

        # Run Simulation
        simflags = [
            "-embeddedServer=opc-ua",
            f"-embeddedServerPort={self._port}"
        ]

        # Run Simulation
        try:
            if self._is_real_time:
                simflags.insert(0, "-rt=1.0")

            # Rn in a different thread
            self.simulation_thread = Thread(target=self.om_system.simulate, daemon=True, kwargs={"simflags": " ".join(simflags)})
            self.simulation_thread.start()
        except:
            pass

        # Set simulation controller
        self.simulation_controller = OpenModelicaSimulationController(f"opc.tcp://127.0.0.1:{self._port}")
        self.simulation_controller.init_connection()
        DirectoryManager().reset_working_directory()

    def set_simulation_options(
            self, 
            start_time: float = None, 
            stop_time: float = None, 
            step_size: float = None, 
            tolerance: float = None, 
            solver: str = None
        ):
        # Common parameters
        super().set_simulation_options(start_time, stop_time, step_size)

        # Tolerance
        if OpenModelicaSimulation.is_valid_tolerance(tolerance):
            self._tolerance = tolerance

        # Solver
        if OpenModelicaSimulation.is_valid_solver(solver):
            self._solver = solver

    def get_node_value(self, param_name: str) -> Any:
        return self.simulation_controller.get_node_value(param_name)

    def set_node_value(self, param_name: str, value: Any) -> Any:
        self.simulation_controller.set_node_value(param_name, value)

    def make_step(self, is_last_step: bool = False):
        self.simulation_controller.make_step(is_last_step)

    def terminate(self):
        # Terminate simulation
        self.simulation_controller.terminate()

        # Wait for thread finished
        self.simulation_thread.join()

        # Disconnect client
        self.simulation_controller.disconnect()

    def get_simulation_time(self):
        return self.simulation_controller.get_simulation_time()
    

    # --------------
    # Static Methods
    # --------------
    @staticmethod
    def extract_continuous_information(component_dict: dict, continuous_item: str, value, depth=1) -> dict:
        # Extract separate component & quantity name
        for match in re.finditer(OpenModelicaSimulation.ComponentPattern, continuous_item):
            # Get component name
            component_name = match.groupdict()["component_name"]

            # Get quantity name
            quantity_name = match.groupdict()["quantity_name"]

            # If component not already added → create it as dict
            if component_name not in component_dict:
                component_dict[component_name] = {}

            if re.match(OpenModelicaSimulation.ComponentPattern, quantity_name):
                # Handle sub quantity parameter
                sub_component_dict = component_dict[component_name]
                OpenModelicaSimulation.extract_continuous_information(sub_component_dict, quantity_name, value, depth+1)
            else:
                # Set value
                component_dict[component_name][quantity_name] = value

    @staticmethod
    def is_valid_tolerance(tolerance: Any):
        return tolerance is not None and isinstance(tolerance, numbers.Number)

    @staticmethod
    def is_valid_solver(solver: Any):
        return solver is not None and isinstance(solver, str) and solver in OpenModelicaSimulation.AvailableSolvers
    
    @staticmethod
    def is_valid_port(port: Any):
        return port is not None and isinstance(port, int)

    @staticmethod
    def is_valid_is_real_time(is_real_time: Any):
        return is_real_time is not None and isinstance(is_real_time, bool) 
    
