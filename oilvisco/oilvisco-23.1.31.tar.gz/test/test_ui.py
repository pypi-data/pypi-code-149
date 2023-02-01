from oilvisco import ui
from oilvisco.datatypes import Oil
import pytest

class TestInput:
    @pytest.mark.parametrize("tin, tout", 
            [("0W20x1", [Oil(0, 20, 1)]),
             ( "0W20x3 10W40x1", [Oil(0,20,3), Oil(10,40,1)]) ])
    def test_convert_input(s, tin, tout):
        assert ui.convert_input(tin) == tout
