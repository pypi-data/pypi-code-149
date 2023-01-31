from re import A, S
from autoai_ts_libs.deps.srom.imputation.pipeline_utils import ImputationKFold, TsIIDConsecutiveKFold
import numpy as np
import sys
import copy


def extreme_outlier(X, loc, factor, random_state):
    """_summary_

    Args:
        X (_type_): Numpy array
        loc (_type_): the place where outlier to be inserted
        factor (_type_): the relative factor by which outlier should be added
        random_state (_type_): random state to control the

    Returns:
        _type_: _description_
    """
    X_anomaly_place = np.full((X.shape[0], 1), 1, dtype=int)
    X_max = X.max(axis=0)
    X_min = X.min(axis=0)
    new_x = copy.copy(X)
    if random_state is not None:
        np.random.seed(random_state)
    for item in loc:
        new_x[item] = factor * np.random.choice([X_max[item[1]], X_min[item[1]]])
        X_anomaly_place[item[0]] = -1
    return new_x, X_anomaly_place


def std_based_outlier(X, loc, factor, random_state):
    """_summary_

    Args:
        X (_type_): Numpy array
        loc (_type_): the place where outlier to be inserted
        factor (_type_): the relative factor by which outlier should be added
        random_state (_type_): random state to control the

    Returns:
        _type_: _description_
    """
    X_anomaly_place = np.full((X.shape[0], 1), 1, dtype=int)
    new_x = copy.copy(X)
    if random_state is not None:
        np.random.seed(random_state)
    # calculate standard deviation as outlier
    X_std = X.std(axis=0)
    for item in loc:
        new_x[item] = new_x[item] + X_std[item[1]] * factor * np.random.choice(
            [-1, 1]
        )
        X_anomaly_place[item[0]] = -1
    return new_x, X_anomaly_place


def localized_extreme_outlier(X, loc, factor, random_state):
    """_summary_

    Args:
        X (_type_): Numpy array
        loc (_type_): the place where outlier to be inserted
        factor (_type_): the relative factor by which outlier should be added
        random_state (_type_): random state to control the

    Returns:
        _type_: _description_
    """
    X_anomaly_place = np.full((X.shape[0], 1), 1, dtype=int)
    new_x = copy.copy(X)
    if random_state is not None:
        np.random.seed(random_state)
    for item in loc:
        local_X_ = X[max(0, item[0] - 10) : min(item[0] + 10, len(X)), item[1]]
        local_std = np.std(local_X_)
        local_mean = np.mean(local_X_)
        value = np.random.choice([-1, 1]) * factor * local_std + local_mean
        new_x[item] = value
        X_anomaly_place[item[0]] = -1
    return new_x, X_anomaly_place


def variance_outlier(X, loc, mean, sigma, random_state):
    """_summary_

    Args:
        X (_type_): _description_
        loc (_type_): _description_
        mean (_type_): _description_
        sigma (_type_): _description_
        random_state (_type_): _description_

    Returns:
        _type_: _description_
    """
    clms = set([i[1] for i in loc])
    X_anomaly_place = np.full((X.shape[0], 1), 1, dtype=int)
    new_x = copy.copy(X)
    gloc = loc.copy()
    for clm in clms:
        loc = [item for item in gloc if item[1] == clm]
        loc = sorted(loc, key=lambda x: x[0])
        start = None
        end = None
        if mean is None:
            new_mean = np.mean(X[:, clm])*0.1
        else:
            new_mean = mean
        if sigma is None:
            new_sigma = np.std(X[:, clm])*0.3
        else:
            new_sigma = sigma
        for idx, item in enumerate(loc):
            if idx < len(loc) - 1:
                current_item = item[0]
                next_item = loc[idx + 1][0]
                if start == None:
                    start = current_item
                if next_item - current_item > 1:
                    end = current_item
            else:
                end = next_item

            if start != None and end != None and start!=end:
                tmp_x = new_x[list(range(start, end)), clm]
                if isinstance(random_state, int):
                    random_state = np.random.RandomState(random_state)
                    slope = random_state.normal(loc=new_mean, scale=new_sigma, size=tmp_x.shape)
                else:
                    slope = np.random.normal(loc=new_mean, scale=new_sigma, size=tmp_x.shape)
                if len(slope.shape) == 1:
                    slope = slope.reshape(-1, 1)
                for ii in list(range(start, end)):
                    new_x[ii, clm] = new_x[ii, clm] + slope[ii - start]
                X_anomaly_place[start:end] = -1
                start = None

    return new_x, X_anomaly_place


