
from muphyn.packages.core.box_library.plci_core_boxes_libraries import BoxesLibraries
from muphyn.packages.core.plci_core_scheduler import Scheduler
from muphyn.packages.core.plci_core_data_type import DataType
from muphyn.packages.core.plci_core_signal import Signal
from muphyn.packages.core.plci_core_scheduler_params import SchedulerParams
from muphyn.packages.core.scheduler_library.plci_core_schedulers_libraries import SchedulersLibraries

from muphyn.packages.unit_test.unit_test import get_boxes_libraries, get_schedulers_library, simulate

# Get library
boxesLibraries : BoxesLibraries = get_boxes_libraries()
schedulersLibraries : SchedulersLibraries = get_schedulers_library()

# Parameters
scheduler : Scheduler = schedulersLibraries.construct_scheduler('Schedulers', 'Default')
scheduler.params = SchedulerParams(stop_time_ = 0.2, step_time_ = 0.0001)


# Signal de source (Carré)
s0 = Signal(0, DataType.FLOAT, 0.0)
scheduler.diagram.append(s0)

# Signal dérivé
s1 = Signal(1, DataType.FLOAT, 0.0)
scheduler.diagram.append(s1)

# Sources (Carré)
period = scheduler.stop_time / 3
high_time = period / 3
print("Square wave period : ", period)
print("High time : ", high_time)
b0 = boxesLibraries.construct_box('Boxes.Sources', 'Square', high_value = 1, low_value = 0, period = period, high_time = high_time)
scheduler.diagram.append(b0)

# Boxe de dérivation
b1 = boxesLibraries.construct_box('Boxes.Math', 'Derivator')
scheduler.diagram.append(b1)

# Sink
b2 = boxesLibraries.construct_box('Boxes.Sinks', 'Graph', start_time = 0, stop_time = scheduler.stop_time, title = "square waves", label_x = "Temps (s)", label_y = "Amplitude (v)")
scheduler.diagram.append(b2)

b3 = boxesLibraries.construct_box('Boxes.Sinks', 'Graph', start_time = 0, stop_time = scheduler.stop_time, title = "Derivative signal", label_x = "Temps (s)", label_y = "Amplitude (v)")
scheduler.diagram.append(b3)

# Diagram creation
scheduler.diagram.add_box_outputs(scheduler.diagram.boxes[0], scheduler.diagram.signals[0])
scheduler.diagram.add_box_outputs(scheduler.diagram.boxes[1], scheduler.diagram.signals[1])

scheduler.diagram.add_box_inputs(scheduler.diagram.boxes[1], scheduler.diagram.signals[0])
scheduler.diagram.add_box_inputs(scheduler.diagram.boxes[2], scheduler.diagram.signals[0])
scheduler.diagram.add_box_inputs(scheduler.diagram.boxes[3], scheduler.diagram.signals[1])


# Launch solver
simulate(scheduler)