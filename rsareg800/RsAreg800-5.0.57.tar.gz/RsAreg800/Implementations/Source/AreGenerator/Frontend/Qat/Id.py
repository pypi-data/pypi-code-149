from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IdCls:
	"""Id commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("id", core, parent)

	def set(self, areg_fe_id: int, qatFrontent=repcap.QatFrontent.Default) -> None:
		"""SCPI: [SOURce<HW>]:AREGenerator:FRONtend:QAT<CH>:ID \n
		Snippet: driver.source.areGenerator.frontend.qat.id.set(areg_fe_id = 1, qatFrontent = repcap.QatFrontent.Default) \n
		No command help available \n
			:param areg_fe_id: integer Range: 0 to 1000
			:param qatFrontent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Qat')
		"""
		param = Conversions.decimal_value_to_str(areg_fe_id)
		qatFrontent_cmd_val = self._cmd_group.get_repcap_cmd_value(qatFrontent, repcap.QatFrontent)
		self._core.io.write(f'SOURce<HwInstance>:AREGenerator:FRONtend:QAT{qatFrontent_cmd_val}:ID {param}')

	def get(self, qatFrontent=repcap.QatFrontent.Default) -> int:
		"""SCPI: [SOURce<HW>]:AREGenerator:FRONtend:QAT<CH>:ID \n
		Snippet: value: int = driver.source.areGenerator.frontend.qat.id.get(qatFrontent = repcap.QatFrontent.Default) \n
		No command help available \n
			:param qatFrontent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Qat')
			:return: areg_fe_id: integer Range: 0 to 1000"""
		qatFrontent_cmd_val = self._cmd_group.get_repcap_cmd_value(qatFrontent, repcap.QatFrontent)
		response = self._core.io.query_str(f'SOURce<HwInstance>:AREGenerator:FRONtend:QAT{qatFrontent_cmd_val}:ID?')
		return Conversions.str_to_int(response)
