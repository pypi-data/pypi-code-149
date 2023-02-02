
from ..core.plci_core_data_type import DataType
from ..core.plci_core_signal import Signal
from ..core.plci_core_scheduler import Scheduler
from ..core.plci_core_scheduler_params import SchedulerParams

from .unit_test import get_boxes_libraries, get_schedulers_library, simulate

# Get library
boxesLibraries = get_boxes_libraries()
schedulersLibraries = get_schedulers_library()

print("Creation of the scheduler")
scheduler : Scheduler = schedulersLibraries.construct_scheduler('Schedulers', 'Default')
print('Schedulers libraries : ', schedulersLibraries)
print('Schedulers libraries count : ', schedulersLibraries.libraries.__len__())
print('Schedulers libraries[0] count : ', schedulersLibraries.libraries[0].schedulers.__len__())
print('scheduler : ', scheduler)
scheduler.params = SchedulerParams(5, 0.001)

print("Creation of the diagram")
# 0 Sinus
scheduler.diagram.append(boxesLibraries.construct_box('Boxes.Sources', 'Sine', amplitude = 10, pulsation = 10, phase = 0)) 
# 1 Sinus
scheduler.diagram.append(boxesLibraries.construct_box('Boxes.Sources', 'Sine', amplitude = 5, pulsation = 20, phase = 0))  
# 2 Addition
scheduler.diagram.append(boxesLibraries.construct_box('Boxes.Math', 'Addition'))                      
# 3 Graph box            
scheduler.diagram.append(boxesLibraries.construct_box('Boxes.Sinks', 'Graph', start_time = 0, stop_time = scheduler.stop_time, title = 'Sinus', label_x = 'Temps (s)', label_y = 'Amplitude (v)' ))
# 4 Sinus
scheduler.diagram.append(boxesLibraries.construct_box('Boxes.Sources', 'Sine', amplitude = 1, pulsation = 100, phase = 0))
# 5 Ramp
scheduler.diagram.append(boxesLibraries.construct_box('Boxes.Sources', 'Ramp', start_time = 0, initial_value = 1, slope = -0.20))
# 6 Multiplication
scheduler.diagram.append(boxesLibraries.construct_box('Boxes.Math', 'Multiplier', start_time = 0, initial_value = 1, slope = -0.20))

print(scheduler.diagram._boxes[5])

# Diagram creation

scheduler.diagram.append(Signal(index_ = 0, signal_type_ = DataType.FLOAT, default_value_ = 0.0))
scheduler.diagram.append(Signal(index_ = 1, signal_type_ = DataType.FLOAT, default_value_ = 0.0))
scheduler.diagram.append(Signal(index_ = 2, signal_type_ = DataType.FLOAT, default_value_ = 0.0))
scheduler.diagram.append(Signal(index_ = 3, signal_type_ = DataType.FLOAT, default_value_ = 0.0))
scheduler.diagram.append(Signal(index_ = 4, signal_type_ = DataType.FLOAT, default_value_ = 0.0))
scheduler.diagram.append(Signal(index_ = 5, signal_type_ = DataType.FLOAT, default_value_ = 0.0))

scheduler.diagram.add_box_outputs(scheduler.diagram.boxes[0], scheduler.diagram.signals[0])
scheduler.diagram.add_box_outputs(scheduler.diagram.boxes[1], scheduler.diagram.signals[1])
scheduler.diagram.add_box_outputs(scheduler.diagram.boxes[2], scheduler.diagram.signals[2])
scheduler.diagram.add_box_outputs(scheduler.diagram.boxes[4], scheduler.diagram.signals[3])
scheduler.diagram.add_box_outputs(scheduler.diagram.boxes[5], scheduler.diagram.signals[4])
scheduler.diagram.add_box_outputs(scheduler.diagram.boxes[6], scheduler.diagram.signals[5])

scheduler.diagram.add_box_inputs(scheduler.diagram.boxes[2], scheduler.diagram.signals[0], scheduler.diagram.signals[1], scheduler.diagram.signals[3])
scheduler.diagram.add_box_inputs(scheduler.diagram.boxes[6], scheduler.diagram.signals[2], scheduler.diagram.signals[4])
scheduler.diagram.add_box_inputs(scheduler.diagram.boxes[3], scheduler.diagram.signals[5])

print("Boxes created : ")
for box in scheduler.diagram.boxes :
    print("\t - ", box) 

# Launch solver
simulate(scheduler)