import os
import argparse
import datetime
import subprocess

import numpy as np
import corner
from scipy.signal import freqresp
from matplotlib import pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

from ._const import IFO
from . import _util
from ._util import logger
from . import report_utils as ru
from .measurement_set import MeasurementSet
from ..sensing import SensingModel
from ..plot import BodePlot


def find_closest_pcal(pcal_measurements, mfile):
    """find the closest pcal measurement to the given measurement file

    For each measurement file, the datetime of the measurement is
    extracted from the filename.  The closest pcal measurement and
    it's correspond datetime object are returned.

    """
    mtime = _util.measurement_extract_datetime(mfile)
    last = (None, abs(mtime - datetime.datetime(1, 1, 1)))
    for f in pcal_measurements:
        dt = _util.measurement_extract_datetime(f)
        diff = abs(dt - mtime)
        if diff < last[1]:
            last = (f, diff)
    return last


def run_sensing_MCMC(processedSensing, config, mset_id, C_ref, mset_dir):
    # Run the MCMC chain
    mcmcChains = np.transpose(
        processedSensing.run_mcmc(
            fmin=config['mcmc_fmin'],
            fmax=config['mcmc_fmax'],
            burn_in_steps=config['mcmc_burn_in'],
            steps=config['mcmc_steps'],
            save_chain_to_file=os.path.join(
                mset_dir, 'sensing_mcmc_chain.hdf5'),
            save_map_to_file=os.path.join(
                mset_dir, 'sensing_mcmc_map.json'),
        ))

    # Set up a dict of dicts to hold the mcmc parameter information
    mcmcParams = {
        'opticalGain': {
            'label': 'Optical gain, H_c (ct/m)',
            'mathlabel': r'$H_C$'},
        'cavityPole': {
            'label': 'Cavity_pole, f_cc (Hz)',
            'mathlabel': r'$f_{cc}$'},
        'springF': {
            'label': 'Detuned SRC spring frequency, f_s (Hz)',
            'mathlabel': r'$f_s$'},
        'springQ': {
            'label': 'Detuned SRC spring quality factor, Q_s',
            'mathlabel': r'$Q$'},
        'resDelay': {
            'label': 'Residual time delay, tau_c (s)',
            'mathlabel': r'$\Delta\tau_C$'},
    }

    # Set up the quantile levels
    quantileLevels = np.array([0.16, 0.5, 0.84])

    # Loop over params and store relevant information into the dict
    for i, param in enumerate(mcmcParams.values()):
        quantiles = corner.quantile(
            mcmcChains[i],
            quantileLevels)
        param['median'] = quantiles[1]
        param['errplus'] = quantiles[2]-quantiles[1]
        param['errminus'] = quantiles[1]-quantiles[0]
        param['quantiles'] = quantiles

    if mcmcParams['resDelay']['median'] >= 5e-3:  # TODO: make user arg
        logger.info(
            "Warning: MCMC fit for residual delay is high"
            f" at {mcmcParams['resDelay']['median']:.2f} s")

    # Make corner plot
    corner_fig = ru.make_corner_plot(
        mcmcChains, mcmcParams, quantileLevels,
        os.path.join(
            mset_dir,
            "sensing_mcmc_corner.png"),
        f"{mset_id} sensing function\nMCMC corner plot")

    # Add additional entry for kappa_c so that values can be printed
    mcmcParams['kappa_c'] = {
        'label': 'kappa_c',
        'mathlabel': r'$kappa_c$'
    }

    for key in ['median', 'errplus', 'errminus', 'quantiles']:
        mcmcParams['kappa_c'][key] = (
            mcmcParams['opticalGain'][key]
            / C_ref.coupled_cavity_optical_gain)

    # Print out and parameter value table
    mcmcTableQuant, mcmcTablePM = ru.print_mcmc_params(mcmcParams, quantileLevels)
    if config['mcmc_print']:
        logger.info(f"\n{mcmcTableQuant}")
        logger.info(f"\n{mcmcTablePM}\n")

    return mcmcParams, mcmcTableQuant, mcmcTablePM, corner_fig


