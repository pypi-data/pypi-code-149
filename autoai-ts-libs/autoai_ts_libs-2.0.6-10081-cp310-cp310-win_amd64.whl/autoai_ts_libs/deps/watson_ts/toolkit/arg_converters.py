"""
This module implements a decorator that can be used to add conversion logic from
pd.DataFrame to Timeseries objects for function arguments. This is used to
enable native DataFrame workflows while implementing individual blocks against
the standard Timeseries object type.
"""

# Standard
from functools import partial
from typing import Any, Callable, List, Optional, Tuple
import copy
import inspect
import warnings

# Third Party
import wrapt

# Local
from .timeseries_conversions import (
    TIMESTAMP_SOURCE_ARG,
    VALUE_SOURCE_ARG,
    to_ndarray,
    to_raw_timeseries,
    to_tspy_unbound,
)

## Public ######################################################################


def tspy_unbound_arg(
    wrapped: Optional[Callable] = None,
    *,
    arg_name: Optional[str] = None,
    ts_col_arg: str = TIMESTAMP_SOURCE_ARG,
    val_col_arg: str = VALUE_SOURCE_ARG,
    **kwargs,
):
    return _arg_converter_decorator(
        wrapped,
        converter=to_tspy_unbound,
        arg_name=arg_name,
        ts_col_arg=ts_col_arg,
        val_col_arg=val_col_arg,
        **kwargs,
    )


def raw_timeseries_arg(
    wrapped: Optional[Callable] = None,
    *,
    arg_name: Optional[str] = None,
    ts_col_arg: str = TIMESTAMP_SOURCE_ARG,
    val_col_arg: str = VALUE_SOURCE_ARG,
):
    """The @raw_timeseries_arg decorator wraps the given function to enable
    automatic conversion from all supported timeseries data types to
    RawTimeseries.

    KWArgs:
        arg_name:  Optional[str]
            The name of the argument that is convertable to a DataFrame. For
            single-argument functions, this can be omitted
        ts_col_arg:  str
            The name of the argument to add to the signature of the wrapped
            function that will be used to specify the column containing the
            timestamp series.
        val_col_arg:  str
            The name of the argument to add to the signature of the wrapped
            function that will be used to specify the column containing the
            value series.

    Example Usage:

    ```py
    @raw_timeseries_arg
    def func(timeseries):
        return [(ts, val * 2) for ts, val in timeseries]

    class Oper:
        @raw_timeseries_arg(arg_name="timeseries")
        def run(self, timeseries, factor=1.5):
            return [(ts, val * factor) for ts, val in timeseries]

    df = pd.DataFrame({"key": [1,2,3], "val": [4,5,6]})
    func(df, ts_col="key", val_col="val")
    op = Oper()
    op.run(df, 3.5, ts_col="key", val_col="val")
    ```
    """
    return _arg_converter_decorator(
        wrapped,
        converter=to_raw_timeseries,
        arg_name=arg_name,
        ts_col_arg=ts_col_arg,
        val_col_arg=val_col_arg,
    )


def ndarray_arg(
    wrapped: Optional[Callable] = None,
    *,
    arg_name: Optional[str] = None,
    ts_col_arg: str = TIMESTAMP_SOURCE_ARG,
    val_col_arg: str = VALUE_SOURCE_ARG,
    **kwargs,
):
    """The @ndarray_arg decorator wraps the given function to enable automatic
    conversion from all supported timeseries types to np.ndarray

    KWArgs:
        arg_name:  Optional[str]
            The name of the argument that is convertable to a DataFrame. For
            single-argument functions, this can be omitted
        ts_col_arg:  str
            The name of the argument to add to the signature of the wrapped
            function that will be used to specify the column containing the
            timestamp series.
        val_col_arg:  str
            The name of the argument to add to the signature of the wrapped
            function that will be used to specify the column containing the
            value series.
        **kwargs:
            Additional keyword args to be bound to the conversion logic (e.g.
            dtype)

    Example Usage:

    ```py
    @ndarray_arg
    def func(timeseries):
        return timeseries * 2
    ```
    """
    return _arg_converter_decorator(
        wrapped,
        converter=to_ndarray,
        arg_name=arg_name,
        ts_col_arg=ts_col_arg,
        val_col_arg=val_col_arg,
        **kwargs,
    )


## Implementation Details ######################################################


