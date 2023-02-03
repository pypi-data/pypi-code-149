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
"""Functions to convert Stem block quantized layers to Akida.
Those layers are:
    - The Embedding layer
    - The Reshape layer
    - The ClassToken (+ the DistToken for distilled models) layer(s)
    - The AddPosEmbedding layer
"""
from akida import LayerType, Stem
import quantizeml.layers as qlayers
import numpy as np

from .weights import broadcast_and_set_variables


def stem_layers(model_k):
    """Returns the Stem layers of a quantized transformer model.
    For now the Stem is composed only of the Embedding QuantizedConv2D
    and QuantizedReshape.

    Args:
        model_k (:obj:`keras.Model`): the quantized transformer model.

    Return:
        list: the stem block layers.
    """
    stem_block = []

    # The stem of a transfomer model starts with a QuantizedConv2D layer
    # (i.e layer just after the InputLayer layer), followed by an optionnal
    # QuantizedReshape
    if isinstance(model_k.layers[1], qlayers.QuantizedConv2D):
        layer = model_k.layers[1]
        assert layer.kernel_size == layer.strides
        assert layer.padding == 'valid'
        stem_block.append(layer)
        # add the QuantizedReshape layer to the stem if available
        if len(model_k.layers) > 2 and isinstance(model_k.layers[2],
                                                  qlayers.QuantizedReshape):
            stem_block.append(model_k.layers[2])

    # Extract the QuantizedClassToken and QuantizedAddPositionEmbs layers
    nb_class_tokens = 0
    first_class_token_layer = None
    last_class_token_layer = None
    for idx, layer in enumerate(model_k.layers):
        if isinstance(layer, qlayers.QuantizedClassToken):
            if first_class_token_layer is None:
                first_class_token_layer = idx
            last_class_token_layer = idx
            stem_block.append(layer)
            nb_class_tokens += 1
        elif isinstance(layer, qlayers.QuantizedAddPositionEmbs):
            stem_block.append(layer)

    # the QuantizedClassToken layers should be in a row
    if nb_class_tokens > 0:
        if any(not isinstance(layer, qlayers.QuantizedClassToken) for layer in
               model_k.layers[first_class_token_layer:last_class_token_layer +
                              1]):
            raise TypeError(
                "The QuantizedClassToken layers of the Stem must be in a row.")

    return stem_block


def _set_stem_variables(ak_layer, stem_layers):
    """Computes and sets the variables for an Akida Stem layer.

    This function converts the variables of a Keras layers and sets them into
    the corresponding variables of the equivalent Akida layer.

    Args:
        ak_layer (:obj:`akida.Layer`): the targeted akida layer.
        stem_layers (list): list of the source quantized layers.
    """
    assert ak_layer.parameters.layer_type == LayerType.Stem

    # Note for now only the Embedding layer conversion is handled
    # the Embedding (i.e the QuantizedConv2D layer) should be the
    # first layer of the Stem
    embedding_layer = stem_layers[0]

    cls_layers = []
    add_pos_emb_layer = None
    # Get the QuantizedClassToken layer(s) and the optional
    # QuantizedAddPositionEmbs layer
    for layer in stem_layers:
        if isinstance(layer, qlayers.QuantizedClassToken):
            cls_layers.append(layer)
        elif isinstance(layer, qlayers.QuantizedAddPositionEmbs):
            add_pos_emb_layer = layer

    # Prepare a dict for akida variables
    variables_ak = {}

    # get the Embedding weights
    weights_ak = embedding_layer.weight_quantizer.qweights.value.fp.values.numpy()

    # get the Embedding bias
    bias_quantizer = embedding_layer.bias_quantizer
    bias = bias_quantizer.qweights.value.values.numpy().astype(np.int32)
    bias_shift = bias_quantizer.shift.value.numpy().astype(np.uint8)
    bias_ak = bias >> bias_shift

    if len(cls_layers) > 0:
        tokens_ak = []
        shifts_tokens_ak = []
        for cls_layer in cls_layers:
            # get the ClassToken layer token variable (aka cls member)
            cls_quantizer = cls_layer.cls_quantizer
            token = cls_quantizer.qweights.value.values.numpy().astype(np.int32)
            token_shift = cls_quantizer.shift.value.numpy().astype(np.uint8)
            token_ak = token >> token_shift
            # Insert the token value at the first position. This allows us to match
            # the model concatenation order.
            tokens_ak.insert(0, np.squeeze(token_ak))
            shifts_tokens_ak.insert(0, token_shift)
        variables_ak["tokens"] = np.stack(tokens_ak)
        variables_ak["tokens_shift"] = np.concatenate(shifts_tokens_ak)

    if add_pos_emb_layer:
        # get the positional embedding matrix
        pos_emb_quantizer = add_pos_emb_layer.pe_quantizer
        pos_emb = pos_emb_quantizer.qweights.value.values.numpy().astype(np.int32)
        pos_emb_shift = pos_emb_quantizer.shift.value.numpy().astype(np.uint8)
        pos_emb_ak = pos_emb >> pos_emb_shift
        variables_ak["pos_embedding"] = pos_emb_ak
        # Get the QuantizedAddPositionEmbs layer shifts
        variables_ak["pos_embs_shift"] = pos_emb_shift

    variables_ak["weights"] = weights_ak.astype(np.int8)
    variables_ak["bias"] = bias_ak.astype(np.int32)
    # Get the Embedding layer shifts
    variables_ak["bias_shift"] = bias_shift.astype(np.uint8)

    # The output quantizer corresponds to the output quantizer of the last layer of the stem
    out_quantizer = getattr(stem_layers[-1], "out_quantizer", False)
    if out_quantizer:
        assert isinstance(out_quantizer, qlayers.OutputQuantizer)
        qscales = out_quantizer.qscales
        variables_ak["output_scales"] = qscales.value.values.numpy().astype(
            np.uint8)
        variables_ak["output_shift"] = out_quantizer.shift.value.numpy(
        ).astype(np.int8)

    broadcast_and_set_variables(ak_layer, variables_ak)


