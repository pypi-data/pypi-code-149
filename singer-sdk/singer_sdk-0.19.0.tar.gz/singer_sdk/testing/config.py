"""Test config classes."""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class SuiteConfig:
    """Test Suite Config, passed to each test.

    Args:
        ignore_no_records: Ignore stream test failures if stream returns no records,
            for all streams.
        ignore_no_records_for_streams: Ignore stream test failures if stream returns
             no records, for named streams.
    """

    ignore_no_records: bool = False
    ignore_no_records_for_streams: list[str] = field(default_factory=list)
