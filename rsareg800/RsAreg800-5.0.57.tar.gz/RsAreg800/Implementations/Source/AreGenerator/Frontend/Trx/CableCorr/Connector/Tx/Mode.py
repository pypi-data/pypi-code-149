from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ModeCls:
	"""Mode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mode", core, parent)

	def set(self, areg_cabel_cor_mod: enums.AregCableCorrSour, trxFrontent=repcap.TrxFrontent.Default, connector=repcap.Connector.Default, txIndexNull=repcap.TxIndexNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:AREGenerator:FRONtend:TRX<CH>:CABLecorr:CONNector<DI>:TX<ST0>:MODE \n
		Snippet: driver.source.areGenerator.frontend.trx.cableCorr.connector.tx.mode.set(areg_cabel_cor_mod = enums.AregCableCorrSour.S2P, trxFrontent = repcap.TrxFrontent.Default, connector = repcap.Connector.Default, txIndexNull = repcap.TxIndexNull.Default) \n
		No command help available \n
			:param areg_cabel_cor_mod: USER| S2P
			:param trxFrontent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Trx')
			:param connector: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Connector')
			:param txIndexNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Tx')
		"""
		param = Conversions.enum_scalar_to_str(areg_cabel_cor_mod, enums.AregCableCorrSour)
		trxFrontent_cmd_val = self._cmd_group.get_repcap_cmd_value(trxFrontent, repcap.TrxFrontent)
		connector_cmd_val = self._cmd_group.get_repcap_cmd_value(connector, repcap.Connector)
		txIndexNull_cmd_val = self._cmd_group.get_repcap_cmd_value(txIndexNull, repcap.TxIndexNull)
		self._core.io.write(f'SOURce<HwInstance>:AREGenerator:FRONtend:TRX{trxFrontent_cmd_val}:CABLecorr:CONNector{connector_cmd_val}:TX{txIndexNull_cmd_val}:MODE {param}')

	# noinspection PyTypeChecker
	def get(self, trxFrontent=repcap.TrxFrontent.Default, connector=repcap.Connector.Default, txIndexNull=repcap.TxIndexNull.Default) -> enums.AregCableCorrSour:
		"""SCPI: [SOURce<HW>]:AREGenerator:FRONtend:TRX<CH>:CABLecorr:CONNector<DI>:TX<ST0>:MODE \n
		Snippet: value: enums.AregCableCorrSour = driver.source.areGenerator.frontend.trx.cableCorr.connector.tx.mode.get(trxFrontent = repcap.TrxFrontent.Default, connector = repcap.Connector.Default, txIndexNull = repcap.TxIndexNull.Default) \n
		No command help available \n
			:param trxFrontent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Trx')
			:param connector: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Connector')
			:param txIndexNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Tx')
			:return: areg_cabel_cor_mod: USER| S2P"""
		trxFrontent_cmd_val = self._cmd_group.get_repcap_cmd_value(trxFrontent, repcap.TrxFrontent)
		connector_cmd_val = self._cmd_group.get_repcap_cmd_value(connector, repcap.Connector)
		txIndexNull_cmd_val = self._cmd_group.get_repcap_cmd_value(txIndexNull, repcap.TxIndexNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:AREGenerator:FRONtend:TRX{trxFrontent_cmd_val}:CABLecorr:CONNector{connector_cmd_val}:TX{txIndexNull_cmd_val}:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.AregCableCorrSour)
