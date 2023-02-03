#-----------------------------------
# Imports
#-----------------------------------
import os
from typing import List
from muphyn.packages.core.plci_core_box import Box
from muphyn.packages.core.plci_core_data_type import DataType
from muphyn.packages.core.plci_core_scheduler_params import SchedulerParams
from muphyn.packages.interface.models.graphical_models.box_model import BoxModel
from muphyn.packages.core.simulation.om_sim import OpenModelicaSimulation
from muphyn.packages.core.simulation.model_parser.open_modelica_model_parser import OpenModelicaModelParser
from muphyn.packages.core.plci_core_scheduler_event import SchedulerEvent


"""
Notes:
 - If the initialization of the node is made in the _init_function then we won't access to the inputs first value 
    → (must implement a way to create firsts values)
 - If the outputs are read before the step is made we get one  step lag ;
 - If the inputs are set before the step then we get one step lag
"""

#-----------------------------------
# Functions
#-----------------------------------
def _on_model_file_selected(box_model: BoxModel) -> List:
    # Get path value
    path_parameter = box_model.get_parameter("model_path")
    path = path_parameter["value"]

    # Init Simulation object 
    om_parser = OpenModelicaModelParser(path)

    # Set inputs
    inputs = om_parser.inputs

    for input_index, input_data in enumerate(inputs):
        if input_index >= box_model.input_len:
            input_ = box_model.append_input("inputs")
            input_.text = input_data.name
        else:
            box_model_inputs_group = box_model.get_inputs_group("inputs")
            input_ = box_model_inputs_group.inputs[input_index]
            input_.text = input_data.name

    # Set outputs
    outputs = om_parser.outputs
    for output_index, output_data in enumerate(outputs):
        if output_index >= box_model.output_len:
            output = box_model.append_output("outputs")
            output.text = output_data.name
        else:
            box_model_outputs_group = box_model.get_outputs_group("outputs")
            output = box_model_outputs_group.outputs[output_index]
            output.text = output_data.name

    return box_model

def _init_simulation (box, simulation_params: SchedulerParams) -> List :
    box.simulation_params = simulation_params
    return box

def _step_simumation (box: Box, event_: SchedulerEvent) -> List :
    # if first step → run first simulation
    if event_.timing == 0:
        # Get path
        path = box.get_parameter("model_path")

        # Get simulation parameters
        simulation_params: SchedulerParams = box.simulation_params

        # Model path parser
        om_parser = OpenModelicaModelParser(path)

        # Set all input values in model file
        for input_signal in box.inputs:
            om_parser.set_input_value(input_signal.input_name, input_signal.value)

        # Get new model file path
        tmp_dirname = os.path.join(os.path.dirname(path), "tmp")
        basename = os.path.basename(path)
        new_model_file_path = os.path.join(tmp_dirname, basename)
        
        # Save file as
        om_parser.save_file_as(new_model_file_path)

        # Init Simulation object 
        om_simulation = OpenModelicaSimulation(new_model_file_path)

        # Init Simulation
        start_time = -simulation_params.step_time # Starting one step before
        stop_time = simulation_params.stop_time + simulation_params.step_time # go one step further
        step_size = simulation_params.step_time
        om_simulation.set_simulation_options(
            start_time=start_time,
            stop_time=stop_time, 
            step_size=step_size
        )

        # Init Simulation
        om_simulation.init_simulation()

        # Run Simulation
        om_simulation.run_simulation()

        om_simulation.make_step()

        # Set om_system attribute
        box.om_simulation = om_simulation

    else:
        # Set inputs value
        muphyn_current_value = None
        for input_signal in box.inputs:
            box.om_simulation.set_node_value(input_signal.input_name, input_signal.value)
            if input_signal.input_name == "instant_current_value":
                muphyn_current_value = input_signal.value

        # Make steps
        box.om_simulation.make_step()


    # Get output values
    events : List = []
    for output_signal in box.outputs:
        output_value = box.om_simulation.get_node_value(output_signal.output_name)
        events.append(box.construct_signal_event(output_signal, output_value))

    # Return outputs
    return events



def _finish_simulation (box) -> List :
    
    # Terminate simulation
    box.om_simulation.terminate()

    v = 1
    events : List = []
    
    for output in box.outputs :
        events.append(box.construct_signal_event(output, v))

    return events