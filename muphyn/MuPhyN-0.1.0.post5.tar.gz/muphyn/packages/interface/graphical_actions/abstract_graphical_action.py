#-----------------------------------
# Imports
#-----------------------------------

#-----------------------------------
# Class
#-----------------------------------

class AbstractGraphicalAction :
    """Est une la classe abstraite permettant de faire et défaire des actions graphiques."""
    
    # -------------
    # Constructors
    # -------------

    def __init__ (self) :
        ...

    # -------------
    # Methods
    # -------------

    def do (self) :
        """Permet de réaliser l'action."""
        raise('AbstractGraphicalAction.do mathod is abstract and must be overhidden.')

    def undo (self) :
        """Permet de défaire l'action."""
        raise('AbstractGraphicalAction.undo mathod is abstract and must be overhidden.')