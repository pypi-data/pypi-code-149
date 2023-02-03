import os
import datetime
from pathlib import Path

from ._const import (
    IFO,
    CAL_MEASUREMENT_ROOT,
    DEFAULT_CONFIG_PATH,
    DEFAULT_MODEL_PATH,
)
from . import _util
from ._util import CMDError
from ._util import logger
from ..darm import DARMModel
from ..measurement import (
    Measurement,
    ProcessSensingMeasurement,
    ProcessActuationMeasurement,
)


def list_all_measurement_sets():
    """return chronologically sorted list of all measurement ids"""
    return sorted(os.listdir(CAL_MEASUREMENT_ROOT))


def template_str_replace(template_file, replacement):
    """replace '_template_' in template file with replacement str

    """
    return os.path.basename(template_file).replace('_template_', replacement)


def find_files_from_template(directory, template):
    """find all files matching template in the specified directory

    The string '_template_' in the template name is replaced with '*',
    and file globbing is used to find files.

    """
    return sorted(list(Path(directory).glob(template_str_replace(template, '*'))))


def measurement_extract_datetime(mfile):
    """extract the datetime from a measurement file

    returns a datetime object

    """
    # FIXME: this is a BAD heuristic based on an assumed location
    # and format of the date in the file name, this should be
    # improved.
    #
    # assumes date is ISO string after final '_' separator
    ds = os.path.splitext(os.path.basename(mfile))[0].split('_')[-1]
    return _util.parse_timestamp(ds)


def find_closest_pcal(pcal_measurements, mfile):
    """find the closest pcal measurement to the given measurement file

    For each measurement file, the datetime of the measurement is
    extracted from the filename.  The closest pcal measurement and
    it's correspond datetime object are returned.

    """
    mtime = measurement_extract_datetime(mfile)
    last = (None, abs(mtime - datetime.datetime(1, 1, 1)))
    for f in pcal_measurements:
        dt = measurement_extract_datetime(f)
        diff = abs(dt - mtime)
        if diff < last[1]:
            last = (f, diff)
    return last


class MeasurementSet:
    """PyDARM Measurement Set class

    Holds information about a specific calibration measurement set.

    """

    def _find_meas_pairs(self, template, pcal_files):
        """find loop/pcal measurement pairs for a measurement matching given template

        Returns loop/pcal Measurement objects.

        """
        m_files = find_files_from_template(self.path, template)
        if len(m_files) > 1:
            logger.warning(f"found more than one measurement file for template {template}, loading latest...") # noqa E501
            m_file = m_files[-1]
        elif len(m_files) < 1:
            raise CMDError(f"no measurement found for template {template}.")
        else:
            m_file = m_files[0]
        pcal_file, pcal_dt = find_closest_pcal(pcal_files, m_file)
        # FIXME: check that pcal dt is within bounds
        return {
            'loop': Measurement(m_file),
            'pcal': Measurement(pcal_file),
        }

    def __init__(self, mset_id=None, config=DEFAULT_CONFIG_PATH):
        """load measurement set

        If `mset_id` is None or 'last'/'latest', the most recent
        measurement set will be retrieved.

        """
        self.config = _util.load_config(config)
        if mset_id in [None, 'last', 'latest']:
            logger.debug("finding last measurement set...")
            mset_list = list_all_measurement_sets()
            self.id = mset_list[-1]
        else:
            self.id = mset_id
        self.path = os.path.join(CAL_MEASUREMENT_ROOT, self.id)
        if not os.path.exists(self.path):
            raise CMDError(f"measurement set '{mset_id}' could not be found.")
        logger.info(f"measurement set: {self.path}")

        logger.debug("finding PCal measurements...")
        self.pcal_files = find_files_from_template(
            self.path,
            self.config['PCal']['template'],
        )

        self.measurements = {}

        name = 'Sensing'
        logger.debug(f"finding {name} measurements...")
        self.measurements[name] = self._find_meas_pairs(
            self.config['Sensing']['template'],
            self.pcal_files,
        )

        for stage in ['L1', 'L2', 'L3']:
            name = f'Actuation/{stage}'
            logger.debug(f"finding {name} measurements...")
            self.measurements[name] = self._find_meas_pairs(
                self.config['Actuation'][stage]['template'],
                self.pcal_files,
            )

        self.model = None
        self.processed_measurements = {}

    def load_model(self, model_ini=DEFAULT_MODEL_PATH):
        """load model and process measurements

        """
        self.model_ini = model_ini
        self.model = DARMModel(self.model_ini)
        ref_pcal = self.model.pcal.pcal_filter_bank.rstrip("_PD")

        ##########
        # load sensing

        name = 'Sensing'
        logger.info(f"processing {name}...")

        self.processed_measurements[name] = \
            ProcessSensingMeasurement(
                self.model_ini,
                self.measurements[name]['loop'],
                self.measurements[name]['pcal'],
                # FIXME: move these into the config
                (f'{IFO}:LSC-DARM1_IN2',
                 f'{IFO}:LSC-DARM1_EXC'),
                (f'{IFO}:CAL-PCALY_RX_PD_OUT_DQ',
                 f'{IFO}:LSC-DARM_IN1_DQ'),
                self.config['Sensing']['coh_thresh_loop'],
                self.config['Sensing']['coh_thresh_pcal']
            )

        ##########
        # load actuation

        self.processed_measurements['actuation'] = {}

        for stage in ['L1', 'L2', 'L3']:
            name = f'Actuation/{stage}'
            logger.info(f"processing {name}...")

            optic = self.config['Actuation'][stage]['optic']
            arm = optic[-1].lower()

            self.processed_measurements[name] = \
                ProcessActuationMeasurement(
                    self.model_ini,
                    f'actuation_{arm}_arm',
                    self.measurements[name]['loop'],
                    self.measurements[name]['pcal'],
                    # FIXME: move these into config
                    (f"{IFO}:SUS-{optic}_{stage}_CAL_EXC",
                     f'{IFO}:LSC-DARM_IN1_DQ'),
                    (f'{IFO}:CAL-{ref_pcal}_PD_OUT_DQ',
                     f'{IFO}:LSC-DARM_IN1_DQ'),
                    self.config['Actuation'][stage]['coh_thresh_loop'],
                    self.config['Actuation'][stage]['coh_thresh_pcal'],
                )

    @property
    def datetime(self):
        """return measurement set date/time as datetime object"""
        return datetime.datetime.fromisoformat(self.id)
