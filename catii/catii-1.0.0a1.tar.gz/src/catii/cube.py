import numpy

from .set_operations import set_intersect_merge_np


class ccube:
    """An N-dimensional contingency cube.

    This object defines a list of `dims`: iindex variables being crosstabbed.
    It also defines the .shape of the working and output arrays, and some
    slice objects to help navigate them.

    The ccube itself does not own the output; instead, use ffunc objects
    (or the shortcut methods on the ccube, like `count`) to calculate the
    aggregate data in a ccube. Multiple ffuncs may apply to a single ccube.

    A single ccube only represents a single "table"; that is, the input dims
    must all be 1-dimensional, and all interact to form the output. To work
    with more dimensions, iterate over the Cartesian product of the higher
    dimensions, take 1-D slices of each iindex, form a ccube for each,
    and stack them. It can save time to initialize "one big region" for each
    ffunc, representing the stacked output, then, after filling each subcube,
    do a single reduce operation on the stacked cube to perform all of the
    marginal differencing in one pass. To that end, this ccube object has
    an optional `container_shape` to declare those higher dimensions.
    """

    def __init__(self, dims, shape=None, container_shape=None):
        self.dims = dims
        if shape is None:
            shape = tuple(max(coords[0] for coords in d) + 1 for d in dims)
        self.shape = shape
        self._working_shape = tuple(s + 1 for s in shape)

        self.container = tuple(slice(None) for s in container_shape or ())
        self.corner = self.container + tuple(-1 for d in dims)
        self.marginless = self.container + tuple(slice(0, -1) for dim in self.dims)

        self.intersection_data_points = 0

    # ------------------------------- stacking ------------------------------- #

    @property
    def product(self):
        """Cartesian product of coordinate dimensions.

        This returns an iterable: each element yielded from it is a "subcube",
        a set of 1-D slices from each dimension. For example, if our dimensions
        are a 2-D iindex 'A' with 3 columns, then 1-D iindexes 'B' and 'C',
        then this would return:
            (
                (A.sliced(0), B, C),
                (A.sliced(1), B, C),
                (A.sliced(2), B, C)
            )

        We can then calculate an aggregate "region" for each subcube and fill it.
        Multiple multidimensional iindexes multiply the number of subcubes.
        Indexes with more than one higher dimension similarly multiply
        the number of subcubes, like `A.sliced(0, 0), A.sliced(1, 0), ...`.
        We always shuffle these stacking dimensions to be outermost loops;
        you may transpose the output afterward to match the desired order
        of dimensions.
        """
        return itertools.product(
            *[
                ({"coords": c, "data": s} for c, s in dim.slices1d())
                for dim in self.dims
            ]
        )

    # ----------------------------- interacting ----------------------------- #

    def _walk(self, dims, base_coords, base_set, func):
        # This method could be made smaller by moving the `if's` inside
        # the loops, but that actually becomes a performance issue when
        # you're looping over tens of thousands of subvariables.
        # Exploded like this can reduce completion time by 10%.
        remaining_dims = dims[1:]
        if remaining_dims:
            if base_set is None:
                # First dim, or the case where all higher dims have passed
                # ((-1,), None) to mean "ignore this dim".
                for coords, rowids in dims[0].items():
                    self._walk(remaining_dims, base_coords + coords, rowids, func)
            else:
                for coords, rowids in dims[0].items():
                    self.intersection_data_points += len(base_set) + len(rowids)
                    rowids = set_intersect_merge_np(base_set, rowids)
                    if rowids.shape[0]:
                        self._walk(remaining_dims, base_coords + coords, rowids, func)

            # Margin
            self._walk(remaining_dims, base_coords + (-1,), base_set, func)
        else:
            # Last dim. The `rowids` in each loop below are the rowids
            # that appear in all dims for this particular tuple of new_coords.
            # Any coordinate which is -1 targets the margin for that axis.
            if base_set is None:
                for coords, rowids in dims[0].items():
                    if rowids.shape[0]:
                        func(base_coords + coords, rowids)
            else:
                for coords, rowids in dims[0].items():
                    self.intersection_data_points += len(base_set) + len(rowids)
                    rowids = set_intersect_merge_np(base_set, rowids)
                    if rowids.shape[0]:
                        func(base_coords + coords, rowids)

                # Margin
                if base_set.shape[0]:
                    func(base_coords + (-1,), base_set)

    def walk(self, func):
        """Call func(interaction-of-coords, intersection-of-rowids) over self.dims.

        This recursively iterates over each dim in self, combining coordinates
        from each along the way. For each distinct combination, we find the
        set of rowids which contain those coordinates--if there are any,
        we yield the combined coordinates and the rowids.

        COMMON VALUES ARE NOT INCLUDED. Instead, yielded coordinates
        with -1 values signify a marginal cell on that axis;
        the corresponding rowids are the set-intersection of all rowids
        in the other dimensions for the distinct coords without regard
        for their coordinate on those -1 axes. For example, if we yield:

            (3, -1, 2, -1): [4, 5, 9, 130]

        ...that means there are four rows in the input frame which have
        category 3 for dims[0] and category 2 for dims[2], regardless of
        what their categories are for dims 1 and 3. There are, therefore,
        four rows at (3, -1, 2, -1), where -1 is the margin along that axis.
        A simple count might then place a `4` in that cell in the cube;
        other ffuncs might use those rowids to look up other outputs.
        """
        self._walk(self.dims, (), None, func)

    def interactions(self):
        """Return (interaction-of-coords, intersection-of-rowids) pairs from self."""
        out = []
        self.walk(lambda c, r: out.append((c, r)))
        return out

    def _compute_common_cells_from_marginal_diffs(self, region):
        """Fill common cells by performing a "marginal diff" along each axis."""
        # That is, we subtract ccube.sum(axis=M) from each margin M.
        # Some of these will be computed multiple times if there are multiple
        # dimensions, but that's ok.
        #
        # For example, if we do a simple count of (X, Y) with the following data:
        #
        #   var X  var Y
        #       0      1 (respondent A)
        #       1      0 (respondent B)
        #
        # ...where 0 is the common value in each, then ccube.interactions will
        # form a 2x2 cube, plus an extra marginal row for the X axis (0)
        # and an extra marginal column for the Y axis (1):
        #
        #     [0,  0,    0],
        #     [0,  0,    1],
        #
        #     [0,  1,    2],
        #
        # It is a bit easier to show what's happening if we replace those
        # zeros with underscores, and the number 1's with the letter
        # of the respondent they represent:
        #
        #     [_,  _,    _],
        #     [_,  _,    b],
        #
        #     [_,  a,   ab],
        #
        # We expect the result to be (after cutting off the margins):
        #
        #     [_,  A],
        #     [B,  _],
        #
        # ...so, in effect, we need to "raise" the marginal "a" to its final
        # place "A" in the common row, and similarly for marginal "b"/common "B".
        #
        # If we start with axis 0, we "raise a to A" by a marginal diff:
        #
        #   `region[0] = region[-1, :] - region[:-1, :].sum(axis=0)`
        #
        # ...and we get:
        #
        #     [_,  A,   a],
        #     [_,  _,   b],
        #     [_,  a,  ab],
        #
        # Diffing that along axis 1, we get:
        #
        #     [_,  A,   a],
        #     [B,  _,   b],
        #     [b,  a,  ab],
        #
        # For data points whose coordinates include more than one common value,
        # we have to do a marginal diff of one axis, including the margin cells,
        # and then diff that along the next axis.
        axes = list(range(len(self.dims)))
        for axis in axes:
            common_slice = self.container + tuple(
                dim.common if a == axis else slice(None)
                for a, dim in enumerate(self.dims)
            )
            margin_slice = self.container + tuple(
                -1 if a == axis else slice(None) for a in axes
            )
            uncommon_slice = self.container + tuple(
                slice(None, -1) if a == axis else slice(None) for a in axes
            )
            sumaxis = len(self.container) + axis
            region[common_slice] = region[margin_slice] - region[uncommon_slice].sum(
                axis=sumaxis
            )

    # -------------------------------- ffuncs -------------------------------- #

    def count(self, weights=None):
        """Return the joint frequency distribution of self.dims."""
        return ffunc_count(self, weights).calculate()

    def sum(self, summables, countables, weights=None):
        """Return sums and valid counts, contingent on self.dims.

        The given `summables` arg must be a NumPy array-like of things to sum,
        with the same rows as each of self.dims.

        The given `countables` arg must be a NumPy array-like of booleans,
        with the same rows as each of self.dims: True to be considered a valid
        value and False to be considered missing. If weights are provided,
        any weight=0 will result in a missing row.
        """
        return ffunc_sum(self, summables, countables, weights).calculate()


