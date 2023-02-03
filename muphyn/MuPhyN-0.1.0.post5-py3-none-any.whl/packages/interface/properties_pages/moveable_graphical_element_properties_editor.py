#-----------------------------------
# Imports
#-----------------------------------

# General Imports

# PyQt5 Imports
from PyQt5.QtCore import QCoreApplication, QPointF, QSizeF, Qt, pyqtSlot
from PyQt5.QtWidgets import QLabel

# Project Imports
from muphyn.packages.interface.properties_pages.abstract_properties_editor import AbstractPropertiesEditor
from muphyn.packages.interface.properties_pages.rotation_slider import RotationSlider
from muphyn.packages.interface.models.graphical_models.abstract_moveable_graphical_element import AbstractMoveableGraphicalElement
from muphyn.packages.interface.models.dbl_spin_box import DblSpinBox
from muphyn.packages.interface.widgets.BaseWidgets.Label import PropertyLabel, TitlePropertyLabel

#-----------------------------------
# Class
#-----------------------------------

class MoveableGraphicalElementPropertiesEditor (AbstractPropertiesEditor) :
    """Est la classe permettant de modifier les paramètres d'un élément mobile dans la scène."""

    # -------------
    # Constructors
    # -------------

    def __init__ (self, moveable_element : AbstractMoveableGraphicalElement) :

        AbstractPropertiesEditor.__init__(self, moveable_element)

        self._size_semaphore = True
        self._pos_semaphore = True
        self._rot_semaphore = True

        self._moveable_element : AbstractMoveableGraphicalElement = None
        self.moveable_element = moveable_element

        self._size_semaphore = False
        self._pos_semaphore = False
        self._rot_semaphore = False

    
    # -------------
    # Properties
    # -------------

    @property
    def moveable_element (self) -> AbstractMoveableGraphicalElement :
        """Permet de récuperer l'élément graphique mobile."""
        return self._moveable_element

    @moveable_element.setter
    def moveable_element (self, moveable_element_ : AbstractMoveableGraphicalElement) -> None :
        """Permet de modifier l'élément graphique mobile."""
        
        if not(self._moveable_element is None) :

            self._moveable_element.size_changed.disconnect(self.element_size_changed)
            self._moveable_element.position_changed.disconnect(self.element_position_changed)
            self._moveable_element.rotation_changed.disconnect(self.element_rotation_changed)

        self._moveable_element = moveable_element_
        self._model = moveable_element_

        if not(self._moveable_element is None) :

            self._spn_x.setValue(self._moveable_element.x())
            self._spn_y.setValue(self._moveable_element.y())
            self._spn_width.setValue(self.moveable_element.size.width())
            self._spn_height.setValue(self.moveable_element.size.height())
            self._sldr_rotation.setValue(int(self._moveable_element.rotation()))
            self._lbl_rotation_value.setText(str(self._moveable_element.rotation()))

            self._moveable_element.size_changed.connect(self.element_size_changed)
            self._moveable_element.position_changed.connect(self.element_position_changed)
            self._moveable_element.rotation_changed.connect(self.element_rotation_changed)

    # -------------
    # Methods
    # -------------

    @pyqtSlot()
    def spn_pos_value_changed (self) -> None : 
        """Est la méthode appelée lorsque l'utilisateur change la position via une des deux spin box."""

        if self._pos_semaphore :
            return

        self._pos_semaphore = True

        self._moveable_element.position = QPointF(self._spn_x.value(), self._spn_y.value())

        self._pos_semaphore = False

    def element_size_changed (self) :
        """Est la méthode appelée lorsque la box change de taille."""
        
        if self._size_semaphore :
            return

        self._size_semaphore = True

        self._spn_width.setValue(self._moveable_element.size.width())
        self._spn_height.setValue(self._moveable_element.size.height())

        self._size_semaphore = False

    @pyqtSlot()
    def spn_size_value_changed (self) :
        """Est la méthode appelée lorsque l'utilisateur change la taille via une des deux spin box."""
    
        if self._pos_semaphore :
            return

        self._pos_semaphore = True

        # Get size
        new_size = QSizeF(self._spn_width.value(), self._spn_height.value())

        if new_size != self._moveable_element.size:

            # Set size
            self._moveable_element.size = QSizeF(self._spn_width.value(), self._spn_height.value())

            # Get size from moveable item
            self._spn_width.setValue(self._moveable_element.size.width())
            self._spn_height.setValue(self._moveable_element.size.height())

        self._pos_semaphore = False

    def element_position_changed (self) :
        """Est la méthode appelée lorsque la box change de taille."""
    
        if self._pos_semaphore :
            return

        self._pos_semaphore = True

        self._spn_x.setValue(self._moveable_element.position.x())
        self._spn_y.setValue(self._moveable_element.position.y())

        self._pos_semaphore = False

    def element_rotation_changed (self) :
        """Est la méthode appelée lorsque la box change de taille."""
        
        if self._rot_semaphore :
            return

        self._rot_semaphore = True

        self._sldr_rotation.setValue(self._moveable_element.rotation())
        self._lbl_rotation_value.setText(str(self._sldr_rotation.value()))

        self._rot_semaphore = False
        
    @pyqtSlot()
    def sldr_rotation_value_changed (self) -> None :
        """Est la méthode appelée lorsque l'utilisateur change la rotation de l'élément via le slider."""
        
        if self._rot_semaphore :
            return

        self._rot_semaphore = True

        self._lbl_rotation_value.setText(str(self._sldr_rotation.value()))
        self._moveable_element.setRotation(self._sldr_rotation.value())

        self._rot_semaphore = False 

    def init_ui (self) :
        
        if not self.objectName() :
            self.setObjectName(u"pnl_moveable_graphical_element_properties_editor")

        self._lbl_geometry : TitlePropertyLabel = TitlePropertyLabel()
        self._lbl_geometry.setObjectName(u"_lbl_geometry")

        # Add Row
        row = self.layout().rowCount()
        self.layout().addWidget(self._lbl_geometry, row, 0)

        self._lbl_x : PropertyLabel = PropertyLabel()
        self._lbl_x.setObjectName(u"_lbl_x")

        self._spn_x : DblSpinBox = DblSpinBox()
        self._spn_x.setObjectName(u"_spn_x")
        self._spn_x.setDecimals(0)
        self._spn_x.valueChanged.connect(self.spn_pos_value_changed)

        # Add Row
        row = self.layout().rowCount()
        self.layout().addWidget(self._lbl_x, row, 0)
        self.layout().addWidget(self._spn_x, row, 1)
        
        self._lbl_y : PropertyLabel = PropertyLabel()
        self._lbl_y.setObjectName(u"_lbl_y")

        self._spn_y : DblSpinBox = DblSpinBox()
        self._spn_y.setObjectName(u"_spn_y")
        self._spn_y.setDecimals(0)
        self._spn_y.valueChanged.connect(self.spn_pos_value_changed)

        # Add Row
        row = self.layout().rowCount()
        self.layout().addWidget(self._lbl_y, row, 0)
        self.layout().addWidget(self._spn_y, row, 1)

        self._lbl_width : PropertyLabel = PropertyLabel()
        self._lbl_width.setObjectName(u"_lbl_width")
        
        self._spn_width : DblSpinBox = DblSpinBox()
        self._spn_width.setObjectName(u"_spn_width")
        self._spn_width.setDecimals(0)
        self._spn_width.setMinimum(0)
        self._spn_width.valueChanged.connect(self.spn_size_value_changed)

        # Add Row
        row = self.layout().rowCount()
        self.layout().addWidget(self._lbl_width, row, 0)
        self.layout().addWidget(self._spn_width, row, 1)

        self._lbl_height : PropertyLabel = PropertyLabel()
        self._lbl_height.setObjectName(u"_lbl_y")
        
        self._spn_height : DblSpinBox = DblSpinBox()
        self._spn_height.setObjectName(u"_spn_height")
        self._spn_height.setDecimals(0)
        self._spn_height.valueChanged.connect(self.spn_size_value_changed)

        # Add Row
        row = self.layout().rowCount()
        self.layout().addWidget(self._lbl_height, row, 0)
        self.layout().addWidget(self._spn_height, row, 1)

        self._lbl_rotation : PropertyLabel = PropertyLabel()
        self._lbl_rotation.setObjectName(u"_lbl_rotation")

        self._sldr_rotation : RotationSlider = RotationSlider()
        self._sldr_rotation.setOrientation(Qt.Horizontal)
        self._sldr_rotation.setObjectName(u"_sldr_rotation")
        self._sldr_rotation.valueChanged.connect(self.sldr_rotation_value_changed)

        # Add Row
        row = self.layout().rowCount()
        self.layout().addWidget(self._lbl_rotation, row, 0)
        self.layout().addWidget(self._sldr_rotation, row, 1)

        self._lbl_rotation_value : PropertyLabel = PropertyLabel()
        self._lbl_rotation_value.setObjectName(u"_lbl_rotation_value")

        # Add Row
        row = self.layout().rowCount()
        self.layout().addWidget(self._lbl_rotation_value, row, 1)
    
    def translate_ui (self) -> None :
        self._lbl_geometry.setText(QCoreApplication.translate(self.objectName(), u"Geometry : ", None))
        self._lbl_x.setText(QCoreApplication.translate(self.objectName(), u"X : ", None))
        self._lbl_width.setText(QCoreApplication.translate(self.objectName(), u"Width : ", None))
        self._lbl_y.setText(QCoreApplication.translate(self.objectName(), u"Y : ", None))
        self._lbl_height.setText(QCoreApplication.translate(self.objectName(), u"Height : ", None))
        self._lbl_rotation.setText(QCoreApplication.translate(self.objectName(), u"Rotate angle : ", None))