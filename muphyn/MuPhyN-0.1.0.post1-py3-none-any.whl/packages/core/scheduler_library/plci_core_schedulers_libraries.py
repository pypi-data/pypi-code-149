#-----------------------------------
# Imports
#-----------------------------------

from typing import Iterable, List, Dict
from os import listdir, path

from muphyn.packages.core.plci_core_scheduler import Scheduler

from muphyn.packages.core.scheduler_library.scheduler_library_data import SchedulerData
from muphyn.packages.core.scheduler_library.abstract_scheduler_library_importer import AbstractSchedulerLibraryImporter
from muphyn.packages.core.scheduler_library.scheduler_library_importer_1_0_0 import SchedulerLibraryImporter_1_0_0
from muphyn.packages.core.utils.log_manager import LogManager

#-----------------------------------
# Classes
#-----------------------------------

class SchedulerLibraryElement : 
    """Est la classe qui permet de stocker les éléments de bibliothèque pour les planificateurs."""

    # -------------
    # Constructors
    # -------------
    def __init__ (self, path : str) :
        self._path = path
        self._loaded = False
        self._schedulers : Dict[str, SchedulerData] = {}

    # -------------
    # Properties
    # -------------
    
    @property
    def path (self) -> str : 
        """Permet de récuperer le lien vers le dossier de la bibliothèque de planificateurs.""" 
        return self._path

    @property
    def loaded (self) -> bool :
        """Permet de récuperer l'état de chargement de la bibliothèque de planificateurs."""
        return self._loaded

    @property
    def schedulers (self) -> Dict[str, SchedulerData] :
        """Permet de récuperer le dictionnaire des nom de bibliothèque et leur éléments de création de planificateurs."""
        return self._schedulers

    # -------------
    # Methods
    # -------------

    def load (self, scheduler_importer : AbstractSchedulerLibraryImporter) :
        """Permet de charger la bibliothèque."""
        for f in listdir(self.path) :

            if f.endswith('.yaml') :

                file_name = f.split('.')[0]
                absolute_yaml_file = self.path + '/' + file_name + '.yaml'

                imported_scheduler = scheduler_importer.import_scheduler_data(self.path, file_name, absolute_yaml_file, self._schedulers)

                if imported_scheduler is None :
                    continue

                if imported_scheduler['scheduler_data'] is None :
                    continue
                    
                self._schedulers[imported_scheduler['library_name']] = imported_scheduler['scheduler_data']

                        

class SchedulersLibraries :
    """Est la classe qui permet de construire les planificateurs.""" 

    # -------------
    # Constructors
    # -------------
    def __init__ (self) :
        self._libraries : List[SchedulerLibraryElement] = []
        self._scheduler_importer : AbstractSchedulerLibraryImporter = SchedulerLibraryImporter_1_0_0()
    
    # -------------
    # Properties
    # -------------

    @property
    def libraries (self) -> List[SchedulerLibraryElement] :
        """Permet de retourner la liste des libraries."""
        return self._libraries

    @property
    def schedulers (self) -> Iterable[SchedulerData] :
        """Permet de retourner la liste des planificateur de toutes les bibliothèques."""
        for schedulers_library in self.libraries :
            for scheduler_name in schedulers_library.schedulers :
                yield schedulers_library.schedulers[scheduler_name]
        
    @property 
    def scheduler_importer (self) -> AbstractSchedulerLibraryImporter :
        """Permet de retourner l'importeur de planificateurs.""" 
        return self._scheduler_importer

    # -------------
    # Methods
    # -------------
    def add_library (self, library_folder : str) :
        """Permet d'ajouter une bibliothèque dans le répertoire des bibliothèque."""

        # Test if library_folder path format is string 
        if not (isinstance(library_folder, str)) :
            LogManager().error(f"Wrong path variable format {type(library_folder)} instead of str")
            return False

        # Test if library folder path exists
        if not path.exists(library_folder):
            LogManager().error(f"Path doesn't exist : {library_folder}")
            return False

        # Check if library has already been added
        if any(libraryElement.path == library_folder for libraryElement in self._libraries):
            LogManager().info(f"Library has already been added : {library_folder}")
            return False

        # Append Scheduler Library
        self._libraries.append(SchedulerLibraryElement(library_folder))

        return True

    def load_libraries (self) :
        """Permet de charger toutes les bibliothèques du répertoire."""

        for libraryElement in self._libraries :

            if not libraryElement.loaded :
                libraryElement.load(self.scheduler_importer)

    def construct_scheduler (self, scheduler_library : str, scheduler_name : str) -> Scheduler:
        """Permet de construire un scheduler suivant son nom et sa librairie."""

        if not (isinstance(scheduler_library, str) and isinstance(scheduler_name, str)) :
            return None

        scheduler_access = self._name_library(scheduler_library, scheduler_name)

        for libraryElement in self._libraries :
            
            if scheduler_access in libraryElement.schedulers :
                return libraryElement.schedulers[scheduler_access].construct_scheduler()

    def _name_library (self, scheduler_library : str, schdeuler_name : str) -> str :
        """Permet de rassembler le nom et la libraire en un seul string."""
        return scheduler_library + "." + schdeuler_name

    def clear (self) -> None :
        """Permet d'éffacer le contenu des solveurs chargées."""
        for libraryElement in self._libraries :
            del libraryElement
        
        del self._libraries
        self._libraries : List[SchedulerLibraryElement] = []