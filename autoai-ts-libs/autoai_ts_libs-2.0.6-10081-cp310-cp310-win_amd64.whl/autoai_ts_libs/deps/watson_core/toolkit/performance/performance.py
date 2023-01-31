# *****************************************************************#
# (C) Copyright IBM Corporation 2021.                             #
#                                                                 #
# The source code for this program is not published or otherwise  #
# divested of its trade secrets, irrespective of what has been    #
# deposited with the U.S. Copyright Office.                       #
# *****************************************************************#
"""Core code running performance tests.
"""

import time
from collections.abc import Iterable

from autoai_ts_libs.deps.watson_core.toolkit import performance_metrics

from . import test_data


class PerformanceRunner:
    @staticmethod
    def _function_per_file(raw_document, function_arg):
        processed_args = [raw_document]
        start_time = time.time()
        func, pre_process = function_arg
        processed_args, processed_time = PerformanceRunner._get_pre_processed(
            pre_process, raw_document, processed_args
        )
        func(*processed_args)
        return (time.time() - start_time - processed_time), processed_time

    @staticmethod
    def _get_pre_processed(pre_process_func, doc, args):
        """Run pre_process function on args if available

        Args:
            pre_process_func: function
                Function to run to pre_process
            doc: str
                raw input document for function
            args: list
                list of arguments for function

        Returns:
            Tuple: (list, int)
                Tuple of processed args list and total pre processing time
        """
        processed_start = time.time()
        if pre_process_func is not None:
            args = pre_process_func(doc)
        if not isinstance(args, Iterable):
            args = [args]  # Convert to iterable since all args are unpacked
        return args, time.time() - processed_start

    @staticmethod
    def timed_function(
        function_arg,
        test_directory,
        num_iterations=1,
        num_seconds=None,
        description="",
        notes="",
    ):
        total_duration = 0
        total_chars = 0
        total_iterations = 0
        total_docs = 0
        total_processed = 0

        test_files = test_data.test_data_iter(test_directory)
        for total_iterations in range(num_iterations):
            for raw_document in test_files:
                if raw_document and (
                    total_duration <= num_seconds if num_seconds else True
                ):
                    total_chars += len(raw_document)
                    (
                        total_duration_iter,
                        total_processed_iter,
                    ) = PerformanceRunner._function_per_file(raw_document, function_arg)
                    total_duration += total_duration_iter
                    total_docs += 1
                    total_processed += total_processed_iter
            total_iterations += 1

        return PerformanceReport(
            total_chars,
            total_duration,
            total_iterations,
            total_processed,
            total_docs,
            description=description,
            notes=notes,
        )


class PerformanceReport:
    """Provides output report of performance tests."""

    def __init__(
        self,
        chars,
        duration,
        iterations,
        pre_processing_duration,
        docs,
        mem_usage=None,
        description=None,
        notes=None,
    ):
        self.chars = chars
        self.duration = duration if duration > 0 else 1
        self.pre_processing_duration = pre_processing_duration
        self.iterations = iterations
        self.docs = docs
        self.mem_usage = mem_usage
        self.notes = notes
        self.description = description
        self.throughput = performance_metrics.kilo_chars_per_second(
            self.chars, self.iterations, self.duration
        )

        self.total_throughput = performance_metrics.kilo_chars_per_second(
            self.chars, self.iterations, self.pre_processing_duration + self.duration
        )