def _arg_converter_decorator(
    wrapped: Optional[Callable] = None,
    *,
    converter: Callable,
    arg_name: Optional[str] = None,
    ts_col_arg: str = "ts_col",
    val_col_arg: str = "val_col",
    **bound_converter_kwargs,
):
    """This is the main converter implementation that is implemented above by
    the various public directional decorators

    KWArgs:
        converter:  Callable
            The converter to call for this decorator implementation
        arg_name:  Optional[str]
            The name of the argument that is convertable to a DataFrame. For
            single-argument functions, this can be omitted
        ts_col_arg:  str
            The name of the argument to add to the signature of the wrapped
            function that will be used to specify the column containing the
            timestamp series.
        val_col_arg:  str
            The name of the argument to add to the signature of the wrapped
            function that will be used to specify the column containing the
            value series.
        **bound_converter_kwargs:
            Additional key/value pairs that should be bound into the converter
            call
    """
    # Handle without parens
    if wrapped is None:
        return partial(
            _arg_converter_decorator,
            converter=converter,
            arg_name=arg_name,
            ts_col_arg=ts_col_arg,
            val_col_arg=val_col_arg,
            **bound_converter_kwargs,
        )

    # Get the names of the arguments for the passed in function
    sig = inspect.signature(wrapped)

    # If no arg name given and there is a single argument to this function,
    # use that name
    if arg_name is None:
        fn_args = list(sig.parameters)
        # If this is a member function, strip off the first arg name. Since
        # at the point member functions have not yet been bound, we need to
        # attempt to deduce this with trickery. To do so, we look at the
        # qualname versus the name. This gets tricky for inline functions or
        # nested functions, so we split off any '<globals>.' or '<locals>.'
        # names.
        local_qualname = wrapped.__qualname__.split(">.")[-1]
        fn_name = wrapped.__name__
        if local_qualname != fn_name:
            fn_args = fn_args[1:]
        assert (
            len(fn_args) == 1
        ), f"Cannot infer arg_name for functions with multiple arguments: {fn_args}"
        arg_name = fn_args[0]

    # Make sure the arg name belongs with this function
    assert (
        arg_name in sig.parameters
    ), f"Invalid argument not in wrapped function {arg_name}"
    arg_pos = list(sig.parameters).index(arg_name)

    # The function that replaces the wrapped function. This is where the
    # conversion logic lives that will be invoked at runtime.
    @wrapt.decorator(
        adapter=_argspec_factory(wrapped, [(ts_col_arg, None), (val_col_arg, None)])
    )
    def decorator(wrapped, instance, args, kwargs):

        # If this is a member function, we need to incorporate the positional
        # arg for the instance in the function
        pos_increment = 0 if instance is None else -1
        lookup_pos = arg_pos + pos_increment

        # Find the named argument
        if len(args) > lookup_pos:
            in_pos_args = True
            arg_val = args[lookup_pos]
        else:
            in_pos_args = False
            arg_val = kwargs.get(arg_name)

        # If a value is provided for the arg, check to see if it's a data
        # frame and convert it accordingly
        if arg_val is not None:

            # Shallow copy the kwargs so that mutating ops don't accidentally
            # mutate a shared kwargs dict
            kwargs = copy.copy(kwargs)

            # Get the columns and make sure they're given
            ts_col_name = kwargs.pop(ts_col_arg, None)
            val_col_name = kwargs.pop(val_col_arg, None)

            # Call the converter
            # NOTE: The converters will handle type-specific validation errors
            updated_arg_val = converter(
                input_arg=arg_val,
                **{
                    TIMESTAMP_SOURCE_ARG: ts_col_name,
                    VALUE_SOURCE_ARG: val_col_name,
                },
                **bound_converter_kwargs,
            )

            # Place the updated arugment back in the appropriate place
            if in_pos_args:
                args = list(args)
                args[lookup_pos] = updated_arg_val
            else:
                kwargs[arg_name] = updated_arg_val

        # Invoke the wrapped function with the updated arguments
        return wrapped(*args, **kwargs)

    # Silence the warning coming out of wrapt for using deprecated APIs
    warnings.filterwarnings(
        "ignore",
        message="`formatargspec` is deprecated since Python 3.5. Use `signature` and the `Signature` object directly",
    )
    return decorator(wrapped)


def _argspec_factory(
    wrapped: Callable,
    extra_kwonly: Optional[List[Tuple[str, Any]]] = None,
) -> inspect.FullArgSpec:
    """This factory will create a new FullArgSpec for the wrapped function with
    the extra keyword-only args added.
    """
    argspec = inspect.getfullargspec(wrapped)
    kwonlyargs = list(argspec.kwonlyargs or [])
    kwonlydefaults = argspec.kwonlydefaults or {}
    for name, dflt in extra_kwonly:
        assert (
            name not in kwonlydefaults
        ), f"Adding kwarg [{name}] conflicts with existing kwarg!"
        kwonlyargs.append(name)
        kwonlydefaults[name] = dflt
    return inspect.FullArgSpec(
        args=argspec.args,
        varargs=argspec.varargs,
        varkw=argspec.varkw,
        defaults=argspec.defaults,
        kwonlyargs=kwonlyargs,
        kwonlydefaults=kwonlydefaults,
        annotations=argspec.annotations,
    )