def run_actuation_MCMC(
        processed_actuation, config, mset_id, stage, gain_units, gain_to_NpCt_factor, mset_dir):
    # TODO write proper doc string
    # Run the MCMC chain
    mcmcChains = np.transpose(
        processed_actuation.run_mcmc(
            fmin=config['mcmc_fmin'],
            fmax=config['mcmc_fmax'],
            burn_in_steps=config['mcmc_burn_in'],
            steps=config['mcmc_steps'],
            save_chain_to_file=os.path.join(
                mset_dir, f'actuation_{stage}_mcmc_chain.hdf5'),
            save_map_to_file=os.path.join(
                mset_dir, f'actuation_{stage}_mcmc_map.json'),
        ))

    # Set up a dict of dicts to hold the mcmc parameter information
    mcmcParams = {
        'gainNpDriveOutUnits': {
            'label': f'Gain, H_A ({gain_units})',
            'mathlabel': r'$H_A$'+f' ({gain_units})'},
        'resDelay': {
            'label': 'Residual time delay, tau_c (s)',
            'mathlabel': r'$\Delta\tau_C$'},
    }

    # Set up the quantile levels
    quantileLevels = np.array([0.16, 0.5, 0.84])

    # Loop over params and store relevant information into the dict
    for i, param in enumerate(mcmcParams.values()):
        quantiles = corner.quantile(
            mcmcChains[i],
            quantileLevels)
        param['median'] = quantiles[1]
        param['errplus'] = quantiles[2]-quantiles[1]
        param['errminus'] = quantiles[1]-quantiles[0]
        param['quantiles'] = quantiles

    if mcmcParams['resDelay']['median'] >= 5e-3:  # TODO: make user arg
        logger.info(
            "Warning: MCMC fit for residual delay is high"
            f" at {mcmcParams['resDelay']['median']:.2f} s")

    # Make corner plot
    corner_fname = f"actuation_{stage}_mcmc_corner.png"
    corner_title = f"{mset_id} {stage} actuation function\nMCMC corner plot"
    corner_fig = ru.make_corner_plot(mcmcChains,
                                     mcmcParams, quantileLevels,
                                     os.path.join(mset_dir, corner_fname),
                                     corner_title)

    # Add additional entry for gain in physical units so it can be printed
    mcmcParams['gainNpCt'] = {
        'label': 'Gain, H_A (N/ct)',
        'mathlabel': r'$H_A$ (N/ct)'
    }

    for key in ['median', 'errplus', 'errminus', 'quantiles']:
        mcmcParams['gainNpCt'][key] = (
            mcmcParams['gainNpDriveOutUnits'][key]
            * gain_to_NpCt_factor)

    # Print out and parameter value table
    mcmcTableQuant, mcmcTablePM = ru.print_mcmc_params(mcmcParams, quantileLevels)

    if config['mcmc_print']:
        logger.info(f"\n{mcmcTableQuant}")
        logger.info(f"\n{mcmcTablePM}\n")

    return mcmcParams, mcmcTableQuant, mcmcTablePM, corner_fig


