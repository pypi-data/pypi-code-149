from typing import Final
from random import randrange, randint

ID_PREFIX: Final = 'i'

Min_DB_Id_Series: Final = 1000000
MIN_TEST_Id_Series: Final = 10000
MAX_TEST_Id_Series: Final = 50000


def rand_test_id() -> str:
    return f'{ID_PREFIX}{randint(MIN_TEST_Id_Series, MAX_TEST_Id_Series)}'


def rand_subfix() -> str:
    return f"{randrange(MIN_TEST_Id_Series, MAX_TEST_Id_Series)}"


def new_rand_test_user_name():
    return f"testuseri{randrange(MIN_TEST_Id_Series, MAX_TEST_Id_Series)}"