class ffunc:
    """A base class for frequency (and other aggregate) functions."""

    def __init__(self, cube, weights=None):
        self.cube = cube
        self.weights = weights

    def get_empty_regions(self):
        """Return a tuple of empty NumPy arrays to fill."""
        raise NotImplementedError

    def fill(self, regions):
        """Fill the `regions` arrays with distributions contingent on self.cube.

        The given `regions` must have already been initialized (including
        any corner values). Common cells are not computed here; instead,
        marginal cells are computed, and common cells are inferred from
        them in self.reduce.
        """
        raise NotImplementedError

    def reduce(self, regions):
        """Calculate common cells for the given regions, and return them without margins."""
        raise NotImplementedError

    def calculate(self):
        """Return a NumPy array, the distribution contingent on self.cube.dims."""
        regions = self.get_empty_regions()
        self.fill(regions)
        return self.reduce(regions)


class ffunc_count(ffunc):
    def get_empty_regions(self):
        if self.weights is None:
            dtype = int
            corner_value = self.cube.dims[0].shape[0]
        else:
            dtype = float
            corner_value = self.weights.sum()

        counts = numpy.zeros(self.cube._working_shape, dtype=dtype)
        # Set the "grand total" value in the corner of each region.
        counts[self.cube.corner] = corner_value

        return (counts,)

    def fill(self, regions):
        """Fill the `regions` arrays with distributions contingent on self.cube.dims.

        The given `regions` is assumed to be part of a (possibly larger) cube,
        one which has already been initialized (including any corner values),
        and which will compute its own common cells from the margins later.
        """
        (counts,) = regions
        if self.weights is None:

            def _fill(x_coords, x_rowids):
                counts[x_coords] = len(x_rowids)

        else:

            def _fill(x_coords, x_rowids):
                counts[x_coords] = self.weights[x_rowids].sum()

        self.cube.walk(_fill)

    def reduce(self, regions):
        # Calculate common slices by subtracting uncommon results from margins.
        (counts,) = regions
        self.cube._compute_common_cells_from_marginal_diffs(counts)

        # Cut the margins off our larger result.
        output = counts[self.cube.marginless]

        # Sometimes, marginal differencing can produce minutely different results
        # (within the machine's floating-point epsilon). For most values, this
        # has little effect, but when the value should be 0 but is just barely
        # not 0, it's easy to end up with e.g. 1e-09/1e-09=1 instead of 0/0=nan.
        output[numpy.isclose(output, 0)] = 0

        return output


