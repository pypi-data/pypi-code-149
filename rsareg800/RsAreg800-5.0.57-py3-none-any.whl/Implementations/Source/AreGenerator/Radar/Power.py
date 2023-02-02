from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PowerCls:
	"""Power commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("power", core, parent)

	# noinspection PyTypeChecker
	def get_indicator(self) -> enums.AregRadarPowIndicator:
		"""SCPI: [SOURce<HW>]:AREGenerator:RADar:POWer:INDicator \n
		Snippet: value: enums.AregRadarPowIndicator = driver.source.areGenerator.radar.power.get_indicator() \n
		No command help available \n
			:return: pow_indicator: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:AREGenerator:RADar:POWer:INDicator?')
		return Conversions.str_to_scalar_enum(response, enums.AregRadarPowIndicator)
