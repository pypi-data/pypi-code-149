#-----------------------------------
# Imports
#-----------------------------------

import os
import yaml
from typing import List, Any, Dict

from muphyn.packages.interface.models.links_model.link_type import LinkType, get_link_type

#-----------------------------------
# Class
#-----------------------------------

class UserData :
    """Sont les données utilisateurs."""

    # -------------
    # Constructors
    # -------------

    def __init__ (self, path : str) :
        
        self._path : str = path
        self._boxes_libraries : List[str] = []
        self._schedulers_libraries : List[str] = []
        self._user_name : str = 'No name'
        self._recent_files : List[str] = []
        self._lang : str = 'french'
        self._theme : str = 'light'
        self._grid_type : str = 'dots'
        self._attach_box_to_grid : bool = False
        self._grid_spacing : int = 5
        self._default_link_type : LinkType = LinkType.SQUARE
        self._default_link_curving : float = 5

    # -------------
    # Properties
    # -------------

    @property
    def boxes_libraries (self) -> List[str] :
        """Permet de récuperer la liste des bibliothèques de boxes que l'utilisateur souhaite utiliser."""
        return self._boxes_libraries

    @property
    def schedulers_libraries (self) -> List[str] :
        """Permet de récuperer la liste des bibliothèques de planificateurs que l'utilisateur souhaite utiliser."""
        return self._schedulers_libraries

    @property
    def user_name (self) -> str :
        """Permet de récuperer le nom d'utilisateur."""
        return self._user_name

    @user_name.setter
    def user_name (self, new_name : str) -> None :
        """Permet de modifier le nom d'utilisateur."""
        if new_name is None : 
            return

        if new_name == '' :
            return

        self._user_name : str = new_name

    @property
    def path (self) -> str :
        """Permet de récuperer le chemin vers le fichier dans lequel il faut lire et sauvegarder les données utilisateur."""
        return self._path

    @path.setter
    def file (self, path_ : str) -> None :
        """Permet de modifier le chemin vers le fichier dans lequel il faut lire et sauvegarder les données utilisateur."""
        if path_ is None : 
            return

        if path_ == '' :
            return

        self._path : str = path_
        

    @property
    def recent_files (self) -> List[str] :
        """Permet de récuperer les fichiers récement ouverts."""
        return self._recent_files

    @property
    def language (self) -> str : 
        """Permet de récuperer le language dans lequel l'utilisateur veut voir l'interface."""
        return self._lang

    @language.setter
    def language (self, lang_ : str) -> None :
        """Permet de modifier la langue dans laquelle l'utilisateur veut voir l'interface."""
        if lang_ is None:
            return

        if lang_ == '':
            return

        self._lang = lang_
        
    @property
    def theme (self) -> str:
        """Permet de récuperer le thème dans lequel l'utilisateur veut voir l'interface."""
        return self._theme

    @theme.setter
    def theme (self, theme_ : str) -> None :
        """Permet de modifier le thème dans lequel l'utilisateur veut voir l'interface."""
        if theme_ is None:
            return

        if theme_ == '':
            return

        self._theme = theme_

    @property
    def grid_type (self) -> str:
        """Permet de récuperer le type dans lequel il faut que la grille de l'éditeur s'affiche."""
        return self._grid_type

    @grid_type.setter
    def grid_type (self, grid_type_ : str) -> None :
        """Permet de modifier le type dans lequel il faut que la grille de l'éditeur s'affiche."""
        if grid_type_ is None:
            return

        if grid_type_ == '':
            return

        self._grid_type = grid_type_

    @property
    def attach_box_to_grid (self) -> bool :
        """Permet de récuperer la variable décrivant si les boxes sont attachées à la grille ou pas."""
        return self._attach_box_to_grid

    @attach_box_to_grid.setter
    def attach_box_to_grid (self, attach_box_to_grid_ : bool) -> None :
        """Permet de modifier la variable décrivant si les boxes sont attachées à la grille ou pas."""
        self._attach_box_to_grid : bool = attach_box_to_grid_

    @property
    def grid_spacing (self) -> int :
        """Permet de récuperer l'espacement de la grille."""
        return self._grid_spacing
    
    @grid_spacing.setter 
    def grid_spacing (self, grid_spacing_ : int) -> None :
        """Permet de modifier l'espacement de la grille."""
        if grid_spacing_ < 1 :
            return 

        self._grid_spacing : int = grid_spacing_

    @property
    def default_link_type (self) -> LinkType :
        """Permet de récuperer le type de liens entre les boxes par défaut."""
        return self._default_link_type

    @default_link_type.setter 
    def default_link_type (self, default_link_type_ : LinkType) -> None :
        """Permet de modifier le type de liens entre les boxes par défaut."""

        if default_link_type_ is None:
            return

        self._default_link_type = default_link_type_

    @property
    def default_link_curving (self) -> float :
        """Permet de récuperer la courbure par défaut des liens courbes."""
        return self._default_link_curving

    @default_link_curving.setter
    def default_link_curving (self, default_link_curving_ : float) -> None :
        """Permet de modifier la courbure par défaut des liens courbes."""
        if default_link_curving_ < 0 :
            return

        self._default_link_curving : float = default_link_curving_

    # -------------
    # Methods
    # -------------

    def save (self) :
        """Est la méthode pour sauvegarder les données utilisateur."""

        to_save : Dict[str, Any] = {}
        to_save['version'] = 1.0
        to_save['user_name'] = self._user_name
        to_save['boxes_libraries'] = self._boxes_libraries
        to_save['schedulers_libraries'] = self._schedulers_libraries
        to_save['recent_files'] = self._recent_files
        to_save['lang'] = self._lang
        to_save['theme'] = self._theme
        to_save['grid_type'] = self._grid_type
        to_save['attach_box_to_grid'] = self._attach_box_to_grid
        to_save['grid_spacing'] = self._grid_spacing
        to_save['default_link_type'] = self._default_link_type.__str__()
        to_save['default_link_curving'] = self._default_link_curving

        with open(self._path, 'w') as file:
            yaml.dump(to_save, file)

    def load (self) :
        """Est la méthode pour charger les données utilisateur."""

        if os.path.isfile(self._path) :
            
            with open(self._path, 'r') as file:
                document = yaml.full_load(file)

                if document['version'] == 1.0 :
                    self._user_name = document['user_name']
                    self._boxes_libraries = document['boxes_libraries']
                    self._schedulers_libraries = document['schedulers_libraries']
                    self._recent_files = document['recent_files']
                    self._lang = document['lang']
                    self._theme = document['theme']
                    self._grid_type = document['grid_type']
                    self._attach_box_to_grid = document['attach_box_to_grid']
                    self._grid_spacing = document['grid_spacing']
                    self._default_link_type = get_link_type(document['default_link_type'])
                    self._default_link_curving = document['default_link_curving']

        