# Authors: Luis Scoccola
# License: 3-clause BSD

# from re import A
from turtle import back
import numpy as np
import warnings


import plotly.graph_objects as go
import plotly
from jupyter_dash import JupyterDash
import dash
from dash import dcc
from dash import html
from dash import DiskcacheManager, CeleryManager
from dash.long_callback import DiskcacheLongCallbackManager

import pandas as pd
import json
import diskcache

PERSISTABLE_STDERR = "./persistable-stderr"
PERSISTABLE_DASH_CACHE = "./persistable-dash-cache"
# WARNINGS_GLOBAL = "test default"

X_START_FIRST_LINE = "x-start-first-line-"
Y_START_FIRST_LINE = "y-start-first-line-"
X_END_FIRST_LINE = "x-end-first-line-"
Y_END_FIRST_LINE = "y-end-first-line-"
X_START_SECOND_LINE = "x-start-second-line-"
Y_START_SECOND_LINE = "y-start-second-line-"
X_END_SECOND_LINE = "x-end-second-line-"
Y_END_SECOND_LINE = "y-end-second-line-"
DISPLAY_LINES_SELECTION = "display-lines-selection-"
ENDPOINT_SELECTION = "endpoint-selection-"
MIN_DIST_SCALE = "min-dist-scale-"
MAX_DIST_SCALE = "max-dist-scale-"
MIN_DENSITY_THRESHOLD = "min-density-threshold-"
MAX_DENSITY_THRESHOLD = "max-density-threshold-"
ENDPOINT_SELECTION_DIV = "endpoint-selection-div-"
PARAMETER_SELECTION_DIV = "parameter-selection-div-"
DISPLAY_PARAMETER_SELECTION = "display-parameter-selection-"

CFF_PLOT = "cff-plot-"
STORED_CCF = "stored-ccf-"
STORED_CCF_DRAWING = "stored-ccf-drawing-"
COMPUTE_CCF_BUTTON = "compute-ccf-button-"
INPUT_LOG_GRANULARITY_CCF = "input-log-granularity-ccf-"
INPUT_NUM_JOBS_CCF = "input-num-jobs-ccf-"
INPUT_MAX_COMPONENTS = "input-max-components-"
LOG = "log-"
WARNINGS_POLLING_INTERVAL = "warnings-polling-interval-"

PV_PLOT = "pv-plot-"
STORED_PV = "stored-pv-"
STORED_PV_DRAWING = "stored-pv-drawing-"
COMPUTE_PV_BUTTON = "compute-pv-button-"
INPUT_MAX_VINES = "input-max-vines-"
INPUT_PROM_VIN_SCALE = "input-prom-vin-scale-"
INPUT_LOG_GRANULARITY_PV = "input-log-granularity-pv-"
INPUT_NUM_JOBS_PV = "input-num-jobs-pv-"

VALUE = "value"
CLICKDATA = "clickData"
HIDDEN = "hidden"
DATA = "data"
N_CLICKS = "n_clicks"
DISABLED = "disabled"
FIGURE = "figure"
CHILDREN = "children"
N_INTERVALS = "n_intervals"

IN = "input"
ST = "state"


def cs(l):
    return l[0] + l[1]


_funcs = []

COUNTER = 0

def my_callback(
    inputs, outputs, _app, prevent_initial_call=False, background=False, running=None, func_num = 0,
):

    def out_function(function):
        print("attaching callback to")
        print(function.__name__)
        # FIX
        dash_inputs = [
            dash.Input(i, v) if t == IN else dash.State(i, v) for i, v, t in inputs
        ]
        dash_outputs = (
            [dash.Output(i, v) for i, v in outputs]
            if len(outputs) > 1
            else dash.Output(outputs[0][0], outputs[0][1])
        )

        if running is None:
            dash_running_outputs = None
        else:
            dash_running_outputs = [
                (dash.Output(i, v), value_start, value_end)
                for i, v, value_start, value_end in running
            ]


        def callback_function(*argv):
            d = {}
            for n, arg in enumerate(argv):
                d[cs(inputs[n])] = arg
            d = function(d)
            return (
                tuple(d[cs(o)] for o in outputs)
                if len(outputs) > 1
                else d[cs(outputs[0])]
            )

        def callback_function_1(*argv):
            d = {}
            for n, arg in enumerate(argv):
                d[cs(inputs[n])] = arg
            d = function(d)
            return (
                tuple(d[cs(o)] for o in outputs)
                if len(outputs) > 1
                else d[cs(outputs[0])]
            )

        def callback_function_2(*argv):
            d = {}
            for n, arg in enumerate(argv):
                d[cs(inputs[n])] = arg
            d = function(d)
            return (
                tuple(d[cs(o)] for o in outputs)
                if len(outputs) > 1
                else d[cs(outputs[0])]
            )

        #global COUNTER
        #import inspect
        #import re
        #fn_source = inspect.getsource(callback_function) 
        #fn_str = fn_source 
        #print(fn_str.encode("utf-8"))
        #new = re.sub("callback_function", "callback_function_" + str(COUNTER), str(fn_str.encode("utf-8")))
        #callback_function = exec(new,globals(),locals())
        #print(str(inspect.getsource(callback_function).encode("utf-8"))) 

        ##locals()[func_label] = locals()["callback_function"]
        ##callback_function.__name__ = func_label
        #COUNTER += 1

        #fn_source = inspect.getsource(callback_function) 
        #fn_str = fn_source 
        #print(fn_str.encode("utf-8"))

        #fn_source = inspect.getsource(locals()[func_label]) 
        #fn_str = fn_source 
        #print(fn_str.encode("utf-8"))

        global _funcs
        _funcs.append(callback_function)
        _funcs.append(function)
        _funcs.append(inputs)
        _funcs.append(outputs)
        _funcs.append(dash_inputs)
        _funcs.append(dash_outputs)
        _funcs.append(dash_running_outputs)


        if background:
            if func_num==0:
                _app.callback(
                    dash_outputs,
                    dash_inputs,
                    prevent_initial_call,
                    running=dash_running_outputs,
                    background=background,
                )(callback_function_1)
            else:
                _app.callback(
                    dash_outputs,
                    dash_inputs,
                    prevent_initial_call,
                    running=dash_running_outputs,
                    background=background,
                )(callback_function_2)
        else:
            _app.callback(
                dash_outputs,
                dash_inputs,
                prevent_initial_call,
                running=dash_running_outputs,
                background=background,
            )(callback_function)

        return function

    return out_function


