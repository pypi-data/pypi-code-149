
from PyQt5.QtWidgets import QLabel, QTabWidget
from muphyn.packages.interface.editors.abstract_editor import AbstractEditor
from muphyn.packages.interface.graphical_actions.actions_holder import ActionsHolder
from muphyn.packages.interface.models.editable_models.abstract_code_model import AbstractCodeModel


class CodeEditor (AbstractEditor) :
    
    def __init__(self, tab_holder : QTabWidget, code_model : AbstractCodeModel, actions_holder : ActionsHolder) :
        AbstractEditor.__init__(self, tab_holder, code_model, actions_holder)
        
        self.lbl : QLabel = QLabel(self)
        self.lbl.setText('code editor')