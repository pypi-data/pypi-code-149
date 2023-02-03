
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QComboBox
from PyQt5.QtCore import QRect, QPointF, QSizeF
from muphyn.packages.core.box_library.box_library_data import AbstractBoxData
from muphyn.packages.core.box_library.plci_core_boxes_libraries import BoxesLibraries
from muphyn.packages.core.plci_core_data_type import DataType
from muphyn.packages.interface.editors.diagram_editor import construct_box
from muphyn.packages.interface.models.graphical_models.box_input_model import BoxInputModel
from muphyn.packages.interface.models.graphical_models.box_model import BoxModel
from muphyn.packages.interface.models.graphical_models.box_output_model import BoxOutputModel
from muphyn.packages.interface.models.signals_model.input_connection_model import InputConnectionModel
from muphyn.packages.interface.models.signals_model.output_connection_model import OutputConnectionModel

from muphyn.packages.interface.properties_pages.properties_widget import PropertiesWidget

from .unit_test import get_boxes_libraries

boxes_libraries : BoxesLibraries = get_boxes_libraries()

def get_box (library, name) -> BoxModel :

    box_data : AbstractBoxData = boxes_libraries.get_box_data(library, name)

    if box_data is None : 
        return None 
    
    return construct_box(box_data, QPointF(0, 0), True)
     

false_input_box = BoxModel('', 'false_box', QPointF(0, 0), QSizeF(0, 0), 0, False, '')
false_input = InputConnectionModel('false_input', DataType.FLOAT, QPointF(0, 0))
false_input_box._inputs.append(false_input)

false_output_box = BoxModel('', '', QPointF(0, 0), QSizeF(0, 0), 0, False, '')
false_output = OutputConnectionModel('false_output', DataType.FLOAT, QPointF(0, 0))
false_output_box._outputs.append(false_output)
link_element = false_output.add_link(false_input)

elements = [
    link_element, 
    BoxInputModel('', DataType.FLOAT, QPointF(0, 0), QSizeF(0, 0)), 
    BoxOutputModel('', DataType.FLOAT, QPointF(0, 0), QSizeF(0, 0)),
    get_box('Boxes.Math', 'Addition'),
    get_box('Boxes.Math', 'Amplifier'),
    get_box('Boxes.Sources', 'Constant'),
    get_box('Boxes.Math', 'Derivator'),
    get_box('Boxes.Sinks', 'Graph'),
    get_box('Boxes.Math', 'Integrator'),
    get_box('Boxes.Math', 'Multiplier'),
    get_box('Boxes.Sources', 'Ramp'),
    get_box('Boxes.Sources', 'Sine'),
    get_box('Boxes.Sources', 'Square'),
    get_box('Boxes.Sources', 'Step')
]

class test_windows (QWidget) :

    def __init__ (self) :

        QWidget.__init__(self, None)
        self.init_ui()
        self.resize(330, 400)

    def init_ui (self) :
        self.cmb_elements = QComboBox(self)
        self.cmb_elements.setObjectName(u"comboBox")
        self.cmb_elements.setGeometry(QRect(10, 10, 311, 22))

        self.cmb_elements.addItem('Link')
        self.cmb_elements.addItem('Composite box input')
        self.cmb_elements.addItem('Composite box output')
        self.cmb_elements.addItem('Box - Addition')
        self.cmb_elements.addItem('Box - Amplifier')
        self.cmb_elements.addItem('Box - Constant')
        self.cmb_elements.addItem('Box - Derivator')
        self.cmb_elements.addItem('Box - Graph')
        self.cmb_elements.addItem('Box - Integrator')
        self.cmb_elements.addItem('Box - Multiplier')
        self.cmb_elements.addItem('Box - Ramp')
        self.cmb_elements.addItem('Box - Sine')
        self.cmb_elements.addItem('Box - Square')
        self.cmb_elements.addItem('Box - Step')

        self.properties_widget = PropertiesWidget(self)
        self.properties_widget.setObjectName(u"widget")
        self.properties_widget.setGeometry(QRect(10, 40, 311, 351))
        
        self.cmb_elements.setCurrentIndex(2)
        self.cmb_elements.currentIndexChanged.connect(self.cmb_elements_current_index_changed)
        self.cmb_elements.setCurrentIndex(3)

    def cmb_elements_current_index_changed (self) -> None : 
        index = self.cmb_elements.currentIndex()
        element = elements[index]
        
        self.properties_widget.current_model = element


app = QApplication(sys.argv)
win = test_windows()
win.show()

sys.exit(app.exec_())