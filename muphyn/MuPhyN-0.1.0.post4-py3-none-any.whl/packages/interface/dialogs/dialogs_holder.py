#-----------------------------------
# Imports
#-----------------------------------

from typing import Callable, List, Any

from PyQt5.QtGui import QWindow
from muphyn.packages.core.box_library.plci_core_boxes_libraries import BoxesLibrariesManager
from muphyn.packages.core.scheduler_library.plci_core_schedulers_libraries import SchedulersLibraries
from muphyn.packages.core.utils.log_manager import LogManager

from muphyn.packages.interface.dialogs.library_dialog import LibraryDialog
from muphyn.packages.interface.dialogs.new_box_dialog import NewBoxDialog
from muphyn.packages.interface.dialogs.new_simulation_dialog import NewSimulationDialog
from muphyn.packages.interface.dialogs.simulation_parameters_dialog import SimulationParametersDialog
from muphyn.packages.interface.models.editable_models.simulation_model import SimulationModel
from muphyn.packages.interface.user_data.user_data import UserData

from .abstract_dialog import AbstractDialog

#-----------------------------------
# Class
# #-----------------------------------

class DialogsHolder :
    """Est la classe qui permet à une classe de fenêtre principale d'afficher des dialogues."""

    # -------------
    # Constructors
    # -------------

    def __init__ (self, main_window : QWindow) :
        self._dialogs : List[AbstractDialog] = []
        self._main_window : QWindow = main_window

        self._dialog_opened_listner : List[Callable[[Any], None]] = []
        self._dialog_closed_listner : List[Callable[[Any, Any], None]] = []
        self._dialog_closed_all_listener : List[Callable[[Any], None]] = []

    # -------------
    # Properties
    # -------------

    @property
    def dialogs (self) -> List[AbstractDialog] :
        """Permet de récuperer la liste des boîtes de dialogues actuellement affichées."""
        return self._dialogs

    @property
    def len (self) -> int :
        """Permet de récuperer le nombre de dialogues actuellement affichées."""
        return self._dialogs.__len__()

    @property
    def main_window (self) -> QWindow :
        """Permet de récuperer la fenêtre principale qui détient le dialog holder"""
        return self._main_window

    @property
    def dialog_opened_listener (self) -> List[Callable[[Any], None]] :
        """Permet de récuperer les écouteurs de l'événement appelés à l'ouverture d'une boite dialogue."""
        return self._dialog_opened_listner

    @property
    def dialog_closed_listener (self) -> List[Callable[[Any, Any], None]] :
        """Permet de récuperer les écouteurs de l'événement appelés à la fermeture d'une boite dialogue."""
        return self._dialog_closed_listner

    @property
    def dialog_closed_all_listener (self) -> List[Callable[[Any], None]] :
        """Permet de récuperer les écouteurs de l'événement appelés à l'ouverture d'une boite dialogue."""
        return self._dialog_closed_all_listener

    # -------------
    # Methods
    # -------------

    def _dialog_closed (self, dialog : AbstractDialog, answer : Any) -> None :
        """Est la méthode appelée par les boite de dialogue quand elle sont fermées."""
        
        if dialog in self._dialogs: 

            self._dialogs.remove(dialog)

            for dialog_listener in self._dialog_closed_listner :
                dialog_listener(dialog, answer)

    def __len__ (self) -> int :
        """Permet de récuperer le nombre de dialogues actuellement affichées."""
        return self._dialogs.__len__()

    def show_dialog (self, name : str, modal : bool, **kwargs) -> None : 
        """Permet d'afficher une nouvelle boite de dialogue."""
        
        dialog = None

        if name == 'library' :
            
            if 'boxes_libraries' in kwargs and 'schedulers_libraries' in kwargs :
            
                if isinstance(kwargs['boxes_libraries'], BoxesLibrariesManager) and isinstance(kwargs['schedulers_libraries'], SchedulersLibraries) :
                    dialog = LibraryDialog(self, kwargs['schedulers_libraries'])

        elif name == 'about' :

            LogManager().error('Not implemented : show about dialog')

        elif name == 'documentation' :

            LogManager().error('Not implemented : show documentation dialog')
            
        elif name == 'new_simulation' : 

            if 'schedulers_libraries' in kwargs :

                if isinstance(kwargs['schedulers_libraries'], SchedulersLibraries) :

                    dialog = NewSimulationDialog(self, kwargs['schedulers_libraries'])

        elif name == 'new_box' :

            LogManager().error('Not implemented : show new box dialog')
            """
            if 'user_data' in kwargs :

                if isinstance(kwargs['user_data'], UserData) :

                    dialog = NewBoxDialog(self, kwargs['user_data'])
            """

        elif name == 'new_scheduler' :

            LogManager().error('Not implemented : show new scheduler dialog')
            """if 'user_data' in kwargs :

                if isinstance(kwargs['user_data'], UserData) :
                    
                    dialog = NewSchedulerDialog(self, kwargs['user_data'])
            """

        elif name == 'simulation_parameters_dialog' : 

            if 'current_simulation' in kwargs and 'schedulers_libraries' in kwargs : 

                if isinstance(kwargs['current_simulation'], SimulationModel) and isinstance(kwargs['schedulers_libraries'], SchedulersLibraries):

                    dialog = SimulationParametersDialog(self, kwargs['current_simulation'], kwargs['schedulers_libraries'])

        if dialog is None: 
            return

        dialog.setModal(modal)

        self._dialogs.append(dialog)
        for dialog_listener in self._dialog_opened_listner :
            dialog_listener(dialog)

        if modal :
            self._dialog_closed(dialog, dialog.exec())
        else :
            dialog.show()

    def close_all (self) -> None :
        """Permet de fermer toutes les boite de dialogue."""

        for dialog in self._dialogs :
            dialog.close()

        for dialog_listener in self._dialog_closed_all_listener:
            dialog_listener(self)