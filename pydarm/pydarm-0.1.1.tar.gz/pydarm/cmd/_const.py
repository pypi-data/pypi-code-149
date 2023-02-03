import os


# instrument designator
IFO = os.getenv('IFO')


# calibration config/data roots
CAL_CONFIG_ROOT = None
CAL_DATA_ROOT = None
if IFO:
    CAL_CONFIG_ROOT = os.path.join(
        '/ligo/groups/cal/ifo/',
        IFO,
    )
    CAL_DATA_ROOT = os.path.join(
        '/ligo/groups/cal/data/',
        IFO,
    )
CAL_CONFIG_ROOT = os.getenv(
    'CAL_CONFIG_ROOT',
    CAL_CONFIG_ROOT,
)
CAL_DATA_ROOT = os.getenv(
    'CAL_DATA_ROOT',
    CAL_DATA_ROOT,
)


CAL_TEMPLATE_ROOT = None
CAL_MEASUREMENT_ROOT = None
DEFAULT_MODEL_PATH = None
DEFAULT_CONFIG_PATH = None
if CAL_CONFIG_ROOT:
    CAL_TEMPLATE_ROOT = os.path.join(
        CAL_CONFIG_ROOT,
        'templates',
    )
    CAL_MEASUREMENT_ROOT = os.path.join(
        CAL_DATA_ROOT,
        'measurements',
    )
    if IFO:
        DEFAULT_MODEL_PATH = os.path.join(
            CAL_CONFIG_ROOT,
            f'pydarm_{IFO}.ini',
        )
        DEFAULT_CONFIG_PATH = os.path.join(
            CAL_CONFIG_ROOT,
            f'pydarm_cmd_{IFO}.yaml',
        )


# default frequency response frequency array
DEFAULT_FREQSPEC = '0.01:5000:3000'
