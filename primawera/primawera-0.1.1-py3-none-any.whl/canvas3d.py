from functools import partial
from typing import Dict, Optional

from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot, Qt, pyqtSignal
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QWidget, QGridLayout, QAction

from primawera.filters import *
from primawera.lut import *
from primawera.visualiser import Visualiser


class Canvas3D(QWidget):
    menus_changed_signal = pyqtSignal()

    def __init__(self, data: ArrayLike, bitdepth: int, mode: str,
                 desktop_height: int, desktop_width: int,
                 filters: Optional[Dict[str, bool]] = None,
                 filters_options: Optional[Dict[str, int]] = None, *args,
                 **kwargs) -> None:
        super(Canvas3D, self).__init__(*args, **kwargs)
        if filters is None:
            filters = dict()
        if filters_options is None:
            filters_options = dict()

        self.desktop_height = desktop_height
        self.desktop_width = desktop_width

        # Interface
        self.main_layout = QVBoxLayout()

        self.coordinates_label = QLabel()
        self.coordinates_label.setText("Please click on an image.")
        self.main_layout.addWidget(self.coordinates_label, stretch=0)

        # Load data
        self.bitdepth = bitdepth
        self.raw_data = data
        self.mode = mode
        self.mode_visualisation = mode
        self.lut = None
        assert self.bitdepth != -1
        assert self.raw_data is not None
        assert self.mode != ""

        # Processing
        self.filters = filters
        self.filters_options = filters_options
        processed_data = self.process_data()

        # Visualise
        maximum_width = int(self.desktop_width * 0.80)
        maximum_height = int(self.desktop_height * 0.80)
        self.view_layout = QGridLayout()
        self.vis_main_window = Visualiser(processed_data.copy(), (0, 1, 2),
                                          self.mode, maximum_height,
                                          maximum_width, True)
        self.vis_main_window.signal_position.connect(self.set_coordinate_label)
        self.vis_row_time = Visualiser(processed_data, (1, 0, 2),
                                       self.mode, maximum_height,
                                       maximum_width, False)
        self.vis_row_time.signal_position.connect(self.set_coordinate_label)
        self.vis_col_time = Visualiser(processed_data, (2, 1, 0),
                                       self.mode, maximum_height,
                                       maximum_width, False)
        self.vis_col_time.signal_position.connect(self.set_coordinate_label)
        self.view_layout.addWidget(self.vis_main_window, 0, 0, Qt.AlignTop)
        self.view_layout.addWidget(self.vis_row_time, 1, 0, Qt.AlignTop)
        self.view_layout.addWidget(self.vis_col_time, 0, 1, Qt.AlignTop)

        self.main_layout.addLayout(self.view_layout, 1)

        # TODO: consider if it is useful any longer
        # Set up scaling factors, so that all extra space is filled using
        # spacers.
        self.view_layout.setColumnStretch(2, 1)
        self.view_layout.setRowStretch(2, 1)

        self.setLayout(self.main_layout)

        # These are just to simplify some member functions
        self.visualisers = [self.vis_main_window, self.vis_row_time,
                            self.vis_col_time]
        self.axes_orientations = [(0, 1, 2), (1, 0, 2), (2, 1, 0)]

        self._connect_visualisers_signals()
        self._hide_scroll_bars()

        # Setup actions
        self._create_actions()
        self._set_actions_checkable()
        self._connect_actions()

        # TODO: move this higher, so that we do not have to process image
        #       twice during this constructor.
        if self.mode != 'F':
            self._no_filter()
        else:
            self._linear_stretch()
        self.get_actions()[0].setChecked(True)

    def _connect_visualisers_signals(self):
        # Here we synchronize the QScrollAreas using signals.
        self.vis_main_window.value_change_emitter_vertical.connect(
            self.vis_col_time.get_vertical_bar().setValue)
        self.vis_main_window.value_change_emitter_horizontal.connect(
            self.vis_row_time.get_horizontal_bar().setValue)

        self.vis_col_time.value_change_emitter_vertical.connect(
            self.vis_main_window.get_vertical_bar().setValue)
        self.vis_row_time.value_change_emitter_horizontal.connect(
            self.vis_main_window.get_horizontal_bar().setValue)

    def _hide_scroll_bars(self):
        # Hide unused bars
        row_time = self.vis_row_time.get_scroll_area()
        row_time.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        row_time.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        col_time = self.vis_col_time.get_scroll_area()
        col_time.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        col_time.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

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

    def _set_actions_checkable(self):
        for action in self.get_actions():
            action.setCheckable(True)

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
        self.current_filter_name = "Logarithmically stretched"

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
        self.current_filter_name = "None"

    def _redraw(self, new_data):
        for vis, axes_orientation in zip(self.visualisers,
                                         self.axes_orientations):
            vis.update_data(new_data, axes_orientation,
                            self.mode_visualisation)
            vis.generate()
            vis.redraw()

    def get_filters(self):
        if self.mode == "F":
            return [self.linear_stretch_action, self.logarithm_stretch_action]

        result = [self.no_filter_action]
        if self.mode == "1":
            return result

        if self.mode == "grayscale":
            result.append(self.linear_stretch_action)
        result.extend([self.linear_contrast_action,
                       self.gamma_correction_action])
        return result

    def get_luts(self):
        if self.mode == "F" or self.mode == "grayscale":
            return [action for _, action in self.lut_actions]
        return []

    def get_actions(self):
        return self.get_filters() + self.get_luts()

    def get_menus(self):
        filters_menu = ("Filters", self.get_filters())
        luts_menu = ("LUT", self.get_luts())
        return [filters_menu, luts_menu] if luts_menu[1] else [filters_menu]

    @pyqtSlot(int, int, int, list)
    def set_coordinate_label(self, frame, row, col, data):
        # Note: numpy is row-centric, that's why y and x are switched
        self.coordinates_label.setText(
            f"current filter = {self.current_filter_name}\n"
            f"row={row}, col={col}\n"
            f"original value={self.raw_data[frame, row, col]}), mapped value={data}")

    def next_frame(self):
        # TODO: improve
        #   sth like assembly in .NET?
        if self.axes_button_x.isChecked():
            self.vis_main_window.next_frame()
        elif self.axes_button_y.isChecked():
            self.vis_row_time.next_frame()
        elif self.axes_button_z.isChecked():
            self.vis_col_time.next_frame()
        else:
            print("[D] no button checked!")

    def previous_frame(self):
        # TODO: improve
        #   sth like assembly in .NET?
        if self.axes_button_x.isChecked():
            self.vis_main_window.previous_frame()
        elif self.axes_button_y.isChecked():
            self.vis_row_time.previous_frame()
        elif self.axes_button_z.isChecked():
            self.vis_col_time.previous_frame()
        else:
            print("[D] no button checked!")

    def process_data(self):
        processed_data = self.raw_data.astype(float)

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
            processed_data = logarithm_stretch(processed_data)
            processed_data = 255.0 * linear_stretch(processed_data)

        processed_data = np.clip(processed_data, 0, 255.0).astype(np.uint8)

        # Apply LUT
        if self.lut is not None:
            self.mode_visualisation = "rgb"
            processed_data = apply_lut(processed_data, self.lut)
        self.menus_changed_signal.emit()
        return processed_data

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Plus:
            for visualiser in self.visualisers:
                visualiser.increase_zoom_level()
        elif event.key() == QtCore.Qt.Key_Minus:
            for visualiser in self.visualisers:
                visualiser.decrease_zoom_level()

        event.ignore()

    def _apply_lut(self, name):
        if name == "None":
            self.mode_visualisation = self.mode
            self.lut = None
        else:
            self.lut = get_lut(name)
        self._redraw(self.process_data())

    def update_desktop_size(self, width, height):
        self.desktop_width = width
        self.desktop_height = height
