
from PyQt5.QtCore import QMimeData, QRegExp, QSortFilterProxyModel, Qt
from PyQt5.QtWidgets import QTreeView, QAbstractItemView
from PyQt5.QtGui import QStandardItemModel, QMouseEvent, QDrag

from muphyn.packages.interface.box_library.library_element import LibraryElement
from muphyn.packages.interface.box_library.box_library_element import BoxLibraryElement, BoxLibraryElementRole
from muphyn.packages.interface.models.graphical_models.abstract_box_model import AbstractBoxModel

class LibraryTreeView(QTreeView):

    MULTIPLE_BOX_IMPORT_OFFSET_X = 0
    MULTIPLE_BOX_IMPORT_OFFSET_Y = AbstractBoxModel.MinimunBoxHeight + 20

    def __init__(self, parent = None) -> None:
        super().__init__(parent)

        # General Parameters
        self.setHeaderHidden(True)
        self.setAnimated(True)

        # Enable Drag
        self.setDragEnabled(True)
        self.setDragDropMode(QAbstractItemView.DragDropMode.DragOnly)

        # Set Selection Mode
        self.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)

    def build_model(self, boxes_data):
        # Init Model
        tree_model: QStandardItemModel = QStandardItemModel()
        root_node = tree_model.invisibleRootItem()

        # Build Model
        model_dict = {}
        for box_data in boxes_data:
            # Split Box Library & Sub Libraries if there is a Sub Library
            library_hierarchy = box_data.box_library.split(".")
            
            # Create Component Item
            component_item = BoxLibraryElement(box_data)
            component_item.setData(box_data, BoxLibraryElementRole.BOX_DATA)

            if len(library_hierarchy) == 2:
                # Extract Library & Sub Library
                library, sub_library = library_hierarchy

                if library in model_dict.keys():
                    # Get Library Element
                    library_item: LibraryElement = model_dict[library]["library_item"]

                    # Get Sub Libraries Dictionnary
                    sub_libraries_dict = model_dict[library]["sub_libraries"]

                    if sub_library in sub_libraries_dict.keys():
                        # Get Sub Library Item
                        sub_library_item = sub_libraries_dict[sub_library]["sub_library_item"]

                        # Append Component
                        sub_library_item.appendRow(component_item)
                    else:
                        # Create Sub Library Item
                        sub_library_item = LibraryElement(sub_library)

                        sub_libraries_dict[sub_library] = {
                            "sub_library_item": sub_library_item
                        }

                        # Append Component
                        sub_library_item.appendRow(component_item)

                        # Append Sub Library
                        library_item.appendRow(sub_library_item)
                    
                else:
                    # Create Library Item
                    library_item = LibraryElement(library)

                    # Create Sub Library Item
                    sub_library_item = LibraryElement(sub_library)

                    model_dict[library] = {
                            "library_item": library_item, 
                            "sub_libraries": {
                                    sub_library: {
                                        "sub_library_item": sub_library_item
                                        }
                                }
                        }

                    # Append Component
                    sub_library_item.appendRow(component_item)

                    # Append Sub Library
                    library_item.appendRow(sub_library_item)

                    # Append Library to Root
                    root_node.appendRow(library_item)
        
        self.source_model = tree_model

        # Init Filter Model
        self.proxy_model =  QSortFilterProxyModel()
        self.proxy_model.setSourceModel(self.source_model)
        self.proxy_model.setRecursiveFilteringEnabled(True)

        self.setModel(self.proxy_model)

    def filter_library_list(self, searched_string: str):
        regex = QRegExp(searched_string, Qt.CaseSensitivity.CaseInsensitive)
        self.proxy_model.setFilterRegExp(regex)
        if searched_string != "":
            self.expandAll()
        else:
            self.collapseAll()
            for selected_index in self.selectedIndexes():
                self.expandRecursively(selected_index)
                expanded_item_parent = selected_index.parent()
                while expanded_item_parent.row() != -1:
                    self.expand(expanded_item_parent)
                    expanded_item_parent = expanded_item_parent.parent()


    def mouseMoveEvent (self, event : QMouseEvent) -> None :
        if self.selectionModel() is not None:
            for box_index, selected_index in enumerate(self.selectedIndexes()):
                # Get Selected Item
                selected_item_data = self.model().itemData(selected_index)

                # If Box Data has been saved
                if BoxLibraryElementRole.BOX_DATA in selected_item_data:
                    box_data = selected_item_data[BoxLibraryElementRole.BOX_DATA]

                    offset_x = LibraryTreeView.MULTIPLE_BOX_IMPORT_OFFSET_X * box_index
                    offset_y = LibraryTreeView.MULTIPLE_BOX_IMPORT_OFFSET_Y * box_index
                    
                    mimeData : QMimeData = QMimeData()
                    mimeData.setData('action', bytearray('new box'.encode()))
                    mimeData.setData('box', bytearray(box_data._box_name.encode()))
                    mimeData.setData('library', bytearray(box_data._box_library.encode()))
                    mimeData.setData('box_data', bytearray(str(id(box_data)).encode()))
                    mimeData.setData('offset', bytearray(str(f"{offset_x};{offset_y}").encode()))

                    drag : QDrag = QDrag(self)
                    drag.setMimeData(mimeData)
                    da : Qt.DropAction = drag.exec(Qt.CopyAction)