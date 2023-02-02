import re
from io import StringIO

import pandas as pd
import pytest
from requests import get


def clean_column(column: str) -> str:

    pattern = "[^0-9a-z]"
    column = column.lower()
    column = re.sub(pattern=pattern, repl="", string=column)

    return column


@pytest.fixture(scope="function")
def data():
    response = get(url="https://people.sc.fsu.edu/~jburkardt/data/csv/cities.csv")
    assert response.status_code == 200

    csv_data = pd.read_csv(StringIO(response.content.decode()))
    csv_data.columns = [clean_column(column) for column in csv_data.columns]

    return csv_data
