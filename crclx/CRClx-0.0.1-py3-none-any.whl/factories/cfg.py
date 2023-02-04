from functools import wraps
from .._t_ import Params
from .._f_ import table, calculator


params = {  # algorithm name: Params(hash_size, poly, xorin, xorout, refin, refout)
	"crc_8": Params(8, 0x07, 0x00, 0x00, False, False),
	"crc_8_cdma2000": Params(8, 0x9b, 0xff, 0x00, False, False),
	"crc_8_darc": Params(8, 0x39, 0x00, 0x00, True, True),
	"crc_8_dvb_s2": Params(8, 0xd5, 0x00, 0x00, False, False),
	"crc_8_ebu": Params(8, 0x1d, 0xff, 0x00, True, True),
	"crc_8_i_code": Params(8, 0x1d, 0xfd, 0x00, False, False),
	"crc_8_itu": Params(8, 0x07, 0x00, 0x55, False, False),
	"crc_8_maxim": Params(8, 0x31, 0x00, 0x00, True, True),
	"crc_8_rohc": Params(8, 0x07, 0xff, 0x00, True, True),
	"crc_8_wcdma": Params(8, 0x9b, 0x00, 0x00, True, True),

	# crc_16_params
	"crc_16_ccitt_false": Params(16, 0x1021, 0xffff, 0x0000, False, False),
	"crc_16_arc": Params(16, 0x8005, 0x0000, 0x0000, True, True),
	"crc_16_aug_ccitt": Params(16, 0x1021, 0x1d0f, 0x0000, False, False),
	"crc_16_buypass": Params(16, 0x8005, 0x0000, 0x0000, False, False),
	"crc_16_cdma2000": Params(16, 0xc867, 0xffff, 0x0000, False, False),
	"crc_16_dds_110": Params(16, 0x8005, 0x800d, 0x0000, False, False),
	"crc_16_dect_r": Params(16, 0x0589, 0x0000, 0x0001, False, False),
	"crc_16_dect_x": Params(16, 0x0589, 0x0000, 0x0000, False, False),
	"crc_16_dnp": Params(16, 0x3d65, 0x0000, 0xffff, True, True),
	"crc_16_en_13757": Params(16, 0x3d65, 0x0000, 0xffff, False, False),
	"crc_16_genibus": Params(16, 0x1021, 0xffff, 0xffff, False, False),
	"crc_16_maxim": Params(16, 0x8005, 0x0000, 0xffff, True, True),
	"crc_16_mcrf4xx": Params(16, 0x1021, 0xffff, 0x0000, True, True),
	"crc_16_riello": Params(16, 0x1021, 0xb2aa, 0x0000, True, True),
	"crc_16_t10_dif": Params(16, 0x8bb7, 0x0000, 0x0000, False, False),
	"crc_16_teledisk": Params(16, 0xa097, 0x0000, 0x0000, False, False),
	"crc_16_tms37157": Params(16, 0x1021, 0x89ec, 0x0000, True, True),
	"crc_16_usb": Params(16, 0x8005, 0xffff, 0xffff, True, True),
	"crc_a": Params(16, 0x1021, 0xc6c6, 0x0000, True, True),
	"crc_16_kermit": Params(16, 0x1021, 0x0000, 0x0000, True, True),
	"crc_16_modbus": Params(16, 0x8005, 0xffff, 0x0000, True, True),
	"crc_16_x_25": Params(16, 0x1021, 0xffff, 0xffff, True, True),
	"crc_16_xmodem": Params(16, 0x1021, 0x0000, 0x0000, False, False),

	# crc_32_params
	"crc_32": Params(32, 0x04c11db7, 0xffffffff, 0xffffffff, True, True),
	"crc_32_bzip2": Params(32, 0x04c11db7, 0xffffffff, 0xffffffff, False, False),
	"crc_32c": Params(32, 0x1edc6f41, 0xffffffff, 0xffffffff, True, True),
	"crc_32d": Params(32, 0xa833982b, 0xffffffff, 0xffffffff, True, True),
	"crc_32_mpeg_2": Params(32, 0x04c11db7, 0xffffffff, 0x00000000, False, False),
	"crc_32_posix": Params(32, 0x04c11db7, 0x00000000, 0xffffffff, False, False),
	"crc_32q": Params(32, 0x814141ab, 0x00000000, 0x00000000, False, False),
	"crc_32_jamcrc": Params(32, 0x04c11db7, 0xffffffff, 0x00000000, True, True),
	"crc_32_xfer": Params(32, 0x000000af, 0x00000000, 0x00000000, False, False),
}


def factory(_f):
	@wraps(_f)
	def gen_calculator():
		name = _f.__name__
		return calculator(table(*params[name]))
	return gen_calculator
