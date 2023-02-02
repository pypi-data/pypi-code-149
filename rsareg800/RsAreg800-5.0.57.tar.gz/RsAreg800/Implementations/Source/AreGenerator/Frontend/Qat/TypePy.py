from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TypePyCls:
	"""TypePy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("typePy", core, parent)

	def set(self, areg_fconf_type: enums.AregFeType, qatFrontent=repcap.QatFrontent.Default) -> None:
		"""SCPI: [SOURce<HW>]:AREGenerator:FRONtend:QAT<CH>:TYPE \n
		Snippet: driver.source.areGenerator.frontend.qat.typePy.set(areg_fconf_type = enums.AregFeType.NONE, qatFrontent = repcap.QatFrontent.Default) \n
		No command help available \n
			:param areg_fconf_type: TRX| QAT| NONE
			:param qatFrontent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Qat')
		"""
		param = Conversions.enum_scalar_to_str(areg_fconf_type, enums.AregFeType)
		qatFrontent_cmd_val = self._cmd_group.get_repcap_cmd_value(qatFrontent, repcap.QatFrontent)
		self._core.io.write(f'SOURce<HwInstance>:AREGenerator:FRONtend:QAT{qatFrontent_cmd_val}:TYPE {param}')

	# noinspection PyTypeChecker
	def get(self, qatFrontent=repcap.QatFrontent.Default) -> enums.AregFeType:
		"""SCPI: [SOURce<HW>]:AREGenerator:FRONtend:QAT<CH>:TYPE \n
		Snippet: value: enums.AregFeType = driver.source.areGenerator.frontend.qat.typePy.get(qatFrontent = repcap.QatFrontent.Default) \n
		No command help available \n
			:param qatFrontent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Qat')
			:return: areg_fconf_type: TRX| QAT| NONE"""
		qatFrontent_cmd_val = self._cmd_group.get_repcap_cmd_value(qatFrontent, repcap.QatFrontent)
		response = self._core.io.query_str(f'SOURce<HwInstance>:AREGenerator:FRONtend:QAT{qatFrontent_cmd_val}:TYPE?')
		return Conversions.str_to_scalar_enum(response, enums.AregFeType)
