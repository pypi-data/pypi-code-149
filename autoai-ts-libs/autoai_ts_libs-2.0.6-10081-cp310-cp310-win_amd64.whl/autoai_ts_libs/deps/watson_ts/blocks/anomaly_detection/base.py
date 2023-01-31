"""
Shared base class for anomaly detection estimators. Anomaly estimators support fit, predict, anomaly_score.
"""

# Standard
import abc

# Local
from ...blocks.base import EstimatorBlockBase
from ...toolkit.timeseries_conversions import TimeseriesType


class AnomalyDetectorBase(EstimatorBlockBase):
    __doc__ = __doc__

    @abc.abstractmethod
    def anomaly_score(
        self, timeseries: TimeseriesType, *args, **kwargs
    ) -> TimeseriesType:
        """The anomaly_score method provides an indication of the degree of abnormality

        Args:
            timeseries: TimeseriesType
                The timeseries data to fit the model to.

        Kwargs:
            **kwargs: Dict[str, any]
                Additional keyword arguments that can influence the anomaly_score
                operation.

        Returns:
            anomaly_score: Time series type
                The anomaly score is another time series where the values indicate the
                degree of abnormality
        """


class SKLearnAnomalyDetectorMixin(AnomalyDetectorBase):
    def anomaly_score(
        self, timeseries: TimeseriesType, *args, **kwargs
    ) -> TimeseriesType:
        """Delegate anomaly_score to the wrapped pipeline"""
        with self._convert_to_internal_timeseries_type(timeseries, **kwargs) as (
            timeseries,
            kwargs,
        ):
            return self._wrapped_model.anomaly_score(timeseries, *args, **kwargs)
