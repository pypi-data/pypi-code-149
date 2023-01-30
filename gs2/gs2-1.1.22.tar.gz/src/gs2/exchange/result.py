# Copyright 2016 Game Server Services, Inc. or its affiliates. All Rights
# Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License").
# You may not use this file except in compliance with the License.
# A copy of the License is located at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
# or in the "license" file accompanying this file. This file is distributed
# on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
# express or implied. See the License for the specific language governing
# permissions and limitations under the License.

from __future__ import annotations

from .model import *


class DescribeNamespacesResult(core.Gs2Result):
    items: List[Namespace] = None
    next_page_token: str = None

    def with_items(self, items: List[Namespace]) -> DescribeNamespacesResult:
        self.items = items
        return self

    def with_next_page_token(self, next_page_token: str) -> DescribeNamespacesResult:
        self.next_page_token = next_page_token
        return self

    def get(self, key, default=None):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return default

    def __getitem__(self, key):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return None

    @staticmethod
    def from_dict(
        data: Dict[str, Any],
    ) -> Optional[DescribeNamespacesResult]:
        if data is None:
            return None
        return DescribeNamespacesResult()\
            .with_items([
                Namespace.from_dict(data.get('items')[i])
                for i in range(len(data.get('items')) if data.get('items') else 0)
            ])\
            .with_next_page_token(data.get('nextPageToken'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "items": [
                self.items[i].to_dict() if self.items[i] else None
                for i in range(len(self.items) if self.items else 0)
            ],
            "nextPageToken": self.next_page_token,
        }


class CreateNamespaceResult(core.Gs2Result):
    item: Namespace = None

    def with_item(self, item: Namespace) -> CreateNamespaceResult:
        self.item = item
        return self

    def get(self, key, default=None):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return default

    def __getitem__(self, key):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return None

    @staticmethod
    def from_dict(
        data: Dict[str, Any],
    ) -> Optional[CreateNamespaceResult]:
        if data is None:
            return None
        return CreateNamespaceResult()\
            .with_item(Namespace.from_dict(data.get('item')))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "item": self.item.to_dict() if self.item else None,
        }


class GetNamespaceStatusResult(core.Gs2Result):
    status: str = None

    def with_status(self, status: str) -> GetNamespaceStatusResult:
        self.status = status
        return self

    def get(self, key, default=None):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return default

    def __getitem__(self, key):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return None

    @staticmethod
    def from_dict(
        data: Dict[str, Any],
    ) -> Optional[GetNamespaceStatusResult]:
        if data is None:
            return None
        return GetNamespaceStatusResult()\
            .with_status(data.get('status'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "status": self.status,
        }


class GetNamespaceResult(core.Gs2Result):
    item: Namespace = None

    def with_item(self, item: Namespace) -> GetNamespaceResult:
        self.item = item
        return self

    def get(self, key, default=None):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return default

    def __getitem__(self, key):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return None

    @staticmethod
    def from_dict(
        data: Dict[str, Any],
    ) -> Optional[GetNamespaceResult]:
        if data is None:
            return None
        return GetNamespaceResult()\
            .with_item(Namespace.from_dict(data.get('item')))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "item": self.item.to_dict() if self.item else None,
        }


class UpdateNamespaceResult(core.Gs2Result):
    item: Namespace = None

    def with_item(self, item: Namespace) -> UpdateNamespaceResult:
        self.item = item
        return self

    def get(self, key, default=None):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return default

    def __getitem__(self, key):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return None

    @staticmethod
    def from_dict(
        data: Dict[str, Any],
    ) -> Optional[UpdateNamespaceResult]:
        if data is None:
            return None
        return UpdateNamespaceResult()\
            .with_item(Namespace.from_dict(data.get('item')))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "item": self.item.to_dict() if self.item else None,
        }


class DeleteNamespaceResult(core.Gs2Result):
    item: Namespace = None

    def with_item(self, item: Namespace) -> DeleteNamespaceResult:
        self.item = item
        return self

    def get(self, key, default=None):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return default

    def __getitem__(self, key):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return None

    @staticmethod
    def from_dict(
        data: Dict[str, Any],
    ) -> Optional[DeleteNamespaceResult]:
        if data is None:
            return None
        return DeleteNamespaceResult()\
            .with_item(Namespace.from_dict(data.get('item')))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "item": self.item.to_dict() if self.item else None,
        }


