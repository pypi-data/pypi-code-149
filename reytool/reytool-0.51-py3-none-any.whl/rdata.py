# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time    : 2022-12-05 14:10:42
@Author  : Rey
@Contact : reyxbo@163.com
@Explain : Rey's directory type
"""


from typing import Any, List, Tuple, Dict, Iterable, Iterator, Literal, Optional, Union
from sqlalchemy.engine.cursor import LegacyCursorResult
from pandas import DataFrame, ExcelWriter

from .rbasic import is_iterable
from .rtime import time_to_str


def to_table(data: Union[LegacyCursorResult, Iterable[Dict]], fields: Optional[Iterable] = None) -> List[Dict]:
    """
    Fetch SQL result or Iterable[Dict] to table in List[Dict] format.

    Parameters
    ----------
    data : Data.
    fields : Table fields.
        - None : Use data fields.
        - Iterable : Use values in Iterable.
    
    Returns
    -------
    Table in List[Dict] format.
    """

    if type(data) == LegacyCursorResult:
        if fields == None:
            fields = data.keys()
        table = [dict(zip(fields, [time_to_str(val) for val in row])) for row in data]
    else:
        data_fields_len = max([len(row) for row in data])
        if fields == None:
            data = [list(row) + [None] * (data_fields_len - len(row)) for row in data]
            field_range = range(data_fields_len)
            table = [dict(zip(field_range, [time_to_str(val) for val in row])) for row in data]
        else:
            field_len = len(fields)
            if data_fields_len > field_len:
                fields += list(range(data_fields_len - field_len))
            data = [list(row) + [None] * (field_len - len(row)) for row in data]
            table = [dict(zip(fields, [time_to_str(val) for val in row])) for row in data]
    return table

def to_df(data: Union[LegacyCursorResult, Iterable[Dict]], fields: Optional[Iterable] = None) -> DataFrame:
    """
    Fetch SQL result or Iterable[Dict] to table of DataFrame object.

    Parameters
    ----------
    data : Data.
    fields : Table fields.
        - None : Use data fields.
        - Iterable : Use values in Iterable.
    
    Returns
    -------
    Table of DataFrame object.
    """

    if type(data) == LegacyCursorResult:
        if fields == None:
            fields = data.keys()
        else:
            fields_len = len(data.keys())
            fields = fields[:fields_len]
        df = DataFrame(data, columns=fields)
    else:
        if fields == None:
            df = DataFrame(data)
        else:
            data_fields_len = max([len(row) for row in data])
            field_len = len(fields)
            if data_fields_len > field_len:
                fields += list(range(data_fields_len - field_len))
            data = [list(row) + [None] * (field_len - len(row)) for row in data]
            df = DataFrame(data, columns=fields)
    return df

def to_sql(data: Union[LegacyCursorResult, Iterable[Dict]], fields: Optional[Iterable] = None) -> str:
    """
    Fetch SQL result or Iterable[Dict] to SQL syntax.
    
    Parameters
    ----------
    data : Data.
    fields : Table fields.
        - None : Use data fields.
        - Iterable : Use values in Iterable.
    
    Returns
    -------
    SQL syntax.
    """

    if type(data) == LegacyCursorResult:
        if fields == None:
            fields = data.keys()
        sqls = [[repr(time_to_str(val)) if val else "NULL" for val in row] for row in data]
    else:
        if fields == None:
            data_fields_len = max([len(row) for row in data])
            fields = ["field_%d" % i for i in range(data_fields_len)]
        sqls = [[repr(time_to_str(val)) if val else "NULL" for val in row] + ["NULL"] * (data_fields_len - len(row)) for row in data]
    sqls[0] = "SELECT " + ",".join(["%s AS `%s`" % (val, fie) for val, fie in list(zip(sqls[0], fields))])
    sqls[1:] = ["SELECT " + ",".join(sql) for sql in sqls[1:]]
    sql = " UNION ALL ".join(sqls)
    return sql

def to_excel(
    data: Union[LegacyCursorResult, Iterable[Dict]],
    group_field: Optional[str] = None,
    file_name: str = "table.xlsx",
    sheets_fields: Optional[Dict[str, Optional[Iterable[str]]]] = None
) -> Tuple[Tuple[str, DataFrame], ...]:
    """
    Fetch SQL result or Iterable[Dict] to save excel file and return sheet name and sheet data.

    Parameters
    ----------
    data : Data.
    group_field : Group filed.
    file_name : File name with suffix.
    sheets_fields : Set sheet name and filter sheet fields.
        - None : Sheet name is group value and sheet fields not filtered.
        - Dict[str, Optional[Iterable[str]]] : Item key is sheet name and item value is filter fields.
    
    Returns
    -------
    Sheet name and sheet data.
    """

    data_df = to_df(data)
    if group_field == None:
        data_group = (("Sheet1", data_df),)
    else:
        data_group = data_df.groupby(group_field)
    excel = ExcelWriter(file_name)
    if sheets_fields == None:
        iterable = data_group
    else:
        iterable = zip(data_group, sheets_fields.items())
    excel_dfs = ()
    for item in iterable:
        if sheets_fields == None:
            group_key, group_df = item
            sheet_name = str(group_key)
            if group_field != None:
                del group_df[group_field]
        else:
            group_item, sheet_item = item
            group_key, group_df = group_item
            sheet_name, sheet_fields = sheet_item
            group_df = group_df[sheet_fields]
        group_df.to_excel(excel, sheet_name, index=False)
        excel_dfs += (sheet_name, group_df)
    excel.close()
    return excel_dfs

class RDict(object):
    """
    Rey's directory type.

    Methods
    -------
    attribute : parms, default
    syntax : [index | slice], for, in/ not in
    enter parameter : len
    symbol : +(l/ r), -(l/ r), &(l/ r), +=, -=, &=
    function : items, keys, values, get, pop
    """
    
    def __init__(self, *dicts: Dict, default: Union[Any, Literal["error"]] = "error") -> None:
        """
        Set directory attribute.

        Parameters
        ----------
        dicts : directory
        default : Default method when index fails.
            - Any : Return this value.
            - Literal['error'] : Throw error.
        """

        data = {}
        for _dict in dicts:
            data.update(_dict)
        self.data = data
        self.default = default
    
    def __call__(self, *keys: Any) -> Any:
        """
        Indexes key value pair.
        """

        if keys == ():
            ret = self.data
        else:
            ret = {key: self.data[key] for key in keys}
        return ret

    def __getattr__(self, key: Any) -> Any:
        """
        Index value.
        """

        value = self.data[key]
        return value

    def __getitem__(self, indexes: Union[Any, Tuple]) -> Any:
        """
        Batch indexing directory values.
        """

        if type(indexes) == tuple:
            if self.default == "error":
                vals = [self.data[key] for key in indexes]
            else:
                vals = [self.data.get(key, self.default) for key in indexes]
        else:
            if self.default == "error":
                vals = self.data[indexes]
            else:
                vals = self.data.get(indexes, self.default)
        return vals

    def __setitem__(self, key: Any, value: Any) -> None:
        """
        Create or modify key value pair.
        """

        self.data[key] = value
    
    def __iter__(self) -> Iterator:
        """
        Return iterable directory keys.
        """

        return self.keys

    def __contains__(self, key: Any) -> bool:
        """
        Judge contain.
        """

        judge = key in self.data
        return judge

    def __len__(self) -> int:
        """
        Return directory length.
        """
        return self.len

    def __add__(self, parms: Dict) -> Dict:
        """
        Union directory.
        """

        if is_iterable(parms, [str, bytes, dict]):
            parms = {key: val for parm in parms for key, val in parm.items()}
        parms = {**self.data, **parms}
        return parms
    
    def __radd__(self, parms: Dict) -> Dict:
        """
        Union directory right.
        """

        if is_iterable(parms, [str, bytes, dict]):
            parms = {key: val for parm in parms for key, val in parm.items()}
        parms = {**parms, **self.data}
        return parms

    def __iadd__(self, parms: Dict) -> Any:
        """
        Union directory and definition.
        """

        if is_iterable(parms, [str, bytes, dict]):
            parms = {key: val for parm in parms for key, val in parm.items()}
        parms = {**self.data, **parms}
        self.data = parms
        return self

    def __sub__(self, parms: Iterable) -> Dict:
        """
        Difference directory.
        """
        
        main_set = set(self.data)
        sub_set = set(parms)
        diff_set = main_set - sub_set
        parms = {key: self.data[key] for key in diff_set}
        return parms

    def __rsub__(self, parms: Dict) -> Dict:
        """
        Difference directory right.
        """

        main_set = set(parms)
        sub_set = set(self.data)
        diff_set = main_set - sub_set
        parms = {key: parms[key] for key in diff_set}
        return parms

    def __isub__(self, parms: Dict) -> Any:
        """
        Difference directory and definition.
        """

        main_set = set(self.data)
        sub_set = set(parms)
        diff_set = main_set - sub_set
        parms = {key: self.data[key] for key in diff_set}
        self.data = parms
        return self

    def __and__(self, parms: Dict) -> Dict:
        """
        Intersection directory.
        """

        if is_iterable(parms, [str, bytes, dict]):
            parms = {key: val for parm in parms for key, val in parm.items()}
        main_set = set(self.data)
        sub_set = set(parms)
        inte_set = main_set & sub_set
        parms = {key: self.data[key] for key in inte_set}
        return parms

    def __rand__(self, parms: Dict) -> Dict:
        """
        Intersection directory right.
        """

        if is_iterable(parms, [str, bytes, dict]):
            parms = {key: val for parm in parms for key, val in parm.items()}
        main_set = set(parms)
        sub_set = set(self.data)
        inte_set = main_set & sub_set
        parms = {key: parms[key] for key in inte_set}
        return parms

    def __iand__(self, parms: Dict) -> Dict:
        """
        Intersection directory and definition.
        """

        if is_iterable(parms, [str, bytes, dict]):
            parms = {key: val for parm in parms for key, val in parm.items()}
        main_set = set(self.data)
        sub_set = set(parms)
        inte_set = main_set & sub_set
        parms = {key: self.data[key] for key in inte_set}
        self.data = parms
        return self

    def items(self) -> Iterator:
        """
        Get directory all keys and values.
        """

        items = self.data.items()
        return items

    def keys(self) -> Iterator:
        """
        Get directory all keys.
        """

        keys = self.data.keys()
        return keys

    def values(self) -> Iterator:
        """
        Get directory all values.
        """

        values = self.data.values()
        return values

    def get(self, keys: Union[Any, Iterable], default: Optional[Any] = None) -> Dict:
        """
        Batch get directory values.
        """

        if default == None and self.default != "error":
            default = self.default
        if is_iterable(keys):
            vals = [self.data.get(key, default) for key in keys]
        else:
            vals = self.data.get(keys, default)
        return vals

    def pop(self, keys: Union[Any, Iterable], default: Optional[Any] = None) -> Dict:
        """
        Batch pop directory values.
        """

        if default == None and self.default != "error":
            default = self.default
        if is_iterable(keys):
            vals = [self.data.pop(key, default) for key in keys]
        else:
            vals = self.data.pop(keys, default)
        return vals