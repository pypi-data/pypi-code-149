
from muphyn.packages.core.plci_core_scheduler import Scheduler
from muphyn.packages.core.simulation_files.plci_core_simulations_importer import SimulationsImporter
from .unit_test import get_boxes_libraries, get_schedulers_library, simulate

# Get library
boxesLibraries = get_boxes_libraries()
schedulersLibraries = get_schedulers_library()
simulationImporter = SimulationsImporter()
simulation : Scheduler = simulationImporter.import_simulation(
                                'D:/OneDrive - Ecole/OneDrive - Haute Ecole Louvain en Hainaut/2021-22 MaGe2/Stage/python-low-code-interface/simulation/retroact.yaml',
                                schedulersLibraries, 
                                boxesLibraries)

if simulation is None :
    print('The simulation imported has not been loaded.')

else :
    simulate(simulation)