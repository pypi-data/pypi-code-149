
from muphyn.packages.core.plci_core_scheduler import Scheduler

from muphyn.packages.core.plci_core_data_type import DataType
from muphyn.packages.core.plci_core_signal import Signal
from muphyn.packages.core.plci_core_scheduler_params import SchedulerParams
from muphyn.packages.core.plci_core_diagram import Diagram

from muphyn.packages.unit_test.unit_test import get_boxes_libraries, get_schedulers_library, simulate

# Get library
boxesLibraries = get_boxes_libraries()
schedulersLibraries = get_schedulers_library()

# Scheduler parameters
scheduler : Scheduler = schedulersLibraries.construct_scheduler('Schedulers', 'Default')
scheduler.params = SchedulerParams(5.0, 0.001)

## DIAGRAM 1
diagram1 : Diagram = Diagram()
diagram1.append(Signal(index_ = 0, signal_type_ = DataType.FLOAT, default_value_ = 0.0))
diagram1.append(Signal(index_ = 1, signal_type_ = DataType.FLOAT, default_value_ = 0.0))
diagram1.append(Signal(index_ = 2, signal_type_ = DataType.FLOAT, default_value_ = 0.0))
diagram1.append(Signal(index_ = 3, signal_type_ = DataType.FLOAT, default_value_ = 0.0))
diagram1.append(Signal(index_ = 4, signal_type_ = DataType.FLOAT, default_value_ = 0.0))

diagram1.append(boxesLibraries.construct_box('Boxes.Math', 'Addition'))
diagram1.append(boxesLibraries.construct_box('Boxes.Sources', 'Constant', value = 3))
diagram1.append(boxesLibraries.construct_box('Boxes.Signals', 'Amplifier', gain = 10))

diagram1.add_box_inputs(diagram1.boxes[0], diagram1.signals[0], diagram1.signals[1], diagram1.signals[2])
diagram1.add_box_inputs(diagram1.boxes[2], diagram1.signals[3])

diagram1.add_box_outputs(diagram1.boxes[0], diagram1.signals[3])
diagram1.add_box_outputs(diagram1.boxes[1], diagram1.signals[2])
diagram1.add_box_outputs(diagram1.boxes[2], diagram1.signals[4])

## DIAGRAM 2
scheduler.diagram.append(Signal(index_ = 0, signal_type_ = DataType.FLOAT, default_value_ = 0.0))
scheduler.diagram.append(Signal(index_ = 1, signal_type_ = DataType.FLOAT, default_value_ = 0.0))
scheduler.diagram.append(Signal(index_ = 2, signal_type_ = DataType.FLOAT, default_value_ = 0.0))

scheduler.diagram.append(boxesLibraries.construct_box('Boxes.Sources', 'Step', start_value = 0, stop_value = 1, step_time = 0.5))
scheduler.diagram.append(boxesLibraries.construct_box('Boxes.Sources', 'Ramp', start_time = 0, initial_value = 0, slope = 0.1))
scheduler.diagram.append(boxesLibraries.construct_box('Boxes.Sinks', 'Graph', start_time = 0, stop_time = scheduler.stop_time))

scheduler.diagram.add_box_inputs(scheduler.diagram.boxes[2], scheduler.diagram.signals[2])

scheduler.diagram.add_box_outputs(scheduler.diagram.boxes[0], scheduler.diagram.signals[0])
scheduler.diagram.add_box_outputs(scheduler.diagram.boxes[1], scheduler.diagram.signals[1])

print("Diagram 1 boxes : ")
for box in diagram1.boxes :
    print("\t - ", box)

print("Diagram 2 boxes : ")
for box in scheduler.diagram.boxes :
    print("\t - ", box)


scheduler.diagram.append(diagram1)
scheduler.diagram.add_linked_signals(scheduler.diagram.signals[0], scheduler.diagram.signals[3])
scheduler.diagram.add_linked_signals(scheduler.diagram.signals[1], scheduler.diagram.signals[4])
scheduler.diagram.add_linked_signals(scheduler.diagram.signals[7], scheduler.diagram.signals[2])

# Launch solver
simulate(scheduler)