# set temporary files
cache = diskcache.Cache(PERSISTABLE_DASH_CACHE)
# cache_2 = diskcache.Cache(PERSISTABLE_DASH_CACHE+"_2")
background_callback_manager = DiskcacheManager(cache)
# long_callback_manager = DiskcacheLongCallbackManager(cache)
# background_callback_manager_2 = DiskcacheManager(cache_2)

_app = dash.Dash(
    __name__,
    # long_callback_manager=long_callback_manager,
    background_callback_manager=background_callback_manager,
)

min_granularity = 4
max_granularity = 8
default_log_granularity = 6

_app.layout = html.Div(
    children=[
        # contains the component counting function as a pandas dataframe
        dcc.Store(id=STORED_CCF),
        # contains the vineyard as a vineyard object
        dcc.Store(id=STORED_PV),
        html.Div(
            className="parameter-single",
            children=[
                html.Span(
                    className="name",
                    children="granularity comp count func",
                ),
                dcc.Slider(
                    min_granularity,
                    max_granularity,
                    step=None,
                    marks={i: str(2**i) for i in range(1, max_granularity + 1)},
                    value=default_log_granularity,
                    id=INPUT_LOG_GRANULARITY_CCF,
                    className=VALUE,
                ),
            ],
        ),
        html.Button(
            "(re)compute component counting function",
            id=COMPUTE_CCF_BUTTON,
            className=VALUE,
        ),
        html.Div(
            className="parameter-single",
            children=[
                html.Span(
                    className="name",
                    children="granularity vineyard",
                ),
                dcc.Slider(
                    min_granularity,
                    max_granularity,
                    step=None,
                    marks={i: str(2**i) for i in range(1, max_granularity + 1)},
                    value=default_log_granularity - 1,
                    id=INPUT_LOG_GRANULARITY_PV,
                    className=VALUE,
                ),
            ],
        ),
        html.Button(
            "compute prominence vineyard",
            id=COMPUTE_PV_BUTTON,
            className=VALUE,
        ),
    ],
)


def compute_ccf(d):
    print("CCF run")
    print(d)
    granularity = 2 ** d[INPUT_LOG_GRANULARITY_CCF + VALUE]
    import time

    time.sleep(2)

    return {STORED_CCF + DATA: json.dumps([])}

compute_ccf = my_callback(
    [
        [COMPUTE_CCF_BUTTON, N_CLICKS, IN],
        [INPUT_LOG_GRANULARITY_CCF, VALUE, ST],
    ],
    [
        [STORED_CCF, DATA],
    ],
    _app,
    prevent_initial_call=True,
    background=True,
    running=[[COMPUTE_CCF_BUTTON, DISABLED, True, False]],
)(compute_ccf)



def compute_pv(d):

    print("PV run")
    print(d)
    granularity = 2 ** d[INPUT_LOG_GRANULARITY_PV + VALUE]

    import time

    time.sleep(2)

    return {STORED_PV + DATA: json.dumps([])}
compute_pv = my_callback(
    [
        [COMPUTE_PV_BUTTON, N_CLICKS, IN],
        [INPUT_LOG_GRANULARITY_PV, VALUE, ST],
    ],
    [[STORED_PV, DATA]],
    _app,
    prevent_initial_call=True,
    background=True,
    running=[[COMPUTE_PV_BUTTON, DISABLED, True, False]],
    func_num=1)(compute_pv)


print(len(_funcs))

def PersistableInteractive(persistable, debug=False):
    _app.run_server(debug=debug)
