#!/usr/bin/env python
# ******************************************************************************
# Copyright 2022 Brainchip Holdings Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ******************************************************************************
"""Functions to convert QuantizedDense to Akida.
"""
from akida import LayerType, Dense2D
import quantizeml.layers as qlayers
import numpy as np

from .weights import broadcast_and_set_variable


def _set_dense2d_variables(ak_layer, k_layer):
    """Computes and sets the variables for an Akida Dense2D layer.

    This function converts the variables of a Keras layer and sets them into
    the corresponding variables of the equivalent Akida layer.

    Args:
        layer_ak (:obj:`akida.Layer`): the targeted akida layer.
        k_layer (:obj:`tf.keras.Layer`): the source quantized layer.
    """
    assert isinstance(k_layer, qlayers.QuantizedDense)
    assert ak_layer.parameters.layer_type == LayerType.Dense2D
    assert isinstance(k_layer.weight_quantizer, qlayers.WeightQuantizer)
    assert isinstance(k_layer.bias_quantizer, qlayers.AlignedWeightQuantizer)

    # get the QuantizedDense weights
    weights_ak = k_layer.weight_quantizer.qweights.value.fp.values.numpy()
    # get the QuantizedDense bias and shift
    bias_quantizer = k_layer.bias_quantizer
    bias = bias_quantizer.qweights.value.values.numpy().astype(np.int32)
    bias_shift = bias_quantizer.shift.value.numpy().astype(np.uint8)
    bias_ak = bias >> bias_shift

    variables_ak = ak_layer.variables

    input_shift = k_layer.input_shift.value
    if input_shift is not None:
        broadcast_and_set_variable(variables_ak, "input_shift",
                                   input_shift.numpy().astype(np.uint8))
    variables_ak["weights"] = weights_ak.astype(np.int8)
    variables_ak["bias"] = bias_ak
    variables_ak["bias_shift"] = bias_shift
    out_quantizer = getattr(k_layer, "out_quantizer", False)
    if out_quantizer:
        assert isinstance(out_quantizer, qlayers.OutputQuantizer)
        qscales = out_quantizer.qscales
        variables_ak["output_scales"] = qscales.value.values.numpy().astype(
            np.uint8)
        variables_ak["output_shift"] = out_quantizer.shift.value.numpy(
        ).astype(np.int8)


def _create_dense2d(layer):
    """Parses a quantizeml QuantizedDense layer and returns the params to
    create the corresponding Akida Dense2D layer.

    Args:
        layer (:obj:`tf.keras.Layer`): the quantizeml QuantizedDense layer to
            convert.
        params (dict): will contain the parameters of the future Akida Dense2D
            layer.

    """
    assert isinstance(layer, qlayers.QuantizedDense)
    weight_bits = layer.weight_quantizer.bitwidth
    # The only weight bitwidth supported is 4
    assert weight_bits == 4
    # Find out if there is a quantizer
    out_quantizer = getattr(layer, "out_quantizer", False)
    # In quantizeml one bit is reserved for the sign in the buffer bitwidth
    # variable, but in akida this value has to be added back to have the
    # correct clipping.
    buffer_bits = layer.buffer_bitwidth + 1
    if out_quantizer:
        output_bits = out_quantizer.bitwidth
    else:
        # Default to buffer bitwidth
        output_bits = buffer_bits

    return Dense2D(units=layer.units,
                   output_bits=output_bits,
                   buffer_bits=buffer_bits,
                   name=layer.name)


def convert_quantized_dense(model_ak, layer_k):
    """Converts QuantizedDense layer and its variables and adds it to the
    Akida's model.

    Args:
        layer (:obj:`tf.keras.Layer`): the quantizeml QuantizedDense layer to
            convert.
        :obj:`akida.Model`: the Akida model where the model will be added.
    """
    if not isinstance(layer_k, qlayers.QuantizedDense):
        raise TypeError(f"Layer {layer_k.name} was expected to be "
                        "QuantizedDense")
    layer_ak = _create_dense2d(layer_k)
    model_ak.add(layer_ak)
    _set_dense2d_variables(layer_ak, layer_k)
