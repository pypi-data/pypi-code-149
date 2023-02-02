from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Utilities import trim_str_response
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class OsetupCls:
	"""Osetup commands group definition. 18 total commands, 3 Subgroups, 7 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("osetup", core, parent)

	@property
	def apply(self):
		"""apply commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_apply'):
			from .Apply import ApplyCls
			self._apply = ApplyCls(self._core, self._cmd_group)
		return self._apply

	@property
	def bw(self):
		"""bw commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_bw'):
			from .Bw import BwCls
			self._bw = BwCls(self._core, self._cmd_group)
		return self._bw

	@property
	def multiInstrument(self):
		"""multiInstrument commands group. 2 Sub-classes, 2 commands."""
		if not hasattr(self, '_multiInstrument'):
			from .MultiInstrument import MultiInstrumentCls
			self._multiInstrument = MultiInstrumentCls(self._core, self._cmd_group)
		return self._multiInstrument

	def get_hostname(self) -> str:
		"""SCPI: [SOURce<HW>]:AREGenerator:OSETup:HOSTname \n
		Snippet: value: str = driver.source.areGenerator.osetup.get_hostname() \n
		No command help available \n
			:return: areg_osetup_ip_address: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:AREGenerator:OSETup:HOSTname?')
		return trim_str_response(response)

	def set_hostname(self, areg_osetup_ip_address: str) -> None:
		"""SCPI: [SOURce<HW>]:AREGenerator:OSETup:HOSTname \n
		Snippet: driver.source.areGenerator.osetup.set_hostname(areg_osetup_ip_address = '1') \n
		No command help available \n
			:param areg_osetup_ip_address: No help available
		"""
		param = Conversions.value_to_quoted_str(areg_osetup_ip_address)
		self._core.io.write(f'SOURce<HwInstance>:AREGenerator:OSETup:HOSTname {param}')

	def get_ip_address(self) -> str:
		"""SCPI: [SOURce<HW>]:AREGenerator:OSETup:IPADdress \n
		Snippet: value: str = driver.source.areGenerator.osetup.get_ip_address() \n
		No command help available \n
			:return: areg_osetup_ip_address: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:AREGenerator:OSETup:IPADdress?')
		return trim_str_response(response)

	def set_ip_address(self, areg_osetup_ip_address: str) -> None:
		"""SCPI: [SOURce<HW>]:AREGenerator:OSETup:IPADdress \n
		Snippet: driver.source.areGenerator.osetup.set_ip_address(areg_osetup_ip_address = '1') \n
		No command help available \n
			:param areg_osetup_ip_address: No help available
		"""
		param = Conversions.value_to_quoted_str(areg_osetup_ip_address)
		self._core.io.write(f'SOURce<HwInstance>:AREGenerator:OSETup:IPADdress {param}')

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.OsetupMode:
		"""SCPI: [SOURce<HW>]:AREGenerator:OSETup:MODE \n
		Snippet: value: enums.OsetupMode = driver.source.areGenerator.osetup.get_mode() \n
		No command help available \n
			:return: areg_oset_mode: STATic| DYNamic
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:AREGenerator:OSETup:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.OsetupMode)

	def set_mode(self, areg_oset_mode: enums.OsetupMode) -> None:
		"""SCPI: [SOURce<HW>]:AREGenerator:OSETup:MODE \n
		Snippet: driver.source.areGenerator.osetup.set_mode(areg_oset_mode = enums.OsetupMode.DYNamic) \n
		No command help available \n
			:param areg_oset_mode: STATic| DYNamic
		"""
		param = Conversions.enum_scalar_to_str(areg_oset_mode, enums.OsetupMode)
		self._core.io.write(f'SOURce<HwInstance>:AREGenerator:OSETup:MODE {param}')

	def get_port(self) -> int:
		"""SCPI: [SOURce<HW>]:AREGenerator:OSETup:PORT \n
		Snippet: value: int = driver.source.areGenerator.osetup.get_port() \n
		No command help available \n
			:return: areg_oset_port: integer Range: 0 to 64000
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:AREGenerator:OSETup:PORT?')
		return Conversions.str_to_int(response)

	def set_port(self, areg_oset_port: int) -> None:
		"""SCPI: [SOURce<HW>]:AREGenerator:OSETup:PORT \n
		Snippet: driver.source.areGenerator.osetup.set_port(areg_oset_port = 1) \n
		No command help available \n
			:param areg_oset_port: integer Range: 0 to 64000
		"""
		param = Conversions.decimal_value_to_str(areg_oset_port)
		self._core.io.write(f'SOURce<HwInstance>:AREGenerator:OSETup:PORT {param}')

	# noinspection PyTypeChecker
	def get_protocol(self) -> enums.OsetupHilProtocol:
		"""SCPI: [SOURce<HW>]:AREGenerator:OSETup:PROTocol \n
		Snippet: value: enums.OsetupHilProtocol = driver.source.areGenerator.osetup.get_protocol() \n
		No command help available \n
			:return: areg_oset_protocol: ZMQ| DCP
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:AREGenerator:OSETup:PROTocol?')
		return Conversions.str_to_scalar_enum(response, enums.OsetupHilProtocol)

	def set_protocol(self, areg_oset_protocol: enums.OsetupHilProtocol) -> None:
		"""SCPI: [SOURce<HW>]:AREGenerator:OSETup:PROTocol \n
		Snippet: driver.source.areGenerator.osetup.set_protocol(areg_oset_protocol = enums.OsetupHilProtocol.DCP) \n
		No command help available \n
			:param areg_oset_protocol: ZMQ| DCP
		"""
		param = Conversions.enum_scalar_to_str(areg_oset_protocol, enums.OsetupHilProtocol)
		self._core.io.write(f'SOURce<HwInstance>:AREGenerator:OSETup:PROTocol {param}')

	# noinspection PyTypeChecker
	def get_reference(self) -> enums.OsetupObjRef:
		"""SCPI: [SOURce<HW>]:AREGenerator:OSETup:REFerence \n
		Snippet: value: enums.OsetupObjRef = driver.source.areGenerator.osetup.get_reference() \n
		No command help available \n
			:return: areg_osetup_ref: ORIGin| MAPPed
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:AREGenerator:OSETup:REFerence?')
		return Conversions.str_to_scalar_enum(response, enums.OsetupObjRef)

	def set_reference(self, areg_osetup_ref: enums.OsetupObjRef) -> None:
		"""SCPI: [SOURce<HW>]:AREGenerator:OSETup:REFerence \n
		Snippet: driver.source.areGenerator.osetup.set_reference(areg_osetup_ref = enums.OsetupObjRef.MAPPed) \n
		No command help available \n
			:param areg_osetup_ref: ORIGin| MAPPed
		"""
		param = Conversions.enum_scalar_to_str(areg_osetup_ref, enums.OsetupObjRef)
		self._core.io.write(f'SOURce<HwInstance>:AREGenerator:OSETup:REFerence {param}')

	# noinspection PyTypeChecker
	def get_source(self) -> enums.OsetupDataSource:
		"""SCPI: [SOURce<HW>]:AREGenerator:OSETup:SOURce \n
		Snippet: value: enums.OsetupDataSource = driver.source.areGenerator.osetup.get_source() \n
		No command help available \n
			:return: areg_oset_source: SCENario| HIL
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:AREGenerator:OSETup:SOURce?')
		return Conversions.str_to_scalar_enum(response, enums.OsetupDataSource)

	def set_source(self, areg_oset_source: enums.OsetupDataSource) -> None:
		"""SCPI: [SOURce<HW>]:AREGenerator:OSETup:SOURce \n
		Snippet: driver.source.areGenerator.osetup.set_source(areg_oset_source = enums.OsetupDataSource.HIL) \n
		No command help available \n
			:param areg_oset_source: SCENario| HIL
		"""
		param = Conversions.enum_scalar_to_str(areg_oset_source, enums.OsetupDataSource)
		self._core.io.write(f'SOURce<HwInstance>:AREGenerator:OSETup:SOURce {param}')

	def clone(self) -> 'OsetupCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = OsetupCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
