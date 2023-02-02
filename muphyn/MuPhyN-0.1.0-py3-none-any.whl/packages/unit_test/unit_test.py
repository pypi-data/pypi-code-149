#-----------------------------------
# Imports
#-----------------------------------

import time

import matplotlib.pylab as plt
from muphyn.packages.core.box_library.plci_core_boxes_libraries import BoxesLibraries
from muphyn.packages.core.plci_core_scheduler import Scheduler
from muphyn.packages.core.plci_core_scheduler_exception import SchedulerException
from muphyn.packages.core.scheduler_library.plci_core_schedulers_libraries import SchedulersLibraries

#-----------------------------------
# Methods
#-----------------------------------

def get_boxes_libraries () -> BoxesLibraries :
    print("Load boxes libraries")
    boxLibrary = BoxesLibraries()
    boxLibrary.add_library("D:/OneDrive - Ecole/OneDrive - Haute Ecole Louvain en Hainaut/2021-22 MaGe2/Stage/python-low-code-interface/box_library")
    boxLibrary.add_library("D:/OneDrive - Ecole/OneDrive - Haute Ecole Louvain en Hainaut/2021-22 MaGe2/Stage/python-low-code-interface/user_box")
    boxLibrary.load_libraries()
    return boxLibrary

def get_schedulers_library () -> SchedulersLibraries :
    print("Load schedulers libraries")
    schedulerLibrary = SchedulersLibraries()
    schedulerLibrary.add_library("D:/OneDrive - Ecole/OneDrive - Haute Ecole Louvain en Hainaut/2021-22 MaGe2/Stage/python-low-code-interface/scheduler_library")
    schedulerLibrary.load_libraries()
    return schedulerLibrary

def simulate (scheduler : Scheduler) -> bool :
        
    print("Start of the simulation #boxes : ", scheduler.diagram._boxes.__len__())
    start_time = time.time()
    schedulerException : SchedulerException = scheduler.schedule()
    stop_time = time.time()

    if schedulerException is None :
        print("The simulation is correctly finished and it took : ", stop_time - start_time, " s.")

        plt.show()

        return True

    else :
        print("The simulation encoutered an error after ", stop_time - start_time, " s of simulation.")
        schedulerException.print()
        return False