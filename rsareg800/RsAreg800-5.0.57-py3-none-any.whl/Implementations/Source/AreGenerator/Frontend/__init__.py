from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FrontendCls:
	"""Frontend commands group definition. 57 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("frontend", core, parent)

	@property
	def last(self):
		"""last commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_last'):
			from .Last import LastCls
			self._last = LastCls(self._core, self._cmd_group)
		return self._last

	@property
	def qat(self):
		"""qat commands group. 21 Sub-classes, 0 commands."""
		if not hasattr(self, '_qat'):
			from .Qat import QatCls
			self._qat = QatCls(self._core, self._cmd_group)
		return self._qat

	@property
	def trx(self):
		"""trx commands group. 15 Sub-classes, 0 commands."""
		if not hasattr(self, '_trx'):
			from .Trx import TrxCls
			self._trx = TrxCls(self._core, self._cmd_group)
		return self._trx

	def clone(self) -> 'FrontendCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = FrontendCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