def trend_outlier(X, loc, factor, random_state):
    """_summary_

    Args:
        X (_type_): _description_
        loc (_type_): _description_
        outlier_factor (_type_): _description_
        random_state (_type_): _description_

    Returns:
        _type_: _description_
    """
    clms = set([i[1] for i in loc])
    X_anomaly_place = np.full((X.shape[0], 1), 1, dtype=int)
    new_x = copy.copy(X)
    gloc = loc.copy()
    
    for clm in clms:
        loc = [item for item in gloc if item[1] == clm]
        loc = sorted(loc, key=lambda x: x[0])
        start = None
        end = None
        max_val = np.max(X[:,clm])*factor 
        min_val = np.min(X[:,clm])*factor
            
        for idx, item in enumerate(loc):
            if idx < len(loc) - 1:
                current_item = item[0]
                next_item = loc[idx + 1][0]
                if start == None:
                    start = current_item
                if next_item - current_item > 1:
                    end = current_item

            else:
                end = next_item
            
            if start != None and end != None and start!=end :
                if random_state is not None:
                    np.random.seed(random_state)
                size =  end - start
                slope=np.linspace(min_val,max_val,size)
                slope = np.random.choice([-1, 1])*slope
                if len(slope.shape) == 1:
                    slope = slope.reshape(-1, 1)
                for ii in list(range(start, end)):
                    new_x[ii, clm] = new_x[ii, clm] + slope[ii - start]
                X_anomaly_place[start + 1 : end] = -1
                start = None
                end = None

    return new_x, X_anomaly_place


def jitter_outlier(X, loc, factor, random_state):
    """_summary_

    Args:
        X (_type_): _description_
        loc (_type_): _description_
        outlier_factor (_type_): _description_
        random_state (_type_): _description_

    Returns:
        _type_: _description_
    """
    clms = set([i[1] for i in loc])
    X_anomaly_place = np.full((X.shape[0], 1), 1, dtype=int)
    new_x = copy.copy(X)
    gloc = loc.copy()
    for clm in clms:
        loc = [item for item in gloc if item[1] == clm]
        loc = sorted(loc, key=lambda x: x[0])
        start = None
        end = None
        outlier_factor = abs((np.max(X[:, clm]) - np.min(X[:, clm])))/2
        for idx, item in enumerate(loc):
            if idx < len(loc) - 1:
                current_item = item[0]
                next_item = loc[idx + 1][0]
                if start == None:
                    start = current_item
                if next_item - current_item > 1:
                    end = current_item
            else:
                end = next_item

            if start != None and end != None and start!=end:
                if random_state is not None:
                    np.random.seed(random_state)
                r_factor = np.random.choice(factor)*outlier_factor
                diff = (
                    np.diff(X[start - 1 : end, clm], axis=0)
                    if start > 0
                    else np.insert(np.diff(X[start:end, clm]), 0, 0)
                )
                if len(diff.shape) == 1:
                    diff = diff.reshape(-1, 1)

                for ii in list(range(start, end)):
                    new_x[ii, clm] = (
                        new_x[ii, clm] + (r_factor ) * diff[ii - start]
                    )
                X_anomaly_place[start:end] = -1
                start = None
                end = None

    return new_x, X_anomaly_place

