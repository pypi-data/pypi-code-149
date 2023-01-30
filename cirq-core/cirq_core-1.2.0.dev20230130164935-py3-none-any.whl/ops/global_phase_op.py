# Copyright 2019 The Cirq Developers
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""A no-qubit global phase operation."""

from typing import AbstractSet, Any, cast, Dict, Sequence, Tuple, Union

import numpy as np
import sympy

import cirq
from cirq import value, protocols
from cirq.ops import raw_types
from cirq.type_workarounds import NotImplementedType


@value.value_equality(approximate=True)
class GlobalPhaseGate(raw_types.Gate):
    def __init__(self, coefficient: 'cirq.TParamValComplex', atol: float = 1e-8) -> None:
        if not isinstance(coefficient, sympy.Basic):
            if abs(1 - abs(coefficient)) > atol:  # type: ignore[operator]
                raise ValueError(f'Coefficient is not unitary: {coefficient!r}')
        self._coefficient = coefficient

    @property
    def coefficient(self) -> 'cirq.TParamValComplex':
        return self._coefficient

    def _value_equality_values_(self) -> Any:
        return self.coefficient

    def _has_unitary_(self) -> bool:
        return not self._is_parameterized_()

    def __pow__(self, power) -> 'cirq.GlobalPhaseGate':
        if isinstance(power, (int, float)):
            return GlobalPhaseGate(self.coefficient**power)
        return NotImplemented

    def _unitary_(self) -> Union[np.ndarray, NotImplementedType]:
        if not self._has_unitary_():
            return NotImplemented
        return np.array([[self.coefficient]])

    def _apply_unitary_(
        self, args: 'cirq.ApplyUnitaryArgs'
    ) -> Union[np.ndarray, NotImplementedType]:
        if not self._has_unitary_():
            return NotImplemented
        assert not cirq.is_parameterized(self)
        args.target_tensor *= cast(np.generic, self.coefficient)
        return args.target_tensor

    def _has_stabilizer_effect_(self) -> bool:
        return True

    def __str__(self) -> str:
        return str(self.coefficient)

    def __repr__(self) -> str:
        return f'cirq.GlobalPhaseGate({self.coefficient!r})'

    def _op_repr_(self, qubits: Sequence['cirq.Qid']) -> str:
        return f'cirq.global_phase_operation({self.coefficient!r})'

    def _json_dict_(self) -> Dict[str, Any]:
        return protocols.obj_to_dict_helper(self, ['coefficient'])

    def _qid_shape_(self) -> Tuple[int, ...]:
        return tuple()

    def _is_parameterized_(self) -> bool:
        return protocols.is_parameterized(self.coefficient)

    def _parameter_names_(self) -> AbstractSet[str]:
        return protocols.parameter_names(self.coefficient)

    def _resolve_parameters_(
        self, resolver: 'cirq.ParamResolver', recursive: bool
    ) -> 'cirq.GlobalPhaseGate':
        coefficient = protocols.resolve_parameters(self.coefficient, resolver, recursive)
        return GlobalPhaseGate(coefficient=coefficient)


def global_phase_operation(
    coefficient: 'cirq.TParamValComplex', atol: float = 1e-8
) -> 'cirq.GateOperation':
    """Creates an operation that represents a global phase on the state."""
    return GlobalPhaseGate(coefficient, atol)()
