from hypothesis import settings, Verbosity, given
from hypothesis import strategies as st
# from sympy.ntheory import sum_as_string
import uem_reader_py

# @given(v1=st.integers(min_value=1, max_value=2**10),
#        v2=st.integers(min_value=1, max_value=2**10))
# @settings(verbosity=Verbosity.normal, max_examples=500)
# def test_sum_as_string(v1, v2):
#     assert uem_reader_py.sum_as_string(v1, v2) == str(v1 + v2)
  
if __name__ == "__main__":
       # test_sum_as_string()
       rdrs = uem_reader_py.find_usb_readers()
       assert len(rdrs) > 0
       print(rdrs)
       print(rdrs[0])
       print(rdrs[0].open())
       print(rdrs[0].send([0x64]))  # Get Version
       print(rdrs[0].send([0x22]))  # Get Serial
       print(rdrs[0].send([0x05, 0x03]))  # Beep 3 times
       print(rdrs[0].close())
       import time
       time.sleep(1)
       print(rdrs[0].open())
       print(rdrs[0].send([0x05, 0x03]))  # Beep 3 times
       print(rdrs[0].close())