def level_shift_outlier(X, loc, factor, random_state):
    """
    """
    X_anomaly_place = np.full((X.shape[0], 1), 1, dtype=int)
    new_x = copy.copy(X)
    if random_state is not None:
        np.random.seed(random_state)
    loc = sorted(loc, key=lambda x: x[0])
    start = loc[-1][0]
    start = max(1,start)
    #Calculate % distance of max point from end 
    dist = int(start/len(X)*100)
    dist = max(1,dist)
    if  dist < 70:
        #new point should lie between 70 to 98 %
        p_range = 98-70
        selected_per = 70 + int(dist*p_range/100)
        start = int(selected_per*len(X)/100)
    
    col = loc[-1][1]
    rand_sign = np.random.choice([-1, 1])
    factor = new_x[start,col]*factor
    line = np.linspace(factor,factor, num=len(X)-start)
    if len(line.shape)==1:
        line = line.reshape(-1,1)
    new_x[start:,[col]] = new_x[start:,[col]] + line  * rand_sign
    X_anomaly_place[start:] = -1
    return new_x, X_anomaly_place

def flat_line_outlier(X, loc, line_value, random_state):
    """_summary_

    Args:
        X (_type_): _description_
        loc (_type_): _description_
        line_value (_type_): _description_, zero, maxfloat, max, min, mean
        random_state (_type_): _description_

    Returns:
        _type_: _description_
    """
    clms = set([i[1] for i in loc])
    X_anomaly_place = np.full((X.shape[0], 1), 1, dtype=int)
    new_x = copy.copy(X)
    gloc = loc.copy()
    minX = np.max(X)
    maxX = np.min(X)
    for clm in clms:
        loc = [item for item in gloc if item[1] == clm]
        loc = sorted(loc, key=lambda x: x[0])
        start = None
        end = None
        for idx, item in enumerate(loc):
            if idx < len(loc) - 1:
                current_item = item[0]
                next_item = loc[idx + 1][0]
                if start == None:
                    start = current_item
                if next_item - current_item > 1:
                    end = current_item
            else:
                end = next_item

            if start != None and end != None and start!=end:
                if random_state is not None:
                    np.random.seed(random_state)
                flat_value = 0
                if line_value == "mean":
                    flat_value = (
                        np.mean(X[start - 1 : end, clm], axis=0)
                        if start > 0
                        else np.mean(X[start:end, clm])
                    )
                new_x[list(range(start, end)), clm] = flat_value
                X_anomaly_place[start:end] = -1
                start = None
                end = None

    return new_x, X_anomaly_place


class AnomalyKFold(ImputationKFold):
    def __init__(
        self,
        anomaly_generator_fun,
        n_iteration=10,
        random_state=None,
        anomaly_size=0.1,
        anomaly_factor=8,
        columns_to_ignore=None,
    ):
        """_summary_

        Args:
            n_iteration (int, optional): _description_. Defaults to 10.
            random_state (_type_, optional): _description_. Defaults to None.
            anomaly_size (float, optional): _description_. Defaults to 0.1.
            anomaly_generator_fun (_type_, optional): _description_. Defaults to add_max_value_of_float_as_outlier.
        """
        self.anomaly_generator_fun = anomaly_generator_fun
        self.anomaly_factor = anomaly_factor
        super(AnomalyKFold, self).__init__(
            n_iteration=n_iteration,
            random_state=random_state,
            impute_size=anomaly_size,
            missing_value=np.NaN,
            first_nullable=False,
            last_nullable=False,
            enable_debug=False,
            return_index=True,
            columns_to_ignore=columns_to_ignore,
        )

    def split(self, X, y=None, groups=None):
        """
        Parameters
        ----------
            X (numpy array): Input features.
            y(numpy array): Target feature.

        Returns
        --------
            Splitted train with externally added missing values and test sets with
            original values.
        """
        for item in super(AnomalyKFold, self).split(X, y, groups):
            yield self.anomaly_generator_fun(X, item[0], self.anomaly_factor, self.random_state)