def actuation(mset):
    """generate actuation function MCMC and plots

    """
    # TODO: write proper docstring
    logger.info("generating actuation report...")

    ifo = mset.model.name
    A_ref = mset.model.actuation

    # Format the reference model date and the filename
    # ref_tag = ru.extract_date_general(model_ini).strftime("%Y-%m-%d")
    ref_tag = ''
    subtitle_text = (
        f"All fixed parameters are drawn from"
        f" {os.path.basename(mset.model_ini)}")

    # Set up common title names
    tfp_title = "Actuation strength transfer functions"
    rp_title = "Actuation strength residuals"
    sp_titlesize = 12

    # figure list to return
    figs = []
    # process by actuator stage
    for stage in ['L1', 'L2', 'L3']:

        config = mset.config['Actuation'][stage]
        processed_actuation = mset.processed_measurements[f'Actuation/{stage}']

        # main figure
        plt.clf()
        # TODO: with multiple figs created here, choose better var names
        fig = plt.figure()
        fig.suptitle(
            f"{ifo}SUS{config['optic']}"
            f" {stage} actuation model history\n",
            fontsize=20)
        fig.text(
            .5, .93,
            subtitle_text,
            horizontalalignment='center',
            transform=fig.transFigure)

        # transfer function plot (comparison)
        # TODO: replace figure vars (tfp & rp) below with better names
        tfp = BodePlot(fig=fig, spspec=[221, 223])
        tfp.ax_mag.set_title(tfp_title, fontsize=sp_titlesize)

        # residuals plot (comparison)
        rp = BodePlot(fig=fig, spspec=[222, 224])
        rp.ax_mag.set_title(rp_title, fontsize=sp_titlesize)

        # In order to be generic and allow for both arms as actuators,
        # A has methods for xarm and yarm. But, if I'm only using one arm's
        # actuator, then I can reduce the complexity (and simplify later
        # code) by extract the layer of method I need and naming it generically
        if config['optic'] == 'ETMX':
            A_ref_arm = A_ref.xarm
        else:
            A_ref_arm = A_ref.yarm

        # gain_units, gain_to_NpCt_factor
        if stage == 'L1':
            ref_actuator_strength_param = abs(A_ref_arm.uim_npa)
            gain_to_NpCt_factor = abs(
                A_ref_arm.uim_dc_gain_Apct())
            gain_units = 'N/A'
        elif stage == 'L2':
            ref_actuator_strength_param = abs(A_ref_arm.pum_npa)
            gain_to_NpCt_factor = abs(
                A_ref_arm.pum_dc_gain_Apct())
            gain_units = 'N/A'
        else:
            ref_actuator_strength_param = abs(A_ref_arm.tst_npv2)
            gain_to_NpCt_factor = abs(
                A_ref_arm.tst_dc_gain_V2pct())
            gain_units = 'N/V**2'

        # Loop over measurement dates/times
        # for im, measXMLpair in enumerate(sensing_xml_pairs):
        if True:
            im = 0

            # Get the common frequency axis and measurement info
            frequencies, meas_actuator_strength, meas_actuator_strength_unc = \
                processed_actuation.get_processed_measurement_response()

            ref_actuator_strength = ref_actuator_strength_param * np.ones(
                frequencies.shape)

            if im == 0:

                # Select scaling for the plot
                expscale = int(np.floor(np.log10(ref_actuator_strength_param)))
                scale = 10**expscale
                tfp.ax_mag.set_ylabel(f'Magnitude x $10^{{{expscale}}}$')

                # Add reference model curve
                tfp.plot(frequencies, ref_actuator_strength/scale,
                         label=f"{ref_tag} model")

                # Add a null curve to keep the color-coding consistent
                # to the residuals plot
                rp.plot([], [])

            if (im == 0 and config['mcmc_mode'] in ['latest', 'all']):

                mcmcParams, mcmcTableQuant, mcmcTablePM, corner_fig = run_actuation_MCMC(
                    processed_actuation,
                    config,
                    mset.id,
                    stage,
                    gain_units,
                    gain_to_NpCt_factor,
                    mset.path,
                )
                figs.append(corner_fig)

                mcmc_actuator_strength = mcmcParams['gainNpDriveOutUnits']['median'] * np.exp(
                    -2*np.pi*1j*mcmcParams['resDelay']['median']*frequencies)

                fig_mcmc = plt.figure(figsize=(10, 10))
                fig_mcmc.suptitle(
                    f"{ifo}SUS{config['optic']} {stage} "
                    "actuation model MCMC summary\n",
                    fontsize=20)
                fig_mcmc.text(
                    .5, .93,
                    subtitle_text,
                    in_layout=True,
                    horizontalalignment='center',
                    transform=fig_mcmc.transFigure)

                tfp_mcmc = BodePlot(fig=fig_mcmc, spspec=[221, 223])
                tfp_mcmc.ax_mag.set_title(tfp_title, fontsize=sp_titlesize)
                tfp_mcmc.ax_mag.set_ylabel(f'Magnitude x $10^{{{expscale}}}$')
                rp_mcmc = BodePlot(fig=fig_mcmc, spspec=[222, 224])
                rp_mcmc.ax_mag.set_title(rp_title, fontsize=sp_titlesize)

                # Add the curves to the plot
                tfp_mcmc.plot(
                    frequencies,
                    ref_actuator_strength/scale,
                    label=(
                        "Model w free params from\n "
                        f"{os.path.basename(mset.model_ini)}"))
                tfp_mcmc.plot(
                    frequencies,
                    mcmc_actuator_strength/scale,
                    label=f"Model w free params from\n MCMC fit to {mset.id} data")
                tfp_mcmc.error(
                    frequencies,
                    meas_actuator_strength/scale,
                    meas_actuator_strength_unc,
                    label=f"{mset.id} measurement",
                    fmt='.')

                rp_mcmc.error(
                    frequencies,
                    meas_actuator_strength/mcmc_actuator_strength,
                    meas_actuator_strength_unc,
                    label=(
                        f"{mset.id} meas / model w free params\n"
                        f" from {os.path.basename(mset.model_ini)}"),
                    fmt='.')
                rp_mcmc.error(
                    frequencies,
                    meas_actuator_strength/ref_actuator_strength,
                    meas_actuator_strength_unc,
                    label=(
                        f"{mset.id} meas / model w free params\n"
                        f" from {os.path.basename(mset.model_ini)}"),
                    fmt='.')

                legends = []
                # Add vertical lines marking the fit range for the MCMC
                for p in [tfp_mcmc, rp_mcmc]:
                    p.vlines(
                        config['mcmc_fmin'], color='k', lw=2,
                        label=f"Fit range {config['mcmc_fmin']} to"
                        f" {config['mcmc_fmax']} Hz")
                    p.vlines(config['mcmc_fmax'], color='k', lw=2)
                    # Add legends
                    leg = p.ax_mag.legend(
                        bbox_to_anchor=(0, 1.1),
                        loc='lower left',
                        bbox_transform=p.ax_mag.transAxes)
                    legends += [leg]

                fig_mcmc.tight_layout()
                tbox = fig_mcmc.text(
                    .5, 0,
                    "\n"*6+mcmcTablePM+"\n",
                    fontfamily='monospace',
                    horizontalalignment='center',
                    verticalalignment='bottom',
                    transform=fig_mcmc.transFigure,
                )

                text_bbox = tbox.get_tightbbox()
                text_height = text_bbox.y1-text_bbox.y0
                fig_height = fig_mcmc.get_size_inches()[1]*fig_mcmc.dpi
                adjust_fraction = (text_height)/fig_height
                fig_mcmc.subplots_adjust(bottom=adjust_fraction)
                fig_mcmc.savefig(
                    os.path.join(
                        mset.path,
                        f"actuation_{stage}_mcmc_compare.png"),
                )
                figs.append(fig_mcmc)

            # Add meas curves to transfer function comparison plots
            tfp.error(
                frequencies,
                meas_actuator_strength/scale,
                meas_actuator_strength_unc,
                label=f"{mset.id} measurement",
                fmt='.')

            # Add meas curves to residuals plot
            rp.error(
                frequencies,
                meas_actuator_strength/ref_actuator_strength,
                meas_actuator_strength_unc,
                label=(
                    f"{mset.id} meas / model w free params\n"
                    f" from {os.path.basename(mset.model_ini)}"),
                fmt='.')

        # Add legends
        for p in [tfp, rp]:
            p.legend(
                bbox_to_anchor=(0, 1.1),
                loc='lower left',
                bbox_transform=p.ax_mag.transAxes)

        # Wrap up and save figure
        fig.tight_layout()
        fig.savefig(
            os.path.join(
                mset.path,
                f"actuation_{stage}_tf_history.png"))
        figs.append(fig)
    return figs


