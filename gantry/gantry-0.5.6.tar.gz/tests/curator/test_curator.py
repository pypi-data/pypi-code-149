import datetime

import pytest
import responses

from gantry.api_client import APIClient
from gantry.curators import (
    AscendedSortCurator,
    BalancedStratificationCurator,
    BoundedRangeCurator,
    Curator,
    DescendedSortCurator,
    NewestCurator,
    OldestCurator,
    ProportionalStratificationCurator,
    StrictStratificationCurator,
    UniformCurator,
)
from gantry.curators.curators import CuratorClient
from gantry.curators.selectors import (
    BoundsFilter,
    DruidDimensionOrderingDirections,
    OrderedSampler,
    Selector,
    StratificationMode,
    StratifiedSampler,
    UniformSampler,
)

from .conftest import HOST


@pytest.fixture
def test_api_client():
    return APIClient(origin=HOST)


@pytest.fixture
def test_client(test_api_client):
    return CuratorClient(api_client=test_api_client)


@pytest.mark.parametrize(
    ("curator_class", "curator_kwargs", "expected_selector"),
    [
        (
            AscendedSortCurator,
            {"sort_field": "ascending_field"},
            Selector(
                method=OrderedSampler(
                    field="ascending_field", sort=DruidDimensionOrderingDirections.ASCENDING
                ),
                limit=10,
            ),
        ),
        (
            DescendedSortCurator,
            {"sort_field": "ascending_field"},
            Selector(
                method=OrderedSampler(
                    field="ascending_field", sort=DruidDimensionOrderingDirections.DESCENDING
                ),
                limit=10,
            ),
        ),
        (
            NewestCurator,
            {},
            Selector(
                method=OrderedSampler(
                    field="__time", sort=DruidDimensionOrderingDirections.DESCENDING
                ),
                limit=10,
            ),
        ),
        (
            OldestCurator,
            {},
            Selector(
                method=OrderedSampler(
                    field="__time", sort=DruidDimensionOrderingDirections.ASCENDING
                ),
                limit=10,
            ),
        ),
        (
            UniformCurator,
            {},
            Selector(
                method=UniformSampler(),
                limit=10,
            ),
        ),
        (
            StrictStratificationCurator,
            {"stratify_field": "category"},
            Selector(
                method=StratifiedSampler(field="category", mode=StratificationMode.strict),
                limit=10,
            ),
        ),
        (
            BalancedStratificationCurator,
            {"stratify_field": "category"},
            Selector(
                method=StratifiedSampler(field="category", mode=StratificationMode.balanced),
                limit=10,
            ),
        ),
        (
            ProportionalStratificationCurator,
            {"stratify_field": "category"},
            Selector(
                method=StratifiedSampler(field="category", mode=StratificationMode.proportional),
                limit=10,
            ),
        ),
        (
            BoundedRangeCurator,
            {"bound_field": "float_field", "lower_bound": 0.0, "upper_bound": 1.0},
            Selector(
                method=OrderedSampler(
                    field="float_field", sort=DruidDimensionOrderingDirections.ASCENDING
                ),
                limit=10,
                filters=[BoundsFilter(field="float_field", lower=0.0, upper=1.0)],
            ),
        ),
    ],
)
def test_selectors_preset_curator(curator_class, curator_kwargs, expected_selector):
    curator_kwargs.update(
        {"name": "test_curator_name", "application_name": "test_application_name", "limit": 10}
    )
    curator = curator_class(**curator_kwargs)

    assert curator._selectors[0] == expected_selector


@pytest.mark.parametrize(
    ("application_name", "expected_len"),
    [(None, 2), ("test_curator_app", 1), ("different_app_name", 0)],
)
def test_get_curators(test_client, test_curators, application_name, expected_len):
    with responses.RequestsMock() as resp:
        resp.add(
            resp.GET,
            f"{HOST}/api/v1/curator",
            json={
                "response": "ok",
                "data": test_curators,
            },
            headers={"Content-Type": "application/json"},
        )
        curators = test_client.get_all_curators(application_name=application_name)
        assert len(curators) == expected_len


@pytest.mark.parametrize(
    ("application_name", "expected_len"),
    [(None, 2), ("test_curator_app", 1), ("different_app_name", 0)],
)
def test_list_curators(test_client, test_curators, application_name, expected_len):
    with responses.RequestsMock() as resp:
        resp.add(
            resp.GET,
            f"{HOST}/api/v1/curator",
            json={
                "response": "ok",
                "data": test_curators,
            },
            headers={"Content-Type": "application/json"},
        )
        curator_names = test_client.list_curators(application_name=application_name)
        assert len(curator_names) == expected_len


