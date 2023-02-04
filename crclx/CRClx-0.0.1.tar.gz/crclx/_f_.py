from ._t_ import Params, Table


def logical_reverse(source: int, length: int):
	r = 0
	for i in reversed(range(length)):
		r |= (source & 1) << i
		source >>= 1
	return r


def table_value(index, hash_size, poly, ref_in):
	hash_size, poly, ref_in = hash_size, poly, ref_in
	mask = ~(-1 << hash_size)
	r = index
	if ref_in:
		r = logical_reverse(r, hash_size)
	elif hash_size > 8:
		r <<= hash_size - 8
	last_bit = 1 << (hash_size - 1)
	for i in range(8):
		if (r & last_bit) != 0:
			r = (r << 1) ^ poly
		else:
			r <<= 1
	if ref_in:
		r = logical_reverse(r, hash_size)
	return r & mask


TABLE_SIZE = 256


def table(hash_size, poly, init, xor_out, ref_in, ref_out):
	params = Params(hash_size, poly, init, xor_out, ref_in, ref_out)
	return Table(params, tuple(table_value(i, hash_size, poly, ref_in) for i in range(TABLE_SIZE)))


def calculator(_table: Table):
	def calculate(data):
		if isinstance(data, str):
			data = (ord(c) for c in data)

		table_params = _table.params
		table_values = _table.values
		hash_size, init, xor_out, ref_out = table_params.hash_size, table_params.init, table_params.xor_out, \
											table_params.ref_out
		mask = ~(-1 << hash_size)

		r = logical_reverse(init, hash_size) if ref_out else init
		if ref_out:
			for value in data:
				r = table_values[(r ^ value) & 0xff] ^ (r >> 8)
				r &= mask
		else:
			to_right = hash_size - 8
			to_right = 0 if to_right < 0 else to_right
			for value in data:
				r = table_values[((r >> to_right) ^ value) & 0xff] ^ (r << 8)
				r &= mask
		return (r ^ xor_out) & mask
	return calculate
