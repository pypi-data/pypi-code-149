from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LastCls:
	"""Last commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("last", core, parent)

	def get_qat(self) -> int:
		"""SCPI: [SOURce<HW>]:AREGenerator:FRONtend:LAST:QAT \n
		Snippet: value: int = driver.source.areGenerator.frontend.last.get_qat() \n
		No command help available \n
			:return: areg_fe_last_add_qa: integer Range: 0 to 12
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:AREGenerator:FRONtend:LAST:QAT?')
		return Conversions.str_to_int(response)
