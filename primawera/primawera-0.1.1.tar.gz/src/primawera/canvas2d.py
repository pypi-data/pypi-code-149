from functools import partial
from typing import Dict, List, Tuple, Optional

from PyQt5 import QtCore
from PyQt5.QtCore import Qt, pyqtSlot, pyqtSignal
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QGridLayout, QLabel, QAction

from primawera.filters import *
from primawera.lut import *
from primawera.visualiser import Visualiser


class Canvas2D(QWidget):
    menus_changed_signal = pyqtSignal()

    def __init__(self, data: ArrayLike, bitdepth: int, mode: str,
                 desktop_height: int, desktop_width: int,
                 filters: Optional[Dict[str, bool]] = None,
                 filters_options: Optional[Dict[str, int]] = None, *args,
                 **kwargs) -> None:
        super(Canvas2D, self).__init__(*args, **kwargs)
        self.data = data
        self.filters = filters
        self.filters_options = filters_options
        self.lut = None
        self.bitdepth = bitdepth
        self.mode = mode
        # This may change, for example when applying LUTs.
        self.mode_visualisation = mode
        self.axes_orientation = (0, 1, 2)
        self.desktop_height = desktop_height
        self.desktop_width = desktop_width
        # TODO: think though if this is needed ... data loader should take
        #       this in count, but this might break if user directly supplies
        #       the data.
        if self.bitdepth <= 0:
            raise RuntimeError("Bitdepth cannot be smaller than 1.")
        if self.mode == "":
            raise RuntimeError("Empty mode encountered.")

        self._init_interface()
        self._create_actions()
        self._set_actions_checkable()
        self._connect_actions()

        if self.mode != 'F':
            self._no_filter()
        else:
            self._linear_stretch()

        # Check default options
        self.get_filters()[0].setChecked(True)
        if self.mode == "grayscale":
            self.get_luts()[0].setChecked(True)

    def process_data(self) -> ArrayLike:
        # TODO: decompose this to remove duplicity in other canvases.
        if self.mode == "1":
            return (self.data * 255).astype(np.uint8)
        processed_data = self.data.astype(float)

        # Apply filters
        if self.filters.get("linear_stretch", False):
            processed_data = 255.0 * linear_stretch(processed_data)
        elif self.filters.get("gamma_correction", False):
            gamma_factor = self.filters_options.get("factor", 0.5)
            processed_data = gamma_correction(processed_data, gamma_factor)
        elif self.filters.get("linear_contrast", False):
            stretch_factor = self.filters_options.get("factor", 2)
            processed_data = linear_contrast(processed_data, stretch_factor)
        elif self.filters.get("logarithm_stretch", False):
            processed_data = logarithm_stretch(processed_data, factor=10.0)
            # Normalise to range [0,255]
            processed_data = 255.0 * linear_stretch(processed_data)

        # Clip data
        processed_data = np.clip(processed_data, 0, 255.0).astype(np.uint8)

        # Apply LUT
        if self.lut is not None:
            self.mode_visualisation = "rgb"
            processed_data = apply_lut(processed_data, self.lut)

        self.menus_changed_signal.emit()
        return processed_data

    def _init_interface(self) -> None:
        self.main_layout = QVBoxLayout()
        self.coordinates_label = QLabel("Please click on the image.")
        self.main_layout.addWidget(self.coordinates_label, stretch=0)

        maximum_width = int(self.desktop_width * 0.80)
        maximum_height = int(self.desktop_height * 0.80)
        # TODO: Grid is an overkill in this case
        self.view_layout = QGridLayout()
        processed_data = self.process_data()
        self.visualiser = Visualiser(processed_data, (0, 1, 2), self.mode,
                                     maximum_height, maximum_width, True)
        self.visualiser.signal_position.connect(self.set_coordinate_label)
        self.view_layout.addWidget(self.visualiser, 0, 0, Qt.AlignTop)
        self.main_layout.addLayout(self.view_layout)

        self.setLayout(self.main_layout)

    # TODO: duplicity in canvas3d
    def _linear_contrast(self):
        self.filters = {"linear_contrast": True}
        factor = "a"
        while not factor.replace(".", "", 1).isdigit():
            factor = input("Please enter the multiplication factor: ")
        self.filters_options = {"factor": float(factor)}
        self._redraw(self.process_data())
        self.current_filter_name = "Linearly adjusted contrast"

    def _logarithm_stretch(self):
        self.filters = {"logarithm_stretch": True}
        self._redraw(self.process_data())
        self.current_filter_name = "Logarithmically stretched."

    def _gamma_correction(self):
        self.filters = {"gamma_correction": True}
        factor = "a"
        while not factor.replace(".", "", 1).isdigit():
            factor = input("Please enter the multiplication factor: ")
        self.filters_options = {"factor": float(factor)}
        self._redraw(self.process_data())
        self.current_filter_name = "Gamma corrected"

    def _linear_stretch(self):
        self.filters = {"linear_stretch": True}
        self._redraw(self.process_data())
        self.current_filter_name = "Linearly stretched"

    def _no_filter(self):
        self.filters.clear()
        self._redraw(self.process_data())
        self.current_filter_name = "No filter"

    def _apply_lut(self, name):
        if name == "None":
            self.mode_visualisation = self.mode
            self.lut = None
        else:
            self.lut = get_lut(name)
        self._redraw(self.process_data())

    @pyqtSlot(int, int, int, list)
    def set_coordinate_label(self, frame, row, col, data):
        # Note: numpy is row-centric, that's why y and x are switched
        self.coordinates_label.setText(
            f"current filter = {self.current_filter_name}\n"
            f"row={row}, col={col}\n"
            f"original value={self.data[frame, row, col]}), "
            f"mapped value={data}")

    def _create_actions(self):
        self.no_filter_action = QAction("None")
        self.logarithm_stretch_action = QAction("Logarithm stretch.")
        self.linear_stretch_action = QAction("Linear stretch.")
        self.linear_contrast_action = QAction("Linear contrast.")
        self.gamma_correction_action = QAction("Gamma correction.")

        self.lut_actions = []
        self.lut_actions.append(("None", QAction("None")))
        for lut_name in LUTS.keys():
            self.lut_actions.append((lut_name, QAction(lut_name)))

    def _connect_actions(self):
        self.no_filter_action.triggered.connect(self._no_filter)
        self.logarithm_stretch_action.triggered.connect(
            self._logarithm_stretch)
        self.linear_stretch_action.triggered.connect(self._linear_stretch)
        self.linear_contrast_action.triggered.connect(self._linear_contrast)
        self.gamma_correction_action.triggered.connect(self._gamma_correction)

        for lut_name, lut_action in self.lut_actions:
            lut_action.triggered.connect(partial(self._apply_lut, lut_name))

    def _set_actions_checkable(self) -> None:
        for action in self.get_actions():
            action.setCheckable(True)

    def get_actions(self) -> List[QAction]:
        result = self.get_filters()
        result.extend(self.get_luts())
        return result

    def get_filters(self) -> List[QAction]:
        if self.mode == "F":
            return [self.linear_stretch_action, self.logarithm_stretch_action]

        result = [self.no_filter_action]
        if self.mode == "1":
            return result

        if self.mode == "grayscale" or self.mode == "F":
            result.append(self.linear_stretch_action)

        result.extend([self.linear_contrast_action,
                       self.gamma_correction_action])
        return result

    def get_luts(self) -> List[QAction]:
        if self.mode == "grayscale" or self.mode == "F":
            return [action for _, action in self.lut_actions]
        return []

    def get_menus(self) -> List[Tuple[str, List[QAction]]]:
        lut_entry = ("LUT", self.get_luts())
        filter_entry = ("Filters", self.get_filters())
        result = [filter_entry, lut_entry] if lut_entry[1] else [filter_entry]
        return result

    def update_desktop_size(self, width: int, height: int) -> None:
        self.desktop_width = width
        self.desktop_height = height

    def keyPressEvent(self, event: QWidget.keyPressEvent) -> None:
        if event.key() == QtCore.Qt.Key_Plus:
            self.visualiser.increase_zoom_level()
        elif event.key() == QtCore.Qt.Key_Minus:
            self.visualiser.decrease_zoom_level()
        else:
            event.ignore()

    def _redraw(self, new_data: ArrayLike) -> None:
        self.visualiser.update_data(new_data, self.axes_orientation,
                                    self.mode_visualisation)
        self.visualiser.generate()
        self.visualiser.redraw()
