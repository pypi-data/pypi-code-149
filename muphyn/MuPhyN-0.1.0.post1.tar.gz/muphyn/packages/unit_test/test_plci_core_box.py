
from muphyn.packages.core.plci_core_scheduler_params import SchedulerParams
from ..core.plci_core_scheduler_event import SchedulerEvent
from ..core.plci_core_box import Box

def box_init_method (box : Box) -> None :
    print("init method")

def box_function_method (box : Box, scheduler_event : SchedulerEvent) -> None :
    print("function method")

def box_end_method (box : Box) -> None:
    print("end method")

b = Box(0, 'a', 'b', box_init_method, box_function_method, box_end_method)

b.init(SchedulerParams())
b.function(SchedulerEvent(None, None, None, 0, None))
b.end()