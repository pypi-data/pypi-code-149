"""Tests for registry."""
import pytest

from usecase_registry.registry import UseCaseRegistry


class TestUseCaseRegistry:
    """Test definitions for UseCaseRegistry."""

    def test_expected_usage(self) -> None:
        """Test an expected usage workflow."""
        registry = UseCaseRegistry[int](max_length=2)
        assert registry.is_empty()
        registry.add_value(v=10)
        registry.add_value(v=39)
        assert not registry.is_empty()
        state = registry.get_state()
        assert state == [10, 39]

    def test_adding_elements_of_different_type(self) -> None:
        """Test registry fails when adding objects of different types."""
        registry = UseCaseRegistry[str](max_length=2)
        assert registry.is_empty()
        registry.add_value(v="a1")
        with pytest.raises(ValueError):  # noqa: PT011
            registry.add_value(v=10)  # type:ignore[arg-type]

    def test_registry_can_only_by_checked_once(self) -> None:
        """Test registry fails when checked multiple times."""
        registry = UseCaseRegistry[int](max_length=2)
        registry.get_state()
        with pytest.raises(RuntimeError):
            registry.get_state()

    def test_registry_can_only_store_up_to_max_capacity(self) -> None:
        """Test registry fails when storage exceeds capacity."""
        registry = UseCaseRegistry[int](max_length=10)
        for value in range(10):
            registry.add_value(v=value)

        with pytest.raises(RuntimeError):
            registry.add_value(v=10)
