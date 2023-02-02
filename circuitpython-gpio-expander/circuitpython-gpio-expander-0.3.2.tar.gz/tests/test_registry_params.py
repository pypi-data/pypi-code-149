"""Common method pytest module file."""

# SPDX-FileCopyrightText: 2017 Scott Shawcroft, written for Adafruit Industries
# SPDX-FileCopyrightText: Copyright (c) 2022 Gabriele Pongelli
#
# SPDX-License-Identifier: MIT

import pytest
from gpio_expander import _get_registry_params


@pytest.mark.parametrize(
    "x_input,exp_name,exp_addr_mul,exp_adder,exp_idx",
    [
        pytest.param(0, "0_", 2, 0, 0, id="input 0"),
        pytest.param(1, "0_", 2, 0, 1, id="input 1"),
        pytest.param(2, "0_", 2, 0, 2, id="input 2"),
        pytest.param(3, "0_", 2, 0, 3, id="input 3"),
        pytest.param(4, "0_", 2, 0, 4, id="input 4"),
        pytest.param(5, "0_", 2, 0, 5, id="input 5"),
        pytest.param(6, "0_", 2, 0, 6, id="input 6"),
        pytest.param(7, "0_", 2, 0, 7, id="input 7"),
        pytest.param(8, "1_", 2, 1, 0, id="input 8"),
        pytest.param(9, "1_", 2, 1, 1, id="input 9"),
        pytest.param(10, "1_", 2, 1, 2, id="input 10"),
        pytest.param(11, "1_", 2, 1, 3, id="input 11"),
        pytest.param(12, "1_", 2, 1, 4, id="input 12"),
        pytest.param(13, "1_", 2, 1, 5, id="input 13"),
        pytest.param(14, "1_", 2, 1, 6, id="input 14"),
        pytest.param(15, "1_", 2, 1, 7, id="input 15"),
    ],
)
def test_loop_16(x_input, exp_name, exp_addr_mul, exp_adder, exp_idx):
    """Test common method for 16 GPIO expander."""
    _name, _reg_address_multiplier, _adder, _idx = _get_registry_params(16, x_input)
    print(_name)
    print(_reg_address_multiplier)
    print(_adder)
    print(_idx)
    assert _name == exp_name
    assert _reg_address_multiplier == exp_addr_mul
    assert _adder == exp_adder
    assert _idx == exp_idx


@pytest.mark.parametrize(
    "x_input,exp_name,exp_addr_mul,exp_adder,exp_idx",
    [
        pytest.param(0, "", 1, 0, 0, id="input 0"),
        pytest.param(1, "", 1, 0, 1, id="input 1"),
        pytest.param(2, "", 1, 0, 2, id="input 2"),
        pytest.param(3, "", 1, 0, 3, id="input 3"),
        pytest.param(4, "", 1, 0, 4, id="input 4"),
        pytest.param(5, "", 1, 0, 5, id="input 5"),
        pytest.param(6, "", 1, 0, 6, id="input 6"),
        pytest.param(7, "", 1, 0, 7, id="input 7"),
    ],
)
def test_loop_8(x_input, exp_name, exp_addr_mul, exp_adder, exp_idx):
    """Test common method for 8 GPIO expander."""
    _name, _reg_address_multiplier, _adder, _idx = _get_registry_params(8, x_input)
    print(_name)
    print(_reg_address_multiplier)
    print(_adder)
    print(_idx)
    assert _name == exp_name
    assert _reg_address_multiplier == exp_addr_mul
    assert _adder == exp_adder
    assert _idx == exp_idx
