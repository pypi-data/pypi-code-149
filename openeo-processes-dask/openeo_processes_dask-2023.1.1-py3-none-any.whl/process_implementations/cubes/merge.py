from typing import Callable, Optional

import numpy as np
import xarray as xr

from openeo_processes_dask.exceptions import OverlapResolverMissing
from openeo_processes_dask.process_implementations.data_model import RasterCube

__all__ = ["merge_cubes"]

NEW_DIM_NAME = "__cubes__"
NEW_DIM_COORDS = ["cube1", "cube2"]


from collections import namedtuple

Overlap = namedtuple("Overlap", ["only_in_cube1", "only_in_cube2", "in_both"])


def merge_cubes(
    cube1: RasterCube,
    cube2: RasterCube,
    overlap_resolver: Callable = None,
    context: Optional[dict] = None,
) -> RasterCube:

    if context is None:
        context = {}
    if not isinstance(cube1, type(cube2)):
        raise Exception(
            f"Provided cubes have incompatible types. cube1: {type(cube1)}, cube2: {type(cube2)}"
        )

    # Key: dimension name
    # Value: (labels in cube1 not in cube2, labels in cube2 not in cube1)
    overlap_per_shared_dim = {
        dim: Overlap(
            only_in_cube1=np.setdiff1d(cube1[dim].data, cube2[dim].data),
            only_in_cube2=np.setdiff1d(cube2[dim].data, cube1[dim].data),
            in_both=np.intersect1d(cube1[dim].data, cube2[dim].data),
        )
        for dim in set(cube1.dims).intersection(set(cube2.dims))
    }

    differing_dims = set(cube1.dims).symmetric_difference(set(cube2.dims))

    if len(differing_dims) == 0:
        # Check whether all of the shared dims have exactly the same labels
        dims_have_no_label_diff = all(
            [
                len(overlap.only_in_cube1) == 0 and len(overlap.only_in_cube2) == 0
                for overlap in overlap_per_shared_dim.values()
            ]
        )
        if dims_have_no_label_diff:
            # Example 3: All dimensions and their labels are equal
            concat_both_cubes = xr.concat([cube1, cube2], dim=NEW_DIM_NAME).reindex(
                {NEW_DIM_NAME: NEW_DIM_COORDS}
            )

            # Need to rechunk here to ensure that the cube dimension isn't chunked and the chunks for the other dimensions are not too large.
            concat_both_cubes_rechunked = concat_both_cubes.chunk(
                {NEW_DIM_NAME: -1}
                | {dim: "auto" for dim in cube1.dims if dim != NEW_DIM_NAME}
            )
            if overlap_resolver is None:
                # Example 3.1: Concat along new "cubes" dimension
                merged_cube = concat_both_cubes_rechunked
            else:
                # Example 3.2: Elementwise operation
                positional_parameters = {"data": 0}
                named_parameters = {"context": context}

                merged_cube = concat_both_cubes_rechunked.reduce(
                    overlap_resolver,
                    dim=NEW_DIM_NAME,
                    keep_attrs=True,
                    positional_parameters=positional_parameters,
                    named_parameters=named_parameters,
                )
        else:
            # Example 1 & 2
            dims_requiring_resolve = [
                dim
                for dim, overlap in overlap_per_shared_dim.items()
                if len(overlap.in_both) > 0
                and (len(overlap.only_in_cube1) > 0 or len(overlap.only_in_cube2) > 0)
            ]

            if len(dims_requiring_resolve) == 0:
                # Example 1: No overlap on any dimensions, can just combine by coords
                merged_cube = xr.combine_by_coords([cube1, cube2])
            elif len(dims_requiring_resolve) == 1:
                # Example 2: Overlap on one dimension, resolve these pixels with overlap resolver
                # and combine the rest by coords

                if overlap_resolver is None or not callable(overlap_resolver):
                    raise OverlapResolverMissing(
                        "Overlapping data cubes, but no overlap resolver has been specified."
                    )

                overlapping_dim = dims_requiring_resolve[0]

                stacked_conflicts = xr.concat(
                    [
                        cube1.sel(
                            **{
                                overlapping_dim: overlap_per_shared_dim[
                                    overlapping_dim
                                ].in_both
                            }
                        ),
                        cube2.sel(
                            **{
                                overlapping_dim: overlap_per_shared_dim[
                                    overlapping_dim
                                ].in_both
                            }
                        ),
                    ],
                    dim=NEW_DIM_NAME,
                ).reindex({NEW_DIM_NAME: NEW_DIM_COORDS})

                # Need to rechunk here to ensure that the cube dimension isn't chunked and the chunks for the other dimensions are not too large.
                stacked_conflicts_rechunked = stacked_conflicts.chunk(
                    {NEW_DIM_NAME: -1}
                    | {dim: "auto" for dim in cube1.dims if dim != NEW_DIM_NAME}
                )

                positional_parameters = {"data": 0}
                named_parameters = {"context": context}

                merge_conflicts = stacked_conflicts_rechunked.reduce(
                    overlap_resolver,
                    dim=NEW_DIM_NAME,
                    keep_attrs=True,
                    positional_parameters=positional_parameters,
                    named_parameters=named_parameters,
                )

                rest_of_cube_1 = cube1.sel(
                    **{
                        overlapping_dim: overlap_per_shared_dim[
                            overlapping_dim
                        ].only_in_cube1
                    }
                )
                rest_of_cube_2 = cube2.sel(
                    **{
                        overlapping_dim: overlap_per_shared_dim[
                            overlapping_dim
                        ].only_in_cube2
                    }
                )
                merged_cube = xr.combine_by_coords(
                    [merge_conflicts, rest_of_cube_1, rest_of_cube_2]
                )

            else:
                raise ValueError(
                    "More than one overlapping dimension, merge not possible."
                )

    elif len(differing_dims) <= 2:
        if overlap_resolver is None or not callable(overlap_resolver):
            raise OverlapResolverMissing(
                "Overlapping data cubes, but no overlap resolver has been specified."
            )

        # Example 4: broadcast lower dimension cube to higher-dimension cube
        lower_dim_cube = cube1 if len(cube1.dims) < len(cube2.dims) else cube2
        higher_dim_cube = cube1 if len(cube1.dims) >= len(cube2.dims) else cube2
        lower_dim_cube_broadcast = lower_dim_cube.broadcast_like(higher_dim_cube)

        # Stack both cubes and use overlap resolver to resolve each pixel
        both_stacked = xr.concat(
            [higher_dim_cube, lower_dim_cube_broadcast], dim=NEW_DIM_NAME
        ).reindex({NEW_DIM_NAME: NEW_DIM_COORDS})

        # Need to rechunk here to ensure that the cube dimension isn't chunked and the chunks for the other dimensions are not too large.
        both_stacked_rechunked = both_stacked.chunk(
            {NEW_DIM_NAME: -1}
            | {dim: "auto" for dim in cube1.dims if dim != NEW_DIM_NAME}
        )

        positional_parameters = {"data": 0}
        named_parameters = {"context": context}
        merged_cube = both_stacked_rechunked.reduce(
            overlap_resolver,
            dim=NEW_DIM_NAME,
            keep_attrs=True,
            positional_parameters=positional_parameters,
            named_parameters=named_parameters,
        )
    else:
        raise ValueError("Number of differing dimensions is >2, merge not possible.")

    return merged_cube