class MCARImputationKFold(ImputationKFold):
    def __init__(
        self,
        anomaly_generator_fun,
        n_iteration=10,
        random_state=None,
        anomaly_size=0.1,
        anomaly_factor=8,
        columns_to_ignore=None,
    ):
        """_summary_

        Args:
            n_iteration (int, optional): _description_. Defaults to 10.
            random_state (_type_, optional): _description_. Defaults to None.
            anomaly_size (float, optional): _description_. Defaults to 0.1.
            anomaly_generator_fun (_type_, optional): _description_. Defaults to add_max_value_of_float_as_outlier.
        """
        self.anomaly_generator_fun = anomaly_generator_fun
        self.anomaly_factor = anomaly_factor
        super(MCARImputationKFold, self).__init__(
            n_iteration=n_iteration,
            random_state=random_state,
            impute_size=anomaly_size,
            missing_value=np.NaN,
            return_index=True,
            columns_to_ignore=columns_to_ignore,
        )

    def split(self, X, y=None, groups=None):
        """
        Parameters
        ----------
            X (numpy array): Input features.
            y(numpy array): Target feature.

        Returns
        --------
            Splitted train with externally added missing values and test sets with
            original values.
        """
        for item in super(MCARImputationKFold, self).split(X, y, groups):
            yield self.anomaly_generator_fun(X, item[0], 2, self.random_state)


class ExtremeOutlier(AnomalyKFold):
    def __init__(
        self,
        anomaly_generator_fun=extreme_outlier,
        n_iteration=10,
        random_state=None,
        anomaly_size=0.1,
        anomaly_factor=2,
        columns_to_ignore=None,
    ):
        """_summary_

        Args:
            n_iteration (int, optional): _description_. Defaults to 10.
            random_state (_type_, optional): _description_. Defaults to None.
            anomaly_size (float, optional): _description_. Defaults to 0.1.
            anomaly_factor (int, optional): _description_. Defaults to 8. It can be 2,4,5.
            columns_to_ignore (int, optional): column to be ignored.
        """
        super(ExtremeOutlier, self).__init__(
            n_iteration=n_iteration,
            random_state=random_state,
            anomaly_size=anomaly_size,
            anomaly_generator_fun=anomaly_generator_fun,
            columns_to_ignore=columns_to_ignore,
            anomaly_factor=anomaly_factor,
        )

class LocalizedExtremeOutlier(AnomalyKFold):
    def __init__(
        self,
        anomaly_generator_fun=localized_extreme_outlier,
        n_iteration=10,
        random_state=None,
        anomaly_size=0.1,
        anomaly_factor=2,
        columns_to_ignore=None,
    ):
        """_summary_

        Args:
            n_iteration (int, optional): _description_. Defaults to 10.
            random_state (_type_, optional): _description_. Defaults to None.
            anomaly_size (float, optional): _description_. Defaults to 0.1.
            anomaly_factor (int, optional): _description_. Defaults to 2. It can be 2,3
            columns_to_ignore (int, optional): _description_. Defaults to None.
        """
        super(LocalizedExtremeOutlier, self).__init__(
            n_iteration=n_iteration,
            random_state=random_state,
            anomaly_size=anomaly_size,
            anomaly_generator_fun=anomaly_generator_fun,
            columns_to_ignore=columns_to_ignore,
            anomaly_factor=anomaly_factor,
        )

class LevelShiftOutlier(AnomalyKFold):
    def __init__(
        self,
        anomaly_generator_fun=level_shift_outlier,
        n_iteration=10,
        random_state=None,
        anomaly_size=0.1,
        anomaly_factor=2,
        columns_to_ignore=None,
    ):
        """_summary_

        Args:
            n_iteration (int, optional): _description_. Defaults to 10.
            random_state (_type_, optional): _description_. Defaults to None.
            anomaly_size (float, optional): _description_. Defaults to 0.1.
            anomaly_factor (int, optional): _description_. Defaults to 2. It can be 2,3
            columns_to_ignore (int, optional): _description_. Defaults to None.
        """
        super(LevelShiftOutlier, self).__init__(
            n_iteration=n_iteration,
            random_state=random_state,
            anomaly_size=anomaly_size,
            anomaly_generator_fun=anomaly_generator_fun,
            columns_to_ignore=columns_to_ignore,
            anomaly_factor=anomaly_factor,
        )

