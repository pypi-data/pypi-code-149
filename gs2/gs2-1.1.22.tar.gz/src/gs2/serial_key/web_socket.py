# encoding: utf-8
#
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

from gs2.core import *
from .request import *
from .result import *


class Gs2SerialKeyWebSocketClient(web_socket.AbstractGs2WebSocketClient):

    def _describe_namespaces(
        self,
        request: DescribeNamespacesRequest,
        callback: Callable[[AsyncResult[DescribeNamespacesResult]], None],
    ):
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service="serialKey",
            component='namespace',
            function='describeNamespaces',
            request_id=request_id,
        )

        if request.context_stack:
            body['contextStack'] = str(request.context_stack)
        if request.page_token is not None:
            body["pageToken"] = request.page_token
        if request.limit is not None:
            body["limit"] = request.limit

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            web_socket.NetworkJob(
                request_id=request_id,
                result_type=DescribeNamespacesResult,
                callback=callback,
                body=body,
            )
        )

    def describe_namespaces(
        self,
        request: DescribeNamespacesRequest,
    ) -> DescribeNamespacesResult:
        async_result = []
        with timeout(30):
            self._describe_namespaces(
                request,
                lambda result: async_result.append(result),
            )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def describe_namespaces_async(
        self,
        request: DescribeNamespacesRequest,
    ) -> DescribeNamespacesResult:
        async_result = []
        self._describe_namespaces(
            request,
            lambda result: async_result.append(result),
        )

        import asyncio
        with timeout(30):
            while not async_result:
                await asyncio.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result

    def _create_namespace(
        self,
        request: CreateNamespaceRequest,
        callback: Callable[[AsyncResult[CreateNamespaceResult]], None],
    ):
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service="serialKey",
            component='namespace',
            function='createNamespace',
            request_id=request_id,
        )

        if request.context_stack:
            body['contextStack'] = str(request.context_stack)
        if request.name is not None:
            body["name"] = request.name
        if request.description is not None:
            body["description"] = request.description
        if request.log_setting is not None:
            body["logSetting"] = request.log_setting.to_dict()

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            web_socket.NetworkJob(
                request_id=request_id,
                result_type=CreateNamespaceResult,
                callback=callback,
                body=body,
            )
        )

    def create_namespace(
        self,
        request: CreateNamespaceRequest,
    ) -> CreateNamespaceResult:
        async_result = []
        with timeout(30):
            self._create_namespace(
                request,
                lambda result: async_result.append(result),
            )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def create_namespace_async(
        self,
        request: CreateNamespaceRequest,
    ) -> CreateNamespaceResult:
        async_result = []
        self._create_namespace(
            request,
            lambda result: async_result.append(result),
        )

        import asyncio
        with timeout(30):
            while not async_result:
                await asyncio.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result

    def _get_namespace_status(
        self,
        request: GetNamespaceStatusRequest,
        callback: Callable[[AsyncResult[GetNamespaceStatusResult]], None],
    ):
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service="serialKey",
            component='namespace',
            function='getNamespaceStatus',
            request_id=request_id,
        )

        if request.context_stack:
            body['contextStack'] = str(request.context_stack)
        if request.namespace_name is not None:
            body["namespaceName"] = request.namespace_name

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            web_socket.NetworkJob(
                request_id=request_id,
                result_type=GetNamespaceStatusResult,
                callback=callback,
                body=body,
            )
        )

    def get_namespace_status(
        self,
        request: GetNamespaceStatusRequest,
    ) -> GetNamespaceStatusResult:
        async_result = []
        with timeout(30):
            self._get_namespace_status(
                request,
                lambda result: async_result.append(result),
            )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def get_namespace_status_async(
        self,
        request: GetNamespaceStatusRequest,
    ) -> GetNamespaceStatusResult:
        async_result = []
        self._get_namespace_status(
            request,
            lambda result: async_result.append(result),
        )

        import asyncio
        with timeout(30):
            while not async_result:
                await asyncio.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result

    def _get_namespace(
        self,
        request: GetNamespaceRequest,
        callback: Callable[[AsyncResult[GetNamespaceResult]], None],
    ):
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service="serialKey",
            component='namespace',
            function='getNamespace',
            request_id=request_id,
        )

        if request.context_stack:
            body['contextStack'] = str(request.context_stack)
        if request.namespace_name is not None:
            body["namespaceName"] = request.namespace_name

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            web_socket.NetworkJob(
                request_id=request_id,
                result_type=GetNamespaceResult,
                callback=callback,
                body=body,
            )
        )

    def get_namespace(
        self,
        request: GetNamespaceRequest,
    ) -> GetNamespaceResult:
        async_result = []
        with timeout(30):
            self._get_namespace(
                request,
                lambda result: async_result.append(result),
            )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def get_namespace_async(
        self,
        request: GetNamespaceRequest,
    ) -> GetNamespaceResult:
        async_result = []
        self._get_namespace(
            request,
            lambda result: async_result.append(result),
        )

        import asyncio
        with timeout(30):
            while not async_result:
                await asyncio.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result

    def _update_namespace(
        self,
        request: UpdateNamespaceRequest,
        callback: Callable[[AsyncResult[UpdateNamespaceResult]], None],
    ):
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service="serialKey",
            component='namespace',
            function='updateNamespace',
            request_id=request_id,
        )

        if request.context_stack:
            body['contextStack'] = str(request.context_stack)
        if request.namespace_name is not None:
            body["namespaceName"] = request.namespace_name
        if request.description is not None:
            body["description"] = request.description
        if request.log_setting is not None:
            body["logSetting"] = request.log_setting.to_dict()

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            web_socket.NetworkJob(
                request_id=request_id,
                result_type=UpdateNamespaceResult,
                callback=callback,
                body=body,
            )
        )

    def update_namespace(
        self,
        request: UpdateNamespaceRequest,
    ) -> UpdateNamespaceResult:
        async_result = []
        with timeout(30):
            self._update_namespace(
                request,
                lambda result: async_result.append(result),
            )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def update_namespace_async(
        self,
        request: UpdateNamespaceRequest,
    ) -> UpdateNamespaceResult:
        async_result = []
        self._update_namespace(
            request,
            lambda result: async_result.append(result),
        )

        import asyncio
        with timeout(30):
            while not async_result:
                await asyncio.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result

    def _delete_namespace(
        self,
        request: DeleteNamespaceRequest,
        callback: Callable[[AsyncResult[DeleteNamespaceResult]], None],
    ):
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service="serialKey",
            component='namespace',
            function='deleteNamespace',
            request_id=request_id,
        )

        if request.context_stack:
            body['contextStack'] = str(request.context_stack)
        if request.namespace_name is not None:
            body["namespaceName"] = request.namespace_name

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            web_socket.NetworkJob(
                request_id=request_id,
                result_type=DeleteNamespaceResult,
                callback=callback,
                body=body,
            )
        )

    def delete_namespace(
        self,
        request: DeleteNamespaceRequest,
    ) -> DeleteNamespaceResult:
        async_result = []
        with timeout(30):
            self._delete_namespace(
                request,
                lambda result: async_result.append(result),
            )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def delete_namespace_async(
        self,
        request: DeleteNamespaceRequest,
    ) -> DeleteNamespaceResult:
        async_result = []
        self._delete_namespace(
            request,
            lambda result: async_result.append(result),
        )

        import asyncio
        with timeout(30):
            while not async_result:
                await asyncio.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result

    def _describe_issue_jobs(
        self,
        request: DescribeIssueJobsRequest,
        callback: Callable[[AsyncResult[DescribeIssueJobsResult]], None],
    ):
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service="serialKey",
            component='issueJob',
            function='describeIssueJobs',
            request_id=request_id,
        )

        if request.context_stack:
            body['contextStack'] = str(request.context_stack)
        if request.namespace_name is not None:
            body["namespaceName"] = request.namespace_name
        if request.campaign_model_name is not None:
            body["campaignModelName"] = request.campaign_model_name
        if request.page_token is not None:
            body["pageToken"] = request.page_token
        if request.limit is not None:
            body["limit"] = request.limit

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            web_socket.NetworkJob(
                request_id=request_id,
                result_type=DescribeIssueJobsResult,
                callback=callback,
                body=body,
            )
        )

    def describe_issue_jobs(
        self,
        request: DescribeIssueJobsRequest,
    ) -> DescribeIssueJobsResult:
        async_result = []
        with timeout(30):
            self._describe_issue_jobs(
                request,
                lambda result: async_result.append(result),
            )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def describe_issue_jobs_async(
        self,
        request: DescribeIssueJobsRequest,
    ) -> DescribeIssueJobsResult:
        async_result = []
        self._describe_issue_jobs(
            request,
            lambda result: async_result.append(result),
        )

        import asyncio
        with timeout(30):
            while not async_result:
                await asyncio.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result

    def _get_issue_job(
        self,
        request: GetIssueJobRequest,
        callback: Callable[[AsyncResult[GetIssueJobResult]], None],
    ):
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service="serialKey",
            component='issueJob',
            function='getIssueJob',
            request_id=request_id,
        )

        if request.context_stack:
            body['contextStack'] = str(request.context_stack)
        if request.namespace_name is not None:
            body["namespaceName"] = request.namespace_name
        if request.campaign_model_name is not None:
            body["campaignModelName"] = request.campaign_model_name
        if request.issue_job_name is not None:
            body["issueJobName"] = request.issue_job_name

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            web_socket.NetworkJob(
                request_id=request_id,
                result_type=GetIssueJobResult,
                callback=callback,
                body=body,
            )
        )

    def get_issue_job(
        self,
        request: GetIssueJobRequest,
    ) -> GetIssueJobResult:
        async_result = []
        with timeout(30):
            self._get_issue_job(
                request,
                lambda result: async_result.append(result),
            )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def get_issue_job_async(
        self,
        request: GetIssueJobRequest,
    ) -> GetIssueJobResult:
        async_result = []
        self._get_issue_job(
            request,
            lambda result: async_result.append(result),
        )

        import asyncio
        with timeout(30):
            while not async_result:
                await asyncio.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result

    def _issue(
        self,
        request: IssueRequest,
        callback: Callable[[AsyncResult[IssueResult]], None],
    ):
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service="serialKey",
            component='issueJob',
            function='issue',
            request_id=request_id,
        )

        if request.context_stack:
            body['contextStack'] = str(request.context_stack)
        if request.namespace_name is not None:
            body["namespaceName"] = request.namespace_name
        if request.campaign_model_name is not None:
            body["campaignModelName"] = request.campaign_model_name
        if request.metadata is not None:
            body["metadata"] = request.metadata
        if request.issue_request_count is not None:
            body["issueRequestCount"] = request.issue_request_count

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            web_socket.NetworkJob(
                request_id=request_id,
                result_type=IssueResult,
                callback=callback,
                body=body,
            )
        )

    def issue(
        self,
        request: IssueRequest,
    ) -> IssueResult:
        async_result = []
        with timeout(30):
            self._issue(
                request,
                lambda result: async_result.append(result),
            )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def issue_async(
        self,
        request: IssueRequest,
    ) -> IssueResult:
        async_result = []
        self._issue(
            request,
            lambda result: async_result.append(result),
        )

        import asyncio
        with timeout(30):
            while not async_result:
                await asyncio.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result

    def _describe_serial_keys(
        self,
        request: DescribeSerialKeysRequest,
        callback: Callable[[AsyncResult[DescribeSerialKeysResult]], None],
    ):
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service="serialKey",
            component='serialKey',
            function='describeSerialKeys',
            request_id=request_id,
        )

        if request.context_stack:
            body['contextStack'] = str(request.context_stack)
        if request.namespace_name is not None:
            body["namespaceName"] = request.namespace_name
        if request.campaign_model_name is not None:
            body["campaignModelName"] = request.campaign_model_name
        if request.issue_job_name is not None:
            body["issueJobName"] = request.issue_job_name
        if request.page_token is not None:
            body["pageToken"] = request.page_token
        if request.limit is not None:
            body["limit"] = request.limit

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            web_socket.NetworkJob(
                request_id=request_id,
                result_type=DescribeSerialKeysResult,
                callback=callback,
                body=body,
            )
        )

    def describe_serial_keys(
        self,
        request: DescribeSerialKeysRequest,
    ) -> DescribeSerialKeysResult:
        async_result = []
        with timeout(30):
            self._describe_serial_keys(
                request,
                lambda result: async_result.append(result),
            )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def describe_serial_keys_async(
        self,
        request: DescribeSerialKeysRequest,
    ) -> DescribeSerialKeysResult:
        async_result = []
        self._describe_serial_keys(
            request,
            lambda result: async_result.append(result),
        )

        import asyncio
        with timeout(30):
            while not async_result:
                await asyncio.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result

    def _download_serial_codes(
        self,
        request: DownloadSerialCodesRequest,
        callback: Callable[[AsyncResult[DownloadSerialCodesResult]], None],
    ):
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service="serialKey",
            component='serialKey',
            function='downloadSerialCodes',
            request_id=request_id,
        )

        if request.context_stack:
            body['contextStack'] = str(request.context_stack)
        if request.namespace_name is not None:
            body["namespaceName"] = request.namespace_name
        if request.campaign_model_name is not None:
            body["campaignModelName"] = request.campaign_model_name
        if request.issue_job_name is not None:
            body["issueJobName"] = request.issue_job_name

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            web_socket.NetworkJob(
                request_id=request_id,
                result_type=DownloadSerialCodesResult,
                callback=callback,
                body=body,
            )
        )

    def download_serial_codes(
        self,
        request: DownloadSerialCodesRequest,
    ) -> DownloadSerialCodesResult:
        async_result = []
        with timeout(30):
            self._download_serial_codes(
                request,
                lambda result: async_result.append(result),
            )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def download_serial_codes_async(
        self,
        request: DownloadSerialCodesRequest,
    ) -> DownloadSerialCodesResult:
        async_result = []
        self._download_serial_codes(
            request,
            lambda result: async_result.append(result),
        )

        import asyncio
        with timeout(30):
            while not async_result:
                await asyncio.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result

    def _get_serial_key(
        self,
        request: GetSerialKeyRequest,
        callback: Callable[[AsyncResult[GetSerialKeyResult]], None],
    ):
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service="serialKey",
            component='serialKey',
            function='getSerialKey',
            request_id=request_id,
        )

        if request.context_stack:
            body['contextStack'] = str(request.context_stack)
        if request.namespace_name is not None:
            body["namespaceName"] = request.namespace_name
        if request.code is not None:
            body["code"] = request.code

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            web_socket.NetworkJob(
                request_id=request_id,
                result_type=GetSerialKeyResult,
                callback=callback,
                body=body,
            )
        )

    def get_serial_key(
        self,
        request: GetSerialKeyRequest,
    ) -> GetSerialKeyResult:
        async_result = []
        with timeout(30):
            self._get_serial_key(
                request,
                lambda result: async_result.append(result),
            )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def get_serial_key_async(
        self,
        request: GetSerialKeyRequest,
    ) -> GetSerialKeyResult:
        async_result = []
        self._get_serial_key(
            request,
            lambda result: async_result.append(result),
        )

        import asyncio
        with timeout(30):
            while not async_result:
                await asyncio.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result

    def _use(
        self,
        request: UseRequest,
        callback: Callable[[AsyncResult[UseResult]], None],
    ):
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service="serialKey",
            component='serialKey',
            function='use',
            request_id=request_id,
        )

        if request.context_stack:
            body['contextStack'] = str(request.context_stack)
        if request.namespace_name is not None:
            body["namespaceName"] = request.namespace_name
        if request.access_token is not None:
            body["accessToken"] = request.access_token
        if request.code is not None:
            body["code"] = request.code

        if request.request_id:
            body["xGs2RequestId"] = request.request_id
        if request.access_token:
            body["xGs2AccessToken"] = request.access_token
        if request.duplication_avoider:
            body["xGs2DuplicationAvoider"] = request.duplication_avoider

        self.session.send(
            web_socket.NetworkJob(
                request_id=request_id,
                result_type=UseResult,
                callback=callback,
                body=body,
            )
        )

    def use(
        self,
        request: UseRequest,
    ) -> UseResult:
        async_result = []
        with timeout(30):
            self._use(
                request,
                lambda result: async_result.append(result),
            )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def use_async(
        self,
        request: UseRequest,
    ) -> UseResult:
        async_result = []
        self._use(
            request,
            lambda result: async_result.append(result),
        )

        import asyncio
        with timeout(30):
            while not async_result:
                await asyncio.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result

    def _use_by_user_id(
        self,
        request: UseByUserIdRequest,
        callback: Callable[[AsyncResult[UseByUserIdResult]], None],
    ):
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service="serialKey",
            component='serialKey',
            function='useByUserId',
            request_id=request_id,
        )

        if request.context_stack:
            body['contextStack'] = str(request.context_stack)
        if request.namespace_name is not None:
            body["namespaceName"] = request.namespace_name
        if request.user_id is not None:
            body["userId"] = request.user_id
        if request.code is not None:
            body["code"] = request.code

        if request.request_id:
            body["xGs2RequestId"] = request.request_id
        if request.duplication_avoider:
            body["xGs2DuplicationAvoider"] = request.duplication_avoider

        self.session.send(
            web_socket.NetworkJob(
                request_id=request_id,
                result_type=UseByUserIdResult,
                callback=callback,
                body=body,
            )
        )

    def use_by_user_id(
        self,
        request: UseByUserIdRequest,
    ) -> UseByUserIdResult:
        async_result = []
        with timeout(30):
            self._use_by_user_id(
                request,
                lambda result: async_result.append(result),
            )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def use_by_user_id_async(
        self,
        request: UseByUserIdRequest,
    ) -> UseByUserIdResult:
        async_result = []
        self._use_by_user_id(
            request,
            lambda result: async_result.append(result),
        )

        import asyncio
        with timeout(30):
            while not async_result:
                await asyncio.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result

    def _use_by_stamp_task(
        self,
        request: UseByStampTaskRequest,
        callback: Callable[[AsyncResult[UseByStampTaskResult]], None],
    ):
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service="serialKey",
            component='serialKey',
            function='useByStampTask',
            request_id=request_id,
        )

        if request.context_stack:
            body['contextStack'] = str(request.context_stack)
        if request.stamp_task is not None:
            body["stampTask"] = request.stamp_task
        if request.key_id is not None:
            body["keyId"] = request.key_id

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            web_socket.NetworkJob(
                request_id=request_id,
                result_type=UseByStampTaskResult,
                callback=callback,
                body=body,
            )
        )

    def use_by_stamp_task(
        self,
        request: UseByStampTaskRequest,
    ) -> UseByStampTaskResult:
        async_result = []
        with timeout(30):
            self._use_by_stamp_task(
                request,
                lambda result: async_result.append(result),
            )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def use_by_stamp_task_async(
        self,
        request: UseByStampTaskRequest,
    ) -> UseByStampTaskResult:
        async_result = []
        self._use_by_stamp_task(
            request,
            lambda result: async_result.append(result),
        )

        import asyncio
        with timeout(30):
            while not async_result:
                await asyncio.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result

    def _describe_campaign_models(
        self,
        request: DescribeCampaignModelsRequest,
        callback: Callable[[AsyncResult[DescribeCampaignModelsResult]], None],
    ):
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service="serialKey",
            component='campaignModel',
            function='describeCampaignModels',
            request_id=request_id,
        )

        if request.context_stack:
            body['contextStack'] = str(request.context_stack)
        if request.namespace_name is not None:
            body["namespaceName"] = request.namespace_name

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            web_socket.NetworkJob(
                request_id=request_id,
                result_type=DescribeCampaignModelsResult,
                callback=callback,
                body=body,
            )
        )

    def describe_campaign_models(
        self,
        request: DescribeCampaignModelsRequest,
    ) -> DescribeCampaignModelsResult:
        async_result = []
        with timeout(30):
            self._describe_campaign_models(
                request,
                lambda result: async_result.append(result),
            )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def describe_campaign_models_async(
        self,
        request: DescribeCampaignModelsRequest,
    ) -> DescribeCampaignModelsResult:
        async_result = []
        self._describe_campaign_models(
            request,
            lambda result: async_result.append(result),
        )

        import asyncio
        with timeout(30):
            while not async_result:
                await asyncio.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result

    def _get_campaign_model(
        self,
        request: GetCampaignModelRequest,
        callback: Callable[[AsyncResult[GetCampaignModelResult]], None],
    ):
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service="serialKey",
            component='campaignModel',
            function='getCampaignModel',
            request_id=request_id,
        )

        if request.context_stack:
            body['contextStack'] = str(request.context_stack)
        if request.namespace_name is not None:
            body["namespaceName"] = request.namespace_name
        if request.campaign_model_name is not None:
            body["campaignModelName"] = request.campaign_model_name

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            web_socket.NetworkJob(
                request_id=request_id,
                result_type=GetCampaignModelResult,
                callback=callback,
                body=body,
            )
        )

    def get_campaign_model(
        self,
        request: GetCampaignModelRequest,
    ) -> GetCampaignModelResult:
        async_result = []
        with timeout(30):
            self._get_campaign_model(
                request,
                lambda result: async_result.append(result),
            )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def get_campaign_model_async(
        self,
        request: GetCampaignModelRequest,
    ) -> GetCampaignModelResult:
        async_result = []
        self._get_campaign_model(
            request,
            lambda result: async_result.append(result),
        )

        import asyncio
        with timeout(30):
            while not async_result:
                await asyncio.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result

    def _describe_campaign_model_masters(
        self,
        request: DescribeCampaignModelMastersRequest,
        callback: Callable[[AsyncResult[DescribeCampaignModelMastersResult]], None],
    ):
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service="serialKey",
            component='campaignModelMaster',
            function='describeCampaignModelMasters',
            request_id=request_id,
        )

        if request.context_stack:
            body['contextStack'] = str(request.context_stack)
        if request.namespace_name is not None:
            body["namespaceName"] = request.namespace_name
        if request.page_token is not None:
            body["pageToken"] = request.page_token
        if request.limit is not None:
            body["limit"] = request.limit

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            web_socket.NetworkJob(
                request_id=request_id,
                result_type=DescribeCampaignModelMastersResult,
                callback=callback,
                body=body,
            )
        )

    def describe_campaign_model_masters(
        self,
        request: DescribeCampaignModelMastersRequest,
    ) -> DescribeCampaignModelMastersResult:
        async_result = []
        with timeout(30):
            self._describe_campaign_model_masters(
                request,
                lambda result: async_result.append(result),
            )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def describe_campaign_model_masters_async(
        self,
        request: DescribeCampaignModelMastersRequest,
    ) -> DescribeCampaignModelMastersResult:
        async_result = []
        self._describe_campaign_model_masters(
            request,
            lambda result: async_result.append(result),
        )

        import asyncio
        with timeout(30):
            while not async_result:
                await asyncio.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result

    def _create_campaign_model_master(
        self,
        request: CreateCampaignModelMasterRequest,
        callback: Callable[[AsyncResult[CreateCampaignModelMasterResult]], None],
    ):
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service="serialKey",
            component='campaignModelMaster',
            function='createCampaignModelMaster',
            request_id=request_id,
        )

        if request.context_stack:
            body['contextStack'] = str(request.context_stack)
        if request.namespace_name is not None:
            body["namespaceName"] = request.namespace_name
        if request.name is not None:
            body["name"] = request.name
        if request.description is not None:
            body["description"] = request.description
        if request.metadata is not None:
            body["metadata"] = request.metadata
        if request.enable_campaign_code is not None:
            body["enableCampaignCode"] = request.enable_campaign_code

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            web_socket.NetworkJob(
                request_id=request_id,
                result_type=CreateCampaignModelMasterResult,
                callback=callback,
                body=body,
            )
        )

    def create_campaign_model_master(
        self,
        request: CreateCampaignModelMasterRequest,
    ) -> CreateCampaignModelMasterResult:
        async_result = []
        with timeout(30):
            self._create_campaign_model_master(
                request,
                lambda result: async_result.append(result),
            )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def create_campaign_model_master_async(
        self,
        request: CreateCampaignModelMasterRequest,
    ) -> CreateCampaignModelMasterResult:
        async_result = []
        self._create_campaign_model_master(
            request,
            lambda result: async_result.append(result),
        )

        import asyncio
        with timeout(30):
            while not async_result:
                await asyncio.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result

    def _get_campaign_model_master(
        self,
        request: GetCampaignModelMasterRequest,
        callback: Callable[[AsyncResult[GetCampaignModelMasterResult]], None],
    ):
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service="serialKey",
            component='campaignModelMaster',
            function='getCampaignModelMaster',
            request_id=request_id,
        )

        if request.context_stack:
            body['contextStack'] = str(request.context_stack)
        if request.namespace_name is not None:
            body["namespaceName"] = request.namespace_name
        if request.campaign_model_name is not None:
            body["campaignModelName"] = request.campaign_model_name

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            web_socket.NetworkJob(
                request_id=request_id,
                result_type=GetCampaignModelMasterResult,
                callback=callback,
                body=body,
            )
        )

    def get_campaign_model_master(
        self,
        request: GetCampaignModelMasterRequest,
    ) -> GetCampaignModelMasterResult:
        async_result = []
        with timeout(30):
            self._get_campaign_model_master(
                request,
                lambda result: async_result.append(result),
            )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def get_campaign_model_master_async(
        self,
        request: GetCampaignModelMasterRequest,
    ) -> GetCampaignModelMasterResult:
        async_result = []
        self._get_campaign_model_master(
            request,
            lambda result: async_result.append(result),
        )

        import asyncio
        with timeout(30):
            while not async_result:
                await asyncio.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result

    def _update_campaign_model_master(
        self,
        request: UpdateCampaignModelMasterRequest,
        callback: Callable[[AsyncResult[UpdateCampaignModelMasterResult]], None],
    ):
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service="serialKey",
            component='campaignModelMaster',
            function='updateCampaignModelMaster',
            request_id=request_id,
        )

        if request.context_stack:
            body['contextStack'] = str(request.context_stack)
        if request.namespace_name is not None:
            body["namespaceName"] = request.namespace_name
        if request.campaign_model_name is not None:
            body["campaignModelName"] = request.campaign_model_name
        if request.description is not None:
            body["description"] = request.description
        if request.metadata is not None:
            body["metadata"] = request.metadata
        if request.enable_campaign_code is not None:
            body["enableCampaignCode"] = request.enable_campaign_code

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            web_socket.NetworkJob(
                request_id=request_id,
                result_type=UpdateCampaignModelMasterResult,
                callback=callback,
                body=body,
            )
        )

    def update_campaign_model_master(
        self,
        request: UpdateCampaignModelMasterRequest,
    ) -> UpdateCampaignModelMasterResult:
        async_result = []
        with timeout(30):
            self._update_campaign_model_master(
                request,
                lambda result: async_result.append(result),
            )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def update_campaign_model_master_async(
        self,
        request: UpdateCampaignModelMasterRequest,
    ) -> UpdateCampaignModelMasterResult:
        async_result = []
        self._update_campaign_model_master(
            request,
            lambda result: async_result.append(result),
        )

        import asyncio
        with timeout(30):
            while not async_result:
                await asyncio.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result

    def _delete_campaign_model_master(
        self,
        request: DeleteCampaignModelMasterRequest,
        callback: Callable[[AsyncResult[DeleteCampaignModelMasterResult]], None],
    ):
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service="serialKey",
            component='campaignModelMaster',
            function='deleteCampaignModelMaster',
            request_id=request_id,
        )

        if request.context_stack:
            body['contextStack'] = str(request.context_stack)
        if request.namespace_name is not None:
            body["namespaceName"] = request.namespace_name
        if request.campaign_model_name is not None:
            body["campaignModelName"] = request.campaign_model_name

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            web_socket.NetworkJob(
                request_id=request_id,
                result_type=DeleteCampaignModelMasterResult,
                callback=callback,
                body=body,
            )
        )

    def delete_campaign_model_master(
        self,
        request: DeleteCampaignModelMasterRequest,
    ) -> DeleteCampaignModelMasterResult:
        async_result = []
        with timeout(30):
            self._delete_campaign_model_master(
                request,
                lambda result: async_result.append(result),
            )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def delete_campaign_model_master_async(
        self,
        request: DeleteCampaignModelMasterRequest,
    ) -> DeleteCampaignModelMasterResult:
        async_result = []
        self._delete_campaign_model_master(
            request,
            lambda result: async_result.append(result),
        )

        import asyncio
        with timeout(30):
            while not async_result:
                await asyncio.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result

    def _export_master(
        self,
        request: ExportMasterRequest,
        callback: Callable[[AsyncResult[ExportMasterResult]], None],
    ):
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service="serialKey",
            component='currentCampaignMaster',
            function='exportMaster',
            request_id=request_id,
        )

        if request.context_stack:
            body['contextStack'] = str(request.context_stack)
        if request.namespace_name is not None:
            body["namespaceName"] = request.namespace_name

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            web_socket.NetworkJob(
                request_id=request_id,
                result_type=ExportMasterResult,
                callback=callback,
                body=body,
            )
        )

    def export_master(
        self,
        request: ExportMasterRequest,
    ) -> ExportMasterResult:
        async_result = []
        with timeout(30):
            self._export_master(
                request,
                lambda result: async_result.append(result),
            )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def export_master_async(
        self,
        request: ExportMasterRequest,
    ) -> ExportMasterResult:
        async_result = []
        self._export_master(
            request,
            lambda result: async_result.append(result),
        )

        import asyncio
        with timeout(30):
            while not async_result:
                await asyncio.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result

    def _get_current_campaign_master(
        self,
        request: GetCurrentCampaignMasterRequest,
        callback: Callable[[AsyncResult[GetCurrentCampaignMasterResult]], None],
    ):
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service="serialKey",
            component='currentCampaignMaster',
            function='getCurrentCampaignMaster',
            request_id=request_id,
        )

        if request.context_stack:
            body['contextStack'] = str(request.context_stack)
        if request.namespace_name is not None:
            body["namespaceName"] = request.namespace_name

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            web_socket.NetworkJob(
                request_id=request_id,
                result_type=GetCurrentCampaignMasterResult,
                callback=callback,
                body=body,
            )
        )

    def get_current_campaign_master(
        self,
        request: GetCurrentCampaignMasterRequest,
    ) -> GetCurrentCampaignMasterResult:
        async_result = []
        with timeout(30):
            self._get_current_campaign_master(
                request,
                lambda result: async_result.append(result),
            )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def get_current_campaign_master_async(
        self,
        request: GetCurrentCampaignMasterRequest,
    ) -> GetCurrentCampaignMasterResult:
        async_result = []
        self._get_current_campaign_master(
            request,
            lambda result: async_result.append(result),
        )

        import asyncio
        with timeout(30):
            while not async_result:
                await asyncio.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result

    def _update_current_campaign_master(
        self,
        request: UpdateCurrentCampaignMasterRequest,
        callback: Callable[[AsyncResult[UpdateCurrentCampaignMasterResult]], None],
    ):
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service="serialKey",
            component='currentCampaignMaster',
            function='updateCurrentCampaignMaster',
            request_id=request_id,
        )

        if request.context_stack:
            body['contextStack'] = str(request.context_stack)
        if request.namespace_name is not None:
            body["namespaceName"] = request.namespace_name
        if request.settings is not None:
            body["settings"] = request.settings

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            web_socket.NetworkJob(
                request_id=request_id,
                result_type=UpdateCurrentCampaignMasterResult,
                callback=callback,
                body=body,
            )
        )

    def update_current_campaign_master(
        self,
        request: UpdateCurrentCampaignMasterRequest,
    ) -> UpdateCurrentCampaignMasterResult:
        async_result = []
        with timeout(30):
            self._update_current_campaign_master(
                request,
                lambda result: async_result.append(result),
            )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def update_current_campaign_master_async(
        self,
        request: UpdateCurrentCampaignMasterRequest,
    ) -> UpdateCurrentCampaignMasterResult:
        async_result = []
        self._update_current_campaign_master(
            request,
            lambda result: async_result.append(result),
        )

        import asyncio
        with timeout(30):
            while not async_result:
                await asyncio.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result

    def _update_current_campaign_master_from_git_hub(
        self,
        request: UpdateCurrentCampaignMasterFromGitHubRequest,
        callback: Callable[[AsyncResult[UpdateCurrentCampaignMasterFromGitHubResult]], None],
    ):
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service="serialKey",
            component='currentCampaignMaster',
            function='updateCurrentCampaignMasterFromGitHub',
            request_id=request_id,
        )

        if request.context_stack:
            body['contextStack'] = str(request.context_stack)
        if request.namespace_name is not None:
            body["namespaceName"] = request.namespace_name
        if request.checkout_setting is not None:
            body["checkoutSetting"] = request.checkout_setting.to_dict()

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            web_socket.NetworkJob(
                request_id=request_id,
                result_type=UpdateCurrentCampaignMasterFromGitHubResult,
                callback=callback,
                body=body,
            )
        )

    def update_current_campaign_master_from_git_hub(
        self,
        request: UpdateCurrentCampaignMasterFromGitHubRequest,
    ) -> UpdateCurrentCampaignMasterFromGitHubResult:
        async_result = []
        with timeout(30):
            self._update_current_campaign_master_from_git_hub(
                request,
                lambda result: async_result.append(result),
            )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def update_current_campaign_master_from_git_hub_async(
        self,
        request: UpdateCurrentCampaignMasterFromGitHubRequest,
    ) -> UpdateCurrentCampaignMasterFromGitHubResult:
        async_result = []
        self._update_current_campaign_master_from_git_hub(
            request,
            lambda result: async_result.append(result),
        )

        import asyncio
        with timeout(30):
            while not async_result:
                await asyncio.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result