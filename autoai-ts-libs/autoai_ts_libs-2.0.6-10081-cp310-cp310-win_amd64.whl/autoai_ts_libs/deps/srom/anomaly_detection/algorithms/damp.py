# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.

from sklearn.base import BaseEstimator
import numpy as np
import numpy.fft as fft
from scipy.signal import convolve

class DAMP(BaseEstimator):
    """ 
    Discord aware Matrix Profile for Time Series
    """

    def __init__(self, lookback_win=50, lookahead_factor = 32, lookaback_factor = 16, handle_training=True):
        """
        Parameters:
            window_size : subsequence length,
            sp_index : start index
        """
        self.handle_training = handle_training
        self.lookback_win = lookback_win
        self.lookahead_factor = lookahead_factor
        self.lookaback_factor = lookaback_factor
        
    def _pre_fit(self, lenX):
        """
        """
        self.train_size_ = lenX
        self.PV_ = np.ones(lenX, dtype=int)
        self.aMP_ = np.zeros(lenX, dtype=float)
        self.x_lag_ = int(2**int(np.ceil(np.log2(self.lookaback_factor * self.lookback_win))))
        self.lookahead_lag_ = int(2**int(np.ceil(np.log2((self.lookahead_factor * self.lookback_win)))))
        self.sp_index_ = 4 * self.lookback_win
        self.bsf_ = 0

    def fit(self, X, y=None):
        """
        Train Model
        """
        self._pre_fit(len(X))
        if self.handle_training:
            self._handle_training(X)
            
        # start from sp_index and stop at the last window
        for i in range(self.sp_index_, len(X) - self.lookback_win + 1):
            
            if not self.PV_[i]: # decided to skip the processing at index "i"
                #if self.aMP_[i-1] - 0.00000000001 > 0:
                #    self.aMP_[i] = self.aMP_[i-1] - 0.00000000001
                #else:
                #    self.aMP_[i] = 0
                continue

            # process backward
            self.aMP_[i] = self._backward_processing(X, i)

            # look forward
            self._forward_processing(X, i)

        return self

    def _backward_processing(self, X, i):
        """
        Going in backword direction
        """
        amp_i = np.inf
        prefix = 2**int(np.ceil(np.log2(self.lookback_win)))
        max_lag = min(self.x_lag_ or i, i)
        reference_ts = X[i-max_lag:i]
        
        first = True
        expansion_num = 0

        # find the discord 
        while amp_i >= self.bsf_:
            
            if prefix >= max_lag:  # search reaches the beginning of the time series, current score
                amp_i = min(self._distance(X[i:i+self.lookback_win], reference_ts))
                if amp_i > self.bsf_:
                    self.bsf_ = amp_i
                break
            else:
                if first:
                    first = False
                    start = i - prefix
                    end = i
                    amp_i = min(self._distance(X[i:i+self.lookback_win], reference_ts[-prefix:]))
                else:
                    start = i - prefix + (expansion_num * self.lookback_win)
                    end = int(i - (prefix/2) + (expansion_num * self.lookback_win))
                    amp_i = min(self._distance(X[i:i+self.lookback_win], X[start:end]))

                if amp_i < self.bsf_:
                    if 2 * prefix < max_lag:
                        # make some random points for comparision, 
                        # just to further make the sampling correct for discord discovery
                        # work to be done for early exit
                        pass
                    break
                elif amp_i == 0:
                    break
                else:
                    prefix = 2 * prefix
                    expansion_num *= 1

        return amp_i

    def _distance(self, Q, T, naive=False):
        """
        Distance
        """
        
        if not naive:
            return self.mass(Q, T)
        
        m = Q.shape[0]
        if Q.ndim == 2 and Q.shape[1] == 1:
            Q = Q.flatten()

        n = T.shape[0]
        if T.ndim == 2 and T.shape[1] == 1:  # pragma: no cover
            T = T.flatten()
                
        distance_profile = np.empty(n - m + 1, dtype=np.float64)
        Q = (Q - Q.mean())/Q.std()

        if np.any(~np.isfinite(Q)):
            distance_profile[:] = np.inf
        else:
            for i in range(n - m + 1):
                P = T[i:i+len(Q)]
                P = (P - P.mean())/P.std()
                if np.any(~np.isfinite(P)):
                    distance_profile[i] = np.sqrt(np.sum(np.square(Q-P)))
        
        return distance_profile
        
    def _forward_processing(self, X, i):
        """
        ---
        """
        start = i + self.lookback_win
        end = start + self.lookahead_lag_
        
        if end > len(X):
            end = len(X)

        if start < end and end-start > self.lookback_win:
            indices = []
            d = self._distance(X[i:i+self.lookback_win], X[start:end])
            indices = np.argwhere(d < self.bsf_)
            indices += start
            self.PV_[indices] = 0
            
            indices = []
            indices = np.argwhere(d <= 0)
            indices += start
            self.PV_[indices] = 0
        

    def _handle_training(self, X):
        """
        """
        # optimization
        for i in range(self.sp_index_, min(self.sp_index_ + (16 * self.lookback_win), self.PV_.shape[0])):
            # elimination process
            if not self.PV_[i]:
                if self.aMP_[i-1]-0.00000000001 > 0:
                    self.aMP_[i] = self.aMP_[i-1]-0.00000000001
                else:
                    self.aMP_[i] = 0
                continue

            # reached to the boarder
            if i + self.lookback_win > X.shape[0]:
                break

            # quick backword processing
            query = X[i:i+self.lookback_win]
            self.aMP_[i] = min(self._distance(query, X[:i]))
            self.bsf_ = max(self.aMP_)

            if self.lookahead_lag_ > 0:
                # skip the lookback window
                start_of_mass = min(i+self.lookback_win, X.shape[0])
                # traverse max lookback in forward direction 
                end_of_mass = min(start_of_mass+self.lookahead_lag_, X.shape[0])

                if (end_of_mass - start_of_mass + 1) > self.lookback_win:
                    distance_profile = self._distance(query, X[start_of_mass:end_of_mass])
                    dp_index_less_than_BSF = np.argwhere(distance_profile < self.bsf_)
                    ts_index_less_than_BSF = dp_index_less_than_BSF + start_of_mass
                    self.PV_[ts_index_less_than_BSF] = 0

                    # this is for distance zero
                    dp_index_equal_to_zero = np.argwhere(distance_profile == 0)
                    ts_index_equal_to_zero = dp_index_equal_to_zero + start_of_mass
                    self.PV_[ts_index_equal_to_zero] = 0                    

    def predict(self, X):
        pass


    def transpose_dataframe(self, df):
        if type(df).__name__ == "DataFrame":
            return df.T
        return df

    def check_dtype(self, a, dtype=np.float64):
        if dtype == int:
            dtype = np.int64
        if dtype == float:
            dtype = np.float64
        if not np.issubdtype(a.dtype, dtype):
            msg = f"{dtype} dtype expected but found {a.dtype} in input array\n"
            msg += "Please change your input `dtype` with `.astype(dtype)`"
            raise TypeError(msg)

        return True

    def slidingDotProduct(self, Q,T):
        n = T.shape[0]
        m = Q.shape[0]
        Qr = np.flipud(Q)  # Reverse/flip Q
        QT = convolve(Qr, T)
        return QT.real[m - 1 : n]

    def _calculate_squared_distance(self, m, QT, Q1, _Q, M_T, _T):
        denom = m * _Q * _T
        D_squared = np.abs(2 * m * (1.0 - (QT - m * Q1 * M_T) / denom))
        return D_squared

    def _calculate_squared_distance_profile(self, m, QT, Q1, _Q, M_T, _T):
        k = M_T.shape[0]
        D_squared = np.empty(k, dtype=np.float64)

        for i in range(k):
            D_squared[i] = self._calculate_squared_distance(m, QT[i], Q1, _Q, M_T[i], _T[i])

        return D_squared

    def calculate_distance_profile(self, m, QT, Q1, _Q, M_T, _T):
        D_squared = self._calculate_squared_distance_profile(m, QT, Q1, _Q, M_T, _T)
        return np.sqrt(D_squared)

    def _preprocess(self, T):
        T = T.copy()
        T = self.transpose_dataframe(T)
        T = np.asarray(T)
        self.check_dtype(T)
        return T

    def compute_mean_std(self, ts, m):
        """
        Calculate the mean and standard deviation within a moving window passing across a time series.

        Parameters
        ----------
        ts: Time series to evaluate.
        m: Width of the moving window.
        """
        if m <= 1:
            raise ValueError("Query length must be longer than one")

        ts = ts.astype("float")
        #Add zero to the beginning of the cumsum of ts
        s = np.insert(np.cumsum(ts),0,0)
        #Add zero to the beginning of the cumsum of ts ** 2
        sSq = np.insert(np.cumsum(ts ** 2),0,0)
        segSum = s[m:] - s[:-m]
        segSumSq = sSq[m:] -sSq[:-m]

        movmean = segSum/m
        movstd = np.sqrt(segSumSq / m - (segSum/m) ** 2)

        return movmean, movstd

    def check_window_size(self, m, max_size=None):
        if m <= 2:
            raise ValueError(
                "All window sizes must be greater than or equal to three",
            )

        if max_size is not None and m > max_size:
            raise ValueError(f"The window size must be less than or equal to {max_size}")

    def preprocess(self, T, m):
        T = self._preprocess(T)
        self.check_window_size(m, max_size=len(T))
        T[np.isinf(T)] = np.nan
        M_T, _T = self.compute_mean_std(T, m)
        T[np.isnan(T)] = 0

        return T, M_T, _T

    def _mass(self, Q, T, QT, Q1, _Q, M_T, _T):
        m = Q.shape[0]
        return self.calculate_distance_profile(m, QT, Q1, _Q, M_T, _T)

    def mass(self, Q, T, M_T=None, _T=None, normalize=True, p=2.0):
        Q = self._preprocess(Q)
        m = Q.shape[0]

        T = self._preprocess(T)
        n = T.shape[0]

        distance_profile = np.empty(n - m + 1, dtype=np.float64)

        if np.any(~np.isfinite(Q)):
            distance_profile[:] = np.inf
        else:
            if M_T is None or _T is None:
                T, M_T, _T = self.preprocess(T, m)

            QT = self.slidingDotProduct(Q, T)
            Q1, _Q = self.compute_mean_std(Q, m)
            Q1 = Q1[0]
            _Q = _Q[0]
            distance_profile[:] = self._mass(Q, T, QT, Q1, _Q, M_T, T)

        return distance_profile
    
    def anomaly_score(self, X):
        # now we get more samples
        self.test_PV_ = np.ones(len(X), dtype=int)
        self.test_aMP_ = np.zeros(len(X), dtype=float)

        back_processingX = None
        foreward_processingX = None
    
        for i in range(0,len(X)-self.lookback_win+1):
            # optimization
            if not self.test_PV_[i]:
                self.test_aMP_[i] = self.test_aMP_[i-1]-0.00001
                continue

            # prepare X and pass
            
            # process backward
            self.test_aMP_[i] = self._backward_processing(back_processingX, i)

            # look forward
            self._forward_processing(X, i)
            
        return self.test_aMP_
