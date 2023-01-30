"""This module contains the PUS telecommand class representation to pack telecommands, most notably
the :py:class:`PusTelecommand` class.
"""
from __future__ import annotations

import struct
from typing import Tuple

from crcmod.predefined import mkPredefinedCrcFun, PredefinedCrc

from spacepackets.log import get_console_logger
from spacepackets.ccsds.spacepacket import (
    SpacePacketHeader,
    PacketType,
    SPACE_PACKET_HEADER_SIZE,
    SpacePacket,
    PacketId,
    PacketSeqCtrl,
    SequenceFlags,
)
from spacepackets.util import get_printable_data_string, PrintFormats
from spacepackets.ecss.conf import (
    get_default_tc_apid,
    PusVersion,
    FETCH_GLOBAL_APID,
)


class PusTcDataFieldHeader:
    PUS_C_SEC_HEADER_LEN = 5

    def __init__(
        self,
        service: int,
        subservice: int,
        source_id: int = 0,
        ack_flags: int = 0b1111,
    ):
        """Create a PUS TC data field header instance

        :param service:
        :param subservice:
        :param source_id:
        :param ack_flags:
        """
        self.service = service
        self.subservice = subservice
        self.source_id = source_id
        self.pus_version = PusVersion.PUS_C
        self.ack_flags = ack_flags

    def pack(self) -> bytearray:
        header_raw = bytearray()
        header_raw.append(self.pus_version << 4 | self.ack_flags)
        header_raw.append(self.service)
        header_raw.append(self.subservice)
        header_raw.extend(struct.pack("!H", self.source_id))
        return header_raw

    @classmethod
    def unpack(cls, raw_packet: bytes) -> PusTcDataFieldHeader:
        """Unpack a TC data field header.

        :param raw_packet: Start of raw data belonging to the TC data field header
        :return:
        """
        min_expected_len = cls.get_header_size()
        if len(raw_packet) < min_expected_len:
            raise ValueError(
                f"Passed bytearray too short, expected minimum length {min_expected_len}"
            )
        version_and_ack_byte = raw_packet[0]
        pus_version = (version_and_ack_byte & 0xF0) >> 4
        if pus_version != PusVersion.PUS_C:
            raise ValueError("This implementation only supports PUS C")
        ack_flags = version_and_ack_byte & 0x0F
        service = raw_packet[1]
        subservice = raw_packet[2]
        source_id = struct.unpack("!H", raw_packet[3:5])[0]
        return cls(
            service=service,
            subservice=subservice,
            ack_flags=ack_flags,
            source_id=source_id,
        )

    def __repr__(self):
        return (
            f"{self.__class__.__name__}(service={self.service!r}, subservice={self.subservice!r},"
            f" ack_flags={self.ack_flags!r} "
        )

    def __eq__(self, other: PusTcDataFieldHeader):
        return self.pack() == other.pack()

    @classmethod
    def get_header_size(cls):
        return cls.PUS_C_SEC_HEADER_LEN


