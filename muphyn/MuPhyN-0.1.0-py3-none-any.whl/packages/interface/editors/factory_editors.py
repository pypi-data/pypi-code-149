#-----------------------------------
# Imports
#-----------------------------------

from PyQt5.QtWidgets import QLabel, QTabWidget
from muphyn.packages.interface.editors.abstract_editor import AbstractEditor
from muphyn.packages.interface.editors.code_editor import CodeEditor
from muphyn.packages.interface.editors.multi_physics_diagram_editor import MultiPhysicsDiagramEditor
from muphyn.packages.interface.graphical_actions.actions_holder import ActionsHolder
from muphyn.packages.interface.models.editable_models.abstract_code_model import AbstractCodeModel
from muphyn.packages.interface.models.editable_models.abstract_diagram_model import AbstractDiagramModel
from muphyn.packages.interface.models.editable_models.abstract_editable_model import AbstractEditableModel
from muphyn.packages.interface.editors.diagram_editor import DiagramEditor

#-----------------------------------
# Functions
#-----------------------------------

def factory_editors (tab_holder : QTabWidget, editable_model : AbstractEditableModel) -> AbstractEditor :
    
    if hasattr(editable_model, 'editor_type') :

        if editable_model.editor_type == 'code-editor' :
            return CodeEditor(tab_holder, editable_model, ActionsHolder())
        
        elif editable_model.editor_type == 'diagram-editor' :
            return DiagramEditor(tab_holder, editable_model, ActionsHolder())

        elif editable_model.editor_type == 'multiphysics-editor' :
            return MultiPhysicsDiagramEditor(tab_holder, editable_model, ActionsHolder())

    lbl : QLabel = QLabel(tab_holder)
    lbl.setText('No editor')
    return lbl