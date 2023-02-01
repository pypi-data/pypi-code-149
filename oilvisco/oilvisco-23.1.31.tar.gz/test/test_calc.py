from oilvisco import calc
from oilvisco.datatypes import Oil
import pytest

class TestBlends:
    @pytest.mark.parametrize("tin,                          tout",
            [([Oil(0,0,1),],                                Oil(0,0,1)),
             ([Oil(0,20,3), Oil(10,40,1)],                  Oil (2.5, 25, 4)),
             ([Oil(20,30,1), Oil(10,20,1), Oil(0,10,1)],    Oil (10, 20, 3)),
            ])
    def test_variable_blend(s, tin, tout):
        assert calc.blend(tin) == tout