class DescribeRateModelsResult(core.Gs2Result):
    items: List[RateModel] = None

    def with_items(self, items: List[RateModel]) -> DescribeRateModelsResult:
        self.items = items
        return self

    def get(self, key, default=None):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return default

    def __getitem__(self, key):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return None

    @staticmethod
    def from_dict(
        data: Dict[str, Any],
    ) -> Optional[DescribeRateModelsResult]:
        if data is None:
            return None
        return DescribeRateModelsResult()\
            .with_items([
                RateModel.from_dict(data.get('items')[i])
                for i in range(len(data.get('items')) if data.get('items') else 0)
            ])

    def to_dict(self) -> Dict[str, Any]:
        return {
            "items": [
                self.items[i].to_dict() if self.items[i] else None
                for i in range(len(self.items) if self.items else 0)
            ],
        }


class GetRateModelResult(core.Gs2Result):
    item: RateModel = None

    def with_item(self, item: RateModel) -> GetRateModelResult:
        self.item = item
        return self

    def get(self, key, default=None):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return default

    def __getitem__(self, key):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return None

    @staticmethod
    def from_dict(
        data: Dict[str, Any],
    ) -> Optional[GetRateModelResult]:
        if data is None:
            return None
        return GetRateModelResult()\
            .with_item(RateModel.from_dict(data.get('item')))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "item": self.item.to_dict() if self.item else None,
        }


class DescribeRateModelMastersResult(core.Gs2Result):
    items: List[RateModelMaster] = None
    next_page_token: str = None

    def with_items(self, items: List[RateModelMaster]) -> DescribeRateModelMastersResult:
        self.items = items
        return self

    def with_next_page_token(self, next_page_token: str) -> DescribeRateModelMastersResult:
        self.next_page_token = next_page_token
        return self

    def get(self, key, default=None):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return default

    def __getitem__(self, key):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return None

    @staticmethod
    def from_dict(
        data: Dict[str, Any],
    ) -> Optional[DescribeRateModelMastersResult]:
        if data is None:
            return None
        return DescribeRateModelMastersResult()\
            .with_items([
                RateModelMaster.from_dict(data.get('items')[i])
                for i in range(len(data.get('items')) if data.get('items') else 0)
            ])\
            .with_next_page_token(data.get('nextPageToken'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "items": [
                self.items[i].to_dict() if self.items[i] else None
                for i in range(len(self.items) if self.items else 0)
            ],
            "nextPageToken": self.next_page_token,
        }


class CreateRateModelMasterResult(core.Gs2Result):
    item: RateModelMaster = None

    def with_item(self, item: RateModelMaster) -> CreateRateModelMasterResult:
        self.item = item
        return self

    def get(self, key, default=None):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return default

    def __getitem__(self, key):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return None

    @staticmethod
    def from_dict(
        data: Dict[str, Any],
    ) -> Optional[CreateRateModelMasterResult]:
        if data is None:
            return None
        return CreateRateModelMasterResult()\
            .with_item(RateModelMaster.from_dict(data.get('item')))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "item": self.item.to_dict() if self.item else None,
        }


class GetRateModelMasterResult(core.Gs2Result):
    item: RateModelMaster = None

    def with_item(self, item: RateModelMaster) -> GetRateModelMasterResult:
        self.item = item
        return self

    def get(self, key, default=None):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return default

    def __getitem__(self, key):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return None

    @staticmethod
    def from_dict(
        data: Dict[str, Any],
    ) -> Optional[GetRateModelMasterResult]:
        if data is None:
            return None
        return GetRateModelMasterResult()\
            .with_item(RateModelMaster.from_dict(data.get('item')))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "item": self.item.to_dict() if self.item else None,
        }


class UpdateRateModelMasterResult(core.Gs2Result):
    item: RateModelMaster = None

    def with_item(self, item: RateModelMaster) -> UpdateRateModelMasterResult:
        self.item = item
        return self

    def get(self, key, default=None):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return default

    def __getitem__(self, key):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return None

    @staticmethod
    def from_dict(
        data: Dict[str, Any],
    ) -> Optional[UpdateRateModelMasterResult]:
        if data is None:
            return None
        return UpdateRateModelMasterResult()\
            .with_item(RateModelMaster.from_dict(data.get('item')))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "item": self.item.to_dict() if self.item else None,
        }


