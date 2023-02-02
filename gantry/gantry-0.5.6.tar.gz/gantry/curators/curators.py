import datetime
import json
import logging
import uuid
from typing import List, Optional

from typeguard import typechecked

from gantry.api_client import APIClient
from gantry.curators import globals
from gantry.curators.models import (
    CreateCuratorRequest,
    CuratorInfo,
    UpdateCuratorRequest,
)
from gantry.curators.selectors import Selector
from gantry.dataset.gantry_dataset import GantryDataset
from gantry.dataset.main import get_dataset

logger = logging.getLogger(__name__)


class CuratorClient:
    def __init__(self, api_client: APIClient) -> None:
        self._api_client = api_client

    @typechecked
    def list_curators(self, application_name: Optional[str] = None) -> List[str]:
        """
        List all curator names associated with an application.

        Returns:
            List[str]
        """
        return [
            curator_info.name
            for curator_info in self._get_all_curator_infos(application_name=application_name)
        ]

    @typechecked
    def get_all_curators(self, application_name: Optional[str] = None) -> List["Curator"]:
        """
        Get all curators associated with an application.

        Returns:
            List[Curator]
        """
        res = self._get_all_curator_infos(application_name=application_name)
        return [Curator.from_curator_info(self._api_client, curator_info) for curator_info in res]

    @typechecked
    def get_curator(self, name: str) -> "Curator":
        """
        Get a curator by name. If the curator does not exist, an exception will be raised.

        Args:
            name (str): Curator name.

        Returns:
            Curator: A Curator object.
        """
        res = self._api_client.request("GET", f"/api/v1/curator/{name}", raise_for_status=True)
        return Curator.from_curator_info(self._api_client, CuratorInfo.parse_obj(res["data"]))

    @typechecked
    def delete_curator(
        self,
    ) -> "Curator":
        """
        Currently, Curators must be deleted using an instance of the Curator class.
        """
        raise NotImplementedError

    @typechecked
    def update_curator(
        self,
    ) -> "Curator":
        """
        Currently, Curators must be updated using an instance of the Curator class.
        """
        raise NotImplementedError

    def _get_all_curator_infos(self, application_name: Optional[str] = None) -> List["CuratorInfo"]:
        """
        Get all curators associated with an application.

        Returns:
            List[Curator]
        """
        res = self._api_client.request("GET", "/api/v1/curator", raise_for_status=True)
        res = res["data"]
        if application_name:
            return [
                CuratorInfo.parse_obj(curator)
                for curator in res
                if curator["application_name"] == application_name
            ]
        return [CuratorInfo.parse_obj(curator) for curator in res]


