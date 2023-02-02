
from muphyn.packages.core.plci_core_diagram import Diagram
from muphyn.packages.core.plci_core_scheduler import Scheduler
from muphyn.packages.core.plci_core_scheduler_params import SchedulerParams
from .unit_test import get_boxes_libraries, get_schedulers_library, simulate

# Get library
boxesLibraries = get_boxes_libraries()
schedulersLibraries = get_schedulers_library()

totalLibraryCount : int = 0

for box in boxesLibraries.boxes:
    print('Box loaded : ', box.box_library, '.', box.box_name)
    totalLibraryCount += 1

print("Nombre de boxes importées : ", totalLibraryCount)
print("13 boxes en code")
print("3 boxes composites (dont 1 dépendante de l'autre)")

diagram : Diagram = boxesLibraries.construct_box('Boxes.User', 'Wrapper')

print("Diagram loaded : ", diagram)
print("Diagram boxes : ", diagram.boxes.__len__())
print("Diagram signals : ", diagram.signals.__len__())
print("Diagram box input : ", diagram._box_inputs.__len__())
print("Diagram linked signals : ", diagram._linked_signals.__len__())

scheduler : Scheduler = schedulersLibraries.construct_scheduler('Schedulers', 'Default')
scheduler.params = SchedulerParams(10, 0.01)
scheduler.diagram = diagram

simulate(scheduler)