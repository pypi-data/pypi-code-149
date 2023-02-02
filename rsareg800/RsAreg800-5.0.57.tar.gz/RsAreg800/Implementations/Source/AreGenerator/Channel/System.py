from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SystemCls:
	"""System commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("system", core, parent)

	# noinspection PyTypeChecker
	def get_alignment(self) -> enums.AregCconfigSystAlign:
		"""SCPI: [SOURce<HW>]:AREGenerator:CHANnel:System:ALIGnment \n
		Snippet: value: enums.AregCconfigSystAlign = driver.source.areGenerator.channel.system.get_alignment() \n
		No command help available \n
			:return: syst_align: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:AREGenerator:CHANnel:System:ALIGnment?')
		return Conversions.str_to_scalar_enum(response, enums.AregCconfigSystAlign)

	def set_alignment(self, syst_align: enums.AregCconfigSystAlign) -> None:
		"""SCPI: [SOURce<HW>]:AREGenerator:CHANnel:System:ALIGnment \n
		Snippet: driver.source.areGenerator.channel.system.set_alignment(syst_align = enums.AregCconfigSystAlign.OFF) \n
		No command help available \n
			:param syst_align: No help available
		"""
		param = Conversions.enum_scalar_to_str(syst_align, enums.AregCconfigSystAlign)
		self._core.io.write(f'SOURce<HwInstance>:AREGenerator:CHANnel:System:ALIGnment {param}')
