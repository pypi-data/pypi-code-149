import math

import jax
import numpy as np
from flax import linen as nn
from jax import numpy as jnp


class PositionalEncoding(nn.Module):
    embed_dim: int = 512
    max_seq_len: int = 5000

    def setup(self) -> None:
        position = np.arange(self.max_seq_len)[:, np.newaxis]  # [max_seq_len, 1]
        div_term = np.exp(
            np.arange(0, self.embed_dim, 2) * -(math.log(10000.0) / self.embed_dim)
        )  # [embed_dim/2]
        positional_encoding = np.zeros(
            (self.max_seq_len, self.embed_dim)
        )  # [max_seq_len, embed_dim]
        positional_encoding[:, 0::2] = np.sin(position * div_term)
        positional_encoding[:, 1::2] = np.cos(position * div_term)
        positional_encoding = positional_encoding[
            np.newaxis, :, :
        ]  # [1, max_seq_len, embed_dim]
        self.positional_encoding = jax.device_put(positional_encoding)

    @nn.compact
    def __call__(self, x: jax.Array) -> jax.Array:
        assert x.ndim == 3, "x must be of shape [batch_size, seq_len, embed_dim]"
        assert x.dtype in [
            jnp.float16,
            jnp.float32,
            jnp.float64,
        ], "x must be of dtype float (float16, float32, float64)"
        assert x.shape[1] <= self.max_seq_len, "seq_len must be <= max_seq_len"
        return x + self.positional_encoding[:, : x.shape[1], :]
