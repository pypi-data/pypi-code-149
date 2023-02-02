from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class BwCls:
	"""Bw commands group definition. 3 total commands, 2 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bw", core, parent)

	@property
	def discard(self):
		"""discard commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_discard'):
			from .Discard import DiscardCls
			self._discard = DiscardCls(self._core, self._cmd_group)
		return self._discard

	@property
	def exec(self):
		"""exec commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_exec'):
			from .Exec import ExecCls
			self._exec = ExecCls(self._core, self._cmd_group)
		return self._exec

	# noinspection PyTypeChecker
	def get_value(self) -> enums.AregCconfigBw:
		"""SCPI: [SOURce<HW>]:AREGenerator:CHANnel:BW \n
		Snippet: value: enums.AregCconfigBw = driver.source.areGenerator.channel.bw.get_value() \n
		No command help available \n
			:return: areg_chan_bw: BW1G| BW2G| BW5G
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:AREGenerator:CHANnel:BW?')
		return Conversions.str_to_scalar_enum(response, enums.AregCconfigBw)

	def clone(self) -> 'BwCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = BwCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
