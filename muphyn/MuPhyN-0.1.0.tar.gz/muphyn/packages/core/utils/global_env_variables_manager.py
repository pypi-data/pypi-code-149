#-----------------------------------
# Imports
#-----------------------------------
from muphyn.packages.core.utils.singleton import SingletonMetaClass


class GlobalEnvVariablesManager(metaclass=SingletonMetaClass) :
    """Est la classe qui permet de construire les boxes.""" 

    # -------------
    # Constructors
    # -------------
    def __init__ (self, global_vars: dict) :
        self.global_vars: dict = global_vars