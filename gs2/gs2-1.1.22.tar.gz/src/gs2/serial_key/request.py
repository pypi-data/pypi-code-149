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


class DescribeNamespacesRequest(core.Gs2Request):

    context_stack: str = None
    page_token: str = None
    limit: int = None

    def with_page_token(self, page_token: str) -> DescribeNamespacesRequest:
        self.page_token = page_token
        return self

    def with_limit(self, limit: int) -> DescribeNamespacesRequest:
        self.limit = limit
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
    ) -> Optional[DescribeNamespacesRequest]:
        if data is None:
            return None
        return DescribeNamespacesRequest()\
            .with_page_token(data.get('pageToken'))\
            .with_limit(data.get('limit'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "pageToken": self.page_token,
            "limit": self.limit,
        }


class CreateNamespaceRequest(core.Gs2Request):

    context_stack: str = None
    name: str = None
    description: str = None
    log_setting: LogSetting = None

    def with_name(self, name: str) -> CreateNamespaceRequest:
        self.name = name
        return self

    def with_description(self, description: str) -> CreateNamespaceRequest:
        self.description = description
        return self

    def with_log_setting(self, log_setting: LogSetting) -> CreateNamespaceRequest:
        self.log_setting = log_setting
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
    ) -> Optional[CreateNamespaceRequest]:
        if data is None:
            return None
        return CreateNamespaceRequest()\
            .with_name(data.get('name'))\
            .with_description(data.get('description'))\
            .with_log_setting(LogSetting.from_dict(data.get('logSetting')))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "description": self.description,
            "logSetting": self.log_setting.to_dict() if self.log_setting else None,
        }


class GetNamespaceStatusRequest(core.Gs2Request):

    context_stack: str = None
    namespace_name: str = None

    def with_namespace_name(self, namespace_name: str) -> GetNamespaceStatusRequest:
        self.namespace_name = namespace_name
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
    ) -> Optional[GetNamespaceStatusRequest]:
        if data is None:
            return None
        return GetNamespaceStatusRequest()\
            .with_namespace_name(data.get('namespaceName'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "namespaceName": self.namespace_name,
        }


class GetNamespaceRequest(core.Gs2Request):

    context_stack: str = None
    namespace_name: str = None

    def with_namespace_name(self, namespace_name: str) -> GetNamespaceRequest:
        self.namespace_name = namespace_name
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
    ) -> Optional[GetNamespaceRequest]:
        if data is None:
            return None
        return GetNamespaceRequest()\
            .with_namespace_name(data.get('namespaceName'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "namespaceName": self.namespace_name,
        }


class UpdateNamespaceRequest(core.Gs2Request):

    context_stack: str = None
    namespace_name: str = None
    description: str = None
    log_setting: LogSetting = None

    def with_namespace_name(self, namespace_name: str) -> UpdateNamespaceRequest:
        self.namespace_name = namespace_name
        return self

    def with_description(self, description: str) -> UpdateNamespaceRequest:
        self.description = description
        return self

    def with_log_setting(self, log_setting: LogSetting) -> UpdateNamespaceRequest:
        self.log_setting = log_setting
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
    ) -> Optional[UpdateNamespaceRequest]:
        if data is None:
            return None
        return UpdateNamespaceRequest()\
            .with_namespace_name(data.get('namespaceName'))\
            .with_description(data.get('description'))\
            .with_log_setting(LogSetting.from_dict(data.get('logSetting')))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "namespaceName": self.namespace_name,
            "description": self.description,
            "logSetting": self.log_setting.to_dict() if self.log_setting else None,
        }


