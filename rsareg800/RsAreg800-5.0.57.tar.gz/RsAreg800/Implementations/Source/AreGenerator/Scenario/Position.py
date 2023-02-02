from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PositionCls:
	"""Position commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("position", core, parent)

	def get_actual(self) -> int:
		"""SCPI: [SOURce<HW>]:AREGenerator:SCENario:POSition:ACTual \n
		Snippet: value: int = driver.source.areGenerator.scenario.position.get_actual() \n
		No command help available \n
			:return: scen_act_pos: integer Range: 0 to 1E9
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:AREGenerator:SCENario:POSition:ACTual?')
		return Conversions.str_to_int(response)

	def get_start(self) -> int:
		"""SCPI: [SOURce<HW>]:AREGenerator:SCENario:POSition:STARt \n
		Snippet: value: int = driver.source.areGenerator.scenario.position.get_start() \n
		No command help available \n
			:return: scen_start_pos: integer Range: 0 to 1E9
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:AREGenerator:SCENario:POSition:STARt?')
		return Conversions.str_to_int(response)

	def set_start(self, scen_start_pos: int) -> None:
		"""SCPI: [SOURce<HW>]:AREGenerator:SCENario:POSition:STARt \n
		Snippet: driver.source.areGenerator.scenario.position.set_start(scen_start_pos = 1) \n
		No command help available \n
			:param scen_start_pos: integer Range: 0 to 1E9
		"""
		param = Conversions.decimal_value_to_str(scen_start_pos)
		self._core.io.write(f'SOURce<HwInstance>:AREGenerator:SCENario:POSition:STARt {param}')

	def get_stop(self) -> int:
		"""SCPI: [SOURce<HW>]:AREGenerator:SCENario:POSition:STOP \n
		Snippet: value: int = driver.source.areGenerator.scenario.position.get_stop() \n
		No command help available \n
			:return: scen_stop_pos: integer Range: 0 to 1E9
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:AREGenerator:SCENario:POSition:STOP?')
		return Conversions.str_to_int(response)

	def set_stop(self, scen_stop_pos: int) -> None:
		"""SCPI: [SOURce<HW>]:AREGenerator:SCENario:POSition:STOP \n
		Snippet: driver.source.areGenerator.scenario.position.set_stop(scen_stop_pos = 1) \n
		No command help available \n
			:param scen_stop_pos: integer Range: 0 to 1E9
		"""
		param = Conversions.decimal_value_to_str(scen_stop_pos)
		self._core.io.write(f'SOURce<HwInstance>:AREGenerator:SCENario:POSition:STOP {param}')
