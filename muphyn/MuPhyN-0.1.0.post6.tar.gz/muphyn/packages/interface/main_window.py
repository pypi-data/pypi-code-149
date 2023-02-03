#-----------------------------------
# Imports
#-----------------------------------

import os
import time
from typing import List, Any, Dict
from datetime import datetime

import matplotlib.pylab as plt

from PyQt5 import QtGui
from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtWidgets import QAction, QLabel, QMainWindow, QMenuBar, QSplitter, QToolBox, QWidget, QFileDialog, QApplication, QVBoxLayout, QGroupBox,QBoxLayout, QScrollArea
from PyQt5.QtGui import QKeySequence

from muphyn.packages.core.plci_core_scheduler import Scheduler
from muphyn.packages.core.plci_core_scheduler_exception import SchedulerException
from muphyn.packages.core.utils.log_manager import LogManager
from muphyn.packages.interface.box_library.box_libraries_list import BoxLibrariesList
from muphyn.packages.interface.files.abstract_importer import AbstractImporter
from muphyn.packages.interface.models.editable_models.scheduler_model import SchedulerModel
from muphyn.packages.interface.properties_pages.properties_widget import PropertiesWidget
from muphyn.packages.interface.dialogs.abstract_dialog import AbstractDialog
from muphyn.packages.interface.dialogs.dialogs_holder import DialogsHolder
from muphyn.packages.interface.editors.factory_editors import factory_editors
from muphyn.packages.interface.models.editable_models.abstract_diagram_model import AbstractDiagramModel
from muphyn.packages.interface.models.editable_models.abstract_editable_model import AbstractEditableModel
from muphyn.packages.interface.models.editable_models.simulation_model import SimulationModel
from muphyn.packages.interface.project_tabs_holder import ProjectTabsHolder
from muphyn.packages.interface.recent_file_menu import RecentFileMenu
from muphyn.packages.interface.user_data.user_data import UserData
from muphyn.packages.interface.new_project_at_startup import new_project_on_startup
from muphyn.packages.core.box_library.plci_core_boxes_libraries import BoxesLibrariesManager
from muphyn.packages.core.scheduler_library.plci_core_schedulers_libraries import SchedulersLibraries
from muphyn.packages.parser.parser import Parser
from muphyn.packages.interface.editors.diagram_editor import DiagramEditor
from muphyn.packages.interface.widgets.PopupWindows.YesNoPopup import YesNoMessageBox
from muphyn.packages.interface.utils.interface_constants import ApplicationWindowTitle
from muphyn.packages.interface.widgets.StandardActions import RotateLeftAction, RotateRightAction, UndoAction, RedoAction, DeleteAction, StartAction, StopAction

import muphyn.packages.interface.files.files as files


#-----------------------------------
# Class
#-----------------------------------