class PusTelecommand:
    """Class representation of a PUS telecommand. Can be converted to the raw byte representation
    but also unpacked from a raw byte stream. Only PUS C telecommands are supported.

    >>> ping_tc = PusTelecommand(service=17, subservice=1, seq_count=22, apid=0x01)
    >>> ping_tc.service
    17
    >>> ping_tc.subservice
    1
    >>> ping_tc.pack().hex(sep=',')
    '18,01,c0,16,00,06,2f,11,01,00,00,ab,62'

    """

    def __init__(
        self,
        service: int,
        subservice: int,
        app_data: bytes = bytes([]),
        seq_count: int = 0,
        source_id: int = 0,
        ack_flags: int = 0b1111,
        apid: int = FETCH_GLOBAL_APID,
    ):
        """Initiate a PUS telecommand from the given parameters. The raw byte representation
        can then be retrieved with the :py:meth:`pack` function.

        :param service: PUS service number
        :param subservice: PUS subservice number
        :param apid: Application Process ID as specified by CCSDS
        :param seq_count: Source Sequence Count. Application should take care of incrementing this.
            Limited to 2 to the power of 14 by the number of bits in the header
        :param app_data: Application data in the Packet Data Field
        :param source_id: Source ID will be supplied as well. Can be used to distinguish
            different packet sources (e.g. different ground stations)
        :raises ValueError: Invalid input parameters
        """
        if apid == -1:
            apid = get_default_tc_apid()
        self.pus_tc_sec_header = PusTcDataFieldHeader(
            service=service,
            subservice=subservice,
            ack_flags=ack_flags,
            source_id=source_id,
        )
        data_length = self.get_data_length(
            secondary_header_len=self.pus_tc_sec_header.get_header_size(),
            app_data_len=len(app_data),
        )
        self.sp_header = SpacePacketHeader(
            apid=apid,
            sec_header_flag=True,
            packet_type=PacketType.TC,
            seq_flags=SequenceFlags.UNSEGMENTED,
            data_len=data_length,
            seq_count=seq_count,
        )
        self._app_data = app_data
        self._valid = True
        self._crc16 = 0

    @classmethod
    def from_sp_header(
        cls,
        sp_header: SpacePacketHeader,
        service: int,
        subservice: int,
        app_data: bytes = bytes([]),
        source_id: int = 0,
        ack_flags: int = 0b1111,
    ):
        pus_tc = cls.__empty()
        sp_header.packet_type = PacketType.TC
        sp_header.sec_header_flag = True
        sp_header.data_len = PusTelecommand.get_data_length(
            secondary_header_len=PusTcDataFieldHeader.get_header_size(),
            app_data_len=len(app_data),
        )
        pus_tc.sp_header = sp_header
        pus_tc.pus_tc_sec_header = PusTcDataFieldHeader(
            service=service,
            subservice=subservice,
            source_id=source_id,
            ack_flags=ack_flags,
        )
        pus_tc._app_data = app_data
        return pus_tc

    @classmethod
    def from_composite_fields(
        cls,
        sp_header: SpacePacketHeader,
        sec_header: PusTcDataFieldHeader,
        app_data: bytes = bytes([]),
    ) -> PusTelecommand:
        pus_tc = cls.__empty()
        if sp_header.packet_type == PacketType.TM:
            raise ValueError(
                f"Invalid Packet Type {sp_header.packet_type} in CCSDS primary header"
            )
        pus_tc.sp_header = sp_header
        pus_tc.pus_tc_sec_header = sec_header
        pus_tc._app_data = app_data
        return pus_tc

    @classmethod
    def __empty(cls) -> PusTelecommand:
        return PusTelecommand(service=0, subservice=0)

    def __repr__(self):
        """Returns the representation of a class instance."""
        return (
            f"{self.__class__.__name__}.from_composite_fields(sp_header={self.sp_header!r}, "
            f"sec_header={self.pus_tc_sec_header!r}, app_data={self.app_data!r})"
        )

    def __str__(self):
        """Returns string representation of a class instance."""
        from .req_id import RequestId

        return (
            f"PUS TC[{self.pus_tc_sec_header.service}, {self.pus_tc_sec_header.subservice}] with "
            f"Request ID {RequestId.from_sp_header(self.sp_header).as_u32():#08x}"
            f", APID {self.apid:#05x}, SSC {self.sp_header.seq_count}"
        )

    def __eq__(self, other: PusTelecommand):
        return (
            self.sp_header == other.sp_header
            and self.pus_tc_sec_header == other.pus_tc_sec_header
            and self._app_data == other._app_data
        )

    def to_space_packet(self) -> SpacePacket:
        """Retrieve the generic CCSDS space packet representation. This also calculates the CRC16
        before converting the PUS TC to a generic Space Packet"""
        self.calc_crc()
        user_data = bytearray(self._app_data)
        user_data.extend(struct.pack("!H", self._crc16))
        return SpacePacket(self.sp_header, self.pus_tc_sec_header.pack(), user_data)

    @property
    def valid(self):
        return self._valid

    def calc_crc(self):
        """Can be called to calculate the CRC16"""
        crc = PredefinedCrc(crc_name="crc-ccitt-false")
        crc.update(self.sp_header.pack())
        crc.update(self.pus_tc_sec_header.pack())
        crc.update(self.app_data)
        self._crc16 = crc.crcValue

    def pack(self, calc_crc: bool = True) -> bytearray:
        """Serializes the TC data fields into a bytearray.

        :param calc_crc: Recalculate the CRC. Can be disabled if :py:func:`calc_crc`
            was called before
        """
        packed_data = bytearray()
        packed_data.extend(self.sp_header.pack())
        packed_data.extend(self.pus_tc_sec_header.pack())
        packed_data += self.app_data
        if calc_crc:
            crc_func = mkPredefinedCrcFun(crc_name="crc-ccitt-false")
            self._crc16 = crc_func(packed_data)
        packed_data.extend(struct.pack("!H", self._crc16))
        return packed_data

    @classmethod
    def unpack(cls, raw_packet: bytes) -> PusTelecommand:
        tc_unpacked = cls.__empty()
        tc_unpacked.sp_header = SpacePacketHeader.unpack(space_packet_raw=raw_packet)
        tc_unpacked.pus_tc_sec_header = PusTcDataFieldHeader.unpack(
            raw_packet=raw_packet[SPACE_PACKET_HEADER_SIZE:]
        )
        header_len = (
            SPACE_PACKET_HEADER_SIZE + tc_unpacked.pus_tc_sec_header.get_header_size()
        )
        expected_packet_len = tc_unpacked.packet_len
        if len(raw_packet) < expected_packet_len:
            logger = get_console_logger()
            logger.warning(
                f"Invalid length of raw telecommand packet, expected minimum length "
                f"{expected_packet_len}"
            )
            raise ValueError
        tc_unpacked._app_data = raw_packet[header_len : expected_packet_len - 2]
        tc_unpacked._crc16 = raw_packet[expected_packet_len - 2 : expected_packet_len]
        crc_func = mkPredefinedCrcFun(crc_name="crc-ccitt-false")
        whole_packet = raw_packet[:expected_packet_len]
        should_be_zero = crc_func(whole_packet)
        if should_be_zero == 0:
            tc_unpacked._valid = True
        else:
            logger = get_console_logger()
            logger.warning("Invalid CRC16 in raw telecommand detected")
            tc_unpacked._valid = False
        return tc_unpacked

    @property
    def packet_len(self) -> int:
        """Retrieve the full packet size when packed
        :return: Size of the TM packet based on the space packet header data length field.
        The space packet data field is the full length of data field minus one without
        the space packet header.
        """
        return self.sp_header.packet_len

    @staticmethod
    def get_data_length(app_data_len: int, secondary_header_len: int) -> int:
        """Retrieve size of TC packet in bytes.
        Formula according to PUS Standard: C = (Number of octets in packet data field) - 1.
        The size of the TC packet is the size of the packet secondary header with
        source ID + the length of the application data + length of the CRC16 checksum - 1
        """
        try:
            data_length = secondary_header_len + app_data_len + 1
            return data_length
        except TypeError:
            logger = get_console_logger()
            logger.warning("PusTelecommand: Invalid type of application data!")
            return 0

    def pack_command_tuple(self) -> Tuple[bytearray, PusTelecommand]:
        """Pack a tuple consisting of the raw packet as the first entry and the class representation
        as the second entry
        """
        command_tuple = (self.pack(), self)
        return command_tuple

    @property
    def service(self) -> int:
        return self.pus_tc_sec_header.service

    @property
    def subservice(self) -> int:
        return self.pus_tc_sec_header.subservice

    @property
    def source_id(self) -> int:
        return self.pus_tc_sec_header.source_id

    @source_id.setter
    def source_id(self, source_id: int):
        self.pus_tc_sec_header.source_id = source_id

    @property
    def seq_count(self) -> int:
        return self.sp_header.seq_count

    @property
    def apid(self) -> int:
        return self.sp_header.apid

    @property
    def packet_id(self) -> PacketId:
        return self.sp_header.packet_id

    @property
    def packet_seq_ctrl(self) -> PacketSeqCtrl:
        return self.sp_header.psc

    @property
    def app_data(self) -> bytes:
        return self._app_data

    @property
    def crc16(self):
        return self._crc16

    @seq_count.setter
    def seq_count(self, value):
        self.sp_header.seq_count = value

    @apid.setter
    def apid(self, apid):
        self.sp_header.apid = apid

    def print(self, print_format: PrintFormats = PrintFormats.HEX):
        """Print the raw command in a clean format."""
        packet = self.pack()
        print(get_printable_data_string(print_format=print_format, data=packet))


def generate_packet_crc(tc_packet: bytearray) -> bytes:
    """Removes current Packet Error Control, calculates new
    CRC16 checksum and adds it as correct Packet Error Control Code.
    Reference: ECSS-E70-41A p. 207-212
    """
    crc_func = mkPredefinedCrcFun(crc_name="crc-ccitt-false")
    crc = crc_func(tc_packet[0 : len(tc_packet) - 2])
    tc_packet[len(tc_packet) - 2] = (crc & 0xFF00) >> 8
    tc_packet[len(tc_packet) - 1] = crc & 0xFF
    return tc_packet


def generate_crc(data: bytearray) -> bytes:
    """Takes the application data, appends the CRC16 checksum and returns resulting bytearray"""
    data_with_crc = bytearray()
    data_with_crc += data
    crc_func = mkPredefinedCrcFun(crc_name="crc-ccitt-false")
    crc = crc_func(data)
    data_with_crc.extend(struct.pack("!H", crc))
    return data_with_crc
