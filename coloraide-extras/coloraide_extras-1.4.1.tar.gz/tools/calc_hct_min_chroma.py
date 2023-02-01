"""
Map our achromatic spline calculation against real achromatic response.

Report the delta between our spline and the real world. Also note the highest chroma climbs.
"""
import sys
import argparse
import os
import matplotlib.pyplot as plt

sys.path.insert(0, os.getcwd())

from coloraide_extras.everything import ColorAll as Color  # noqa: E402
from coloraide_extras.spaces.hct import HCT, xyz_to_hct, HCTAchromaTest  # noqa: E402


def main():
    """Main."""

    parser = argparse.ArgumentParser(
        prog='calc_hct_min_chroma.py',
        description='Calculate minimum chroma for achromatic colors in HCT and maps current spline against real values.'
    )
    # Flag arguments
    parser.add_argument(
        '--rgb', '-r', action='store', default='srgb', help="The RGB space which the color will be sized against."
    )
    parser.add_argument(
        '--res', '-s', type=int, default=50000, help="Resolution to use when calculating range, default is 10000."
    )
    args = parser.parse_args()

    return run(args.res)


def run(res):
    """Run."""

    test = HCTAchromaTest(HCT.ENV)

    color = Color('srgb', [0, 0, 0])
    points1 = {}
    points2 = {}
    diff = 0
    max_m = 0

    for i in range(res + 1):
        div = res / 5
        color.update('srgb', [i / div, i / div, i / div])
        xyz = color.convert('xyz-d65')
        m, l = xyz_to_hct(xyz[:-1], HCT.ENV)[1:]

        if m > max_m:
            max_m = m

        domain = test.scale(l)
        calc = test.spline(domain)

        delta = abs(calc[1] - m)
        if delta > diff:
            diff = delta

        points1[l] = m
        points2[calc[0]] = calc[1]

    print('Delta: ', diff)
    print('Max Chroma: ', max_m)

    l1 = []
    l2 = []
    m1 = []
    m2 = []
    for l in sorted(points1):
        l1.append(l)
        m1.append(points1[l])
    for l in sorted(points2):
        l2.append(l)
        m2.append(points2[l])

    figure = plt.figure()

    # Create axes
    ax = plt.axes(
        xlabel='C',
        ylabel='T'
    )
    ax.set_aspect('auto')
    ax.set_title('HCT: Delta = {} - Max C = {}'.format(diff, max_m))
    figure.add_axes(ax)

    # Print the calculated line against the real line
    plt.style.use('seaborn-v0_8-whitegrid')
    plt.plot(m1, l1, '.', color='black')
    plt.plot(m2, l2, '.', color='red', markersize=0.5)
    plt.show()

    return 0


if __name__ == "__main__":
    sys.exit(main())