def sensing(mset):
    """generate sensing function MCMC and plots

    """
    # TODO: write proper docstring
    logger.info("generating sensing report...")

    ifo = mset.model.name
    config = mset.config['Sensing']
    processed_sensing = mset.processed_measurements['Sensing']

    # Format the reference model date and filename
    # refDateTag = ru.extract_date_general(model_ini).strftime("%Y-%m-%d")
    refDateTag = ''
    subtitleText = (f"All fixed parameters are drawn from"
                    f" {os.path.basename(mset.model_ini)}")

    # Set up common title names
    tfp_title = "Optical response transfer functions"
    rp_title = "Optical response residuals"
    sp_titlesize = 12

    # === Plotting setup

    # main figure
    plt.clf()
    fig = plt.figure()
    fig.suptitle(f"{ifo} sensing model history\n", fontsize=20)
    fig.text(
        .5, .93,
        subtitleText,
        horizontalalignment='center',
        transform=fig.transFigure)

    # transfer function plot (comparison)
    tfp = BodePlot(fig=fig, spspec=[221, 223])
    tfp.ax_mag.set_title(tfp_title, fontsize=sp_titlesize)

    # residuals plot (comparison)
    rp = BodePlot(fig=fig, spspec=[222, 224])
    rp.ax_mag.set_title(rp_title, fontsize=sp_titlesize)

    # figure list to return
    figs = [fig]

    # Create reference sensing model
    C_ref = SensingModel(mset.model_ini)

    # Get the common frequency axis and measurement info
    frequencies, measOpticalResponse, measOpticalResponseUnc = \
        processed_sensing.get_processed_measurement_response()

    angular_frequencies = 2*np.pi*frequencies

    # Compute the optical response based on reference parameters
    # Note: this reference optical response needs to be computed for
    # each measurement pair despite the fact that it is only plotted
    # once. This is because the frequency axis could differ between
    # measurements, and `refOpticalResponse` must divide the measurement
    # in order to generate the residuals plot.

    refNormOpticalResponse = freqresp(
        SensingModel.optical_response(
            C_ref.coupled_cavity_pole_frequency,
            C_ref.detuned_spring_frequency,
            C_ref.detuned_spring_q,
            C_ref.is_pro_spring),
        angular_frequencies)[1]

    refOpticalResponse = refNormOpticalResponse * \
        C_ref.coupled_cavity_optical_gain

    # If this is the first measurement, we need to compute the
    # reference model response. (This can't be done ahead of time
    # because it relies on the common frequency axis)
    # If requested, we will also run the MCMC on this first measurement.
    im = 0
    if im == 0:

        # Select scaling for the plot
        expscale = int(np.floor(np.log10(C_ref.coupled_cavity_optical_gain)))
        tfp.ax_mag.set_ylabel(f'Magnitude (ct/m) x $10^{{{expscale}}}$')
        scale = 10**expscale

        # Add reference model curve
        tfp.plot(frequencies, refOpticalResponse/scale, label=f"{refDateTag} model")

        # Add a null curve to keep the color-coding consistent on the residuals plot
        rp.plot([], [])

    # If requested, run the MCMC at this point
    fig_mcmc = None
    if (im == 0 and config['mcmc_mode'] == 'latest') \
       or config['mcmc_mode'] == 'all':

        # Run, return parameters, and create corner plot
        mcmcParams, mcmcTableQuant, mcmcTablePM, corner_fig = run_sensing_MCMC(
            processed_sensing,
            config,
            mset.id,
            C_ref,
            mset.path,
        )
        figs.append(corner_fig)

        # Compute the optical response based on MCMC parameters
        mcmcNormOpticalResponse = freqresp(
            SensingModel.optical_response(
                mcmcParams['cavityPole']['median'],
                mcmcParams['springF']['median'],
                mcmcParams['springQ']['median'],
                C_ref.is_pro_spring),
            angular_frequencies)[1]

        mcmcOpticalResponse = mcmcNormOpticalResponse * \
            mcmcParams['opticalGain']['median'] * \
            np.exp(
                -2*np.pi*1j*mcmcParams['resDelay']['median'] *
                frequencies)

        # We need an additional figure for the MCMC results comparison.
        # Setup is in the same format as the multi-measurement comparison.
        fig_mcmc = plt.figure(figsize=(10, 10))
        fig_mcmc.suptitle(f"{ifo} sensing model MCMC summary\n", fontsize=20)
        fig_mcmc.text(
            .5, .93,
            subtitleText,
            in_layout=True,
            horizontalalignment='center',
            transform=fig_mcmc.transFigure)

        tfp_mcmc = BodePlot(fig=fig_mcmc, spspec=[221, 223])
        tfp_mcmc.ax_mag.set_title(tfp_title, fontsize=sp_titlesize)
        tfp_mcmc.ax_mag.set_ylabel(f'Magnitude (ct/m) x $10^{{{expscale}}}$')
        rp_mcmc = BodePlot(fig=fig_mcmc, spspec=[222, 224])
        rp_mcmc.ax_mag.set_title(rp_title, fontsize=sp_titlesize)

        # Add the curves to the plot
        tfp_mcmc.plot(
            frequencies,
            refOpticalResponse/scale,
            label=f"Model w free params from\n {os.path.basename(mset.model_ini)}")
        tfp_mcmc.plot(
            frequencies,
            mcmcOpticalResponse/scale,
            label=f"Model w free params from\n MCMC fit to {mset.id} data")
        tfp_mcmc.error(
            frequencies,
            measOpticalResponse/scale,
            measOpticalResponseUnc,
            label=f"{mset.id} measurement / C_R",
            fmt='.')

        rp_mcmc.error(
            frequencies,
            measOpticalResponse/mcmcOpticalResponse,
            measOpticalResponseUnc,
            label=(
                f"{mset.id} meas / model w free params\n"
                f" from {os.path.basename(mset.model_ini)}"),
            fmt='.')
        rp_mcmc.error(
            frequencies,
            measOpticalResponse/refOpticalResponse,
            measOpticalResponseUnc,
            label=(
                f"{mset.id} meas / model w free params\n"
                f" from {os.path.basename(mset.model_ini)}"),
            fmt='.')

        legends = []
        # Add vertical lines marking the fit range for the MCMC
        for p in [tfp_mcmc, rp_mcmc]:
            p.vlines(
                config['mcmc_fmin'], color='k', lw=2,
                label=f"Fit range {config['mcmc_fmin']} to"
                f" {config['mcmc_fmax']} Hz")
            p.vlines(config['mcmc_fmax'], color='k', lw=2)
            # Add legends
            leg = p.ax_mag.legend(
                bbox_to_anchor=(0, 1.1),
                loc='lower left',
                bbox_transform=p.ax_mag.transAxes)
            legends += [leg]

        fig_mcmc.tight_layout()
        tbox = fig_mcmc.text(
            .5, 0,
            "\n"*6+mcmcTablePM+"\n",
            fontfamily='monospace',
            horizontalalignment='center',
            verticalalignment='bottom',
            transform=fig_mcmc.transFigure,
        )

        text_bbox = tbox.get_tightbbox()
        text_height = text_bbox.y1-text_bbox.y0
        fig_height = fig_mcmc.get_size_inches()[1]*fig_mcmc.dpi
        adjust_fraction = (text_height)/fig_height
        fig_mcmc.subplots_adjust(bottom=adjust_fraction)
        fig_mcmc.savefig(
            os.path.join(
                mset.path,
                "sensing_mcmc_compare.png"),
        )
        figs.append(fig_mcmc)

    # Add meas curves to transfer function comparison plots
    tfp.error(
        frequencies,
        measOpticalResponse/scale,
        measOpticalResponseUnc,
        label=f"{mset.id} measurement / C_R",
        fmt='.')

    # Add meas curves to residuals plot
    rp.error(
        frequencies,
        measOpticalResponse/refOpticalResponse,
        measOpticalResponseUnc,
        label=(
            f"{mset.id} meas / model w free params\n"
            f" from {os.path.basename(mset.model_ini)}"),
        fmt='.')

    # Add legends
    for p in [tfp, rp]:
        p.legend(
            bbox_to_anchor=(0, 1.1),
            loc='lower left',
            bbox_transform=p.ax_mag.transAxes)

    # Wrap up and save figure
    fig.tight_layout()
    fig.savefig(
        os.path.join(
            mset.path,
            "sensing_tf_history.png"))
    return figs