class DeviationbasedExtremeOutlier(AnomalyKFold):
    def __init__(
        self,
        anomaly_generator_fun=std_based_outlier,
        n_iteration=10,
        random_state=None,
        anomaly_size=0.1,
        anomaly_factor=2,
        columns_to_ignore=None,
    ):
        """_summary_

        Args:
            n_iteration (int, optional): _description_. Defaults to 10.
            random_state (_type_, optional): _description_. Defaults to None.
            anomaly_size (float, optional): _description_. Defaults to 0.1.
            anomaly_factor (int, optional): _description_. Defaults to 2. It can be 2 or 3.
            columns_to_ignore (int, optional): _description_. Defaults to None.
        """
        super(DeviationbasedExtremeOutlier, self).__init__(
            n_iteration=n_iteration,
            random_state=random_state,
            anomaly_size=anomaly_size,
            anomaly_generator_fun=anomaly_generator_fun,
            columns_to_ignore=columns_to_ignore,
            anomaly_factor=anomaly_factor,
        )

class TrendOutlier(TsIIDConsecutiveKFold):
    def __init__(
        self,
        n_iteration=10,
        random_state=None,
        anomaly_size=0.1,
        anomaly_factor=2,
        n_consecutive=0.07,
        columns_to_ignore=None,
    ):
        """_summary_

        Args:
            n_iteration (int, optional): _description_. Defaults to 10.
            random_state (_type_, optional): _description_. Defaults to None.
            anomaly_size (float, optional): _description_. Defaults to 0.1.
            anomaly_factor (int, optional): _description_. Defaults to 2. It can be 2 or 3.
            n_consecutive(int, optional): Default 10.
            columns_to_ignore (int, optional): _description_. Defaults to None.
        """
        self.anomaly_generator_fun = trend_outlier
        self.anomaly_factor = anomaly_factor
        super(TrendOutlier, self).__init__(
            n_iteration=n_iteration,
            random_state=random_state,
            impute_size=anomaly_size,
            n_consecutive=n_consecutive,
            return_index=True,
            columns_to_ignore=columns_to_ignore,
        )

    def split(self, X, y=None, groups=None):
        """
        Parameters
        ----------
            X (numpy array): Input features.
            y(numpy array): Target feature.

        Returns
        --------
            Splitted train with externally added missing values and test sets with
            original values.
        """
        self.n_consecutive = max(3,self.n_consecutive)

        for item in super(TrendOutlier, self).split(X, y, groups):
            yield self.anomaly_generator_fun(
                X, item[0], self.anomaly_factor, self.random_state
            )


class VarianceOutlier(TsIIDConsecutiveKFold):
    def __init__(
        self,
        n_iteration=10,
        random_state=None,
        anomaly_size=0.1,
        sigma=None,
        mean=None,
        n_consecutive=10,
        columns_to_ignore=None,
    ):
        """_summary_

        Args:
            n_iteration (int, optional): _description_. Defaults to 10.
            random_state (_type_, optional): _description_. Defaults to None.
            anomaly_size (float, optional): _description_. Defaults to 0.1.
            sigma (float, optional): _description_. Defaults to None.
            mean (float, optional): _description_. Defaults to None.
            n_consecutive(int, optional): Default 10.
            columns_to_ignore (int, optional): _description_. Defaults to None.

        """
        self.anomaly_generator_fun = variance_outlier
        self.mean = mean
        self.sigma = sigma
        super(VarianceOutlier, self).__init__(
            n_iteration=n_iteration,
            random_state=random_state,
            impute_size=anomaly_size,
            n_consecutive=n_consecutive,
            return_index=True,
            columns_to_ignore=columns_to_ignore,
        )

    def split(self, X, y=None, groups=None):
        """
        Parameters
        ----------
            X (numpy array): Input features.
            y(numpy array): Target feature.

        Returns
        --------
            Splitted train with externally added missing values and test sets with
            original values.
        """
        self.n_consecutive = max(3,self.n_consecutive)
        
        for item in super(VarianceOutlier, self).split(X, y, groups):
            yield self.anomaly_generator_fun(
                X, item[0], self.mean, self.sigma, self.random_state
            )