class DeleteNamespaceRequest(core.Gs2Request):

    context_stack: str = None
    namespace_name: str = None

    def with_namespace_name(self, namespace_name: str) -> DeleteNamespaceRequest:
        self.namespace_name = namespace_name
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
    ) -> Optional[DeleteNamespaceRequest]:
        if data is None:
            return None
        return DeleteNamespaceRequest()\
            .with_namespace_name(data.get('namespaceName'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "namespaceName": self.namespace_name,
        }


class DescribeIssueJobsRequest(core.Gs2Request):

    context_stack: str = None
    namespace_name: str = None
    campaign_model_name: str = None
    page_token: str = None
    limit: int = None

    def with_namespace_name(self, namespace_name: str) -> DescribeIssueJobsRequest:
        self.namespace_name = namespace_name
        return self

    def with_campaign_model_name(self, campaign_model_name: str) -> DescribeIssueJobsRequest:
        self.campaign_model_name = campaign_model_name
        return self

    def with_page_token(self, page_token: str) -> DescribeIssueJobsRequest:
        self.page_token = page_token
        return self

    def with_limit(self, limit: int) -> DescribeIssueJobsRequest:
        self.limit = limit
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
    ) -> Optional[DescribeIssueJobsRequest]:
        if data is None:
            return None
        return DescribeIssueJobsRequest()\
            .with_namespace_name(data.get('namespaceName'))\
            .with_campaign_model_name(data.get('campaignModelName'))\
            .with_page_token(data.get('pageToken'))\
            .with_limit(data.get('limit'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "namespaceName": self.namespace_name,
            "campaignModelName": self.campaign_model_name,
            "pageToken": self.page_token,
            "limit": self.limit,
        }


class GetIssueJobRequest(core.Gs2Request):

    context_stack: str = None
    namespace_name: str = None
    campaign_model_name: str = None
    issue_job_name: str = None

    def with_namespace_name(self, namespace_name: str) -> GetIssueJobRequest:
        self.namespace_name = namespace_name
        return self

    def with_campaign_model_name(self, campaign_model_name: str) -> GetIssueJobRequest:
        self.campaign_model_name = campaign_model_name
        return self

    def with_issue_job_name(self, issue_job_name: str) -> GetIssueJobRequest:
        self.issue_job_name = issue_job_name
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
    ) -> Optional[GetIssueJobRequest]:
        if data is None:
            return None
        return GetIssueJobRequest()\
            .with_namespace_name(data.get('namespaceName'))\
            .with_campaign_model_name(data.get('campaignModelName'))\
            .with_issue_job_name(data.get('issueJobName'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "namespaceName": self.namespace_name,
            "campaignModelName": self.campaign_model_name,
            "issueJobName": self.issue_job_name,
        }


class IssueRequest(core.Gs2Request):

    context_stack: str = None
    namespace_name: str = None
    campaign_model_name: str = None
    metadata: str = None
    issue_request_count: int = None

    def with_namespace_name(self, namespace_name: str) -> IssueRequest:
        self.namespace_name = namespace_name
        return self

    def with_campaign_model_name(self, campaign_model_name: str) -> IssueRequest:
        self.campaign_model_name = campaign_model_name
        return self

    def with_metadata(self, metadata: str) -> IssueRequest:
        self.metadata = metadata
        return self

    def with_issue_request_count(self, issue_request_count: int) -> IssueRequest:
        self.issue_request_count = issue_request_count
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
    ) -> Optional[IssueRequest]:
        if data is None:
            return None
        return IssueRequest()\
            .with_namespace_name(data.get('namespaceName'))\
            .with_campaign_model_name(data.get('campaignModelName'))\
            .with_metadata(data.get('metadata'))\
            .with_issue_request_count(data.get('issueRequestCount'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "namespaceName": self.namespace_name,
            "campaignModelName": self.campaign_model_name,
            "metadata": self.metadata,
            "issueRequestCount": self.issue_request_count,
        }


class DescribeSerialKeysRequest(core.Gs2Request):

    context_stack: str = None
    namespace_name: str = None
    campaign_model_name: str = None
    issue_job_name: str = None
    page_token: str = None
    limit: int = None

    def with_namespace_name(self, namespace_name: str) -> DescribeSerialKeysRequest:
        self.namespace_name = namespace_name
        return self

    def with_campaign_model_name(self, campaign_model_name: str) -> DescribeSerialKeysRequest:
        self.campaign_model_name = campaign_model_name
        return self

    def with_issue_job_name(self, issue_job_name: str) -> DescribeSerialKeysRequest:
        self.issue_job_name = issue_job_name
        return self

    def with_page_token(self, page_token: str) -> DescribeSerialKeysRequest:
        self.page_token = page_token
        return self

    def with_limit(self, limit: int) -> DescribeSerialKeysRequest:
        self.limit = limit
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
    ) -> Optional[DescribeSerialKeysRequest]:
        if data is None:
            return None
        return DescribeSerialKeysRequest()\
            .with_namespace_name(data.get('namespaceName'))\
            .with_campaign_model_name(data.get('campaignModelName'))\
            .with_issue_job_name(data.get('issueJobName'))\
            .with_page_token(data.get('pageToken'))\
            .with_limit(data.get('limit'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "namespaceName": self.namespace_name,
            "campaignModelName": self.campaign_model_name,
            "issueJobName": self.issue_job_name,
            "pageToken": self.page_token,
            "limit": self.limit,
        }


class DownloadSerialCodesRequest(core.Gs2Request):

    context_stack: str = None
    namespace_name: str = None
    campaign_model_name: str = None
    issue_job_name: str = None

    def with_namespace_name(self, namespace_name: str) -> DownloadSerialCodesRequest:
        self.namespace_name = namespace_name
        return self

    def with_campaign_model_name(self, campaign_model_name: str) -> DownloadSerialCodesRequest:
        self.campaign_model_name = campaign_model_name
        return self

    def with_issue_job_name(self, issue_job_name: str) -> DownloadSerialCodesRequest:
        self.issue_job_name = issue_job_name
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
    ) -> Optional[DownloadSerialCodesRequest]:
        if data is None:
            return None
        return DownloadSerialCodesRequest()\
            .with_namespace_name(data.get('namespaceName'))\
            .with_campaign_model_name(data.get('campaignModelName'))\
            .with_issue_job_name(data.get('issueJobName'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "namespaceName": self.namespace_name,
            "campaignModelName": self.campaign_model_name,
            "issueJobName": self.issue_job_name,
        }


class GetSerialKeyRequest(core.Gs2Request):

    context_stack: str = None
    namespace_name: str = None
    code: str = None

    def with_namespace_name(self, namespace_name: str) -> GetSerialKeyRequest:
        self.namespace_name = namespace_name
        return self

    def with_code(self, code: str) -> GetSerialKeyRequest:
        self.code = code
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
    ) -> Optional[GetSerialKeyRequest]:
        if data is None:
            return None
        return GetSerialKeyRequest()\
            .with_namespace_name(data.get('namespaceName'))\
            .with_code(data.get('code'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "namespaceName": self.namespace_name,
            "code": self.code,
        }


class UseRequest(core.Gs2Request):

    context_stack: str = None
    namespace_name: str = None
    access_token: str = None
    code: str = None
    duplication_avoider: str = None

    def with_namespace_name(self, namespace_name: str) -> UseRequest:
        self.namespace_name = namespace_name
        return self

    def with_access_token(self, access_token: str) -> UseRequest:
        self.access_token = access_token
        return self

    def with_code(self, code: str) -> UseRequest:
        self.code = code
        return self

    def with_duplication_avoider(self, duplication_avoider: str) -> UseRequest:
        self.duplication_avoider = duplication_avoider
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
    ) -> Optional[UseRequest]:
        if data is None:
            return None
        return UseRequest()\
            .with_namespace_name(data.get('namespaceName'))\
            .with_access_token(data.get('accessToken'))\
            .with_code(data.get('code'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "namespaceName": self.namespace_name,
            "accessToken": self.access_token,
            "code": self.code,
        }


class UseByUserIdRequest(core.Gs2Request):

    context_stack: str = None
    namespace_name: str = None
    user_id: str = None
    code: str = None
    duplication_avoider: str = None

    def with_namespace_name(self, namespace_name: str) -> UseByUserIdRequest:
        self.namespace_name = namespace_name
        return self

    def with_user_id(self, user_id: str) -> UseByUserIdRequest:
        self.user_id = user_id
        return self

    def with_code(self, code: str) -> UseByUserIdRequest:
        self.code = code
        return self

    def with_duplication_avoider(self, duplication_avoider: str) -> UseByUserIdRequest:
        self.duplication_avoider = duplication_avoider
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
    ) -> Optional[UseByUserIdRequest]:
        if data is None:
            return None
        return UseByUserIdRequest()\
            .with_namespace_name(data.get('namespaceName'))\
            .with_user_id(data.get('userId'))\
            .with_code(data.get('code'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "namespaceName": self.namespace_name,
            "userId": self.user_id,
            "code": self.code,
        }


class UseByStampTaskRequest(core.Gs2Request):

    context_stack: str = None
    stamp_task: str = None
    key_id: str = None

    def with_stamp_task(self, stamp_task: str) -> UseByStampTaskRequest:
        self.stamp_task = stamp_task
        return self

    def with_key_id(self, key_id: str) -> UseByStampTaskRequest:
        self.key_id = key_id
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
    ) -> Optional[UseByStampTaskRequest]:
        if data is None:
            return None
        return UseByStampTaskRequest()\
            .with_stamp_task(data.get('stampTask'))\
            .with_key_id(data.get('keyId'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "stampTask": self.stamp_task,
            "keyId": self.key_id,
        }


class DescribeCampaignModelsRequest(core.Gs2Request):

    context_stack: str = None
    namespace_name: str = None

    def with_namespace_name(self, namespace_name: str) -> DescribeCampaignModelsRequest:
        self.namespace_name = namespace_name
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
    ) -> Optional[DescribeCampaignModelsRequest]:
        if data is None:
            return None
        return DescribeCampaignModelsRequest()\
            .with_namespace_name(data.get('namespaceName'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "namespaceName": self.namespace_name,
        }


class GetCampaignModelRequest(core.Gs2Request):

    context_stack: str = None
    namespace_name: str = None
    campaign_model_name: str = None

    def with_namespace_name(self, namespace_name: str) -> GetCampaignModelRequest:
        self.namespace_name = namespace_name
        return self

    def with_campaign_model_name(self, campaign_model_name: str) -> GetCampaignModelRequest:
        self.campaign_model_name = campaign_model_name
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
    ) -> Optional[GetCampaignModelRequest]:
        if data is None:
            return None
        return GetCampaignModelRequest()\
            .with_namespace_name(data.get('namespaceName'))\
            .with_campaign_model_name(data.get('campaignModelName'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "namespaceName": self.namespace_name,
            "campaignModelName": self.campaign_model_name,
        }


class DescribeCampaignModelMastersRequest(core.Gs2Request):

    context_stack: str = None
    namespace_name: str = None
    page_token: str = None
    limit: int = None

    def with_namespace_name(self, namespace_name: str) -> DescribeCampaignModelMastersRequest:
        self.namespace_name = namespace_name
        return self

    def with_page_token(self, page_token: str) -> DescribeCampaignModelMastersRequest:
        self.page_token = page_token
        return self

    def with_limit(self, limit: int) -> DescribeCampaignModelMastersRequest:
        self.limit = limit
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
    ) -> Optional[DescribeCampaignModelMastersRequest]:
        if data is None:
            return None
        return DescribeCampaignModelMastersRequest()\
            .with_namespace_name(data.get('namespaceName'))\
            .with_page_token(data.get('pageToken'))\
            .with_limit(data.get('limit'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "namespaceName": self.namespace_name,
            "pageToken": self.page_token,
            "limit": self.limit,
        }


class CreateCampaignModelMasterRequest(core.Gs2Request):

    context_stack: str = None
    namespace_name: str = None
    name: str = None
    description: str = None
    metadata: str = None
    enable_campaign_code: bool = None

    def with_namespace_name(self, namespace_name: str) -> CreateCampaignModelMasterRequest:
        self.namespace_name = namespace_name
        return self

    def with_name(self, name: str) -> CreateCampaignModelMasterRequest:
        self.name = name
        return self

    def with_description(self, description: str) -> CreateCampaignModelMasterRequest:
        self.description = description
        return self

    def with_metadata(self, metadata: str) -> CreateCampaignModelMasterRequest:
        self.metadata = metadata
        return self

    def with_enable_campaign_code(self, enable_campaign_code: bool) -> CreateCampaignModelMasterRequest:
        self.enable_campaign_code = enable_campaign_code
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
    ) -> Optional[CreateCampaignModelMasterRequest]:
        if data is None:
            return None
        return CreateCampaignModelMasterRequest()\
            .with_namespace_name(data.get('namespaceName'))\
            .with_name(data.get('name'))\
            .with_description(data.get('description'))\
            .with_metadata(data.get('metadata'))\
            .with_enable_campaign_code(data.get('enableCampaignCode'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "namespaceName": self.namespace_name,
            "name": self.name,
            "description": self.description,
            "metadata": self.metadata,
            "enableCampaignCode": self.enable_campaign_code,
        }


class GetCampaignModelMasterRequest(core.Gs2Request):

    context_stack: str = None
    namespace_name: str = None
    campaign_model_name: str = None

    def with_namespace_name(self, namespace_name: str) -> GetCampaignModelMasterRequest:
        self.namespace_name = namespace_name
        return self

    def with_campaign_model_name(self, campaign_model_name: str) -> GetCampaignModelMasterRequest:
        self.campaign_model_name = campaign_model_name
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
    ) -> Optional[GetCampaignModelMasterRequest]:
        if data is None:
            return None
        return GetCampaignModelMasterRequest()\
            .with_namespace_name(data.get('namespaceName'))\
            .with_campaign_model_name(data.get('campaignModelName'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "namespaceName": self.namespace_name,
            "campaignModelName": self.campaign_model_name,
        }


class UpdateCampaignModelMasterRequest(core.Gs2Request):

    context_stack: str = None
    namespace_name: str = None
    campaign_model_name: str = None
    description: str = None
    metadata: str = None
    enable_campaign_code: bool = None

    def with_namespace_name(self, namespace_name: str) -> UpdateCampaignModelMasterRequest:
        self.namespace_name = namespace_name
        return self

    def with_campaign_model_name(self, campaign_model_name: str) -> UpdateCampaignModelMasterRequest:
        self.campaign_model_name = campaign_model_name
        return self

    def with_description(self, description: str) -> UpdateCampaignModelMasterRequest:
        self.description = description
        return self

    def with_metadata(self, metadata: str) -> UpdateCampaignModelMasterRequest:
        self.metadata = metadata
        return self

    def with_enable_campaign_code(self, enable_campaign_code: bool) -> UpdateCampaignModelMasterRequest:
        self.enable_campaign_code = enable_campaign_code
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
    ) -> Optional[UpdateCampaignModelMasterRequest]:
        if data is None:
            return None
        return UpdateCampaignModelMasterRequest()\
            .with_namespace_name(data.get('namespaceName'))\
            .with_campaign_model_name(data.get('campaignModelName'))\
            .with_description(data.get('description'))\
            .with_metadata(data.get('metadata'))\
            .with_enable_campaign_code(data.get('enableCampaignCode'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "namespaceName": self.namespace_name,
            "campaignModelName": self.campaign_model_name,
            "description": self.description,
            "metadata": self.metadata,
            "enableCampaignCode": self.enable_campaign_code,
        }


class DeleteCampaignModelMasterRequest(core.Gs2Request):

    context_stack: str = None
    namespace_name: str = None
    campaign_model_name: str = None

    def with_namespace_name(self, namespace_name: str) -> DeleteCampaignModelMasterRequest:
        self.namespace_name = namespace_name
        return self

    def with_campaign_model_name(self, campaign_model_name: str) -> DeleteCampaignModelMasterRequest:
        self.campaign_model_name = campaign_model_name
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
    ) -> Optional[DeleteCampaignModelMasterRequest]:
        if data is None:
            return None
        return DeleteCampaignModelMasterRequest()\
            .with_namespace_name(data.get('namespaceName'))\
            .with_campaign_model_name(data.get('campaignModelName'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "namespaceName": self.namespace_name,
            "campaignModelName": self.campaign_model_name,
        }


class ExportMasterRequest(core.Gs2Request):

    context_stack: str = None
    namespace_name: str = None

    def with_namespace_name(self, namespace_name: str) -> ExportMasterRequest:
        self.namespace_name = namespace_name
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
    ) -> Optional[ExportMasterRequest]:
        if data is None:
            return None
        return ExportMasterRequest()\
            .with_namespace_name(data.get('namespaceName'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "namespaceName": self.namespace_name,
        }


class GetCurrentCampaignMasterRequest(core.Gs2Request):

    context_stack: str = None
    namespace_name: str = None

    def with_namespace_name(self, namespace_name: str) -> GetCurrentCampaignMasterRequest:
        self.namespace_name = namespace_name
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
    ) -> Optional[GetCurrentCampaignMasterRequest]:
        if data is None:
            return None
        return GetCurrentCampaignMasterRequest()\
            .with_namespace_name(data.get('namespaceName'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "namespaceName": self.namespace_name,
        }


class UpdateCurrentCampaignMasterRequest(core.Gs2Request):

    context_stack: str = None
    namespace_name: str = None
    settings: str = None

    def with_namespace_name(self, namespace_name: str) -> UpdateCurrentCampaignMasterRequest:
        self.namespace_name = namespace_name
        return self

    def with_settings(self, settings: str) -> UpdateCurrentCampaignMasterRequest:
        self.settings = settings
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
    ) -> Optional[UpdateCurrentCampaignMasterRequest]:
        if data is None:
            return None
        return UpdateCurrentCampaignMasterRequest()\
            .with_namespace_name(data.get('namespaceName'))\
            .with_settings(data.get('settings'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "namespaceName": self.namespace_name,
            "settings": self.settings,
        }


class UpdateCurrentCampaignMasterFromGitHubRequest(core.Gs2Request):

    context_stack: str = None
    namespace_name: str = None
    checkout_setting: GitHubCheckoutSetting = None

    def with_namespace_name(self, namespace_name: str) -> UpdateCurrentCampaignMasterFromGitHubRequest:
        self.namespace_name = namespace_name
        return self

    def with_checkout_setting(self, checkout_setting: GitHubCheckoutSetting) -> UpdateCurrentCampaignMasterFromGitHubRequest:
        self.checkout_setting = checkout_setting
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
    ) -> Optional[UpdateCurrentCampaignMasterFromGitHubRequest]:
        if data is None:
            return None
        return UpdateCurrentCampaignMasterFromGitHubRequest()\
            .with_namespace_name(data.get('namespaceName'))\
            .with_checkout_setting(GitHubCheckoutSetting.from_dict(data.get('checkoutSetting')))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "namespaceName": self.namespace_name,
            "checkoutSetting": self.checkout_setting.to_dict() if self.checkout_setting else None,
        }