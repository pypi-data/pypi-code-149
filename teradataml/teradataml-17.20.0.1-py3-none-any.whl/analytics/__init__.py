from .byom import *
from .mle import *
from .sqle import *
from .valib import valib
from .Transformations import Binning, Derive, OneHotEncoder, FillNa, LabelEncoder, MinMaxScalar, \
    Retain, Sigmoid, ZScore
from teradataml.analytics.json_parser.utils import _get_json_data_from_tdml_repo
from teradataml.analytics.analytic_function_executor import _SQLEFunctionExecutor, _TableOperatorExecutor,\
    _UAFFunctionExecutor, _BYOMFunctionExecutor
import sys
from teradataml.common.constants import TeradataAnalyticFunctionTypes


def _process_analytic_functions():
    """
    DESCRIPTION:
        Internal function to generate the analytic function based on the json data
        and attach it to teradataml.

    RETURNS:
        None

    RAISES:
        TeradataMlException.

    EXAMPLES:
        _process_analytic_functions()
    """
    for metadata in _get_json_data_from_tdml_repo():
        function_name = metadata.func_name
        function_type = metadata.func_type
        executor_class = _get_executor_class_name(function_type)
        signature = metadata.get_function_parameters_string()
        function = "def {function_name}({signature}): return globals()" \
                   "['{executor_class}']('{function_name}')._execute_" \
                   "function(**locals())".format(function_name=function_name, 
                                                 signature=signature, 
                                                 executor_class=executor_class)
        exec(function, globals())
        # Add the doc string.
        globals()[function_name].__doc__ = metadata.get_doc_string()
        # Attach it to teradataml.
        setattr(sys.modules["teradataml"], function_name, globals()[function_name])
        if function_type == TeradataAnalyticFunctionTypes.SQLE.value.lower():
            function_type = "sqle"
        func_module = "teradataml.analytics.{}".format(function_type.lower())
        setattr(sys.modules[func_module], function_name, globals()[function_name])

def _get_executor_class_name(function_type):
    """
    DESCRIPTION:
        Internal function to get executor class name for function_type provided.
    
    PARAMETERS:
        function_type:
            Required Argument.
            Specifies the type of function.
            Permitted Values: ['FASTPATH', 'TABLE_OPERATOR']
            Types: str

    RETURNS:
        str

    RAISES:
        None.

    EXAMPLES:
        _get_executor_class_name("table_operator")
    """
    func_type_to_executor = {
        TeradataAnalyticFunctionTypes.SQLE.value: _SQLEFunctionExecutor,
        TeradataAnalyticFunctionTypes.TABLEOPERATOR.value: _TableOperatorExecutor,
        TeradataAnalyticFunctionTypes.UAF.value: _UAFFunctionExecutor,
        TeradataAnalyticFunctionTypes.BYOM.value: _BYOMFunctionExecutor
    }
    return func_type_to_executor.get(function_type.upper(), _SQLEFunctionExecutor).__name__
