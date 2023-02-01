from sklearn.metrics import median_absolute_error

from dmm.metric.metric_base import ModelMetricBase


class MedianAbsoluteError(ModelMetricBase):
    """
    An example of how to calculate the median absolute error of the difference
    between predictions and actuals. This metric is stateless
    """

    def __init__(self):
        super().__init__(
            name="Median Absolute Error",
            description="Median absolute error between prediction and actual value",
            need_training_data=False,
        )

    def score(self, predictions=None, actuals=None, **kwargs) -> float:
        return median_absolute_error(actuals, predictions)