class JitterOutlier(TsIIDConsecutiveKFold):
    def __init__(
        self,
        n_iteration=10,
        random_state=None,
        anomaly_size=0.1,
        outlier_factor=[2,3],
        n_consecutive=10,
        columns_to_ignore=None,
    ):
        """_summary_

        Args:
            n_iteration (int, optional): _description_. Defaults to 10.
            random_state (_type_, optional): _description_. Defaults to None.
            anomaly_size (float, optional): _description_. Defaults to 0.1.
            anomaly_factor (int, optional): _description_. Defaults to 2. It can be 2 or 3.
            n_consecutive(int, optional): Default 10.
            columns_to_ignore (int, optional): _description_. Defaults to None.

        """
        self.anomaly_generator_fun = jitter_outlier
        self.outlier_factor = outlier_factor
        super(JitterOutlier, self).__init__(
            n_iteration=n_iteration,
            random_state=random_state,
            impute_size=anomaly_size,
            n_consecutive=n_consecutive,
            return_index=True,
            columns_to_ignore=columns_to_ignore,
        )

    def split(self, X, y=None, groups=None):
        """
        Parameters
        ----------
            X (numpy array): Input features.
            y(numpy array): Target feature.

        Returns
        --------
            Splitted train with externally added missing values and test sets with
            original values.
        """
        self.n_consecutive = max(3,self.n_consecutive)

        for item in super(JitterOutlier, self).split(X, y, groups):
            yield self.anomaly_generator_fun(
                X, item[0], self.outlier_factor, self.random_state
            )


class FlatLineOutlier(TsIIDConsecutiveKFold):
    def __init__(
        self,
        n_iteration=10,
        random_state=None,
        anomaly_size=0.1,
        line_value="mean",
        n_consecutive=10,
        columns_to_ignore=None,
    ):
        """_summary_

        Args:
            n_iteration (int, optional): _description_. Defaults to 10.
            random_state (_type_, optional): _description_. Defaults to None.
            anomaly_size (float, optional): _description_. Defaults to 0.1.
            line_value (str, optional): _description_. Defaults to mean.
            n_consecutive(int, optional): Default 10.
            columns_to_ignore (int, optional): _description_. Defaults to None.

        """
        self.anomaly_generator_fun = flat_line_outlier
        self.line_value = line_value
        super(FlatLineOutlier, self).__init__(
            n_iteration=n_iteration,
            random_state=random_state,
            impute_size=anomaly_size,
            n_consecutive=n_consecutive,
            return_index=True,
            columns_to_ignore=columns_to_ignore,
        )

    def split(self, X, y=None, groups=None):
        """
        Parameters
        ----------
            X (numpy array): Input features.
            y(numpy array): Target feature.

        Returns
        --------
            Splitted train with externally added missing values and test sets with
            original values.
        """
        self.n_consecutive = max(3,self.n_consecutive)
            
        for item in super(FlatLineOutlier, self).split(X, y, groups):
            yield self.anomaly_generator_fun(
                X, item[0], self.line_value, self.random_state
            )


# if __name__ == "__main__":
#     x = np.random.rand(50, 1)

#     # cv = MCARKFold(n_iteration=5)
#     # cv = MARKFold(n_iteration=5)
#     # cv = TsIIDConsecutiveKFold(return_index=True)
#     # cv = TrendOutlierKFold(random_state=1)
#     # cv = MARImputationKFold()
#     # cv = MNARImputationKFold()
#     for newts, location in cv.split(x):
#         print(newts, "location", location)
