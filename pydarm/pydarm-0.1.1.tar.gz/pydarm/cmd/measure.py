import os
import shutil
import subprocess

from ._const import (
    CAL_TEMPLATE_ROOT,
    CAL_MEASUREMENT_ROOT,
)
from . import _util
from ._util import logger
from ._util import CMDError
from .measurement_set import template_str_replace


def diag_run(run_xml, save_xml=None, dry=False):
    """execute a DTT measurement template

    """
    if not save_xml:
        save_xml = run_xml
    diag_cmd = f'''
open
restore {run_xml}
run -w
save {save_xml}
quit
'''
    print(diag_cmd)
    if not dry:
        subprocess.run(
            ['diag'],
            input=diag_cmd.strip(),
            text=True,
        )
        print()
    # FIXME: check for errors somehow


def touch(path):
    """touch a file"""
    open(path, 'w').close()

##################################################


def add_args(parser):
    _util.add_config_option(parser)
    parser.add_argument(
        '--measure', '-m', nargs='*',
        help="measurements to be run (by default user default sequence from config)")
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        '--dry-run', '--dry', action='store_const', dest='run', const='dry',
        help="run measurement in headless mode")
    group.add_argument(
        '--run-interactive', action='store_const', dest='run', const='interactive',
        help="run measurement in interactive mode")
    group.add_argument(
        '--run-headless', action='store_const', dest='run', const='headless',
        help="run measurement in headless mode")


def main(args):
    """run calibration plant transer function measurements

    This command by default runs the full set of sensing and actuation
    chain calibration measurements.  The measurement config and
    templates are retrieved from the CAL_CONFIG_ROOT directory.  Each
    time a measurement is initiated a timestamped directory is created
    in the CAL_DATA_ROOT/measurements/ directory, and all resulting
    measurement output files are saved to that directory.

    When run without arguments the available measurements, the
    templates they use, and the default measurement sequence will be
    printed.

    A '--run-*' argument must be provided to actually run the
    measurements.

    """
    # https://cdswiki.ligo-wa.caltech.edu/wiki/TakingCalibrationMeasurements

    if not CAL_TEMPLATE_ROOT:
        raise CMDError("CAL_TEMPLATE_ROOT not specified.")
    if not CAL_MEASUREMENT_ROOT:
        raise CMDError("CAL_MEASUREMENT_ROOT not specified.")

    config = _util.load_config(args.config)

    measurements = {}
    for nick, mref in config['Common']['measurements'].items():
        section = config
        for name in mref.split('/'):
            section = section[name]
        measurements[nick] = {
            'description': section['description'],
            'template': os.path.join(
                CAL_TEMPLATE_ROOT,
                section['template'],
            ),
        }

    logger.info("available measurements:")
    for meas, conf in measurements.items():
        print(f"  {meas:<4}: {conf['description']} [{conf['template']}]")
        # check that all template files exist
        if not os.path.exists(conf['template']):
            raise CMDError(f"measurement '{meas}' template file not found: {conf['template']}")

    # construct the measurement sequence
    default_measurement_sequence = config['Common']['measurement_sequence']

    if not args.measure:
        mseq = default_measurement_sequence
    else:
        mseq = args.measure

    for meas in mseq:
        if meas not in measurements:
            raise CMDError(f"'{meas}' is not a valid measurement.")

    logger.info("measurement sequence:")
    logger.info(f"  {mseq}")

    if not args.run:
        logger.warning("Use --run-* option to actually execute measurement.")
        return

    ##########

    if args.run == 'dry':
        logger.warning("MEASUREMENT DRY RUN, use --run option to actually execute measurement")

    # ISO timestamp as measurement ID
    mset_id = _util.gen_timestamp()
    logger.info(f"measurement ID: {mset_id}")

    output_dir = os.path.join(CAL_MEASUREMENT_ROOT, mset_id)

    if args.run not in [None, 'dry']:
        if os.path.exists(output_dir):
            raise CMDError(f"output directory already exists: {output_dir}")
        os.makedirs(output_dir, exist_ok=False)
    logger.info(f"output directory: {output_dir}")

    # FIXME: check/verify IFO is in correct state for measurement:
    # e.g. ISC_LOCK == NLN_CAL_MEAS

    # FIXME: warning for thermalization status (less than an hour in
    # NLN)

    # FIXME: print expected measurement time
    # FIXME: progress bar?

    # FIXME: capture IFO config (EPICS/foton/etc) at measurement time

    ##########
    # loop over measurements
    for meas in mseq:
        logger.info("##########")

        measurement = measurements[meas]
        description = measurement['description']
        template_path = measurement['template']
        meas_timestamp = _util.gen_timestamp()
        output_path = os.path.join(
            output_dir,
            template_str_replace(os.path.basename(template_path), meas_timestamp),
        )

        logger.info(f"measurement: {meas}: {description} measurement")
        logger.info(f"measurement template: {template_path}")
        logger.info(f"measurement timestamp: {meas_timestamp}")
        logger.info(f"measurement output: {output_path}")

        if args.run not in [None, 'dry']:
            logger.info(f"executing {meas} measurement {args.run}...")

            # interactive running
            if args.run == 'interactive':
                tmp_path = output_path + '.tmp'
                shutil.copy(template_path, tmp_path)
                logger.warning("executing diaggui for interactive usage")
                logger.warning("save file to SAME PATH and exit to continue...")
                cmd = ['diaggui', tmp_path]
                logger.debug(cmd)
                subprocess.run(
                    cmd,
                )
                os.rename(tmp_path, output_path)

            # headless run
            elif args.run == 'headless':
                diag_run(template_path, output_path, dry=not args.run)

            # FIXME: somehow capture measurement errors

            logger.info(f"{meas} measurement complete.")
        else:
            continue

        # FIXME: validate the output somehow
        # FIXME: should we continue with the rest of the measurments
        # if there was an issue?

        if not os.path.exists(output_path):
            raise CMDError(f"output measurement file not found: {output_path}")
        logger.info(f"{meas} output: {output_path}")

    if args.run in [None, 'dry']:
        return

    # touch a file to indicate that all measurements were completed
    # successfully
    touch(os.path.join(output_dir, 'completed'))

    # touch a file to indicate that this measurement set corresponds
    # to a complete cal measurement set
    if mseq == default_measurement_sequence:
        touch(os.path.join(output_dir, 'full_measurement'))

    logger.info(f"all measurements complete: {output_dir}")
