#-----------------------------------
# Imports
#-----------------------------------

from typing import Iterable, List
from PyQt5 import QtGui
from PyQt5.QtCore import QCoreApplication, QRect, Qt
from PyQt5.QtWidgets import QLabel, QLineEdit, QWidget, QGridLayout
from muphyn.packages.core.box_library.box_library_data import AbstractBoxData
from muphyn.packages.core.box_library.plci_core_boxes_libraries import BoxesLibrariesManager
from muphyn.packages.interface.box_library.library_treeview import LibraryTreeView
from muphyn.packages.interface.widgets.BaseWidgets.Label import PropertyLabel

#-----------------------------------
# Class
#-----------------------------------

class BoxLibrariesList (QWidget) :
    """Est l'élément graphique qui permet de maintenir les bibliothèques de boxes."""

    # -------------
    # Constructors
    # -------------

    def __init__ (self, parent : QWidget = None) :
        QWidget.__init__(self, parent)
        self.init_gui()

    # -------------
    # Properties
    # -------------

    @property
    def boxes_libraries (self) :
        """Permet de récuperer la bibliothèque de boxes."""
        return BoxesLibrariesManager()

    # -------------
    # Methods
    # -------------

    def searched_boxes (self) -> Iterable[AbstractBoxData] : 
        """Permet de récuperer les éléments après recherche."""

        search_text = self.fld_search.text() 
        elements : List[AbstractBoxData] = []

        if search_text.__len__() == 0 :
            for box_data in BoxesLibrariesManager().boxes :
                elements.append(box_data)

        else :
            keywords = search_text.split(' ')
            for box_data in BoxesLibrariesManager().boxes :

                b = True
                for k in keywords :
                    keyword = k.strip()

                    if keyword.__len__() == 0 :
                        continue
                    
                    if not(box_data._full_box_path.__contains__(keyword)) :
                        b = False
                        break

                if b : 
                    elements.append(box_data)

        elements.sort()
        
        for el in elements :
            yield el

    def resizeEvent (self, event : QtGui.QResizeEvent) -> None :

        self.tree_view.setGeometry(QRect(5, 30, self.width() - 15, self.height() - 35))
        self.fld_search.setGeometry(QRect(90, 1, self.width() - 100, 22))

        return super().resizeEvent(event)

    def libraries_reloaded (self) -> None :
        """Est la méthode appelée pour recharger la bibliothèque."""
        self.tree_view.build_model(BoxesLibrariesManager().boxes)
        
    def init_gui (self) -> None :
        """Est la méthode appelée pour afficher les éléments visuels dans la fenêtre."""
        
        if not self.objectName():
            self.setObjectName(u"box_libraries")

        # Init Layout
        layout = QGridLayout()
        layout.setContentsMargins(8, 8, 8, 8)
        layout.setColumnStretch(1, 1)
        layout.setRowStretch(1, 1)
        layout.setVerticalSpacing(10)
            
        # Init Tree View
        self.tree_view: LibraryTreeView = LibraryTreeView()
        self.tree_view.build_model(BoxesLibrariesManager().boxes)
        self.tree_view.setObjectName(u"lbr_treeview")
        self.tree_view.setMinimumHeight(250)

        # Init Search Field
        self.fld_search : QLineEdit = QLineEdit()
        self.fld_search.setObjectName(u"fld_search")
        self.fld_search.textChanged.connect(self.search_text_changed)

        # Init Search Label
        self.lbl_search : PropertyLabel = PropertyLabel()
        self.lbl_search.setObjectName(u"lbl_search")

        # Add widget in layout
        layout.addWidget(self.lbl_search, 0, 0, alignment=Qt.AlignmentFlag.AlignVCenter)
        layout.addWidget(self.fld_search, 0, 1, alignment=Qt.AlignmentFlag.AlignVCenter)
        layout.addWidget(self.tree_view, 1, 0, 1, 2)

        # Set Layout
        self.setLayout(layout)

        self.retranslateUi()
        
    def retranslateUi (self) -> None :
        self.lbl_search.setText(QCoreApplication.translate("Search : ", u"Search : ", None))

    def search_text_changed (self, searched_string: str) -> None :
        """Est la méthode appelée lorsque le texte contenus dans la barre de recherche est changée."""
        self.tree_view.filter_library_list(searched_string)
