#-----------------------------------
# Imports
#-----------------------------------

# PyQt5 Imports
from PyQt5.QtCore import QObject, QPointF, QSizeF, pyqtSignal
from PyQt5.QtWidgets import QGraphicsItem, QGraphicsSceneMouseEvent

# Project Imports
from muphyn.packages.interface.shapes.basic_shape.grouped_shapes import GroupedShapes

#-----------------------------------
# Class
#-----------------------------------
class AbstractGraphicalElement (GroupedShapes) :
    """Est la classe abstraite commune aux éléments graphiques affichés dans l'interface."""

    # -------------
    # Static Element
    # -------------

    GRAPHICAL_INDEX : int = 0
    
    # -------------
    # Signals
    # -------------

    param_changed = pyqtSignal(object, str, object, object)
    """
    Params : 
    - *object [AbstractGraphicalElement]* model
    - *str* param name
    - *object* old value
    - *object* new value
    """

    # -------------
    # Constructors
    # -------------

    def __init__ (self, name : str, position : QPointF, rotation : float = 0, text : str = '', parent : QGraphicsItem = None) :
        
        # Init Inherited class
        GroupedShapes.__init__(self, position, parent)

        # Set Graphical Index
        self._graphical_index = AbstractGraphicalElement.GRAPHICAL_INDEX
        AbstractGraphicalElement.GRAPHICAL_INDEX += 1

        # Init Action Semaphore
        self._action_size_semaphore : bool = True 
        self._action_pos_semaphore : bool = True
        self._action_rot_semaphore : bool = True
        self._action_param_semaphore : bool = True

        # Init Item Parameters
        self._name : str = name
        self._text = text

        self.setRotation(rotation)
        
    # -------------
    # Properties
    # -------------

    @property
    def graphical_index (self) -> int :
        """
        Permet de récuperer l'index graphique.
        Cet index est utilisé pour référencé les objets pour les actions.
        Il permet de retenir quel élément est quel élément peut importe l'ordre des graphical elements dans le diagram.
        Il n'est pas nécessaire de le sauvegarder dans un fichier. Les actions ne portent que sur les éléments actuellement dans l'interface.
        """
        return self._graphical_index

    @graphical_index.setter
    def graphical_index (self, new_graphical_index_ : int) -> None : 
        """Permet de modifier l'index graphique."""

        if new_graphical_index_ >= 0 and new_graphical_index_ != self._graphical_index :
            self._graphical_index = new_graphical_index_

    @property
    def name (self) -> str :
        """Permet de récuperer le nom de l'élément."""
        return self._name

    @name.setter
    def name (self, new_name : str) -> None :
        """Permet de modifier le nom de l'élément."""
        if new_name != self._name:
            self._name = new_name

    @property
    def position (self) -> QPointF :
        """Permet de récuperer la position de l'élément graphique."""
        return self.pos()

    @position.setter
    def position (self, new_position : QPointF) -> None :
        """Permet de modifier la position de l'élement graphique."""
        if new_position != self.pos():
            self.setPos(new_position) 

    @property
    def size (self) -> QSizeF :
        """Permet de récuperer la taille de l'élement graphique."""
        return self.boundingRect().size()

    @property
    def rot (self) -> float :
        """Permet de récuperer la rotation de la box."""
        return self.rotation()

    @rot.setter
    def rot (self, new_rot : float) -> None :
        """Permet de modifier la rotation de la box."""
        if new_rot != self.rotation():
            self.setRotation(new_rot)

    @property 
    def text (self) -> str :
        """Permet de récuperer le texte à afficher."""
        return self._text

    @text.setter
    def text (self, new_text: str) -> None :
        """Permet de modifier le texte à afficher."""

        if new_text != self._text:
            old_text = self._text
            self._text = new_text or '' 

            if self.action_param_semaphore :
                return

            self.param_changed.emit(self, 'text', old_text, self._text)
        
    @property
    def rendered_text (self) -> str :
        """Permet de récuperer le texte à afficher."""

        if self._text is None : 
            return self._name

        if self._text.strip().__len__() == 0 :
            return self._name

        return self._text

    @rendered_text.setter
    def rendered_text (self, new_rendered_text : str) -> None :
        """Permet de modifier le texte à afficher."""
        self.text = new_rendered_text

    @property
    def diagram_model (self) :
        """Permet de récuperer l'éditeur visuel."""
        return self._diagram_model

    @diagram_model.setter
    def diagram_model (self, diagram_model_) -> None :
        """Permet de modifier l'éditeur visuel."""
        self._diagram_model = diagram_model_

        if self._diagram_model is None :
            self._action_size_semaphore : bool = True 
            self._action_pos_semaphore : bool = True
            self._action_rot_semaphore : bool = True
            self._action_param_semaphore : bool = True
        
        else : 
            self._action_size_semaphore : bool = False 
            self._action_pos_semaphore : bool = False
            self._action_rot_semaphore : bool = False
            self._action_param_semaphore : bool = False

    @property
    def action_size_semaphore (self) -> bool :
        """Permet de récuperer l'état du sémpahore pour le changement de taille de l'objet."""
        return self._action_size_semaphore

    @action_size_semaphore.setter 
    def action_size_semaphore (self, action_size_semaphore_ : bool) :
        """Permet de modifier l'état du sémaphore pour le changement de taille de l'objet."""
        self._action_size_semaphore = action_size_semaphore_

    @property
    def action_pos_semaphore (self) -> bool :
        """Permet de récuperer l'état du sémpahore pour le changement de position de l'objet."""
        return self._action_pos_semaphore

    @action_pos_semaphore.setter 
    def action_pos_semaphore (self, action_pos_semaphore_ : bool) :
        """Permet de modifier l'état du sémaphore pour le changement de position de l'objet."""
        self._action_pos_semaphore = action_pos_semaphore_

    @property
    def action_rot_semaphore (self) -> bool :
        """Permet de récuperer l'état du sémpahore pour le changement de rotation de l'objet."""
        return self._action_rot_semaphore

    @action_rot_semaphore.setter 
    def action_rot_semaphore (self, action_rot_semaphore_ : bool) :
        """Permet de modifier l'état du sémaphore pour le changement de rotation de l'objet."""
        self._action_rot_semaphore = action_rot_semaphore_

    @property
    def action_param_semaphore (self) -> bool :
        """Permet de récuperer le sémaphore pour les paramètres de l'objet."""
        return self._action_param_semaphore

    @action_param_semaphore.setter
    def action_param_semaphore (self, action_param_semaphore_ : bool) -> None :
        """Permet de modifier le sémaphore pour les paramètres de l'objet."""
        self._action_param_semaphore = action_param_semaphore_

    # -------------
    # Methods
    # -------------
    def mouseDoubleClickEvent(self, event: QGraphicsSceneMouseEvent) -> None:
        return super().mouseDoubleClickEvent(event)


    def parent(self) -> QObject:
        parent = super().parent()
        return parent if parent is not None else self.parentItem()