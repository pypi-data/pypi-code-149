import math
import scipy.constants

__all__ = ('calc_wavelength', 'calc_relativistic_correction', 'calc_interaction_constant')


# TODO: make constants tractable to CODATA version
PLANCK_CONSTANT_JS = scipy.constants.value("Planck constant")
ELECTRON_MASS_KG = scipy.constants.value("electron mass")
ELECTRON_MASS_EV = scipy.constants.value("electron mass energy equivalent in MeV") * 1e6
ELEMENTARY_CHARGE_C = scipy.constants.value("elementary charge")

# Constant to convert atom form factors from nm (as usually tabulated) to volt * nm^3
# i.e. FORMFACTOR_TO_VOLT_NM3 = h^2 / (2 pi m e)
FORMFACTOR_TO_VOLT_NM3 = PLANCK_CONSTANT_JS ** 2 / (2.0e-18 * math.pi * ELECTRON_MASS_KG * ELEMENTARY_CHARGE_C)


def calc_wavelength(voltage: float) -> float:
    """
    Calculate relativistically corrected wavelength from acceleration voltage.

    :param voltage: Acceleration voltage (kV)
    :returns: Electron wavelength (nm)
    :raises ValueError: If voltage is <= 0
    """
    voltage = 1e3 * float(voltage)
    if voltage <= 0.0:
        raise ValueError("Acceleration voltage must be positive.")
    # See de Graef, Introduction to conventional transmission electron microscopy (2003), page 92.
    pre = 1e9 * PLANCK_CONSTANT_JS / math.sqrt(2.0 * ELECTRON_MASS_KG * ELEMENTARY_CHARGE_C)
    return pre / math.sqrt(voltage + 0.5 / ELECTRON_MASS_EV * voltage**2)


def calc_relativistic_correction(voltage: float) -> float:
    """
    Calculate relativistic correction factor.

    .. math:
        \\gamma = 1 \\over \\sqrt{1 - v^2/c^2}

    :param voltage: Acceleration voltage (kV)
    :returns: Relativistic correction factor
    :raises ValueError: If voltage is < 0
    """
    voltage = 1e3 * float(voltage)
    if voltage < 0.0:
        raise ValueError("Acceleration voltage must be positive.")
    return 1.0 + voltage / ELECTRON_MASS_EV


def calc_interaction_constant(voltage: float) -> float:
    """
    Calculate relativistically corrected interaction constant.

    :param voltage: Acceleration voltage (kV)
    :returns: Interaction constant (1/Vnm).
    :raises ValueError: If voltage is <= 0
    """
    # See de Graef, Introduction to conventional transmission electron microscopy (2003), page 93.
    return calc_wavelength(voltage) * calc_relativistic_correction(voltage) / FORMFACTOR_TO_VOLT_NM3
