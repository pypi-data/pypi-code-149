from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ValidCls:
	"""Valid commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("valid", core, parent)

	def get_catalog(self) -> List[str]:
		"""SCPI: [SOURce<HW>]:AREGenerator:OBJects:VALid:CATalog \n
		Snippet: value: List[str] = driver.source.areGenerator.objects.valid.get_catalog() \n
		No command help available \n
			:return: areg_obj_valid_cat: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:AREGenerator:OBJects:VALid:CATalog?')
		return Conversions.str_to_str_list(response)