class Curator:
    def __init__(
        self,
        api_client: Optional[APIClient] = None,
        id: Optional[uuid.UUID] = None,
        name: Optional[str] = None,
        curated_dataset_name: Optional[str] = None,
        application_name: Optional[str] = None,
        start_on: Optional[datetime.datetime] = None,
        curation_interval: datetime.timedelta = datetime.timedelta(days=1),
        curate_past_intervals: bool = True,
        created_at: Optional[datetime.datetime] = None,
        selectors: Optional[List[Selector]] = None,
    ):
        """
        A Curator defines a process that runs periodically to curate a dataset. It uses
        selectors to select rows from the dataset and write them to a curated dataset.
        The curated dataset is a new dataset that is created by the curator. The curator
        will create the curated dataset if it does not already exist, or update it if it
        does exist.

        Instantiating a curator does not create the curator in Gantry. To create the curator,
        call `Curator.create` after instantiating the curator. Curators that have been created
        in Gantry can be instantiated as a `Curator` object using `Curator.from_curator_info`,
        although it is recommended to use the module-level `get_curator` function instead.

        Curators can be updated using `Curator.update`. This will update the curator in Gantry
        and also update the curator object in memory.

        Curators can be deleted using `Curator.delete`. This will delete the curator in Gantry
        but will not delete the curator object in memory.

        Args:
            api_client (Optional[APIClient], optional): APIClient to use. Defaults to None,
                in which case the Curator will use the global APIClient.
            id (Optional[uuid.UUID], optional): The id of the curator. Defaults to None. The
                id only exists in Gantry for curators that have been created. Typically, you
                will not need to set this. But some methods, such as
                `Curator.from_curator_info`, will set this for you.
            name (Optional[str], optional): The name of the curator. Defaults to None.
            curated_dataset_name (Optional[str], optional): The name of the curated dataset.
                Defaults to None. If None, the curated dataset name will be the same as the
                curator name.
            application_name (str): The name of the application that the curator is running in.
            start_on (Optional[datetime.datetime], optional): The time at which the curator
                should start curating. Defaults to None. If None, the curator will start
                curating immediately, looking back one curation_interval.
            curation_interval (datetime.timedelta, optional): The interval at which the curator
                should curate. Defaults to datetime.timedelta(days=1).
            curate_past_intervals (bool, optional): Whether the curator should curate past
                intervals. Defaults to True. If True, the curator will immediately curate
                all intervals that have passed since the start_on time.
            created_at (Optional[datetime.datetime], optional): The time at which the curator
                was created. Defaults to None. The created_at time only exists in Gantry for
                curators that have been created. Typically, you will not need to set this. But
                some methods, such as `Curator.from_curator_info`, will set this for you.
            selectors (Optional[List[Selector]], optional): The selectors that the curator
                should use to curate. Defaults to None. If None, the request to create the
                curator will fail.
        """
        self._api_client: APIClient = (
            globals._API_CLIENT if api_client is None else api_client  # type: ignore
        )
        self._id = id
        self._name = name
        self._curated_dataset_name = name if curated_dataset_name is None else curated_dataset_name
        self._application_name = application_name
        self._start_on = datetime.datetime.now() if start_on is None else start_on
        self._curation_interval = curation_interval
        self._curate_past_intervals = curate_past_intervals
        self._created_at = created_at
        self._selectors = [] if selectors is None else selectors

    @property
    def id(self) -> uuid.UUID:
        if self._id is None:
            raise ValueError("Curator has no id. Has it been created yet?")
        return self._id

    @property
    def name(self) -> str:
        return self._name  # type: ignore

    @property
    def curated_dataset_name(self) -> str:
        return self._curated_dataset_name  # type: ignore

    @property
    def application_name(self) -> str:
        return self._application_name  # type: ignore

    @property
    def start_on(self) -> datetime.datetime:
        return self._start_on

    @property
    def curation_interval(self) -> datetime.timedelta:
        return self._curation_interval

    @property
    def curate_past_intervals(self) -> bool:
        return self._curate_past_intervals

    @property
    def created_at(self) -> datetime.datetime:
        if self._created_at is None:
            raise ValueError("Curator has not been created yet")
        return self._created_at

    @property
    def selectors(self) -> List[Selector]:
        return self._selectors

    def create(self) -> "Curator":
        """
        Creates the Curator.

        Once created, the Curator will start curating the dataset according to the
        curation_interval. If curate_past_intervals is set to True, it will curate all
        past intervals and continue curating in the future. The Curator will exist in
        Gantry until it is deleted.

        The results of the curation will be stored in a dataset with the name
        curated_dataset_name. If the dataset does not exist, it will be created. If it
        does exist, it will be appended to. Curation commits will be made by the user
        with the api key used when initializing gantry services.

        The curated dataset can be accessed using the get_curated_dataset method..

        Returns:
            Curator: The created curator.
        """
        create_curator_request = self._form_create_curator_request()
        return self._create_curator(create_curator_request)

    def update(
        self,
        new_curator_name: Optional[str] = None,
        new_curated_dataset_name: Optional[str] = None,
        new_curation_interval: Optional[datetime.timedelta] = None,
        new_selectors: Optional[List[Selector]] = None,
        create_new_dataset: bool = False,
    ) -> "Curator":
        """
        Updates the curator. At least one of the update parameters must be provided. If a parameter
        is not provided, it will not be updated.

        Args:
            new_curator_name (Optional[str], optional): The new name of the curator. Defaults to
                None.
            new_curated_dataset_name (Optional[str], optional): The name of the new dataset to
                curate to. Defaults to None.
            new_curation_interval (Optional[datetime.timedelta], optional): The new curation
                interval. Defaults to None.
            new_selectors (Optional[List[Selector]], optional): The new selectors. Defaults to
                None.
            create_new_dataset (bool, optional): Whether to create a new dataset if the requested
                name does not correspond to an existing dataset. Defaults to False.

        Raises:
            ValueError: If curator id is not set.
            ValueError: If no update parameters are provided.

        Returns:
            Curator: The updated curator.
        """
        if self._id is None:
            raise ValueError("Curator id is required to update a curator.")
        if all(arg is None for arg in (new_curator_name, new_curation_interval, new_selectors)):
            raise ValueError("No update parameters provided")
        return self._update_curator(
            self._form_update_curator_request(
                new_curator_name=new_curator_name,
                new_curated_dataset_name=new_curated_dataset_name,
                new_curation_interval=new_curation_interval,
                new_selectors=new_selectors,
                allow_create_new_dataset=create_new_dataset,
            )
        )

    def delete(self) -> str:
        """
        Deletes the curator using the curator id. The Curator object is not deleted, but the
        curator id is reset to None, as well as the created_at time.

        Raises:
            ValueError: If curator id is not set.

        Returns:
            str: A message indicating the curator was deleted. The message also contains the
                time the curator was deleted.
        """
        if self._id is None:
            raise ValueError("Curator id is required to delete a curator.")
        res = self._api_client.request(
            "DELETE",
            f"/api/v1/curator/{self._id}",
            raise_for_status=True,
        )
        if res["response"] == "ok":
            msg = f"Curator {self._name} ({self._id}) deleted at {res['data']['deleted_at']}"
            self._id = None
            # will not be able to recreate curator with same name as long as dataset is coupled
            self._created_at = None
        return msg

    def get_curated_dataset(self) -> GantryDataset:
        """
        Gets the curated dataset associated with the Curator.

        Returns:
            GantryDataset: A GantryDataset object representing the curated dataset.
        """
        return get_dataset(self._curated_dataset_name)

    @classmethod
    def from_curator_info(cls, api_client: APIClient, curator_info: CuratorInfo) -> "Curator":
        """
        Instantiates a Curator object from a CuratorInfo object.

        Args:
            api_client (APIClient): _description_
            curator_info (CuratorInfo): _description_

        Returns:
            Curator: _description_
        """
        return cls(api_client, **curator_info.dict())

    def _form_create_curator_request(self) -> CreateCuratorRequest:
        """
        Forms a create curator request model.

        Returns:
            CreateCuratorRequest: Create request model.
        """
        return CreateCuratorRequest(
            name=self._name,
            curated_dataset_name=self._curated_dataset_name,
            application_name=self._application_name,
            start_on=self._start_on,
            curation_interval=self._curation_interval,
            curate_past_intervals=self._curate_past_intervals,
            selectors=self._selectors,
        )

    def _create_curator(
        self,
        create_curator_request: CreateCuratorRequest,
    ) -> "Curator":
        """
        Makes the API call to create a curator.

        Args:
            create_curator_request (CreateCuratorRequest): Create reqest model.

        Returns:
            Curator: The created curator.
        """

        res = self._api_client.request(
            "POST",
            "/api/v1/curator",
            json=json.loads(create_curator_request.json()),
            raise_for_status=True,
        )

        curator_info = CuratorInfo.parse_obj(res["data"])
        self._id = curator_info.id
        self._name = curator_info.name
        self._curated_dataset_name = curator_info.curated_dataset_name
        self._application_name = curator_info.application_name
        self._start_on = curator_info.start_on
        self._curation_interval = curator_info.curation_interval
        self._curate_past_intervals = curator_info.curate_past_intervals
        self._created_at = curator_info.created_at
        self._selectors = curator_info.selectors
        return self

    def _form_update_curator_request(
        self,
        new_curator_name: Optional[str] = None,
        new_curated_dataset_name: Optional[str] = None,
        new_curation_interval: Optional[datetime.timedelta] = None,
        new_selectors: Optional[List[Selector]] = None,
        allow_create_new_dataset: bool = False,
    ) -> UpdateCuratorRequest:
        """
        Instantiates a valid update request model.

        Args:
            new_curator_name (Optional[str], optional): The new name of the curator. Defaults to
                None.
            new_curation_interval (Optional[datetime.timedelta], optional): The new curation
                interval. Defaults to None.
            new_selectors (Optional[List[Selector]], optional): The new selectors. Defaults to
                None.

        Returns:
            UpdateCuratorRequest: Valid update request model.
        """
        return UpdateCuratorRequest(
            name=self._name,
            new_name=new_curator_name,
            new_curated_dataset_name=new_curated_dataset_name,
            curation_interval=new_curation_interval,
            selectors=new_selectors,
            allow_create_new_dataset=allow_create_new_dataset,
        )

    def _update_curator(self, update_curator_request: UpdateCuratorRequest) -> "Curator":
        """
        Issues the request to update the curator using the API client and an update request.

        Args:
            update_curator_request (UpdateCuratorRequest): Update request model.

        Returns:
            Curator: the updated curator.
        """
        res = self._api_client.request(
            "PATCH",
            "/api/v1/curator",
            json=json.loads(update_curator_request.json()),
            raise_for_status=True,
        )
        curator_info = CuratorInfo.parse_obj(res["data"])
        self._name = curator_info.name
        self._curated_dataset_name = curator_info.curated_dataset_name
        self._curation_interval = curator_info.curation_interval
        self._selectors = curator_info.selectors
        return self