class ffunc_sum(ffunc):
    def __init__(self, cube, summables, countables, weights=None):
        self.cube = cube
        self.summables = numpy.asarray(summables)
        self.countables = numpy.asarray(countables)
        self.weights = weights
        if weights is not None:
            self.summables = (summables.T * weights).T
            self.countables = self.countables.copy()
            self.countables[weights == 0] = False

    def get_empty_regions(self):
        dtype = int if self.weights is None else float

        sums = numpy.zeros(self._working_shape, dtype=self.summables.dtype)
        valid_counts = numpy.zeros(self._working_shape, dtype=self.countables.dtype)

        # Set the "grand total" value in the corner of each region.
        if self.weights is None:
            counts = numpy.zeros(self.cube._working_shape, dtype=dtype)
            counts[self.cube.corner] = self.cube.dims[0].shape[0]
        else:
            counts[self.cube.corner] = self.weights.sum()

        return sums, valid_counts

    def fill(self, regions):
        """Fill the `regions` arrays with distributions contingent on self.cube.dims.

        The given `regions` is assumed to be part of a (possibly larger) cube,
        one which has already been initialized (including any corner values),
        and which will compute its own common cells from the margins later.
        """
        sums, valid_counts = regions

        def _fill(x_coords, x_rowids):
            sums[x_coords] = numpy.sum(self.summables[x_rowids], axis=0)
            valid_counts[x_coords] = numpy.count_nonzero(
                self.countables[x_rowids], axis=0
            )

        self.cube.walk(_fill)

    def reduce(self, regions):
        # Calculate common slices by subtracting uncommon results from margins.
        sums, valid_counts = regions
        self.cube._compute_common_cells_from_marginal_diffs(sums)
        self.cube._compute_common_cells_from_marginal_diffs(valid_counts)

        # Cut the margins off our larger result.
        sums = sums[self.cube.marginless]
        valid_counts = valid_counts[self.cube.marginless]

        # Sometimes, marginal differencing can produce minutely different results
        # (within the machine's floating-point epsilon). For most values, this
        # has little effect, but when the value should be 0 but is just barely
        # not 0, it's easy to end up with e.g. 1e-09/1e-09=1 instead of 0/0=nan.
        no_valids_mask = numpy.isclose(valid_counts, 0)
        sums[no_valids_mask] = 0
        valid_counts[no_valids_mask] = 0

        return sums, valid_counts
