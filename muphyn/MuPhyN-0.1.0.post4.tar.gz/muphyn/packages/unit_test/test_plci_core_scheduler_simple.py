
from ..core.plci_core_scheduler import Scheduler
from ..core.plci_core_data_type import DataType
from ..core.plci_core_signal import Signal
from ..core.plci_core_scheduler_params import SchedulerParams

from .unit_test import get_boxes_libraries, get_schedulers_library, simulate

# Get library
boxesLibraries = get_boxes_libraries()
schedulersLibraries = get_schedulers_library()

# Scheduler parameters
scheduler : Scheduler = schedulersLibraries.construct_scheduler('Schedulers', 'Default')
scheduler.params = SchedulerParams(stop_time_ = 1.0, step_time_ = 0.001)

scheduler.diagram.append(Signal(0, DataType.FLOAT, 0.0))
scheduler.diagram.append(Signal(1, DataType.FLOAT, 0.0))
scheduler.diagram.append(Signal(2, DataType.FLOAT, 0.0))
scheduler.diagram.append(Signal(3, DataType.FLOAT, 0.0))
scheduler.diagram.append(Signal(4, DataType.FLOAT, 0.0))

# Sources
scheduler.diagram.append(boxesLibraries.construct_box('Boxes.Sources', 'Step', start_value = 0.0, stop_value = 1.0, step_time = 0.5))
scheduler.diagram.append(boxesLibraries.construct_box('Boxes.Sources', 'Ramp', start_time = 0.5, initial_value = 0.0, slope = 0.5))
scheduler.diagram.append(boxesLibraries.construct_box('Boxes.Sources', 'Constant', value = 7))

# Multiplier
scheduler.diagram.append(boxesLibraries.construct_box('Boxes.Math', 'Multiplier'))
scheduler.diagram.append(boxesLibraries.construct_box('Boxes.Math', 'Multiplier'))

# Sink
scheduler.diagram.append(boxesLibraries.construct_box('Boxes.Sinks', 'Graph', start_time = 0, stop_time = 1.0, title = "step box"))
scheduler.diagram.append(boxesLibraries.construct_box('Boxes.Sinks', 'Graph', start_time = 0, stop_time = 1.0, title = "ramp box"))
scheduler.diagram.append(boxesLibraries.construct_box('Boxes.Sinks', 'Graph', start_time = 0, stop_time = 1.0, title = "output"))
 
# Diagram creation
scheduler.diagram.add_box_outputs(scheduler.diagram.boxes[0], scheduler.diagram.signals[0])
scheduler.diagram.add_box_outputs(scheduler.diagram.boxes[1], scheduler.diagram.signals[1])
scheduler.diagram.add_box_outputs(scheduler.diagram.boxes[2], scheduler.diagram.signals[2])
scheduler.diagram.add_box_outputs(scheduler.diagram.boxes[3], scheduler.diagram.signals[3])
scheduler.diagram.add_box_outputs(scheduler.diagram.boxes[4], scheduler.diagram.signals[4])

scheduler.diagram.add_box_inputs(scheduler.diagram.boxes[3], scheduler.diagram.signals[0], scheduler.diagram.signals[1])
scheduler.diagram.add_box_inputs(scheduler.diagram.boxes[4], scheduler.diagram.signals[3], scheduler.diagram.signals[2])
scheduler.diagram.add_box_inputs(scheduler.diagram.boxes[5], scheduler.diagram.signals[0])
scheduler.diagram.add_box_inputs(scheduler.diagram.boxes[6], scheduler.diagram.signals[1])
scheduler.diagram.add_box_inputs(scheduler.diagram.boxes[7], scheduler.diagram.signals[4])


# Launch solver
simulate(scheduler)