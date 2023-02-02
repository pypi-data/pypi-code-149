from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class HilCls:
	"""Hil commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("hil", core, parent)

	def get_rate(self) -> float:
		"""SCPI: [SOURce<HW>]:AREGenerator:HIL:RATE \n
		Snippet: value: float = driver.source.areGenerator.hil.get_rate() \n
		No command help available \n
			:return: hil: float Range: 0 to 1E9
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:AREGenerator:HIL:RATE?')
		return Conversions.str_to_float(response)

	# noinspection PyTypeChecker
	def get_received(self) -> enums.HilDataReceive:
		"""SCPI: [SOURce<HW>]:AREGenerator:HIL:RECeived \n
		Snippet: value: enums.HilDataReceive = driver.source.areGenerator.hil.get_received() \n
		No command help available \n
			:return: hil_data_received: NOData| RECeived| NOTHil
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:AREGenerator:HIL:RECeived?')
		return Conversions.str_to_scalar_enum(response, enums.HilDataReceive)

	def set_received(self, hil_data_received: enums.HilDataReceive) -> None:
		"""SCPI: [SOURce<HW>]:AREGenerator:HIL:RECeived \n
		Snippet: driver.source.areGenerator.hil.set_received(hil_data_received = enums.HilDataReceive.NOData) \n
		No command help available \n
			:param hil_data_received: NOData| RECeived| NOTHil
		"""
		param = Conversions.enum_scalar_to_str(hil_data_received, enums.HilDataReceive)
		self._core.io.write(f'SOURce<HwInstance>:AREGenerator:HIL:RECeived {param}')