class MainWindow (QMainWindow) :
    """Est la fenêtre principale."""
    
    # -------------
    # Constructors
    # -------------

    def __init__ (self) :
        super(MainWindow, self).__init__()
        
        self.setGeometry(100, 100, 1024, 768)
        self.setWindowTitle(ApplicationWindowTitle)

        self._schedulers_libraries : SchedulersLibraries = SchedulersLibraries()
        
        # Load User parameters
        self._user_data : UserData = UserData("./user_data.yaml")
        self._user_data.load()

        # Load already added library
        for box_library in self._user_data.boxes_libraries :
            BoxesLibrariesManager().add_library(box_library)

        # Load schedulers libraries
        for scheduler_library in self._user_data.schedulers_libraries :
            self._schedulers_libraries.add_library(scheduler_library)

        BoxesLibrariesManager().load_libraries()
        self._schedulers_libraries.load_libraries()

        self._dialogs_holder : DialogsHolder = DialogsHolder(self)
        self._dialogs_holder.dialog_opened_listener.append(self._dialog_opened_event)
        self._dialogs_holder.dialog_closed_listener.append(self._dialog_closed_event)
        self._dialogs_holder.dialog_closed_all_listener.append(self._dialogs_closed_all_event)

        self._opened_dialogs_actions : Dict[AbstractDialog, QAction] = {}

        self._init_actions()
        self._init_menu()
        self._init_ui()

        self.setAcceptDrops(True)

        self.regenerate_recent_files()
        self.open(new_project_on_startup(self._user_data, self._schedulers_libraries))

        # 
        if os.path.exists("backup.backup"):
            # Open Popup Window
            yesNoMessageBox = YesNoMessageBox("Nous avons détecté que l'application s'est fermé brutalement sans que vous ayez eu l'occasion de sauvegarder vos fichiers.\nVoulez-vous les récupérer ?", parent=self)
            yesNoMessageBox.show()

            yesNoMessageBox.accepted.connect(self.load_backup_files)
            yesNoMessageBox.rejected.connect(self.delete_backup_files)

    # -------------
    # Properties
    # -------------

    @property
    def dialogs_holder (self) -> DialogsHolder :
        """Permet de récuperer l'objet contenant les dialogues."""
        return self._dialogs_holder

    @property
    def schedulers_libraries (self) -> SchedulersLibraries :
        """Permet de récuperer l'objet contenant les bibliothèques de planificateurs."""
        return self._schedulers_libraries


    # -------------
    # Methods
    # -------------

    def dropEvent (self, drop_event : QtGui.QDropEvent) -> None :
        if drop_event.mimeData().hasUrls() :
            for url in drop_event.mimeData().urls() :
                self.open_file(url.toLocalFile())

        super().dropEvent(drop_event)

    def dragEnterEvent (self, drag_enter_event : QtGui.QDragEnterEvent) -> None :

        if drag_enter_event.mimeData().hasUrls() :
            drag_enter_event.accept()

        super().dragEnterEvent(drag_enter_event)

    def dragMoveEvent (self, drag_move_event : QtGui.QDragMoveEvent) -> None :
        return super().dragMoveEvent(drag_move_event)
    
    def open_file (self, path : str) -> None :
        """Permet d'ouvrir un fichier."""

        if os.path.exists(path) :
            editable_model : AbstractEditableModel = files.load(path)

            if editable_model is None :
                LogManager().error('no file to load !!')
                return

            else :
                self.open(editable_model)

    def open (self, adm : AbstractEditableModel) -> None :
        """Permet d'ouvrir un model d'édition."""

        # Check if a project with the same name already exists
        for graphical_editor_index in range(self._tabs.count()) :
            graphical_editor : AbstractEditableModel = self._tabs.widget(graphical_editor_index)

            if graphical_editor.editable_model.name == adm.name and graphical_editor.editable_model.path == adm.path :
                return
        
        # Create new tab
        tab : QWidget = factory_editors(self._tabs, adm)

        # Add Project to the LogManager
        LogManager().add_project_logger(tab.id, adm.name, adm.path)
        
        if isinstance(tab, QLabel) :
            self._tabs.addTab(tab, adm.name)

        else :
            self._tabs.addEditor(tab)

        if self._tabs.count() > 1 :
            self._tabs.setCurrentIndex(self._tabs.count() - 1)

        # Add opened file to recent files
        self.add_recent_file(adm.path + adm.name + '.yaml')

    def add_recent_file (self, path : str) -> None :
        """Permet d'essayer d'ajouter le fichier dans les fichiers récents."""

        if path in self._user_data.recent_files :
            self._user_data.recent_files.remove(path)
        
        self._user_data.recent_files.insert(0, path)
        self.regenerate_recent_files()

    def regenerate_recent_files (self) -> None : 
        """Permet de regénérer le menu des fichiers récents."""
        max_files = 10
        current_file_number = 0
        for action_index in range(len(self._mn_recent_files.actions())).__reversed__() :
            self._mn_recent_files.removeAction(self._mn_recent_files.actions()[action_index])

        for path in self._user_data.recent_files :

            if current_file_number >= max_files : 
                return

            if os.path.exists(path) :
                mn_recent_file_action = RecentFileMenu(self, path, self.open_file)
                self._mn_recent_files.addAction(mn_recent_file_action)

                current_file_number += 1

    @pyqtSlot()
    def _file_open_method (self) -> None :
        """Est la méthode appelée lorsque l'utilisateur veut ouvrir un fichier."""

        path = QFileDialog.getOpenFileName(self, f'{ApplicationWindowTitle} - Open project file', os.getcwd(), 'YAML (*.yaml)')[0]
        if path is None or len(path) == 0 :
            return

        self.open_file(path)

    @pyqtSlot()
    def _file_save_method (self) -> None :
        """Est la méthode appelée lorsque l'utilisateur veut sauvegarder le fichier en cours."""

        if self._tabs.current_editor is None : 
            return

        if self._tabs.current_editor.editable_model is None : 
            return
        
        file_name = self._tabs.current_editor.editable_model.path.__str__()
        if not(file_name.endswith(os.sep)) :
            file_name = file_name + os.sep

        file_name = file_name + self._tabs.current_editor.editable_model.name

        if not(file_name.endswith('.yaml')):
            file_name = file_name + '.yaml'

        files.save(self._tabs.current_editor.editable_model, file_name)

    @pyqtSlot()
    def _file_save_as_method (self) -> None :
        """Est la méthode appelée lorsque l'utilisateur veut sauvegarder le fichier en cours sous un nouveau nom."""

        if self._tabs.current_editor is None : 
            return

        if self._tabs.current_editor.editable_model is None : 
            return

        path = QFileDialog.getSaveFileName(self, f'{ApplicationWindowTitle} - Save as file', os.getcwd(), 'YAML (*.yaml)')[0]

        if path is None or len(path) == 0 :
            return

        if files.save(self._tabs.current_editor.editable_model, path) : 

            file_name = os.path.basename(path)
            abs_path = path[:-file_name.__len__()]
            file_name = file_name[:-('.yaml').__len__()]

            self._tabs.current_editor.editable_model.set_path_name(abs_path, file_name)

    @pyqtSlot()
    def _file_close_method (self) -> None : 
        """Est la méthode appelée pour fermer le fichier actuel."""
        self.tab_close_request(self._tabs.currentIndex())

    @pyqtSlot()
    def _undo_method (self) -> None :
        """Est la méthode appelée pour défaire la dernière action."""

        if self._tabs.current_editor is None : 
            return

        self._tabs.current_editor.actions_holder.undo()

    @pyqtSlot()
    def _redo_method (self) -> None : 
        """Est la méthode appelée pour refaire la dernière action défaite."""

        if self._tabs.current_editor is None : 
            return

        self._tabs.current_editor.actions_holder.redo()

    @pyqtSlot()
    def _window_libraries_method (self) -> None :
        """Est la méthode appelée pour afficher un dialogue permettant à l'utilisateur de modifier les bibliothèques."""
        self.dialogs_holder.show_dialog('library', True, boxes_libraries = BoxesLibrariesManager(), schedulers_libraries = self._schedulers_libraries)

    @pyqtSlot()
    def _help_documentation_method (self) -> None :
        """Est la méthode appelée pour afficher un dialogue permettant d'aider l'utilisateur."""
        self.dialogs_holder.show_dialog('documentation', False)

    @pyqtSlot()
    def _help_about_method (self) -> None :
        """Est la méthode appelée pour afficher un dialogue affichant les détails des licences et des personnes ayant travaillés sur le programme."""
        self.dialogs_holder.show_dialog('about', False)

    @pyqtSlot()
    def _file_new_simulation_method (self) -> None :
        """Est la méthode appellée lorsque l'utilisateur veut créer une nouvelle simulation."""
        self.dialogs_holder.show_dialog('new_simulation', True, schedulers_libraries = self._schedulers_libraries)

    @pyqtSlot()
    def _simulation_parameters_method (self) -> None :
        """Est la méthode appelée pour afficher un digalogue permettant de modifier les paramètres de la simulation."""
        if isinstance(self._tabs.current_editor.editable_model, SimulationModel) : 
            self.dialogs_holder.show_dialog('simulation_parameters_dialog', True, current_simulation = self._tabs.current_editor.editable_model, schedulers_libraries = self._schedulers_libraries)

    @pyqtSlot()
    def _simulation_launch_method (self) -> None :
        """Est la méthode appelée pour lancer la simulation en cours d'édition."""

        global_simulation_start = time.perf_counter()
        
        if self._tabs.current_editor is None : 
            return

        if self._tabs.current_editor.editable_model is None : 
            return

        parser = Parser()
        scheduler : Scheduler = parser.parse(self._tabs.current_editor.editable_model, self.schedulers_libraries)
        
        if scheduler is None : 
            LogManager().error('No scheduler returned for the simulation !!')

        else :
            start_time = time.perf_counter()

            schedulerException : SchedulerException = scheduler.schedule()
            stop_time = time.perf_counter()

            if schedulerException is None :
                LogManager().debug(f"The simulation is correctly finished and it took : {stop_time - start_time}s.")
                LogManager().debug(f"The simulation + initialization took : {stop_time - global_simulation_start}s.")

                plt.show()
                if len(plt.get_fignums()) > 0 :
                    LogManager().debug('figures shown : ')
                    for i in plt.get_fignums() :
                        LogManager().debug(f' - {i}')

            else :
                LogManager().error(f"The simulation encoutered an error after {stop_time - start_time: .3f}s of simulation.")
                schedulerException.print()

    @pyqtSlot()
    def _file_new_box_method (self) -> None :
        """Est la méthode appellée lorsque l'utilisateur veut créer une nouvelle box."""
        self.dialogs_holder.show_dialog('new_box', True, user_data = self._user_data)

    @pyqtSlot()
    def _file_new_solver_method (self) -> None :
        """Est la méthode appellée lorsque l'utilisateur veut créer un nouveau solveur."""
        self.dialogs_holder.show_dialog('new_scheduler', True, user_data = self._user_data)

    @pyqtSlot()
    def _edit_copy_method (self) -> None :
        """Est la méthode appelée pour copier la sélection actuelle."""
        if self._tabs.current_editor is None : 
            return

        self._tabs.current_editor.copy()

    @pyqtSlot()
    def _edit_cut_method (self) -> None :
        """Est la méthode appelée pour couper la sélection actuelle."""
        if self._tabs.current_editor is None : 
            return

        self._tabs.current_editor.cut()

    @pyqtSlot()
    def _edit_paste_method (self) -> None :
        """Est la méthode appelée pour coller le contenu du clipboard."""
        if self._tabs.current_editor is None : 
            return

        self._tabs.current_editor.paste()

    @pyqtSlot()    
    def _edit_rot_clock_90_method (self) -> None :
        """Est la méthode appelée pour faire tourner la box sélectionné de 90° dans le sens des aiguilles d'une montre."""
        
        current_editor = self._tabs.current_editor

        if current_editor is None :
            return

        for element in current_editor.selected_elements() :
            if hasattr(element, 'setRotation') :
                element.setRotation(element.rotation() + 90)

        
    @pyqtSlot()
    def _edit_rot_anti_clock_90_method (self) -> None :
        """Est la méthode appelée pour faire tourner la box sélectionné de 90° dans le sens des aiguilles d'une montre."""
        
        current_editor = self._tabs.current_editor

        if current_editor is None :
            return

        for element in current_editor.selected_elements() :
            if hasattr(element, 'setRotation') :
                element.setRotation(element.rotation() - 90)

    @pyqtSlot()
    def _edit_rot_reverse_method (self) -> None :
        """Est la méthode appelée pour retourner la box sélectionné."""
        
        current_editor = self._tabs.current_editor

        if current_editor is None :
            return

        for element in current_editor.selected_elements() :
            if hasattr(element, 'setRotation') :
                element.setRotation(element.rotation() + 180)

    @pyqtSlot()
    def _edit_select_all_method (self) -> None :
        """Est la méthode appelée pour sélectionner tous les éléments."""
        
        current_editor = self._tabs.current_editor

        if current_editor is None :
            return

        for element in current_editor.elements() :
            element.setSelected(True)

    @pyqtSlot()
    def _edit_reverse_selection_method (self) -> None :
        """Est la méthode appelée pour inverser la sélection des éléments."""
        current_editor = self._tabs.current_editor

        if current_editor is None :
            return

        for element in current_editor.elements() :
            element.setSelected(not(element.isSelected()))
    
    @pyqtSlot()
    def _edit_erase_selection_method (self) -> None :
        """Est la méthode appelée pour supprimer la sélection."""
        current_editor = self._tabs.current_editor

        if current_editor is None :
            return
        
        current_editor.delete_selection()
    
    @pyqtSlot()
    def _window_zoom_method (self) -> None : 
        """Est la méthode appelée pour zoomer dans l'interface d'édition."""
        
        current_editor = self._tabs.current_editor

        if current_editor is None :
            return

        current_editor.zoom(1)
    
    @pyqtSlot()
    def _window_dezoom_method (self) -> None :
        """Est la méthode appelée pour dézoomer dans l'interface d'édition."""
        
        current_editor = self._tabs.current_editor

        if current_editor is None :
            return

        current_editor.zoom(-1)

    def _init_actions (self) -> None :
        """Permet de créer les actions que la fenêtres peut réaliser."""

        self._file_new_simulation_action = QAction('&Simulation', self)
        self._file_new_simulation_action.triggered.connect(self._file_new_simulation_method)
        self._file_new_simulation_action.setShortcut(QKeySequence('Ctrl+N'))

        self._file_new_box_action = QAction('&Box', self)
        self._file_new_box_action.triggered.connect(self._file_new_box_method)
        self._file_new_box_action.setShortcut(QKeySequence('Ctrl+Shift+N'))

        self._file_new_solver_action = QAction('Sche&duler', self)
        self._file_new_solver_action.triggered.connect(self._file_new_solver_method)

        self._file_open_action = QAction('&Open', self)
        self._file_open_action.triggered.connect(self._file_open_method)
        self._file_open_action.setShortcut(QKeySequence('Ctrl+O'))
        
        self._file_save_action = QAction('&Save', self)
        self._file_save_action.triggered.connect(self._file_save_method)
        self._file_save_action.setShortcut(QKeySequence('Ctrl+S'))

        self._file_save_as_action = QAction('S&ave as', self)
        self._file_save_as_action.triggered.connect(self._file_save_as_method)
        self._file_save_as_action.setShortcut(QKeySequence('Ctrl+Shift+S'))

        self._file_export_action = QAction('&Export', self)
        self._file_export_action.triggered.connect(self._file_export_method)
        self._file_export_action.setShortcut(QKeySequence('Ctrl+E'))

        self._file_close_action = QAction('&Close', self)
        self._file_close_action.triggered.connect(self._file_close_method)
        self._file_close_action.setShortcut(QKeySequence('Ctrl+W'))

        self._file_exit_action = QAction('&Quit', self)
        self._file_exit_action.triggered.connect(self.close)
        self._file_exit_action.setShortcut(QKeySequence('Alt+F4'))

        self._edit_undo_action = UndoAction('&Undo', self)
        self._edit_undo_action.triggered.connect(self._undo_method)
        self._edit_undo_action.setShortcut(QKeySequence('Ctrl+Z'))

        self._edit_redo_action = RedoAction('&Redo', self)
        self._edit_redo_action.triggered.connect(self._redo_method)
        self._edit_redo_action.setShortcut(QKeySequence('Ctrl+Y'))

        self._edit_cut_action = QAction('C&ut', self)
        self._edit_cut_action.triggered.connect(self._edit_cut_method)
        self._edit_cut_action.setShortcut(QKeySequence('Ctrl+X'))

        self._edit_copy_action = QAction('&Copy', self)
        self._edit_copy_action.triggered.connect(self._edit_copy_method)
        self._edit_copy_action.setShortcut(QKeySequence('Ctrl+C'))

        self._edit_paste_action = QAction('&Paste', self)
        self._edit_paste_action.triggered.connect(self._edit_paste_method)
        self._edit_paste_action.setShortcut(QKeySequence('Ctrl+V'))

        self._rot_clock_90_action = RotateRightAction('Rotate right', self)
        self._rot_clock_90_action.triggered.connect(self._edit_rot_clock_90_method)

        self._rot_anti_clock_90_action = RotateLeftAction('Rotate left', self)
        self._rot_anti_clock_90_action.triggered.connect(self._edit_rot_anti_clock_90_method)

        self._rot_reverse_action = QAction('Flip', self)
        self._rot_reverse_action.triggered.connect(self._edit_rot_reverse_method)

        self._select_all_action = QAction('Select all', self)
        self._select_all_action.triggered.connect(self._edit_select_all_method)
        self._select_all_action.setShortcut(QKeySequence('Ctrl+A'))

        self._reverse_selection_action = QAction('Invert selection', self)
        self._reverse_selection_action.triggered.connect(self._edit_reverse_selection_method)
        self._reverse_selection_action.setShortcut(QKeySequence('Ctrl+Shift+A'))

        self._edit_new_simulation_from_selection_action = QAction('Create simulation from selection', self)
        self._edit_new_simulation_from_selection_action.triggered.connect(self._edit_new_simulation_from_selection_method)

        self._edit_new_composite_box_from_selection_action = QAction('Create composite box from selection', self)
        self._edit_new_composite_box_from_selection_action.triggered.connect(self._edit_new_composite_box_from_selection_method)

        self._edit_erase_selection_action = DeleteAction('Delete', self)
        self._edit_erase_selection_action.triggered.connect(self._edit_erase_selection_method)
        self._edit_erase_selection_action.setShortcut(QKeySequence('Delete'))

        self._window_zoom_action = QAction('Zoom +', self)
        self._window_zoom_action.triggered.connect(self._window_zoom_method)
        self._window_zoom_action.setShortcut(QKeySequence('Ctrl++'))

        self._window_dezoom_action = QAction('Zoom -', self)
        self._window_dezoom_action.triggered.connect(self._window_dezoom_method)
        self._window_dezoom_action.setShortcut(QKeySequence('Ctrl+-'))

        self._window_close_all_action = QAction('Close dialog windows', self)
        self._window_close_all_action.triggered.connect(self._dialogs_holder.close_all)
        self._window_close_all_action.setEnabled(self._dialogs_holder.len > 0)

        self._window_libraries_action = QAction('Libraries', self)
        self._window_libraries_action.triggered.connect(self._window_libraries_method)
        
        self._window_options_action = QAction('Options', self)
        self._window_options_action.triggered.connect(self._window_options_method)

        self._simulation_parameters_action = QAction('Parameters', self)
        self._simulation_parameters_action.triggered.connect(self._simulation_parameters_method)

        self._simulation_launch_action = StartAction('Start simulation', self)
        self._simulation_launch_action.triggered.connect(self._simulation_launch_method)
        self._simulation_launch_action.setShortcut(QKeySequence('F5'))

        self._simulation_stop_action = StopAction('Stop simulation', self)
        self._simulation_stop_action.triggered.connect(self._simulation_stop_method)
        self._simulation_stop_action.setShortcut(QKeySequence('Shift+F5'))

        self._help_documentation_action = QAction('&Documentation', self)
        self._help_documentation_action.triggered.connect(self._help_documentation_method)
        self._help_documentation_action.setShortcut(QKeySequence('F1'))
        
        self._help_about_action = QAction('&About', self)
        self._help_about_action.triggered.connect(self._help_about_method)

    def _init_menu (self) -> None : 
        """Permet de créer le menu afficher dans la fenêtre."""

        self._menu_bar = QMenuBar()
        self.setMenuBar(self._menu_bar)

        self._mn_file = self._menu_bar.addMenu('&Files')
        self._mn_file_new = self._mn_file.addMenu('&New')
        self._mn_file_new.addAction(self._file_new_simulation_action)
        self._mn_file_new.addAction(self._file_new_box_action)
        self._mn_file_new.addAction(self._file_new_solver_action)
        self._mn_file.addAction(self._file_open_action)
        self._mn_file.addAction(self._file_save_action)
        self._mn_file.addAction(self._file_save_as_action)
        self._mn_recent_files = self._mn_file.addMenu("Recent Files")
        self._mn_file.addSeparator()
        self._mn_file.addAction(self._file_export_action)
        self._mn_file.addSeparator()
        self._mn_file.addAction(self._file_close_action)
        self._mn_file.addSeparator()
        self._mn_file.addAction(self._file_exit_action)

        self._mn_edit = self._menu_bar.addMenu('&Edit')
        self._mn_edit.addAction(self._edit_undo_action)
        self._mn_edit.addAction(self._edit_redo_action)
        self._mn_edit.addSeparator()
        self._mn_edit.addAction(self._edit_cut_action)
        self._mn_edit.addAction(self._edit_copy_action)
        self._mn_edit.addAction(self._edit_paste_action)
        self._mn_edit.addSeparator()
        self._mn_edit_rotation = self._mn_edit.addMenu('Rotate')
        self._mn_edit_rotation.addAction(self._rot_clock_90_action)
        self._mn_edit_rotation.addAction(self._rot_anti_clock_90_action)
        self._mn_edit_rotation.addAction(self._rot_reverse_action)
        self._mn_edit.addSeparator()
        self._mn_edit.addAction(self._select_all_action)
        self._mn_edit.addAction(self._reverse_selection_action)
        self._mn_edit.addSeparator()
        self._mn_edit.addAction(self._edit_new_simulation_from_selection_action)
        self._mn_edit.addAction(self._edit_new_composite_box_from_selection_action)
        self._mn_edit.addSeparator()
        self._mn_edit.addAction(self._edit_erase_selection_action)

        self._mn_window = self._menu_bar.addMenu('&View')
        self._mn_window.addAction(self._window_zoom_action)
        self._mn_window.addAction(self._window_dezoom_action)
        self._mn_window.addSeparator()
        self._mn_window_dialogues = self._mn_window.addMenu('Opened dialog windows')
        self._mn_window_dialogues.setEnabled(self._dialogs_holder.len > 0)
        self._mn_window.addAction(self._window_close_all_action)
        self._mn_window.addSeparator()
        self._mn_window.addAction(self._window_libraries_action)
        self._mn_window.addAction(self._window_options_action)
        
        self._mn_simulation = self._menu_bar.addMenu('&Simulation')
        self._mn_simulation.addAction(self._simulation_parameters_action)
        self._mn_simulation.addSeparator()
        self._mn_simulation.addAction(self._simulation_launch_action)
        self._mn_simulation.addAction(self._simulation_stop_action)

        self._mn_help = self._menu_bar.addMenu('&?')
        self._mn_help.addAction(self._help_documentation_action)
        self._mn_help.addSeparator()
        self._mn_help.addAction(self._help_about_action)

    def tabs_elements_selected_changed (self, elements_i) -> None :
        """Est la méthode appelée lorsque l'utilisateur modifie sa sélection."""
        # Get Current editor instance
        current_editor = self._tabs.current_editor

        # If no current editor -> error
        if current_editor is None :
            LogManager().error("MainWindow.tabs_elements_selected_changed: Trying to select current editor but get None")
            return
        
        # Get all selected elements
        elements_l: list = list(elements_i())

        # If only one element is selected
        #   Note : If more than one element selected we can't get the last selected one
        #           because the elements are in the list in the same order of creation
        if len(elements_l) == 1 :
            self._tool_box_page_properties.actions_holder = current_editor.actions_holder
            self._tool_box_page_properties.current_model = elements_l[0]

        else :
            self._tool_box_page_properties.actions_holder = None
            self._tool_box_page_properties.current_model = None
    
    def _init_ui (self) :
        """Est la méthode appelée pour afficher les éléments visuels."""

        # Main Window Splitter
        self._splt_main_window = QSplitter(Qt.Orientation.Horizontal)
        self._splt_main_window.setChildrenCollapsible(False)
        self._splt_main_window.setContentsMargins(5, 5, 5, 5)

        # Vertical Splitter
        self._splitter_lib_prop = QSplitter(Qt.Orientation.Vertical)
        self._splitter_lib_prop.setMinimumWidth(355)
        self._splitter_lib_prop.setChildrenCollapsible(False)

        # Project tab holder
        self._tabs = ProjectTabsHolder(self._splt_main_window)
        self._tabs.elements_selected_changed.connect(self.tabs_elements_selected_changed)
        self._tabs.tabCloseRequested.connect(self.tab_close_request)

        # Init Libraries list widget
        lib_groupbox = QGroupBox("Libraries")
        self._libraries = BoxLibrariesList()
        lib_groupbox.setLayout(self._libraries.layout())

        # Init Properties list widget
        properties_groupbox = QGroupBox("Properties")
        self._tool_box_page_properties = PropertiesWidget()
        boxLayout = QVBoxLayout()

        # Init Scroll Area
        scrollArea = QScrollArea()
        scrollArea.setWidgetResizable(True)
        scrollArea.setBaseSize
        scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        # Add Properties Widget to Scroll Area
        scrollArea.setWidget(self._tool_box_page_properties)

        # Add Scroll Area to Box Layout
        boxLayout.addWidget(scrollArea)

        # Add Properties Box Layout to GroupBox
        properties_groupbox.setLayout(boxLayout.layout())

        # Add Items in right Vertical Splitter
        self._splitter_lib_prop.addWidget(lib_groupbox)
        self._splitter_lib_prop.addWidget(properties_groupbox)
        self._splitter_lib_prop.setStretchFactor(0, 0)
        self._splitter_lib_prop.setStretchFactor(1, 1)

        # Add Item in Main Window Splitter
        self._splt_main_window.addWidget(self._tabs)
        self._splt_main_window.addWidget(self._splitter_lib_prop)
        self._splt_main_window.setStretchFactor(0, 1)
        self._splt_main_window.setStretchFactor(1, 0)

        # Set Splitter as main widget
        self.setCentralWidget(self._splt_main_window)

    @pyqtSlot(int)
    def tab_close_request (self, index : int = ...) :
        
        if self._tabs.count() == 1 :
            return

        # Get current widget
        current_widget = self._tabs.widget(index)

        # Remove project in LogManager
        LogManager().remove_project_logger(current_widget.id)

        # Remove tab from Tabs Holder
        self._tabs.removeTab(index)

        # Delete Widget
        current_widget.deleteLater()



    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        """Est la méthode appelée à la fermeture de la fenêtre."""
        super().closeEvent(event)

        self._user_data.save()

    def _dialog_opened_event (self, abstract_dialog : AbstractDialog) -> None :
        """Est la méthode appelée lorsqu'un dialogue est ouvert."""

        self._mn_window_dialogues.setEnabled(self._dialogs_holder.len > 0)
        self._window_close_all_action.setEnabled(self._dialogs_holder.len > 0)

        new_dialog_action : QAction = QAction(abstract_dialog.windowTitle(), self)
        new_dialog_action.triggered.connect(lambda : abstract_dialog.close())
        self._opened_dialogs_actions[abstract_dialog] = new_dialog_action
        self._mn_window_dialogues.addAction(new_dialog_action)

    def _dialog_closed_event (self, abstract_dialog : AbstractDialog, arg : Any) -> None :
        """Est la méthode appelée lorsqu'un dialogue est fermé.""" 

        self._mn_window_dialogues.setEnabled(self._dialogs_holder.len > 0)
        self._window_close_all_action.setEnabled(self._dialogs_holder.len > 0)

        self._mn_window_dialogues.removeAction(self._opened_dialogs_actions[abstract_dialog])
        del self._opened_dialogs_actions[abstract_dialog]

        if abstract_dialog.name == 'library':
            self._user_data.schedulers_libraries.clear()
            self._user_data.boxes_libraries.clear()

            for library in BoxesLibrariesManager()._libraries:
                if not library.path in self._user_data.boxes_libraries :
                    self._user_data.boxes_libraries.append(library.path)

            self._libraries.libraries_reloaded()

            for library in self._schedulers_libraries._libraries:
                if not library.path in self._user_data.schedulers_libraries :
                    self._user_data.schedulers_libraries.append(library.path)

        elif abstract_dialog.name == 'new_simulation' :

            if abstract_dialog.value is None :
                return

            self.open(abstract_dialog.value)

        elif abstract_dialog.name == 'new_box' :

            if abstract_dialog.value is None :
                return

            self.open(abstract_dialog.value)

        elif abstract_dialog.name == 'simulation_parameters_dialog' :

            if abstract_dialog.value is None : 
                return

            if self._tabs.current_editor is None : 
                return

            if not(isinstance(self._tabs.current_editor.editable_model, SimulationModel)) :
                return

            if isinstance(abstract_dialog.value, SchedulerModel) :
                self._tabs.current_editor.editable_model.scheduler_model = abstract_dialog.value

        else :
            LogManager().error(f"dialog closed not supported : {abstract_dialog.name}")


    def _dialogs_closed_all_event (self, dialogs_holder : DialogsHolder) -> None :
        """Est la méthode appelée lorsque toutes les boite de dialogues ont été fermée."""
        
        self._mn_window_dialogues.setEnabled(self._dialogs_holder.len > 0)
        self._window_close_all_action.setEnabled(self._dialogs_holder.len > 0)

        for dialog in self._opened_dialogs_actions :
            self._mn_window_dialogues.removeAction(self._opened_dialogs_actions[dialog])

        self._opened_dialogs_actions.clear()

    def backup_save_projects(self):
        # Init Bakcup Files list 
        backup_files = []
        for tab in self._tabs:
            # Get Project Directory
            dirname = tab.editable_model.path.__str__()

            # Build Project backup file name
            filename = f"{tab.editable_model.name}_backup.yaml"

            # Save backup file
            bakcup_file_path = os.path.join(dirname, filename)
            files.save(tab.editable_model, bakcup_file_path)

            # Append backup file path to list
            backup_files.append(bakcup_file_path)
        
        # Save Bakcup Files list in main application directory
        with open("backup.backup", "w") as f:
            f.write("\n".join(backup_files))

    def load_backup_files(self):
        # Load Backup files
        with open("backup.backup", "r") as f:
            backup_files = [backup_file_path for backup_file_path in f.readlines()]
            for backup_file in backup_files:
                self.open_file(backup_file)
                
        # Delete Backup files
        self.delete_backup_files()

    def delete_backup_files(self):
        os.remove("backup.backup")

    @pyqtSlot()
    def _file_export_method (self) -> None :
        """Est la méthode appelée pour exporter le fichier actuel."""
        LogManager().error('Not implemented : Export')
    
    @pyqtSlot()
    def _edit_new_simulation_from_selection_method (self) -> None :
        """Est la méthode appelée pour créer une nouvelle simulation depuis la sélection."""
        LogManager().error('Not implemented : New simulation from selection')

    @pyqtSlot()
    def _edit_new_composite_box_from_selection_method (self) -> None :
        """Est la méthode appelée pour créer une nouvelle box composite depuis la sélection."""
        LogManager().error('Not implemented : New composite box from selection')
        
    @pyqtSlot()
    def _window_options_method (self) -> None :
        """Est la méthode appelée pour afficher un dialogue permettant à l'utilisateur de gérer les options du programme."""
        LogManager().error('Not implemented : Show options popup')

    @pyqtSlot()
    def _simulation_stop_method (self) -> None :
        """Est la méthode appelée pour stopper l'éventuel simulation en cours de simulation."""
        LogManager().error('Not implemented : Stop simulate')