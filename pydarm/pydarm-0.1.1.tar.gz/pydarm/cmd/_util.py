import os
import logging
import argparse
import datetime
from pathlib import Path

import yaml
import numpy as np

from ._const import (
    DEFAULT_CONFIG_PATH,
    DEFAULT_MODEL_PATH,
    DEFAULT_FREQSPEC,
)


logger = logging.getLogger('pydarm')


class CMDError(Exception):
    pass


class ModelNameParseAction(argparse.Action):
    """model path argparse argument parser Action.

    """
    help = 'model INI config file'

    def __init__(self, *args, **kwargs):
        kwargs['metavar'] = kwargs.get('metavar', 'MODEL')
        kwargs['default'] = kwargs.get('default', DEFAULT_MODEL_PATH)
        helps = 'model INI config file'
        if DEFAULT_MODEL_PATH:
            helps += f' [{DEFAULT_MODEL_PATH}]'
        kwargs['help'] = kwargs.get('help', helps)
        super().__init__(*args, **kwargs)

    def __call__(self, parser, namespace, values, option_string=False):
        if not values:
            raise argparse.ArgumentError(self, f"the following argument is required: {self.metavar}") # noqa E501
        path = values
        if not os.path.exists(path):
            raise argparse.ArgumentError(self, f"model file not found: {path}")
        setattr(namespace, self.dest, path)


def add_model_option(parser, **kwargs):
    """add a subparser argument for a model file"""
    parser.add_argument(
        '--model', action=ModelNameParseAction, **kwargs)


def freq_from_spec(spec):
    """logarithmicly spaced frequency array, based on specification string

    Specification string should be of form 'START:[NPOINTS:]STOP'.

    """
    fspec = spec.split(':')
    if len(fspec) == 2:
        fspec = fspec[0], DEFAULT_FREQSPEC.split(':')[1], fspec[1]
    return np.logspace(
        np.log10(float(fspec[0])),
        np.log10(float(fspec[2])),
        int(fspec[1]),
    )


def add_freqspec_option(parser, **kwargs):
    """add a subparser option for specifying a frequency array"""
    parser.add_argument(
        '--freq', '-f', metavar='FLO:[NPOINTS:]FHI', default=DEFAULT_FREQSPEC,
        help=f'logarithmic frequency array specification in Hz [{DEFAULT_FREQSPEC}]')


def add_config_option(parser, **kwargs):
    """add a subparser option for the pydarm cmd config file."""
    parser.add_argument(
        '--config', default=DEFAULT_CONFIG_PATH,
        help=f"pydarm cmd configuration YAML file ({DEFAULT_CONFIG_PATH})")


def mcmc_mode_check(x):
    x = str(x).lower()
    if x not in ['all', 'latest', 'none']:
        raise Exception("`mcmc_mode` must be one of: all, latest, none")
    return x


def load_config(config_file):
    """load configuration file for sensing and actuation function measurements

    Parameters
    ----------
    config_file : str
        Path to config file.

    Returns
    -------
    config : dict

    """
    config_file = Path(config_file)

    logger.info(f"loading config: {config_file}")

    if not config_file.exists():
        raise IOError(filename=config_file.name)

    with open(config_file) as f:
        config = yaml.safe_load(f)

    # Default parameters in case something wasn't supplied
    defaults = {
        'n_recent_meas': 0,
        'meas_tags': [],
        'meas_dir': '',
        }

    # Define argument type processing beyond what yaml loading
    # already does
    argtypes = {
        'meas_dir': Path,
        'mcmc_mode': mcmc_mode_check
        }

    for key, val in defaults.items():
        if key not in config['Common'].keys():
            config['Common'][key] = val

    # Sensing and Actuation inherit from Common any attributes they
    # don't already have
    modes = ['Sensing', 'Actuation']
    for key, val in config['Common'].items():
        for mode in modes:
            if key not in config[mode].keys():
                config[mode][key] = val

    # actuation stages inherit from Actuation any attributes they
    # don't already have
    stages = ['L1', 'L2', 'L3']
    for key, val in config['Actuation'].items():
        if key in stages:
            pass
        else:
            for stage in stages:
                if key not in config['Actuation'][stage].keys():
                    config['Actuation'][stage][key] = val

    # convert arguments to correct type
    for mode in ['Common', 'Actuation', 'Sensing']:
        for key in config[mode].keys():
            if key in argtypes.keys():
                config[mode][key] = argtypes[key](config[mode][key])
    for stage in stages:
        for key in config['Actuation'][stage].keys():
            if key in argtypes.keys():
                config['Actuation'][stage][key] = argtypes[key](config['Actuation'][stage][key])

    return config


# this is a "ISO 8601-1:2019, basic format" date/time format to minute
# precision
DATETIME_FMT = '%Y%m%dT%H%MZ'


def gen_timestamp(dt=None):
    """generate an ISO timestamp string with minute precision

    """
    if dt is None:
        dt = datetime.datetime.utcnow()
    # return dt.isoformat(timespec='minutes')
    return dt.strftime(DATETIME_FMT)


def parse_timestamp(ds):
    """parse timestamp (generated with gen_timestamp) into a datetime object

    """
    # return datetime.datetime.fromisoformat(ds)
    return datetime.datetime.strptime(ds, DATETIME_FMT)