class DeleteRateModelMasterResult(core.Gs2Result):
    item: RateModelMaster = None

    def with_item(self, item: RateModelMaster) -> DeleteRateModelMasterResult:
        self.item = item
        return self

    def get(self, key, default=None):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return default

    def __getitem__(self, key):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return None

    @staticmethod
    def from_dict(
        data: Dict[str, Any],
    ) -> Optional[DeleteRateModelMasterResult]:
        if data is None:
            return None
        return DeleteRateModelMasterResult()\
            .with_item(RateModelMaster.from_dict(data.get('item')))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "item": self.item.to_dict() if self.item else None,
        }


class ExchangeResult(core.Gs2Result):
    item: RateModel = None
    transaction_id: str = None
    stamp_sheet: str = None
    stamp_sheet_encryption_key_id: str = None
    auto_run_stamp_sheet: bool = None

    def with_item(self, item: RateModel) -> ExchangeResult:
        self.item = item
        return self

    def with_transaction_id(self, transaction_id: str) -> ExchangeResult:
        self.transaction_id = transaction_id
        return self

    def with_stamp_sheet(self, stamp_sheet: str) -> ExchangeResult:
        self.stamp_sheet = stamp_sheet
        return self

    def with_stamp_sheet_encryption_key_id(self, stamp_sheet_encryption_key_id: str) -> ExchangeResult:
        self.stamp_sheet_encryption_key_id = stamp_sheet_encryption_key_id
        return self

    def with_auto_run_stamp_sheet(self, auto_run_stamp_sheet: bool) -> ExchangeResult:
        self.auto_run_stamp_sheet = auto_run_stamp_sheet
        return self

    def get(self, key, default=None):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return default

    def __getitem__(self, key):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return None

    @staticmethod
    def from_dict(
        data: Dict[str, Any],
    ) -> Optional[ExchangeResult]:
        if data is None:
            return None
        return ExchangeResult()\
            .with_item(RateModel.from_dict(data.get('item')))\
            .with_transaction_id(data.get('transactionId'))\
            .with_stamp_sheet(data.get('stampSheet'))\
            .with_stamp_sheet_encryption_key_id(data.get('stampSheetEncryptionKeyId'))\
            .with_auto_run_stamp_sheet(data.get('autoRunStampSheet'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "item": self.item.to_dict() if self.item else None,
            "transactionId": self.transaction_id,
            "stampSheet": self.stamp_sheet,
            "stampSheetEncryptionKeyId": self.stamp_sheet_encryption_key_id,
            "autoRunStampSheet": self.auto_run_stamp_sheet,
        }


class ExchangeByUserIdResult(core.Gs2Result):
    item: RateModel = None
    transaction_id: str = None
    stamp_sheet: str = None
    stamp_sheet_encryption_key_id: str = None
    auto_run_stamp_sheet: bool = None

    def with_item(self, item: RateModel) -> ExchangeByUserIdResult:
        self.item = item
        return self

    def with_transaction_id(self, transaction_id: str) -> ExchangeByUserIdResult:
        self.transaction_id = transaction_id
        return self

    def with_stamp_sheet(self, stamp_sheet: str) -> ExchangeByUserIdResult:
        self.stamp_sheet = stamp_sheet
        return self

    def with_stamp_sheet_encryption_key_id(self, stamp_sheet_encryption_key_id: str) -> ExchangeByUserIdResult:
        self.stamp_sheet_encryption_key_id = stamp_sheet_encryption_key_id
        return self

    def with_auto_run_stamp_sheet(self, auto_run_stamp_sheet: bool) -> ExchangeByUserIdResult:
        self.auto_run_stamp_sheet = auto_run_stamp_sheet
        return self

    def get(self, key, default=None):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return default

    def __getitem__(self, key):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return None

    @staticmethod
    def from_dict(
        data: Dict[str, Any],
    ) -> Optional[ExchangeByUserIdResult]:
        if data is None:
            return None
        return ExchangeByUserIdResult()\
            .with_item(RateModel.from_dict(data.get('item')))\
            .with_transaction_id(data.get('transactionId'))\
            .with_stamp_sheet(data.get('stampSheet'))\
            .with_stamp_sheet_encryption_key_id(data.get('stampSheetEncryptionKeyId'))\
            .with_auto_run_stamp_sheet(data.get('autoRunStampSheet'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "item": self.item.to_dict() if self.item else None,
            "transactionId": self.transaction_id,
            "stampSheet": self.stamp_sheet,
            "stampSheetEncryptionKeyId": self.stamp_sheet_encryption_key_id,
            "autoRunStampSheet": self.auto_run_stamp_sheet,
        }


class ExchangeByStampSheetResult(core.Gs2Result):
    item: RateModel = None
    transaction_id: str = None
    stamp_sheet: str = None
    stamp_sheet_encryption_key_id: str = None
    auto_run_stamp_sheet: bool = None

    def with_item(self, item: RateModel) -> ExchangeByStampSheetResult:
        self.item = item
        return self

    def with_transaction_id(self, transaction_id: str) -> ExchangeByStampSheetResult:
        self.transaction_id = transaction_id
        return self

    def with_stamp_sheet(self, stamp_sheet: str) -> ExchangeByStampSheetResult:
        self.stamp_sheet = stamp_sheet
        return self

    def with_stamp_sheet_encryption_key_id(self, stamp_sheet_encryption_key_id: str) -> ExchangeByStampSheetResult:
        self.stamp_sheet_encryption_key_id = stamp_sheet_encryption_key_id
        return self

    def with_auto_run_stamp_sheet(self, auto_run_stamp_sheet: bool) -> ExchangeByStampSheetResult:
        self.auto_run_stamp_sheet = auto_run_stamp_sheet
        return self

    def get(self, key, default=None):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return default

    def __getitem__(self, key):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return None

    @staticmethod
    def from_dict(
        data: Dict[str, Any],
    ) -> Optional[ExchangeByStampSheetResult]:
        if data is None:
            return None
        return ExchangeByStampSheetResult()\
            .with_item(RateModel.from_dict(data.get('item')))\
            .with_transaction_id(data.get('transactionId'))\
            .with_stamp_sheet(data.get('stampSheet'))\
            .with_stamp_sheet_encryption_key_id(data.get('stampSheetEncryptionKeyId'))\
            .with_auto_run_stamp_sheet(data.get('autoRunStampSheet'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "item": self.item.to_dict() if self.item else None,
            "transactionId": self.transaction_id,
            "stampSheet": self.stamp_sheet,
            "stampSheetEncryptionKeyId": self.stamp_sheet_encryption_key_id,
            "autoRunStampSheet": self.auto_run_stamp_sheet,
        }


class ExportMasterResult(core.Gs2Result):
    item: CurrentRateMaster = None

    def with_item(self, item: CurrentRateMaster) -> ExportMasterResult:
        self.item = item
        return self

    def get(self, key, default=None):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return default

    def __getitem__(self, key):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return None

    @staticmethod
    def from_dict(
        data: Dict[str, Any],
    ) -> Optional[ExportMasterResult]:
        if data is None:
            return None
        return ExportMasterResult()\
            .with_item(CurrentRateMaster.from_dict(data.get('item')))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "item": self.item.to_dict() if self.item else None,
        }


class GetCurrentRateMasterResult(core.Gs2Result):
    item: CurrentRateMaster = None

    def with_item(self, item: CurrentRateMaster) -> GetCurrentRateMasterResult:
        self.item = item
        return self

    def get(self, key, default=None):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return default

    def __getitem__(self, key):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return None

    @staticmethod
    def from_dict(
        data: Dict[str, Any],
    ) -> Optional[GetCurrentRateMasterResult]:
        if data is None:
            return None
        return GetCurrentRateMasterResult()\
            .with_item(CurrentRateMaster.from_dict(data.get('item')))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "item": self.item.to_dict() if self.item else None,
        }


class UpdateCurrentRateMasterResult(core.Gs2Result):
    item: CurrentRateMaster = None

    def with_item(self, item: CurrentRateMaster) -> UpdateCurrentRateMasterResult:
        self.item = item
        return self

    def get(self, key, default=None):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return default

    def __getitem__(self, key):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return None

    @staticmethod
    def from_dict(
        data: Dict[str, Any],
    ) -> Optional[UpdateCurrentRateMasterResult]:
        if data is None:
            return None
        return UpdateCurrentRateMasterResult()\
            .with_item(CurrentRateMaster.from_dict(data.get('item')))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "item": self.item.to_dict() if self.item else None,
        }