def _create_stem(input_shape, layers):
    """Parses the quantizeml quantized layers of the Stem block and returns the
    params to create the corresponding Akida Stem layer.

    Args:
        input_shape (tuple): the input shape of the Stem.
        layers (list): the quantizeml quantized layers of the Stem to convert.
    """
    # Note: for now only the Embedding layer conversion is handled
    embedding_layer = layers[0]

    cls_layers = []
    add_pos_emb_layer = None
    # Get the QuantizedClassToken layer(s) and the optional
    # QuantizedAddPositionEmbs layer
    for layer in layers:
        if isinstance(layer, qlayers.QuantizedClassToken):
            cls_layers.append(layer)
        elif isinstance(layer, qlayers.QuantizedAddPositionEmbs):
            add_pos_emb_layer = layer

    # Find out if there is a quantizer
    out_quantizer = getattr(layers[-1], "out_quantizer", False)
    # In quantizeml one reserves automaticaly one bit for the sign, but in akida
    # this is rather checked during the clipping operations.
    buffer_bits = embedding_layer.buffer_bitwidth + 1
    if out_quantizer:
        output_bits = out_quantizer.bitwidth
    else:
        # Default to buffer bitwidth
        output_bits = buffer_bits

    collapse_spatial_dims = len(layers) > 1 and isinstance(
        layers[1], qlayers.QuantizedReshape)

    num_non_patch_tokens = len(cls_layers)

    # Default tokens_bits at 10
    tokens_bits = 10
    # All the ClassToken layers should normally have the same cls_bitwidth
    if num_non_patch_tokens > 0:
        tokens_bits = cls_layers[0].cls_quantizer.bitwidth

    # Handle optional AddPositionEmbedding params
    add_pos_embs_available = False
    pos_embedding_bits = 8
    if add_pos_emb_layer:
        add_pos_embs_available = True
        pos_embedding_bits = add_pos_emb_layer.pe_quantizer.bitwidth

    return Stem(input_shape=input_shape,
                filters=embedding_layer.filters,
                kernel_size=embedding_layer.kernel_size[0],
                weights_bits=embedding_layer.weight_quantizer.bitwidth,
                bias_bits=embedding_layer.bias_quantizer.bitwidth,
                tokens_bits=tokens_bits,
                pos_embedding_bits=pos_embedding_bits,
                output_bits=output_bits,
                buffer_bits=buffer_bits,
                collapse_spatial_dims=collapse_spatial_dims,
                num_non_patch_tokens=num_non_patch_tokens,
                add_pos_embs_available=add_pos_embs_available,
                name="Stem")


def convert_quantized_stem_layers(model_ak, input_shape, layers_k):
    """Converts QuantizedDense layer and its variables and adds it to the
    Akida's model.

    Args:
        model_ak (:obj:`akida.Model`): the Akida model where the model will be added.
        input_shape (tuple): the input shape of the Stem.
        layers_k (list): the quantizeml quantized layers of the Stem to convert.
    """
    # Note: for now only the Embedding layer conversion is handled
    embedding_layer = layers_k[0]
    if not isinstance(embedding_layer, qlayers.QuantizedConv2D):
        raise TypeError(f"Layer {embedding_layer.name} was expected to be "
                        "QuantizedConv2D")

    layer_ak = _create_stem(input_shape, layers_k)
    model_ak.add(layer_ak)
    _set_stem_variables(layer_ak, layers_k)
