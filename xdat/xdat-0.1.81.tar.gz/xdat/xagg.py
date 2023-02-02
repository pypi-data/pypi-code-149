import numpy as np


class _Agg:
    def __init__(self, col_name):
        self.col_name = col_name

    def _get_func(self):
        raise NotImplemented

    def as_tuple(self):
        func = self._get_func()
        return self.col_name, func


class _AggMultiCol:
    def __init__(self, *col_names, **kwargs):
        self.col_names = list(col_names)
        self.kwargs = kwargs

    def calc_func(self, df, **kwargs):
        raise NotImplemented


class Count(_Agg):
    def __init__(self):
        super().__init__(None)

    def _get_func(self):
        return np.size


class Min(_Agg):
    def _get_func(self):
        return np.min


class Max(_Agg):
    def _get_func(self):
        return np.max


class Mean(_Agg):
    def _get_func(self):
        return np.mean


class Std(_Agg):
    def _get_func(self):
        return np.std


class Sum(_Agg):
    def _get_func(self):
        return np.sum


class Any(_Agg):
    def _get_func(self):
        return lambda x: x.values[0] if len(x) else np.NaN


class UniqueVals(_Agg):
    def _get_func(self):
        return lambda x: np.unique(x.values).tolist() if len(x) else []


class Lambda(_Agg):
    def __init__(self, col_name, func):
        super().__init__(col_name)
        self.func = func

    def _get_func(self):
        return self.func


class WMean(_AggMultiCol):
    def __init__(self, col_name, weight_col=None):
        assert weight_col, 'must specify weight column'
        super().__init__(col_name, weight_col)
        self.main_col = col_name
        self.weight_col = weight_col

    def calc_func(self, df, **kwargs):
        if df[self.weight_col].sum() == 0:
            return np.NaN

        return np.average(df[self.main_col], weights=df[self.weight_col])


class LambdaMultiCol(_AggMultiCol):
    def __init__(self, col_name, func):
        raise NotImplemented

