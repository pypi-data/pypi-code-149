
from ..core.plci_core_scheduler import Scheduler
from ..core.plci_core_data_type import DataType
from ..core.plci_core_signal import Signal
from ..core.plci_core_scheduler_params import SchedulerParams

from .unit_test import get_boxes_libraries, get_schedulers_library, simulate

# Get library
boxesLibraries = get_boxes_libraries()
schedulersLibraries = get_schedulers_library()

print("Creation of the diagram")
# Scheduler parameters
scheduler : Scheduler = schedulersLibraries.construct_scheduler('Schedulers', 'Default')
scheduler.params = SchedulerParams(10.0, 0.001)

# Signals
scheduler.diagram.append(Signal(index_ = 0, signal_type_ = DataType.FLOAT, default_value_ = 0.0))
scheduler.diagram.append(Signal(index_ = 1, signal_type_ = DataType.FLOAT, default_value_ = 0.0))
scheduler.diagram.append(Signal(index_ = 2, signal_type_ = DataType.FLOAT, default_value_ = 0.0))
scheduler.diagram.append(Signal(index_ = 3, signal_type_ = DataType.FLOAT, default_value_ = 0.0))
scheduler.diagram.append(Signal(index_ = 4, signal_type_ = DataType.FLOAT, default_value_ = 0.0))
scheduler.diagram.append(Signal(index_ = 5, signal_type_ = DataType.FLOAT, default_value_ = 0.0))
scheduler.diagram.append(Signal(index_ = 6, signal_type_ = DataType.FLOAT, default_value_ = 0.0))

# Sources
scheduler.diagram.append(boxesLibraries.construct_box('Boxes.Sources', 'Ramp', start_time = 0.0, initial_value = 0.0, slope = 1.0))

# Constants
scheduler.diagram.append(boxesLibraries.construct_box('Boxes.Sources', 'Constant', value = -5.0))

# Additioner
scheduler.diagram.append(boxesLibraries.construct_box('Boxes.Math', 'Addition'))

# Multiplier
scheduler.diagram.append(boxesLibraries.construct_box('Boxes.Math', 'Multiplier'))

# Integrator
scheduler.diagram.append(boxesLibraries.construct_box('Boxes.Math', 'Integrator'))

# Derivator
scheduler.diagram.append(boxesLibraries.construct_box('Boxes.Math', 'Derivator'))

# Sink
scheduler.diagram.append(boxesLibraries.construct_box('Boxes.Sinks', 'Graph', start_time = 0.0, stop_time = scheduler.stop_time, title = "x_1"))
scheduler.diagram.append(boxesLibraries.construct_box('Boxes.Sinks', 'Graph', start_time = 0.0, stop_time = scheduler.stop_time, title = "x_squared"))
scheduler.diagram.append(boxesLibraries.construct_box('Boxes.Sinks', 'Graph', start_time = 0.0, stop_time = scheduler.stop_time, title = "integrated_x_squared"))
scheduler.diagram.append(boxesLibraries.construct_box('Boxes.Sinks', 'Graph', start_time = 0.0, stop_time = scheduler.stop_time, title = "derivated_x_squared"))
 
# Diagram creation
scheduler.diagram.add_box_outputs(scheduler.diagram.boxes[0], scheduler.diagram.signals[0])
scheduler.diagram.add_box_outputs(scheduler.diagram.boxes[1], scheduler.diagram.signals[1])
scheduler.diagram.add_box_outputs(scheduler.diagram.boxes[2], scheduler.diagram.signals[2], scheduler.diagram.signals[6])
scheduler.diagram.add_box_outputs(scheduler.diagram.boxes[3], scheduler.diagram.signals[3])
scheduler.diagram.add_box_outputs(scheduler.diagram.boxes[4], scheduler.diagram.signals[4])
scheduler.diagram.add_box_outputs(scheduler.diagram.boxes[5], scheduler.diagram.signals[5])

scheduler.diagram.add_box_inputs(scheduler.diagram.boxes[2], scheduler.diagram.signals[0], scheduler.diagram.signals[1])
scheduler.diagram.add_box_inputs(scheduler.diagram.boxes[3], scheduler.diagram.signals[2], scheduler.diagram.signals[6])
scheduler.diagram.add_box_inputs(scheduler.diagram.boxes[6], scheduler.diagram.signals[6])
scheduler.diagram.add_box_inputs(scheduler.diagram.boxes[7], scheduler.diagram.signals[3])
scheduler.diagram.add_box_inputs(scheduler.diagram.boxes[4], scheduler.diagram.signals[3])
scheduler.diagram.add_box_inputs(scheduler.diagram.boxes[5], scheduler.diagram.signals[3])
scheduler.diagram.add_box_inputs(scheduler.diagram.boxes[8], scheduler.diagram.signals[4])
scheduler.diagram.add_box_inputs(scheduler.diagram.boxes[9], scheduler.diagram.signals[5])

# Launch solver
simulate(scheduler)