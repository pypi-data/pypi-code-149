from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LevelCls:
	"""Level commands group definition. 3 total commands, 2 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("level", core, parent)

	@property
	def digHeadroom(self):
		"""digHeadroom commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_digHeadroom'):
			from .DigHeadroom import DigHeadroomCls
			self._digHeadroom = DigHeadroomCls(self._core, self._cmd_group)
		return self._digHeadroom

	@property
	def otime(self):
		"""otime commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_otime'):
			from .Otime import OtimeCls
			self._otime = OtimeCls(self._core, self._cmd_group)
		return self._otime

	def set(self, mappingChannel=repcap.MappingChannel.Default) -> None:
		"""SCPI: [SOURce<HW>]:AREGenerator:MAPPing<CH>:ADJust:LEVel \n
		Snippet: driver.source.areGenerator.mapping.adjust.level.set(mappingChannel = repcap.MappingChannel.Default) \n
		Triggers adjustment of the power level of the selected output channels. \n
			:param mappingChannel: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mapping')
		"""
		mappingChannel_cmd_val = self._cmd_group.get_repcap_cmd_value(mappingChannel, repcap.MappingChannel)
		self._core.io.write(f'SOURce<HwInstance>:AREGenerator:MAPPing{mappingChannel_cmd_val}:ADJust:LEVel')

	def set_with_opc(self, mappingChannel=repcap.MappingChannel.Default, opc_timeout_ms: int = -1) -> None:
		mappingChannel_cmd_val = self._cmd_group.get_repcap_cmd_value(mappingChannel, repcap.MappingChannel)
		"""SCPI: [SOURce<HW>]:AREGenerator:MAPPing<CH>:ADJust:LEVel \n
		Snippet: driver.source.areGenerator.mapping.adjust.level.set_with_opc(mappingChannel = repcap.MappingChannel.Default) \n
		Triggers adjustment of the power level of the selected output channels. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsAreg800.utilities.opc_timeout_set() to set the timeout value. \n
			:param mappingChannel: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mapping')
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SOURce<HwInstance>:AREGenerator:MAPPing{mappingChannel_cmd_val}:ADJust:LEVel', opc_timeout_ms)

	def clone(self) -> 'LevelCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = LevelCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
