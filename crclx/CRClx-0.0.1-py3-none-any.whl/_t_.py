import typing as _tp


class Params(_tp.NamedTuple):
	hash_size: int
	poly: int
	init: int
	xor_out: int
	ref_in: bool
	ref_out: bool


class Table(_tp.NamedTuple):
	params: Params
	values: tuple
