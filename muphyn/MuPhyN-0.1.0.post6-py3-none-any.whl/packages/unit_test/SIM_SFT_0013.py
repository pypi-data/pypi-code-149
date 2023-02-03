
from .unit_test import get_boxes_libraries

# Get library
boxesLibraries = get_boxes_libraries()

print("param for graph box : ", boxesLibraries.get_required_params('Boxes.Sinks', 'Graph'))

print("param for wrong box : ", boxesLibraries.get_required_params('Boxes.Sinks', 'E'))

print("param for wrong library : ", boxesLibraries.get_required_params('Boxes.Sinks', 'Ramp'))

print("param for error in library : ", boxesLibraries.get_required_params(1, 'Ramp'))