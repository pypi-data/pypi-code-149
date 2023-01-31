from enum import Enum, auto
from functools import partial
from typing import Dict, Optional

from PyQt5 import QtCore
from PyQt5.QtCore import Qt, pyqtSlot, pyqtSignal
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QGridLayout, QLabel, QAction

from primawera.filters import *
from primawera.lut import *
from primawera.visualiser import Visualiser


class ShowEnum(Enum):
    MAGNITUDE = auto()
    PHASE = auto()
    REAL_PART = auto()
    IMAG_PART = auto()


class CanvasComplex(QWidget):
    menus_changed_signal = pyqtSignal()

    def __init__(self, data: ArrayLike, bitdepth: int, mode: str,
                 desktop_height: int, desktop_width: int,
                 filters: Optional[Dict[str, bool]] = None,
                 filters_options: Optional[Dict[str, int]] = None, *args,
                 **kwargs) -> None:
        super(CanvasComplex, self).__init__(*args, **kwargs)
        self.data = data
        if filters:
            self.filters = filters
        else:
            self.filters = {"linear_stretch": True}
        self.filters_options = filters_options
        self.bitdepth = bitdepth
        self.mode = mode
        # This may change, for example when applying LUTs.
        self.mode_visualisation = mode
        self.lut = None
        self.axes_orientation = (0, 1, 2)
        self.desktop_height = desktop_height
        self.desktop_width = desktop_width
        self.show = ShowEnum.MAGNITUDE
        # TODO: think through if this is needed ... data loader should take
        #       this in count, but this might break if user directly supplies
        #       the data.
        if self.bitdepth <= 0:
            raise RuntimeError("Bitdepth cannot be smaller than 1.")
        if self.mode != "C":
            raise RuntimeError("CanvasComplex expects complex data!")

        self._init_interface()
        self._create_actions()
        self._set_actions_checkable()
        self._reset_checked_states()
        self._connect_actions()
        self._show_magnitude()
        self.get_luts()[0].setChecked(True)

    def _init_interface(self):
        self.main_layout = QVBoxLayout()
        self.coordinates_label = QLabel("Please click on the image.")
        self.main_layout.addWidget(self.coordinates_label, stretch=0)

        maximum_width = int(self.desktop_width * 0.8)
        maximum_height = int(self.desktop_height * 0.8)
        self.view_layout = QGridLayout()
        processed_data = self._process_data()
        self.visualiser = Visualiser(processed_data, (0, 1, 2), self.mode,
                                     maximum_height, maximum_width, True)
        self.visualiser.signal_position.connect(self.set_coordinate_label)
        self.view_layout.addWidget(self.visualiser, 0, 0, Qt.AlignTop)
        self.main_layout.addLayout(self.view_layout)

        self.setLayout(self.main_layout)

    def _process_data(self) -> ArrayLike:
        data = self.data.copy()
        if self.show == ShowEnum.MAGNITUDE:
            data = np.abs(data)
        elif self.show == ShowEnum.PHASE:
            data = np.arctan2(data.imag, data.real)
        elif self.show == ShowEnum.REAL_PART:
            data = np.real(data)
        else:
            data = np.imag(data)

        if self.filters.get("apply_log", False):
            data = logarithm_stretch(data)
            data = linear_stretch(data) * 255.0
        elif self.filters.get("linear_stretch", False):
            data = linear_stretch(data) * 255.0

        # Clip data
        data = np.clip(data, 0, 255.0).astype(np.uint8)

        # Apply LUT
        if self.lut is not None:
            self.mode_visualisation = "rgb"
            data = apply_lut(data, self.lut)

        self.menus_changed_signal.emit()
        return data

    def _reset_view(self):
        self._reset_checked_states()
        self.get_luts()[0].setChecked(True)
        self.lut = None
        self.mode_visualisation = self.mode

    def _log_filter(self):
        self.filters.clear()
        self.filters["apply_log"] = True
        self.current_filter_name = "Logarithmically stretched"
        self._redraw(self._process_data())

    def _linear_stretch(self):
        self.filters.clear()
        self.filters["linear_stretch"] = True
        self.current_filter_name = "Linearly stretched"
        self._redraw(self._process_data())

    def _show_magnitude(self):
        self._reset_view()
        self.show_magnitude_action.setChecked(True)
        self.linear_stretch_action.setChecked(True)
        self.show = ShowEnum.MAGNITUDE
        self.menus_changed_signal.emit()
        self._linear_stretch()

    def _show_phase(self):
        self._reset_view()
        self.show_phase_action.setChecked(True)
        self.linear_stretch_action.setChecked(True)
        self.show = ShowEnum.PHASE
        self.menus_changed_signal.emit()
        self._linear_stretch()

    def _show_real_part(self):
        self._reset_view()
        self.show_real_part_action.setChecked(True)
        self.linear_stretch_action.setChecked(True)
        self.show = ShowEnum.REAL_PART
        self.menus_changed_signal.emit()
        self._linear_stretch()

    def _show_imag_part(self):
        self._reset_view()
        self.show_imag_part_action.setChecked(True)
        self.linear_stretch_action.setChecked(True)
        self.show = ShowEnum.IMAG_PART
        self.menus_changed_signal.emit()
        self._linear_stretch()

    def _apply_lut(self, name):
        if name == "None":
            self.mode_visualisation = self.mode
            self.lut = None
        else:
            self.lut = get_lut(name)
        self._redraw(self._process_data())

    def _reset_checked_states(self):
        for action in self.get_actions():
            action.setChecked(False)

    def _redraw(self, new_data):
        self.visualiser.update_data(new_data, self.axes_orientation,
                                    self.mode_visualisation)
        self.visualiser.generate()
        self.visualiser.redraw()

    def _create_actions(self):
        self.linear_stretch_action = QAction("Linear stretch")
        self.log_filter_action = QAction("Logarithm")
        self.show_magnitude_action = QAction("Show magnitude")
        self.show_phase_action = QAction("Show phase")
        self.show_real_part_action = QAction("Show real part")
        self.show_imag_part_action = QAction("Show imaginary part")

        self.lut_actions = []
        self.lut_actions.append(("None", QAction("None")))
        for lut_name in lut.LUTS.keys():
            self.lut_actions.append((lut_name, QAction(lut_name)))

    def _connect_actions(self):
        self.linear_stretch_action.triggered.connect(self._linear_stretch)
        self.log_filter_action.triggered.connect(self._log_filter)
        self.show_magnitude_action.triggered.connect(self._show_magnitude)
        self.show_phase_action.triggered.connect(self._show_phase)
        self.show_real_part_action.triggered.connect(self._show_real_part)
        self.show_imag_part_action.triggered.connect(self._show_imag_part)

        for lut_name, lut_action in self.lut_actions:
            lut_action.triggered.connect(partial(self._apply_lut, lut_name))

    def _set_actions_checkable(self):
        for action in self.get_actions():
            action.setCheckable(True)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Plus:
            self.visualiser.increase_zoom_level()
        elif event.key() == QtCore.Qt.Key_Minus:
            self.visualiser.decrease_zoom_level()
        else:
            event.ignore()

    def update_desktop_size(self, width, height):
        self.desktop_width = width
        self.desktop_height = height

    @pyqtSlot(int, int, int, list)
    def set_coordinate_label(self, frame, row, col, data):
        # Showing phase/magnitude
        if self.show == ShowEnum.MAGNITUDE:
            showing = "Magnitude"
        elif self.show == ShowEnum.PHASE:
            showing = "Phase"
        elif self.show == ShowEnum.REAL_PART:
            showing = "Real part"
        else:
            showing = "Imaginary part"

        # Note: numpy is row-centric, that's why y and x are switched
        self.coordinates_label.setText(
            f"current filter = {self.current_filter_name}; "
            f"Showing = {showing}\n"
            f"row={row}, col={col}\n"
            f"original value={self.data[frame, row, col]}), "
            f"mapped value={data}")

    def get_filters(self):
        return [self.linear_stretch_action, self.log_filter_action]

    def get_luts(self):
        return [action for _, action in self.lut_actions]

    def get_views(self):
        return [self.show_magnitude_action, self.show_phase_action,
                self.show_real_part_action, self.show_imag_part_action]

    def get_actions(self):
        result = self.get_filters()
        result.extend(self.get_luts())
        result.extend(self.get_views())
        return result

    def get_menus(self):
        view_filters = ("View", self.get_views())
        if self.show == ShowEnum.PHASE:
            return [
                ("Filters", [
                    self.linear_stretch_action
                ]),
                view_filters,
                ("LUT", self.get_luts())
            ]
        return [
            ("Filters", self.get_filters()),
            view_filters
        ]