class ReportPDF:

    def __init__(self, path):
        self.path = path

    def __enter__(self):
        self.pdf = PdfPages(self.path)
        return self

    def add_figure(self, new_fig):
        if hasattr(new_fig, '__iter__'):
            for f in new_fig:
                self.pdf.savefig(f)
        else:
            self.pdf.savefig(new_fig)

    def __exit__(self, exception_type, exception_value, traceback):
        self.pdf.close()
        # remove the report if there was an exception, so that we
        # don't leave around a malformed report.
        # FIXME: confirm this is what we want
        if exception_type is not None:
            os.unlink(self.path)
        return False


def add_args(parser):
    parser.add_argument(
        'mset_id', metavar='MSET_ID', nargs='?',
        help="measurement set ID to view/process, or last measurement set if not specified")
    _util.add_model_option(parser)
    _util.add_config_option(parser)
    parser.add_argument(
        '--force', action='store_true',
        help="force generate report if it already exists")
    parser.add_argument(
        '--display', action=argparse.BooleanOptionalAction, default=True,
        help="display report after generation or not (display by default)")


def main(args):
    """generate full calibration report

    """
    mset = MeasurementSet(args.mset_id, args.config)
    logger.info(f"measurement set: {mset.id}")

    report_file = os.path.join(
        mset.path,
        f"{IFO}_calibration_report_{args.mset_id}.pdf",
    )

    if not os.path.exists(report_file) or args.force:
        if os.path.exists(report_file):
            value = input(f"Really regenerate report for measurement set {mset.id} [Y|n]? ")
            if value.upper() not in ['Y', '']:
                logger.info("aborting.")
                return
        logger.info(f"generating report for {mset.id}...")
        mset.load_model(args.model)
        with ReportPDF(report_file) as report:
            report.add_figure(sensing(mset))
            report.add_figure(actuation(mset))
        logger.info("report generation complete.")

    if args.display:
        logger.info(f"displaying report {report_file}")
        # FIXME: make viewer this configurable
        subprocess.run(['evince', '-w', report_file])
