from __future__ import annotations

import enum
from dataclasses import dataclass, field
from datetime import date, datetime
from decimal import Decimal
from typing import Dict, List, Optional, Set, Union

"""
any	used to filter on to many relationships
between	used to filter a field between two values
endswith	check if field ends with a string
eq	check if field is equal to something
ge	check if field is greater than or equal to something
gt	check if field is greater than to something
has	used to filter on to one relationships
ilike	check if field contains a string (case insensitive)
in_	check if field is in a list of values
is_	check if field is a value
isnot	check if field is not a value
like	check if field contains a string
le	check if field is less than or equal to something
lt	check if field is less than to something
match	check if field match against a string or pattern
ne	check if field is not equal to something
notilike	check if field does not contains a string (case insensitive)
notin_	check if field is not in a list of values
notlike	check if field does not contains a string
startswith	check if field starts with a string
"""

filter_1 = {
    "name": "nabave",
    "op": "any",
    "val": {
        "name": "verifikacije",
        "op": "any",
        "val": {"name": "datum_prihvacanja", "op": "le", "val": "2013-09-16"},
    },
}

filter_2 = {
    "or": [
        {
            "name": "nabave",
            "op": "any",
            "val": {
                "name": "verifikacije",
                "op": "any",
                "val": {
                    "name": "datum_prihvacanja",
                    "op": "ge",
                    "val": "2013-09-16",
                },
            },
        },
        {
            "name": "nabave",
            "op": "any",
            "val": {
                "name": "verifikacije",
                "op": "any",
                "val": {
                    "name": "datum_primitka",
                    "op": "ge",
                    "val": "2013-08-30",
                },
            },
        },
    ]
}


LiteralT = Union[str, int, float, date, datetime, Decimal]


FILTER_OP = [
any
between
endswith
eq	check if field is equal to something
ge	check if field is greater than or equal to something
gt	check if field is greater than to something
has	used to filter on to one relationships
ilike	check if field contains a string (case insensitive)
in_	check if field is in a list of values
is_	check if field is a value
isnot	check if field is not a value
like	check if field contains a string
le	check if field is less than or equal to something
lt	check if field is less than to something
match	check if field match against a string or pattern
ne	check if field is not equal to something
notilike	check if field does not contains a string (case insensitive)
notin_	check if field is not in a list of values
notlike	check if field does not contains a string
startswith	check if field starts with a string

]



@dataclass
class FilterExpression:
    name: str
    op: str
    val: Union[LiteralT, FilterExpression]

    @classmethod
    def from_data(cls, data) -> FilterExpression:
        name = data["name"]
        op = data["op"]
        val = data["val"]

        if isinstance(val, dict):
            val = cls.from_data(val)

        return cls(name, op, val)


@dataclass
class Not:
    op: Union[Not, Or, And, FilterExpression]


@dataclass
class Or:
    op: Union[Not, Or, And, FilterExpression]


@dataclass
class And:
    op: Union[Not, Or, And, FilterExpression]
