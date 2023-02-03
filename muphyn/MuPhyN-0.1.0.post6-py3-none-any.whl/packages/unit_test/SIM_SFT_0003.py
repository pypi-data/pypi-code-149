#-----------------------------------
# Imports
#-----------------------------------

from ..core.plci_core_signal_event import SignalEvent
from ..core.plci_core_scheduler import Scheduler
from ..core.plci_core_data_type import DataType
from ..core.plci_core_data import Data
from ..core.plci_core_signal import Signal
from ..core.plci_core_scheduler_params import SchedulerParams
from ..core.plci_core_diagram import Diagram

from .unit_test import get_boxes_libraries, get_schedulers_library

# Get library
boxesLibraries = get_boxes_libraries()
schedulersLibraries = get_schedulers_library()

d = Diagram()
d.append(Signal(index_ = 0, signal_type_ = DataType.FLOAT, default_value_ = 0.0))
d.append(Signal(index_ = 1, signal_type_ = DataType.FLOAT, default_value_ = 0.0))
d.append(Signal(index_ = 2, signal_type_ = DataType.FLOAT, default_value_ = 0.0))

d.append(boxesLibraries.construct_box('Boxes.Math', 'Multiplier'))
d.append(boxesLibraries.construct_box('Boxes.Sources', 'Constant', value = 0.0))
 
# Diagram creation

d.add_box_inputs(d.boxes[0], d.signals[0], d.signals[1])
d.add_box_outputs(d.boxes[0], d.signals[2])

scheduler : Scheduler = schedulersLibraries.construct_scheduler('Schedulers', 'Default')
scheduler.diagram = d
scheduler.params = SchedulerParams(10.0, 0.001)

# test output
value_0 : float = 10.0
value_1 : float = -5.0
answer : float = value_0 - value_1

se0 = scheduler.construct_event(None)
return_data = d.boxes[0].function(se0)

print("box current timing : " + str(d.boxes[0].current_timing))
print("box wait for events : " + str(d.boxes[0].wait_for_events))
print("box wait for all signal events : " + str(d.boxes[0].wait_for_all_signal_events))
print("box events on all inputs : " + str(d.boxes[0].events_on_all_inputs))
print("retrun data : " + str(return_data))
if len(return_data) == 0 :
    print("return data : no data")
else:
    print("return data new value : " + str(return_data[0].new_signal_value))

print("========================================================")

se1 = scheduler.construct_event(SignalEvent(d.signals[0], d.boxes[1], Data(DataType.FLOAT, value_0)))
se1.signal.data = se1.new_signal_data
return_data = d.boxes[0].function(se1)

print("box current timing : " + str(d.boxes[0].current_timing))
print("box wait for events : " + str(d.boxes[0].wait_for_events))
print("box wait for all signal events : " + str(d.boxes[0].wait_for_all_signal_events))
print("box events on all inputs : " + str(d.boxes[0].events_on_all_inputs))
print("retrun data : " + str(return_data))
if len(return_data) == 0 :
    print("return data : no data")
else:
    print("return data new value : " + str(return_data[0].new_signal_value))

print("========================================================")

scheduler.stepping_time()

se2 = scheduler.construct_event(SignalEvent(d.signals[0], d.boxes[1], Data(DataType.FLOAT, value_0)))
se2.signal.data = se2.new_signal_data
return_data = d.boxes[0].function(se2)

print("box current timing : " + str(d.boxes[0].current_timing))
print("box wait for events : " + str(d.boxes[0].wait_for_events))
print("box wait for all signal events : " + str(d.boxes[0].wait_for_all_signal_events))
print("box events on all inputs : " + str(d.boxes[0].events_on_all_inputs))
print("retrun data : " + str(return_data))
if len(return_data) == 0 :
    print("return data : no data")
else:
    print("return data new value : " + str(return_data[0].new_signal_value))

print("========================================================")

se3 = scheduler.construct_event(SignalEvent(d.signals[1], d.boxes[1], Data(DataType.FLOAT, value_1)))
se3.signal.data = se3.new_signal_data
return_data = d.boxes[0].function(se3)

print("box current timing : " + str(d.boxes[0].current_timing))
print("box wait for events : " + str(d.boxes[0].wait_for_events))
print("box wait for all signal events : " + str(d.boxes[0].wait_for_all_signal_events))
print("box events on all inputs : " + str(d.boxes[0].events_on_all_inputs))
print("retrun data : " + str(return_data))
if len(return_data) == 0 :
    print("return data : no data")
else:
    print("return data new value : " + str(return_data[0].new_signal_value))

print("========================================================")