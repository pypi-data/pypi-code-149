#-----------------------------------
# Imports
#-----------------------------------

from datetime import date

from muphyn.packages.interface.models.model_signal import ModelSignal

#-----------------------------------
# Class
#-----------------------------------

class AbstractEditableModel :
    """Est la classe abstraite commune aux éléments affichable et modifiable dans l'interface graphique."""

    # -------------
    # Signals
    # -------------

    # -------------
    # Constructors
    # -------------

    def __init__ (self, name : str, path : str, creator : str, date_creation : date, version : float) :

        self._name : str = name
        self._path : str = path
        self._is_unsaved : bool = False

        self.creator = creator
        self.date_creation = date_creation
        self.version = version

        self.name_changed = ModelSignal()
        """Est le signal utilisé quand le modèle voit son nom changer."""

        self.saved_changed = ModelSignal()
        """Est le signal utilisé quand le modèle est sauvegarder."""

        self.selection_changed = ModelSignal()
        """Est le signal utilisé quand le modèle voit sa sélection d'élément modifié."""

    # -------------
    # Properties
    # -------------

    @property
    def name (self) -> str :
        """Permet de récuperer le nom de l'élément mdoifiable."""
        return self._name
    
    @name.setter
    def name (self, name_ : str) -> None :
        """Permet de modifier le nom de l'élément modifiable."""
        self._name : str = name_.__str__()
        self.name_changed.emit(name = self._name)

    @property
    def path (self) -> str :
        """Permet de récuperer le chemin d'accès vers le fichier contenant l'élément modifiable."""
        return self._path

    @path.setter
    def path (self, path_ : str) -> None :
        """Permet de modifier le chemin d'accès vers el fichier contenant l'élément modifiable."""
        self._path : str = path_.__str__()

    @property
    def is_unsaved (self) -> bool :
        """Permet de récuperer l'état de sauvegarde actuel de l'élement modifiable."""
        return self._is_unsaved

    @is_unsaved.setter
    def is_unsaved (self, is_unsaved_ : bool) -> None :
        """Permet de modifier l'état de sauvegarde actuel de l'élément modifiable."""
        self._is_unsaved : bool = is_unsaved_
        self.saved_changed.emit()

    @property
    def creator (self) -> str :
        """Permet de récuperer le nom du créateur."""
        return self._creator

    @creator.setter
    def creator (self, creator_ : str) -> None :
        """Permet de modifier le nom créateur."""
        self._creator : str = creator_ or ''

    @property 
    def date_creation (self) -> date :
        """Permet de récuperer la date à laquelle l'élément a été créé."""
        return self._date_creation

    @date_creation.setter 
    def date_creation (self, date_creation_ : date) -> None : 
        """Permet de modifier la date à laquelle l'élément a été créé."""
        self._date_creation : date = date_creation_

    @property
    def version (self) -> float :
        """Permet de récuperer la version actuelle de l'élément."""
        return self._version

    @version.setter
    def version (self, version_ : float) -> None :
        """Permet de modifier la version actuelle de l'élément."""

        if version_ < 0 :
            return

        self._version : float = version_
        
    # -------------
    # Methods
    # -------------

    def set_path_name (self, path : str = None, name : str = None) -> None :
        """Permet de sauvegarder le modèle dans le dossier/fichier renseigné."""
        self.path = path
        self.name = name