def test_get_curator(test_client, test_curator):
    with responses.RequestsMock() as resp:
        resp.add(
            resp.GET,
            f"{HOST}/api/v1/curator/test_curator_name",
            json={
                "response": "ok",
                "data": test_curator,
            },
            headers={"Content-Type": "application/json"},
        )
        _ = test_client.get_curator(name="test_curator_name")


def test_curator_properties(test_curator):
    curator = Curator(**test_curator)

    assert curator.id == test_curator["id"]
    assert curator.application_name == test_curator["application_name"]
    assert curator.name == test_curator["name"]
    assert curator.curated_dataset_name == test_curator["curated_dataset_name"]
    assert curator.start_on == test_curator["start_on"]
    assert curator.curation_interval == test_curator["curation_interval"]
    assert curator.curate_past_intervals == test_curator["curate_past_intervals"]
    assert curator.created_at == test_curator["created_at"]
    assert curator.selectors == test_curator["selectors"]


def test_create_curator(test_api_client, test_curators):
    curator = Curator(**test_curators[0], api_client=test_api_client)

    with responses.RequestsMock() as resp:
        resp.add(
            resp.POST,
            f"{HOST}/api/v1/curator",
            json={
                "response": "ok",
                "data": test_curators[1],
            },
            headers={"Content-Type": "application/json"},
        )
        assert curator.create() is curator

    assert str(curator.id) == test_curators[1]["id"]
    assert curator.name == test_curators[1]["name"]
    assert curator.curated_dataset_name == test_curators[1]["curated_dataset_name"]
    assert curator.application_name == test_curators[1]["application_name"]
    assert curator.start_on.isoformat() == test_curators[1]["start_on"]
    assert str(curator.curation_interval) == test_curators[1]["curation_interval"]
    assert curator.curate_past_intervals == test_curators[1]["curate_past_intervals"]
    assert curator.created_at.isoformat() == test_curators[1]["created_at"]
    assert curator.selectors == [Selector(**info) for info in test_curators[1]["selectors"]]


def test_update_curator(test_api_client, test_curator):
    curator = Curator(**test_curator, api_client=test_api_client)

    update_info = {
        "name": "updated_name",
        "curated_dataset_name": "updated_dataset_name",
        "curation_interval": str(datetime.timedelta(hours=5)),
        "selectors": [Selector(limit=123).dict()],
    }

    updated_json = {
        key: test_curator[key] if key not in update_info else update_info[key]
        for key in test_curator
    }

    with responses.RequestsMock() as resp:
        resp.add(
            resp.PATCH,
            f"{HOST}/api/v1/curator",
            json={
                "response": "ok",
                "data": updated_json,
            },
            headers={"Content-Type": "application/json"},
        )

        assert (
            curator.update(
                new_curator_name=update_info["name"],
                new_curated_dataset_name=update_info["curated_dataset_name"],
                new_curation_interval=update_info["curation_interval"],
                new_selectors=update_info["selectors"],
            )
            is curator
        )

    assert curator.name == update_info["name"]
    assert str(curator.curation_interval) == update_info["curation_interval"]
    assert curator.selectors == update_info["selectors"]
    assert curator.curated_dataset_name == update_info["curated_dataset_name"]


def test_delete_curator(test_api_client, test_curator):
    curator = Curator(**test_curator, api_client=test_api_client)

    with responses.RequestsMock() as resp:
        resp.add(
            resp.DELETE,
            f"{HOST}/api/v1/curator/{test_curator['id']}",
            json={
                "response": "ok",
                "data": {
                    "curated_dataset_name": test_curator["name"],
                    "id": test_curator["id"],
                    "application_name": test_curator["application_name"],
                    "deleted_at": str(datetime.datetime(2022, 1, 1)),
                },
            },
            headers={"Content-Type": "application/json"},
        )

        curator_info = f"{test_curator['name']} ({test_curator['id']})"
        assert curator.delete() == f"Curator {curator_info} deleted at 2022-01-01 00:00:00"

    with pytest.raises(ValueError):
        _ = curator.id
    with pytest.raises(ValueError):
        _ = curator.created_at
