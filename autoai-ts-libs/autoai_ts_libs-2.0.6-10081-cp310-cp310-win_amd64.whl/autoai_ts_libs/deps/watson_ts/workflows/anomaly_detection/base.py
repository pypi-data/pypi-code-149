"""
Shared baseclasses for anomaly detection pipelines. Anomaly pipelines support fit, predict, anomaly_score.
"""

# Standard
import abc

# Local
from ...toolkit.prediction_types import PredictionTypes
from ...toolkit.timeseries_conversions import TimeseriesType
from ..base import TSWorkflowBase
from ..sklearn_mixins import SKLearnWorkflowMixin


class AnomalyDetectorWorkflowBase(TSWorkflowBase):
    __doc__ = __doc__

    @abc.abstractmethod
    def anomaly_score(
        self, timeseries: TimeseriesType, *args, **kwargs
    ) -> TimeseriesType:
        """The anomaly_score methods provides an indication of the degree of abnormality

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


class SKLearnAnomalyDetectorWorkflowMixin(AnomalyDetectorWorkflowBase):
    """
    Mixin for sklearn native anomlay detector workflows
    """

    def anomaly_score(
        self, timeseries: TimeseriesType, *args, **kwargs
    ) -> TimeseriesType:
        """Delegate anomaly_score to the wrapped pipeline"""
        with self._convert_to_internal_timeseries_type(timeseries, **kwargs) as (
            timeseries,
            kwargs,
        ):
            return self._wrapped_model.anomaly_score(timeseries, *args, **kwargs)


class SROMPredictionTypeMixin:
    def predict(self, X: TimeseriesType, *args, **kwargs) -> TimeseriesType:
        """Predict method. Calls the predict method of the superclass, but handles the prediction
        type appropriately.

        Args:
            X (TimeseriesType): Time series input

        Returns:
            TimeseriesType: Output predictions
        """

        with self._convert_to_internal_timeseries_type(X, **kwargs) as (
            X,
            kwargs,
        ):
            if "prediction_type" not in kwargs:
                kwargs["prediction_type"] = PredictionTypes.Sliding.value

            return self._wrapped_model.predict(X, **kwargs)
