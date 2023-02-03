#-----------------------------------
# Class
#-----------------------------------

class AbstractCodeModel :
    """Est la classe abstraite commune aux model des éléments graphique ayant à modifier du code."""

    # -------------
    # Constructors
    # -------------

    def __init__(self, code : str = '') :
        self._code : str = code
        self._base_code : str = code

    # -------------
    # Properties
    # -------------
    
    @property
    def editor_type (self) -> str :
        """Permet de récuperer le type d'éditeur à utiliser."""
        return 'code-editor'

    @property
    def code (self) -> str :
        """Permet de récuperer le code du planificateur en cours de modification."""
        return self._code

    @property
    def is_code_changed (self) -> bool :
        """Permet de savoir si le code en cours est différent du code "non sauvegarder"."""
        return not(self._code == self._base_code)

    # -------------
    # Methods
    # -------------

    def accept_changed (self) -> None :
        """Permet d'accepter les changements du code."""
        self._base_code : str = self._code