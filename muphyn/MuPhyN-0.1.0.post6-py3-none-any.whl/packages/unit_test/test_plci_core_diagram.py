
from ..core.plci_core_data_type import DataType
from ..core.plci_core_signal import Signal
from ..core.plci_core_box import Box
from ..core.plci_core_diagram import Diagram

s0 = Signal(0, DataType.FLOAT, 0)
s1 = Signal(1, DataType.FLOAT, 0)

b0 = Box(0, 'a', 'e')
b1 = Box(1, 'b', 'e')
b2 = Box(2, 'c', 'e')

d = Diagram()
d.append(s0)
d.append(s1)
d.append(b0)
d.append(b1)
d.append(b2)

d.add_box_outputs(d.boxes[0], d.signals[0])
d.add_box_outputs(d.boxes[1], d.signals[1])

d.add_box_inputs(d.boxes[1], d.signals[0])
d.add_box_inputs(d.boxes[2], d.signals[1])

print("Boxes : ")
for box in d._boxes:
    print("\t - ", box)

print("Signals : ")
for signal in d._signals:
    print("\t - ", signal)

for signal in d._box_inputs:
    print("signal " + str(signal.index) + " : ")

    for box in d._box_inputs[signal] :
        print("\t - Box " + str(box.index))
