
from muphyn.packages.core.box_library.plci_core_boxes_libraries import BoxesLibraries
from muphyn.packages.core.scheduler_library.plci_core_schedulers_libraries import SchedulersLibraries
from muphyn.packages.core.plci_core_data_type import DataType
from muphyn.packages.core.plci_core_signal import Signal
from muphyn.packages.core.plci_core_scheduler_params import SchedulerParams
from muphyn.packages.core.plci_core_scheduler import Scheduler

from muphyn.packages.unit_test.unit_test import get_boxes_libraries, get_schedulers_library, simulate

# Get library
boxesLibraries : BoxesLibraries = get_boxes_libraries()
schedulersLibraries : SchedulersLibraries = get_schedulers_library()

print("Creation of the diagram")
# Scheduler parameters
scheduler : Scheduler = schedulersLibraries.construct_scheduler('Schedulers', 'Default')
scheduler.params = SchedulerParams(0.05, 0.001)

# Signals
scheduler.diagram.append(Signal(index_ = 0, signal_type_ = DataType.FLOAT, default_value_ = 0.0))
scheduler.diagram.append(Signal(index_ = 1, signal_type_ = DataType.FLOAT, default_value_ = 0.0))
scheduler.diagram.append(Signal(index_ = 2, signal_type_ = DataType.FLOAT, default_value_ = 0.0))

# Sources
scheduler.diagram.append(boxesLibraries.construct_box('Boxes.Sources', 'Step', start_value = 1, stop_value = 0, step_time = 0.035))
scheduler.diagram.append(boxesLibraries.construct_box('Boxes.Sources', 'Step', start_value = 0, stop_value = 1, step_time = 0.017))

# Reccurence
C = [
        [1/2,   1/4,    1/8,    1/16,   1/32,   1/64],
        [4,     4/3,    4/9,    4/27,   4/81,  4/243],
        [1,     1/5,   1/25,   1/125,  1/625, 1/3125]  
    ]

scheduler.diagram.append(boxesLibraries.construct_box('Boxes.Math', 'Reccurence', coefficients = C))

# Sink
scheduler.diagram.append(boxesLibraries.construct_box('Boxes.Sinks', 'Graph', start_time = 0, stop_time = scheduler.stop_time, title = "Reccurence"))
 

scheduler.diagram.add_box_outputs(scheduler.diagram.boxes[0], scheduler.diagram.signals[0])
scheduler.diagram.add_box_outputs(scheduler.diagram.boxes[1], scheduler.diagram.signals[1])
scheduler.diagram.add_box_outputs(scheduler.diagram.boxes[2], scheduler.diagram.signals[2])

scheduler.diagram.add_box_inputs(scheduler.diagram.boxes[2], scheduler.diagram.signals[0], scheduler.diagram.signals[1])
scheduler.diagram.add_box_inputs(scheduler.diagram.boxes[3], scheduler.diagram.signals[2])

# Launch solver
if simulate(scheduler) :
    print("===============================================")
    print("Values : ")
    l = len(scheduler.diagram.boxes[2].params['values'][0])
    for i in range(l) :
        j = l - 1 - i
        print(str(scheduler.diagram.boxes[2].params['values'][0][j]).replace('.', ','))