class UpdateCurrentRateMasterFromGitHubResult(core.Gs2Result):
    item: CurrentRateMaster = None

    def with_item(self, item: CurrentRateMaster) -> UpdateCurrentRateMasterFromGitHubResult:
        self.item = item
        return self

    def get(self, key, default=None):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return default

    def __getitem__(self, key):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return None

    @staticmethod
    def from_dict(
        data: Dict[str, Any],
    ) -> Optional[UpdateCurrentRateMasterFromGitHubResult]:
        if data is None:
            return None
        return UpdateCurrentRateMasterFromGitHubResult()\
            .with_item(CurrentRateMaster.from_dict(data.get('item')))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "item": self.item.to_dict() if self.item else None,
        }


class CreateAwaitByUserIdResult(core.Gs2Result):
    item: Await = None
    unlock_at: int = None

    def with_item(self, item: Await) -> CreateAwaitByUserIdResult:
        self.item = item
        return self

    def with_unlock_at(self, unlock_at: int) -> CreateAwaitByUserIdResult:
        self.unlock_at = unlock_at
        return self

    def get(self, key, default=None):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return default

    def __getitem__(self, key):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return None

    @staticmethod
    def from_dict(
        data: Dict[str, Any],
    ) -> Optional[CreateAwaitByUserIdResult]:
        if data is None:
            return None
        return CreateAwaitByUserIdResult()\
            .with_item(Await.from_dict(data.get('item')))\
            .with_unlock_at(data.get('unlockAt'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "item": self.item.to_dict() if self.item else None,
            "unlockAt": self.unlock_at,
        }


class DescribeAwaitsResult(core.Gs2Result):
    items: List[Await] = None
    next_page_token: str = None

    def with_items(self, items: List[Await]) -> DescribeAwaitsResult:
        self.items = items
        return self

    def with_next_page_token(self, next_page_token: str) -> DescribeAwaitsResult:
        self.next_page_token = next_page_token
        return self

    def get(self, key, default=None):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return default

    def __getitem__(self, key):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return None

    @staticmethod
    def from_dict(
        data: Dict[str, Any],
    ) -> Optional[DescribeAwaitsResult]:
        if data is None:
            return None
        return DescribeAwaitsResult()\
            .with_items([
                Await.from_dict(data.get('items')[i])
                for i in range(len(data.get('items')) if data.get('items') else 0)
            ])\
            .with_next_page_token(data.get('nextPageToken'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "items": [
                self.items[i].to_dict() if self.items[i] else None
                for i in range(len(self.items) if self.items else 0)
            ],
            "nextPageToken": self.next_page_token,
        }


class DescribeAwaitsByUserIdResult(core.Gs2Result):
    items: List[Await] = None
    next_page_token: str = None

    def with_items(self, items: List[Await]) -> DescribeAwaitsByUserIdResult:
        self.items = items
        return self

    def with_next_page_token(self, next_page_token: str) -> DescribeAwaitsByUserIdResult:
        self.next_page_token = next_page_token
        return self

    def get(self, key, default=None):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return default

    def __getitem__(self, key):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return None

    @staticmethod
    def from_dict(
        data: Dict[str, Any],
    ) -> Optional[DescribeAwaitsByUserIdResult]:
        if data is None:
            return None
        return DescribeAwaitsByUserIdResult()\
            .with_items([
                Await.from_dict(data.get('items')[i])
                for i in range(len(data.get('items')) if data.get('items') else 0)
            ])\
            .with_next_page_token(data.get('nextPageToken'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "items": [
                self.items[i].to_dict() if self.items[i] else None
                for i in range(len(self.items) if self.items else 0)
            ],
            "nextPageToken": self.next_page_token,
        }


class GetAwaitResult(core.Gs2Result):
    item: Await = None

    def with_item(self, item: Await) -> GetAwaitResult:
        self.item = item
        return self

    def get(self, key, default=None):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return default

    def __getitem__(self, key):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return None

    @staticmethod
    def from_dict(
        data: Dict[str, Any],
    ) -> Optional[GetAwaitResult]:
        if data is None:
            return None
        return GetAwaitResult()\
            .with_item(Await.from_dict(data.get('item')))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "item": self.item.to_dict() if self.item else None,
        }


class GetAwaitByUserIdResult(core.Gs2Result):
    item: Await = None

    def with_item(self, item: Await) -> GetAwaitByUserIdResult:
        self.item = item
        return self

    def get(self, key, default=None):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return default

    def __getitem__(self, key):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return None

    @staticmethod
    def from_dict(
        data: Dict[str, Any],
    ) -> Optional[GetAwaitByUserIdResult]:
        if data is None:
            return None
        return GetAwaitByUserIdResult()\
            .with_item(Await.from_dict(data.get('item')))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "item": self.item.to_dict() if self.item else None,
        }


class AcquireResult(core.Gs2Result):
    item: Await = None
    transaction_id: str = None
    stamp_sheet: str = None
    stamp_sheet_encryption_key_id: str = None
    auto_run_stamp_sheet: bool = None

    def with_item(self, item: Await) -> AcquireResult:
        self.item = item
        return self

    def with_transaction_id(self, transaction_id: str) -> AcquireResult:
        self.transaction_id = transaction_id
        return self

    def with_stamp_sheet(self, stamp_sheet: str) -> AcquireResult:
        self.stamp_sheet = stamp_sheet
        return self

    def with_stamp_sheet_encryption_key_id(self, stamp_sheet_encryption_key_id: str) -> AcquireResult:
        self.stamp_sheet_encryption_key_id = stamp_sheet_encryption_key_id
        return self

    def with_auto_run_stamp_sheet(self, auto_run_stamp_sheet: bool) -> AcquireResult:
        self.auto_run_stamp_sheet = auto_run_stamp_sheet
        return self

    def get(self, key, default=None):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return default

    def __getitem__(self, key):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return None

    @staticmethod
    def from_dict(
        data: Dict[str, Any],
    ) -> Optional[AcquireResult]:
        if data is None:
            return None
        return AcquireResult()\
            .with_item(Await.from_dict(data.get('item')))\
            .with_transaction_id(data.get('transactionId'))\
            .with_stamp_sheet(data.get('stampSheet'))\
            .with_stamp_sheet_encryption_key_id(data.get('stampSheetEncryptionKeyId'))\
            .with_auto_run_stamp_sheet(data.get('autoRunStampSheet'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "item": self.item.to_dict() if self.item else None,
            "transactionId": self.transaction_id,
            "stampSheet": self.stamp_sheet,
            "stampSheetEncryptionKeyId": self.stamp_sheet_encryption_key_id,
            "autoRunStampSheet": self.auto_run_stamp_sheet,
        }


class AcquireByUserIdResult(core.Gs2Result):
    item: Await = None
    transaction_id: str = None
    stamp_sheet: str = None
    stamp_sheet_encryption_key_id: str = None
    auto_run_stamp_sheet: bool = None

    def with_item(self, item: Await) -> AcquireByUserIdResult:
        self.item = item
        return self

    def with_transaction_id(self, transaction_id: str) -> AcquireByUserIdResult:
        self.transaction_id = transaction_id
        return self

    def with_stamp_sheet(self, stamp_sheet: str) -> AcquireByUserIdResult:
        self.stamp_sheet = stamp_sheet
        return self

    def with_stamp_sheet_encryption_key_id(self, stamp_sheet_encryption_key_id: str) -> AcquireByUserIdResult:
        self.stamp_sheet_encryption_key_id = stamp_sheet_encryption_key_id
        return self

    def with_auto_run_stamp_sheet(self, auto_run_stamp_sheet: bool) -> AcquireByUserIdResult:
        self.auto_run_stamp_sheet = auto_run_stamp_sheet
        return self

    def get(self, key, default=None):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return default

    def __getitem__(self, key):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return None

    @staticmethod
    def from_dict(
        data: Dict[str, Any],
    ) -> Optional[AcquireByUserIdResult]:
        if data is None:
            return None
        return AcquireByUserIdResult()\
            .with_item(Await.from_dict(data.get('item')))\
            .with_transaction_id(data.get('transactionId'))\
            .with_stamp_sheet(data.get('stampSheet'))\
            .with_stamp_sheet_encryption_key_id(data.get('stampSheetEncryptionKeyId'))\
            .with_auto_run_stamp_sheet(data.get('autoRunStampSheet'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "item": self.item.to_dict() if self.item else None,
            "transactionId": self.transaction_id,
            "stampSheet": self.stamp_sheet,
            "stampSheetEncryptionKeyId": self.stamp_sheet_encryption_key_id,
            "autoRunStampSheet": self.auto_run_stamp_sheet,
        }


class AcquireForceByUserIdResult(core.Gs2Result):
    item: Await = None
    transaction_id: str = None
    stamp_sheet: str = None
    stamp_sheet_encryption_key_id: str = None
    auto_run_stamp_sheet: bool = None

    def with_item(self, item: Await) -> AcquireForceByUserIdResult:
        self.item = item
        return self

    def with_transaction_id(self, transaction_id: str) -> AcquireForceByUserIdResult:
        self.transaction_id = transaction_id
        return self

    def with_stamp_sheet(self, stamp_sheet: str) -> AcquireForceByUserIdResult:
        self.stamp_sheet = stamp_sheet
        return self

    def with_stamp_sheet_encryption_key_id(self, stamp_sheet_encryption_key_id: str) -> AcquireForceByUserIdResult:
        self.stamp_sheet_encryption_key_id = stamp_sheet_encryption_key_id
        return self

    def with_auto_run_stamp_sheet(self, auto_run_stamp_sheet: bool) -> AcquireForceByUserIdResult:
        self.auto_run_stamp_sheet = auto_run_stamp_sheet
        return self

    def get(self, key, default=None):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return default

    def __getitem__(self, key):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return None

    @staticmethod
    def from_dict(
        data: Dict[str, Any],
    ) -> Optional[AcquireForceByUserIdResult]:
        if data is None:
            return None
        return AcquireForceByUserIdResult()\
            .with_item(Await.from_dict(data.get('item')))\
            .with_transaction_id(data.get('transactionId'))\
            .with_stamp_sheet(data.get('stampSheet'))\
            .with_stamp_sheet_encryption_key_id(data.get('stampSheetEncryptionKeyId'))\
            .with_auto_run_stamp_sheet(data.get('autoRunStampSheet'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "item": self.item.to_dict() if self.item else None,
            "transactionId": self.transaction_id,
            "stampSheet": self.stamp_sheet,
            "stampSheetEncryptionKeyId": self.stamp_sheet_encryption_key_id,
            "autoRunStampSheet": self.auto_run_stamp_sheet,
        }


class SkipResult(core.Gs2Result):
    item: Await = None
    transaction_id: str = None
    stamp_sheet: str = None
    stamp_sheet_encryption_key_id: str = None
    auto_run_stamp_sheet: bool = None

    def with_item(self, item: Await) -> SkipResult:
        self.item = item
        return self

    def with_transaction_id(self, transaction_id: str) -> SkipResult:
        self.transaction_id = transaction_id
        return self

    def with_stamp_sheet(self, stamp_sheet: str) -> SkipResult:
        self.stamp_sheet = stamp_sheet
        return self

    def with_stamp_sheet_encryption_key_id(self, stamp_sheet_encryption_key_id: str) -> SkipResult:
        self.stamp_sheet_encryption_key_id = stamp_sheet_encryption_key_id
        return self

    def with_auto_run_stamp_sheet(self, auto_run_stamp_sheet: bool) -> SkipResult:
        self.auto_run_stamp_sheet = auto_run_stamp_sheet
        return self

    def get(self, key, default=None):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return default

    def __getitem__(self, key):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return None

    @staticmethod
    def from_dict(
        data: Dict[str, Any],
    ) -> Optional[SkipResult]:
        if data is None:
            return None
        return SkipResult()\
            .with_item(Await.from_dict(data.get('item')))\
            .with_transaction_id(data.get('transactionId'))\
            .with_stamp_sheet(data.get('stampSheet'))\
            .with_stamp_sheet_encryption_key_id(data.get('stampSheetEncryptionKeyId'))\
            .with_auto_run_stamp_sheet(data.get('autoRunStampSheet'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "item": self.item.to_dict() if self.item else None,
            "transactionId": self.transaction_id,
            "stampSheet": self.stamp_sheet,
            "stampSheetEncryptionKeyId": self.stamp_sheet_encryption_key_id,
            "autoRunStampSheet": self.auto_run_stamp_sheet,
        }


class SkipByUserIdResult(core.Gs2Result):
    item: Await = None
    transaction_id: str = None
    stamp_sheet: str = None
    stamp_sheet_encryption_key_id: str = None
    auto_run_stamp_sheet: bool = None

    def with_item(self, item: Await) -> SkipByUserIdResult:
        self.item = item
        return self

    def with_transaction_id(self, transaction_id: str) -> SkipByUserIdResult:
        self.transaction_id = transaction_id
        return self

    def with_stamp_sheet(self, stamp_sheet: str) -> SkipByUserIdResult:
        self.stamp_sheet = stamp_sheet
        return self

    def with_stamp_sheet_encryption_key_id(self, stamp_sheet_encryption_key_id: str) -> SkipByUserIdResult:
        self.stamp_sheet_encryption_key_id = stamp_sheet_encryption_key_id
        return self

    def with_auto_run_stamp_sheet(self, auto_run_stamp_sheet: bool) -> SkipByUserIdResult:
        self.auto_run_stamp_sheet = auto_run_stamp_sheet
        return self

    def get(self, key, default=None):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return default

    def __getitem__(self, key):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return None

    @staticmethod
    def from_dict(
        data: Dict[str, Any],
    ) -> Optional[SkipByUserIdResult]:
        if data is None:
            return None
        return SkipByUserIdResult()\
            .with_item(Await.from_dict(data.get('item')))\
            .with_transaction_id(data.get('transactionId'))\
            .with_stamp_sheet(data.get('stampSheet'))\
            .with_stamp_sheet_encryption_key_id(data.get('stampSheetEncryptionKeyId'))\
            .with_auto_run_stamp_sheet(data.get('autoRunStampSheet'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "item": self.item.to_dict() if self.item else None,
            "transactionId": self.transaction_id,
            "stampSheet": self.stamp_sheet,
            "stampSheetEncryptionKeyId": self.stamp_sheet_encryption_key_id,
            "autoRunStampSheet": self.auto_run_stamp_sheet,
        }


class DeleteAwaitResult(core.Gs2Result):
    item: Await = None

    def with_item(self, item: Await) -> DeleteAwaitResult:
        self.item = item
        return self

    def get(self, key, default=None):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return default

    def __getitem__(self, key):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return None

    @staticmethod
    def from_dict(
        data: Dict[str, Any],
    ) -> Optional[DeleteAwaitResult]:
        if data is None:
            return None
        return DeleteAwaitResult()\
            .with_item(Await.from_dict(data.get('item')))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "item": self.item.to_dict() if self.item else None,
        }


class DeleteAwaitByUserIdResult(core.Gs2Result):
    item: Await = None

    def with_item(self, item: Await) -> DeleteAwaitByUserIdResult:
        self.item = item
        return self

    def get(self, key, default=None):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return default

    def __getitem__(self, key):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return None

    @staticmethod
    def from_dict(
        data: Dict[str, Any],
    ) -> Optional[DeleteAwaitByUserIdResult]:
        if data is None:
            return None
        return DeleteAwaitByUserIdResult()\
            .with_item(Await.from_dict(data.get('item')))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "item": self.item.to_dict() if self.item else None,
        }


class CreateAwaitByStampSheetResult(core.Gs2Result):
    item: Await = None
    unlock_at: int = None

    def with_item(self, item: Await) -> CreateAwaitByStampSheetResult:
        self.item = item
        return self

    def with_unlock_at(self, unlock_at: int) -> CreateAwaitByStampSheetResult:
        self.unlock_at = unlock_at
        return self

    def get(self, key, default=None):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return default

    def __getitem__(self, key):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return None

    @staticmethod
    def from_dict(
        data: Dict[str, Any],
    ) -> Optional[CreateAwaitByStampSheetResult]:
        if data is None:
            return None
        return CreateAwaitByStampSheetResult()\
            .with_item(Await.from_dict(data.get('item')))\
            .with_unlock_at(data.get('unlockAt'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "item": self.item.to_dict() if self.item else None,
            "unlockAt": self.unlock_at,
        }


class DeleteAwaitByStampTaskResult(core.Gs2Result):
    item: Await = None
    new_context_stack: str = None

    def with_item(self, item: Await) -> DeleteAwaitByStampTaskResult:
        self.item = item
        return self

    def with_new_context_stack(self, new_context_stack: str) -> DeleteAwaitByStampTaskResult:
        self.new_context_stack = new_context_stack
        return self

    def get(self, key, default=None):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return default

    def __getitem__(self, key):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return None

    @staticmethod
    def from_dict(
        data: Dict[str, Any],
    ) -> Optional[DeleteAwaitByStampTaskResult]:
        if data is None:
            return None
        return DeleteAwaitByStampTaskResult()\
            .with_item(Await.from_dict(data.get('item')))\
            .with_new_context_stack(data.get('newContextStack'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "item": self.item.to_dict() if self.item else None,
            "newContextStack": self.new_context_stack,
        }