#-----------------------------------
# Imports
#-----------------------------------

# Project Imports
from muphyn.packages.core.utils.log_manager import LogManager
from muphyn.packages.interface.graphical_actions.abstract_unique_element_diagram_action import AbstractUniqueElementDiagramAction
from muphyn.packages.interface.models.graphical_models.abstract_graphical_element import AbstractGraphicalElement
from muphyn.packages.interface.models.graphical_models.box_model import BoxModel
from muphyn.packages.interface.models.links_model.abstract_link_model import AbstractLinkModel

#-----------------------------------
# Class
#-----------------------------------

class DiagramChangeElementParamsAction (AbstractUniqueElementDiagramAction) :
    """Est l'action capable de modifier les paramètres d'un élément."""

    # -------------
    # Constructors
    # -------------

    def __init__ (self, graphical_element : AbstractGraphicalElement, param_name : str, new_param_value : object, old_param_value : object) :
        
        AbstractUniqueElementDiagramAction.__init__(self, graphical_element)
        
        self._param_name = param_name
        self._old_param_value = old_param_value
        self._new_param_value = new_param_value

    # -------------
    # Properties
    # -------------

    @property
    def param_name (self) -> str : 
        """Permet de récuperer le nom du paramètre à modifier."""
        return self._param_name

    @property
    def old_param_value (self) -> object :
        """Permet de récuperer la valeur du paramètre avant modification."""
        return self._old_param_value

    @property
    def new_param_value (self) -> object :
        """Permet de récuperer la valeur du paramètre par lequel modifier le nouveau paramètre."""
        return self._new_param_value

    @new_param_value.setter
    def new_param_value (self, new_param_value_ : object) -> None :
        """Permet de modifier la valeur du paramètre par lequel modifier le nouveau paramètre."""

        if new_param_value_ is None : 
            return

        self._new_param_value = new_param_value_

    # -------------
    # Methods
    # -------------

    def do (self) :

        graphical_element = self.graphical_element

        if graphical_element is None : 
            return

        if self.param_name == 'text' :
            graphical_element.text = self.new_param_value 

        elif self.param_name == 'name' :
            graphical_element.name = self.new_param_value

        elif self.param_name == 'color' :
            graphical_element.color = self.new_param_value

        elif self.param_name == 'link_value' :

            if isinstance(graphical_element, AbstractLinkModel) :
                graphical_element.link_value = self.new_param_value
                LogManager().debug(f'-> redo link value : {self.old_param_value} -> {self.new_param_value}')
                graphical_element.self_update()
            else:
                LogManager().error('-> element is not a link')

        elif self.param_name == 'link_type' :
            
            if isinstance(graphical_element, AbstractLinkModel) :
                graphical_element.link_type = self.new_param_value
                LogManager().debug(f'-> redo link value : {self.old_param_value} -> {self.new_param_value}')
                graphical_element.self_update()
            else:
                LogManager().error('-> element is not a link')

        elif self.param_name == 'library' :

            if isinstance(graphical_element, BoxModel) :
                graphical_element.library = self.new_param_value

        elif self.param_name.startswith('params.') :
            
            if isinstance(graphical_element, BoxModel) : 
                graphical_element.set_parameter(self.param_name.split('.')[1], self.new_param_value)
        
        graphical_element.update(graphical_element.boundingRect())

    def undo (self) :

        graphical_element = self.graphical_element

        if graphical_element is None : 
            return
                
        if self.param_name == 'text' :
            graphical_element.text = self.old_param_value 

        elif self.param_name == 'name' :
            graphical_element.name = self.old_param_value

        elif self.param_name == 'color' :
            graphical_element.color = self.old_param_value

        elif self.param_name == 'link_value' :
            
            if isinstance(graphical_element, AbstractLinkModel) :
                graphical_element.link_value = self.old_param_value
                LogManager().debug(f'-> redo link value : {self.new_param_value} -> {self.old_param_value}')
                graphical_element.self_update()

        elif self.param_name == 'link_type' :
            
            if isinstance(graphical_element, AbstractLinkModel) :
                graphical_element.link_type = self.old_param_value
                LogManager().debug(f'-> redo link value : {self.new_param_value} -> {self.old_param_value}')
                graphical_element.self_update()

        elif self.param_name == 'library' :

            if isinstance(graphical_element, BoxModel) :
                graphical_element.library = self.old_param_value

        elif self.param_name.startswith('params.') :
            
            if isinstance(graphical_element, BoxModel) : 
                graphical_element.set_parameter(self.param_name.split('.')[1], self.old_param_value)

        graphical_element.update(graphical_element.boundingRect())