# Copyright 2023 Google LLC.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import annotations

"""Utilities for handling GRPC API."""

from typing import Optional
import grpc
from vizier.service import custom_errors


# TODO: Create a type Union[_InactiveRpcError, LocalRpcError]
class LocalRpcError(grpc.RpcError):
  """Class for imitating both a `grpc.ServiceContext` and a `grpc.RpcError`."""

  _code: grpc.StatusCode = grpc.StatusCode.UNKNOWN
  _details: Optional[str] = None

  def set_code(self, code: grpc.StatusCode) -> None:
    self._code = code

  def set_details(self, details: str) -> None:
    self._details = details

  def code(self) -> grpc.StatusCode:
    return self._code

  def details(self) -> Optional[str]:
    return self._details


# TODO: Use this for all service errors.
def handle_exception(
    e: Exception, context: Optional[grpc.ServicerContext] = None
) -> None:
  """Converts custom exception into correct context error code.

  The rules for gRPC are:

  1) In the remote case (servicer wrapped into a server), the context is
  automatically generated by gRPC. Calling `context.set_code()` will
  automatically trigger an ` _InactiveRpcError` on the client side, which can
  collect the code and details from said RPC error.

  2) In the local case (e.g. when using a `VizierServicer` only), contexts are
  not used and set to None. In order to imitate the behavior of 1), we will
  instead use `LocalRpcError` to imitate both the behavior of a
  `ServicerContext` for setting codes and details, AND as an `_InactiveRpcError`
  to be raised on the client side.

  Args:
    e: Exception to be wrapped.
    context: For collecting error code and details. Set to None in the local
      case.

  Raises:
    LocalRpcError: If in the local case (when context is None).
  """
  if context is None:
    context = LocalRpcError(e)

  if isinstance(
      e, (custom_errors.ImmutableStudyError, custom_errors.ImmutableTrialError)
  ):
    context.set_code(grpc.StatusCode.FAILED_PRECONDITION)
  elif isinstance(e, custom_errors.NotFoundError):
    context.set_code(grpc.StatusCode.NOT_FOUND)
  elif isinstance(e, custom_errors.AlreadyExistsError):
    context.set_code(grpc.StatusCode.ALREADY_EXISTS)
  else:
    context.set_code(grpc.StatusCode.UNKNOWN)

  context.set_details(str(e))

  if isinstance(context, LocalRpcError):
    raise context
