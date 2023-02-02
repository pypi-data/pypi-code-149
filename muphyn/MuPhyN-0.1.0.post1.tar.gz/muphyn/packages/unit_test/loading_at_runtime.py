
from muphyn.packages.core.box_library.plci_core_boxes_libraries import *

from muphyn.packages.unit_test.unit_test import get_boxes_libraries

boxesLibraries = get_boxes_libraries()
box = boxesLibraries.construct_box('Boxes.Sources', 'Step')
print(box)