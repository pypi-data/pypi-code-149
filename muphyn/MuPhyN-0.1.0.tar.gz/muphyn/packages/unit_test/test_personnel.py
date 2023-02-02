
from ..core.plci_core_scheduler import Scheduler
from ..core.plci_core_data_type import DataType
from ..core.plci_core_signal import Signal
from ..core.plci_core_scheduler_params import SchedulerParams

from .unit_test import get_boxes_libraries, get_schedulers_library, simulate

# Get libraries
boxesLibraries = get_boxes_libraries()
schedulersLibraries = get_schedulers_library()

# Scheduler parameters
print("Creation of the scheduler")
scheduler : Scheduler = schedulersLibraries.construct_scheduler('Schedulers', 'Default')
scheduler.params = SchedulerParams(5.0, 0.001)

# Signals
print("Creation of the diagram")
scheduler.diagram.append(Signal(index_ = 0, signal_type_ = DataType.FLOAT, default_value_ = 0.0))
scheduler.diagram.append(Signal(index_ = 1, signal_type_ = DataType.FLOAT, default_value_ = 0.0))
scheduler.diagram.append(Signal(index_ = 2, signal_type_ = DataType.FLOAT, default_value_ = 0.0))
scheduler.diagram.append(Signal(index_ = 3, signal_type_ = DataType.FLOAT, default_value_ = 0.0))
scheduler.diagram.append(Signal(index_ = 4, signal_type_ = DataType.FLOAT, default_value_ = 0.0))
scheduler.diagram.append(Signal(index_ = 5, signal_type_ = DataType.FLOAT, default_value_ = 0.0))

# Sources
scheduler.diagram.append(boxesLibraries.construct_box('Boxes.Sources', 'Sine', amplitude = 10, pulsation = 10, phase = 0))
scheduler.diagram.append(boxesLibraries.construct_box('Boxes.Sources', 'Sine', amplitude = 5, pulsation = 20, phase = 0))

# Addition
scheduler.diagram.append(boxesLibraries.construct_box('Boxes.Math', 'Addition'))

# Sink
scheduler.diagram.append(boxesLibraries.construct_box('Boxes.Sinks', 'Graph', start_time = 0, stop_time = scheduler.stop_time, title = 'Sinus', label_x = 'Temps (s)', label_y = 'Amplitude (v)' ))

# Sources additional
scheduler.diagram.append(boxesLibraries.construct_box('Boxes.Sources', 'Sine', amplitude = 1, pulsation = 100, phase = 0))

# Rampe
scheduler.diagram.append(boxesLibraries.construct_box('Boxes.Sources', 'Ramp', start_time = 0, initial_value = 1, slope = -0.20))

# Multiplication
scheduler.diagram.append(boxesLibraries.construct_box('Boxes.Math', 'Multiplier'))
 
# Diagram creation
scheduler.diagram.add_box_outputs(scheduler.diagram.boxes[0], scheduler.diagram.signals[0])
scheduler.diagram.add_box_outputs(scheduler.diagram.boxes[1], scheduler.diagram.signals[1])
scheduler.diagram.add_box_outputs(scheduler.diagram.boxes[2], scheduler.diagram.signals[2])
scheduler.diagram.add_box_outputs(scheduler.diagram.boxes[4], scheduler.diagram.signals[3])
scheduler.diagram.add_box_outputs(scheduler.diagram.boxes[5], scheduler.diagram.signals[4])
scheduler.diagram.add_box_outputs(scheduler.diagram.boxes[6], scheduler.diagram.signals[5])

scheduler.diagram.add_box_inputs(scheduler.diagram.boxes[2], scheduler.diagram.signals[0], scheduler.diagram.signals[1], scheduler.diagram.signals[3])
scheduler.diagram.add_box_inputs(scheduler.diagram.boxes[6], scheduler.diagram.signals[2], scheduler.diagram.signals[4])
scheduler.diagram.add_box_inputs(scheduler.diagram.boxes[3], scheduler.diagram.signals[5])

# Launch solver
simulate(scheduler)