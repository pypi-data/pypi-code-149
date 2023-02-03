#-----------------------------------
# Imports
#-----------------------------------

#-----------------------------------
# Class
#-----------------------------------

from muphyn.packages.interface.models.editable_models.abstract_editable_model import AbstractEditableModel


class AbstractExporter :
    """Est la classe abstraite commune aux classes capables d'exporter des modèles."""

    # -------------
    # Constructors
    # -------------

    def __init__ (self) :
        ...

    # -------------
    # Methods
    # -------------

    def save (self, model : AbstractEditableModel, path : str) -> bool :
        """Est la méthode appelée pour sauvegarder le modèle éditable."""
        raise Exception("AbstractExporter save is an abstract method and must be overloaded.")