from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StatusCls:
	"""Status commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("status", core, parent)

	# noinspection PyTypeChecker
	def get(self, qatFrontent=repcap.QatFrontent.Default) -> enums.AregFeQatConnMode:
		"""SCPI: [SOURce<HW>]:AREGenerator:FRONtend:QAT<CH>:STATus \n
		Snippet: value: enums.AregFeQatConnMode = driver.source.areGenerator.frontend.qat.status.get(qatFrontent = repcap.QatFrontent.Default) \n
		No command help available \n
			:param qatFrontent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Qat')
			:return: areg_fe_qat_status: DISConnected| DIALing| CONNected| CERRor| UPDate| UERRor"""
		qatFrontent_cmd_val = self._cmd_group.get_repcap_cmd_value(qatFrontent, repcap.QatFrontent)
		response = self._core.io.query_str(f'SOURce<HwInstance>:AREGenerator:FRONtend:QAT{qatFrontent_cmd_val}:STATus?')
		return Conversions.str_to_scalar_enum(response, enums.AregFeQatConnMode)
