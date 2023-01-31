import numpy as np
from autoai_ts_libs.deps.srom.time_series.augmentor._base import BaseAugmentor


def _add_noise(x, distr, seed, loc, scale, kind, normalize):
    """ """
    N, T = x.shape
    rand = np.random.RandomState(seed)
    if distr == "gaussian":
        gen_noise = lambda size: rand.normal(0.0, 1.0, size=size)
    elif distr == "laplace":
        gen_noise = lambda size: rand.laplace(0.0, 1.0, size=size)
    else:
        gen_noise = lambda size: rand.uniform(low=-(3**0.5), high=3**0.5, size=size)

    if isinstance(loc, (float, int)):
        loc = np.ones(N) * loc
    elif isinstance(loc, tuple):
        loc = rand.uniform(low=loc[0], high=loc[1], size=N)
    else:
        loc = rand.choice(loc, size=N)

    if isinstance(scale, (float, int)):
        scale = np.ones(N) * scale
    elif isinstance(scale, tuple):
        scale = rand.uniform(low=scale[0], high=scale[1], size=N)
    else:
        scale = rand.choice(scale, size=N)

    noise = gen_noise((N, T))

    noise = noise * scale.reshape(
        (
            N,
            1,
        )
    ) + loc.reshape((N, 1))

    if kind == "additive":
        if normalize:
            x_aug = x + noise * (
                x.max(axis=0, keepdims=True) - x.min(axis=0, keepdims=True)
            )
        else:
            x_aug = x + noise
    else:
        x_aug = x * (1.0 + noise)

    return x_aug


def _augment_noise(x, distr, loc, scale, kind, normalize, seed, repeats, prob):
    """ """
    x = x.reshape(-1, 1)
    rand = np.random.RandomState(seed)
    N = x.shape[0]
    ind = rand.uniform(size=repeats * N) <= prob

    if repeats > 1:
        x_aug = np.repeat(x.copy(), repeats, axis=0)
    else:
        x_aug = x.copy()
    if ind.any():
        x_aug[ind, :] = _add_noise(
            x_aug[ind, :], distr, seed, loc, scale, kind, normalize
        )
    x_aug = x_aug.reshape(-1)
    return x_aug


class Noise(BaseAugmentor):
    """Class for Noise augmentor"""

    def __init__(
        self,
        feature_columns=[0],
        target_columns=[0],
        loc=0.0,
        scale=0.1,
        distr="gaussian",
        kind="additive",
        normalize=True,
        repeats=1,
        prob=1.0,
        seed=1,
    ):
        self.feature_columns = feature_columns
        self.target_columns = target_columns
        self.loc = loc
        self.scale = scale
        self.distr = distr
        self.kind = kind
        self.normalize = normalize
        self.repeats = repeats
        self.prob = prob
        self.seed = seed
        super().__init__()

    def transform(self, X):
        """ """
        clm_index = list(set(self.feature_columns + self.target_columns))
        X = X.copy()
        X[:, clm_index] = np.apply_along_axis(
            _augment_noise,
            0,
            X[:, clm_index],
            self.distr,
            self.loc,
            self.scale,
            self.kind,
            self.normalize,
            self.seed,
            self.repeats,
            self.prob,
        )
        return X
