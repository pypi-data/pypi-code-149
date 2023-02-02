from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LastCls:
	"""Last commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("last", core, parent)

	def get_sensor(self) -> int:
		"""SCPI: [SOURce<HW>]:AREGenerator:LAST:SENSor \n
		Snippet: value: int = driver.source.areGenerator.last.get_sensor() \n
		No command help available \n
			:return: areg_last_sensor: integer Range: 0 to 8
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:AREGenerator:LAST:SENSor?')
		return Conversions.str_to_int(response)
