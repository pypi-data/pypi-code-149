#-----------------------------------
# Imports
#-----------------------------------

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QLabel
from muphyn.packages.interface.models.graphical_models.box_model import BoxModel
from muphyn.packages.interface.properties_pages.abstract_properties_editor import AbstractPropertiesEditor
from muphyn.packages.interface.widgets.BaseWidgets.Label import PropertyLabel

#-----------------------------------
# Class
#-----------------------------------

class BoxProperties (AbstractPropertiesEditor) :
    """Est la classe qui affiche une page capable de modifier les propriétés d'une box."""

    # -------------
    # Constructors
    # -------------

    def __init__ (self, box_model : BoxModel) :

        AbstractPropertiesEditor.__init__(self, box_model)

        self._box_model : BoxModel = None
        self.box_model = box_model

    # -------------
    # Properties
    # -------------

    @property
    def box_model (self) -> BoxModel :
        """Permet de récuperer le box model dont les propriétées sont changées."""
        return self._box_model

    @box_model.setter
    def box_model (self, box_model_ : BoxModel) -> None :
        """Permet de modifier le box model dont les propriétées sont changées."""

        self._box_model = box_model_
        self._model = box_model_
        self.moveable_element = box_model_

        if self._box_model is None : 
            self._lbl_library_value.setText('')
            self._lbl_name_value.setText('')

        else :
            self._lbl_library_value.setText(self._box_model.library)
            self._lbl_name_value.setText(self._box_model.name)

    # -------------
    # Methods
    # -------------

    def init_ui (self) :
        if not self.objectName() :
            self.setObjectName(u"pnl_box_properties")

        self._lbl_library : PropertyLabel = PropertyLabel()
        self._lbl_library.setObjectName(u'_lbl_library')

        self._lbl_library_value : PropertyLabel = PropertyLabel()
        self._lbl_library_value.setObjectName(u'_lbl_library_value')

        # Adding Library name
        row = self.layout().rowCount()
        self.layout().addWidget(self._lbl_library, row, 0)
        self.layout().addWidget(self._lbl_library_value, row, 1)

        self._lbl_name : PropertyLabel = PropertyLabel()
        self._lbl_name.setObjectName(u'_lbl_name')

        self._lbl_name_value : PropertyLabel = PropertyLabel()
        self._lbl_name_value.setObjectName(u'_lbl_name_value')

        # Adding Box name
        row = self.layout().rowCount()
        self.layout().addWidget(self._lbl_name, row, 0)
        self.layout().addWidget(self._lbl_name_value, row, 1)

    def translate_ui (self) -> None :
        
        self._lbl_library.setText(QCoreApplication.translate(self.objectName(), u"Library : ", None))
        self._lbl_name.setText(QCoreApplication.translate(self.objectName(), u"Name : ", None))