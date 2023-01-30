# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.


from typing import Optional


from .._uniffi import CommonMetricData
from .._uniffi import TimeUnit
from .._uniffi import TimespanMetric
from ..testing import ErrorType


class TimespanMetricType:
    """
    This implements the developer facing API for recording timespan metrics.

    Instances of this class type are automatically generated by
    `glean.load_metrics`, allowing developers to record values that were
    previously registered in the metrics.yaml file.

    The timespan API exposes the `TimespanMetricType.start`,
    `TimespanMetricType.stop` and `TimespanMetricType.cancel` methods.
    """

    def __init__(
        self,
        common_metric_data: CommonMetricData,
        time_unit: TimeUnit,
    ):
        self._inner = TimespanMetric(common_metric_data, time_unit)

    def start(self) -> None:
        """
        Start tracking time for the provided metric.

        This records an error if it’s already tracking time (i.e. `start` was
        already called with no corresponding `stop`): in that case the original
        start time will be preserved.
        """
        self._inner.start()

    def stop(self) -> None:
        """
        Stop tracking time for the provided metric.

        Sets the metric to the elapsed time, but does not overwrite an already
        existing value.
        This will record an error if no `start` was called or there is an already
        existing value.
        """
        self._inner.stop()

    def cancel(self) -> None:
        """
        Abort a previous `start` call. No error is recorded if no `start` was called.
        """
        self._inner.cancel()

    class _TimespanContextManager:
        """
        A context manager for recording timings. Used by the `measure` method.
        """

        def __init__(self, timespan: "TimespanMetricType"):
            self._timespan = timespan

        def __enter__(self) -> None:
            self._timespan.start()

        def __exit__(self, type, value, tb) -> None:
            if tb is None:
                self._timespan.stop()
            else:
                self._timespan.cancel()

    def measure(self) -> "_TimespanContextManager":
        """
        Provides a context manager for measuring the time it takes to execute
        snippets of code in a `with` statement.

        If the contents of the `with` statement raise an exception, the timing
        is not recorded.

        Usage:
            with metrics.perf.timer.measure():
                # ... do something that takes time ...
        """
        return self._TimespanContextManager(self)

    def set_raw_nanos(self, elapsed_nanos: int) -> None:
        """
        Explicitly set the timespan value, in nanoseconds.

        This API should only be used if your library or application requires recording
        times in a way that can not make use of [start]/[stop]/[cancel].

        [setRawNanos] does not overwrite a running timer or an already existing value.

        Args:
            elapsed_nanos (int): The elapsed time to record, in nanoseconds.
        """
        self._inner.set_raw_nanos(elapsed_nanos)

    def test_get_value(self, ping_name: Optional[str] = None) -> Optional[int]:
        """
        Returns the stored value for testing purposes only.

        Args:
            ping_name (str): (default: first value in send_in_pings) The name
                of the ping to retrieve the metric for.

        Returns:
            value (bool): value of the stored metric.
        """
        return self._inner.test_get_value(ping_name)

    def test_get_num_recorded_errors(self, error_type: ErrorType) -> int:
        """
        Returns the number of errors recorded for the given metric.

        Args:
            error_type (ErrorType): The type of error recorded.
            ping_name (str): (default: first value in send_in_pings) The name
                of the ping to retrieve the metric for.

        Returns:
            num_errors (int): The number of errors recorded for the metric for
                the given error type.
        """
        return self._inner.test_get_num_recorded_errors(error_type)


__all__ = ["TimespanMetricType"]
