"""
This module contains configuration of the members which should in-/excluded in sphinx
(see :event:`autodoc-skip-member`)
"""
INCLUDE_MEMBERS: set[str] = set()
EXCLUDE_MEMBERS: set[str] = {"Meta", "validate"}
