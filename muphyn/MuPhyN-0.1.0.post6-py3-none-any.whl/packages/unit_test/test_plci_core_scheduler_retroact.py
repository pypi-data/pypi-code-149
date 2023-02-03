
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
scheduler.params = SchedulerParams(4.0, 0.001)

scheduler.diagram.append(Signal(index_ = 0, signal_type_ = DataType.FLOAT, default_value_ = 0.0))
scheduler.diagram.append(Signal(index_ = 1, signal_type_ = DataType.FLOAT, default_value_ = 0.0))
scheduler.diagram.append(Signal(index_ = 2, signal_type_ = DataType.FLOAT, default_value_ = 0.0))
scheduler.diagram.append(Signal(index_ = 3, signal_type_ = DataType.FLOAT, default_value_ = 0.0))
scheduler.diagram.append(Signal(index_ = 4, signal_type_ = DataType.FLOAT, default_value_ = 0.0))
scheduler.diagram.append(Signal(index_ = 5, signal_type_ = DataType.FLOAT, default_value_ = 0.0))

scheduler.diagram.append(boxesLibraries.construct_box('Boxes.Sources', 'Step', start_value = 0, stop_value = 1, step_time = 1))
scheduler.diagram.append(boxesLibraries.construct_box('Boxes.Math', 'Addition'))
scheduler.diagram.append(boxesLibraries.construct_box('Boxes.Sources', 'Constant', value = 3))
scheduler.diagram.append(boxesLibraries.construct_box('Boxes.Math', 'Multiplier'))
scheduler.diagram.append(boxesLibraries.construct_box('Boxes.Math', 'Integrator'))
scheduler.diagram.append(boxesLibraries.construct_box('Boxes.Signals', 'Amplifier', gain = -0.98))
scheduler.diagram.append(boxesLibraries.construct_box('Boxes.Sinks', 'Graph', start_time = 0, stop_time = scheduler.stop_time, title = "step", label_y = "Amplitude (V)", label_x = "Time (s)"))
scheduler.diagram.append(boxesLibraries.construct_box('Boxes.Sinks', 'Graph', start_time = 0, stop_time = scheduler.stop_time, title = "output", label_y = "Amplitude (V)", label_x = "Time (s)"))
 
# Diagram creation
#ODE

scheduler.diagram.add_box_outputs(scheduler.diagram.boxes[0], scheduler.diagram.signals[0])
scheduler.diagram.add_box_outputs(scheduler.diagram.boxes[1], scheduler.diagram.signals[1])
scheduler.diagram.add_box_outputs(scheduler.diagram.boxes[2], scheduler.diagram.signals[2])
scheduler.diagram.add_box_outputs(scheduler.diagram.boxes[3], scheduler.diagram.signals[3])
scheduler.diagram.add_box_outputs(scheduler.diagram.boxes[4], scheduler.diagram.signals[4])
scheduler.diagram.add_box_outputs(scheduler.diagram.boxes[5], scheduler.diagram.signals[5])

scheduler.diagram.add_box_inputs(scheduler.diagram.boxes[1], scheduler.diagram.signals[0], scheduler.diagram.signals[5])
scheduler.diagram.add_box_inputs(scheduler.diagram.boxes[3], scheduler.diagram.signals[1], scheduler.diagram.signals[2])
scheduler.diagram.add_box_inputs(scheduler.diagram.boxes[4], scheduler.diagram.signals[3])
scheduler.diagram.add_box_inputs(scheduler.diagram.boxes[5], scheduler.diagram.signals[4])
scheduler.diagram.add_box_inputs(scheduler.diagram.boxes[6], scheduler.diagram.signals[0])
scheduler.diagram.add_box_inputs(scheduler.diagram.boxes[7], scheduler.diagram.signals[4])

# Launch solver
if simulate(scheduler) :
    print("===============================================")
    print("Values : ")
    l = len(scheduler.diagram.boxes[7].params['data_y'])
    for i in range(l) :
        print(str(scheduler.diagram.boxes[7].params['data_y'][i]).replace('.', ','))