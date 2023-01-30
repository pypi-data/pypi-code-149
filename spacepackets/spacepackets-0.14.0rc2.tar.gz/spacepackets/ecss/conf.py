import enum


FETCH_GLOBAL_APID = -1


class PusVersion(enum.IntEnum):
    # ESA PSS-07-101. Not supported by this package!
    ESA_PUS = 0
    # ECSS-E-70-41A
    PUS_A = 1
    # ECSS-E-ST-70-41C
    PUS_C = 2
    GLOBAL_CONFIG = 98
    UNKNOWN = 99


class EcssConfKeys(enum.IntEnum):
    ECSS_TC_APID = 0
    ECSS_TM_APID = 1
    PUS_TM_TYPE = 2
    PUS_TC_TYPE = 3
    MAX_TC_PACKET_SIZE = 4


__ECSS_DICT = {
    EcssConfKeys.ECSS_TM_APID: 0x00,
    EcssConfKeys.ECSS_TC_APID: 0x00,
    EcssConfKeys.MAX_TC_PACKET_SIZE: 1500,
}


def set_default_tm_apid(tm_apid: int):
    __ECSS_DICT[EcssConfKeys.ECSS_TM_APID] = tm_apid


def get_default_tm_apid() -> int:
    return __ECSS_DICT[EcssConfKeys.ECSS_TM_APID]


def set_default_tc_apid(tc_apid: int):
    __ECSS_DICT[EcssConfKeys.ECSS_TC_APID] = tc_apid


def get_default_tc_apid() -> int:
    return __ECSS_DICT[EcssConfKeys.ECSS_TC_APID]


def set_max_tc_packet_size(max_len: int):
    __ECSS_DICT[EcssConfKeys.MAX_TC_PACKET_SIZE] = max_len


def get_max_tc_packet_size() -> int:
    return __ECSS_DICT[EcssConfKeys.MAX_TC_PACKET_SIZE]
