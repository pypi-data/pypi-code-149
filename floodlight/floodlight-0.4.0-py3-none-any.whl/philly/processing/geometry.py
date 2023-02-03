import numpy as np


def point_in_zone(point, zone, direction, pitch, tolerance=0):
    """Checks whether a 2D point is in a specific zone.

    Parameters
    ----------
    point: Tuple(float)
    zone: str
        From ["opp_penalty_area", "opp_box", "attacking_third", "medium_third",
        "defensive_third", "attacking_half", "defensive_half"]
    direction: str
        Playing direction, "lr" or "rl"
    pitch: Pitch
    tolerance: float, optional
        Spatial error tolerance, in meter. Defaults to 0 (sharp boundaries).

    Returns
    -------
    in_zone: Bool,
        Returns True if point is in zone, else False.
    """
    # params
    x, y = point
    xmin, xmax = pitch.xlim
    ymin, ymax = pitch.ylim
    length = abs(xmin) + abs(xmax)                    # differs in 2S from pitch.length
    width = abs(ymin) + abs(ymax)
    length_one_third = np.round(length/3, 3)
    zone_minimum_x, zone_maximum_x = None, None
    zone_minimum_y, zone_maximum_y = None, None

    # cases - define x and y boundaries
    if zone == "opp_penalty_area" or zone == "opp_box":
        if direction == "rl":
            zone_minimum_x = xmin
            zone_maximum_x = xmin + 16.5
            zone_minimum_y = pitch.center[1] - 20.16
            zone_maximum_y = pitch.center[1] + 20.16
        elif direction == "lr":
            zone_minimum_x = xmax - 16.5
            zone_maximum_x = xmax
            zone_minimum_y = pitch.center[1] - 20.16
            zone_maximum_y = pitch.center[1] + 20.16
    elif zone == "attacking_third":
        if direction == "lr":
            zone_minimum_x = xmax - length_one_third
            zone_maximum_x = xmax
            zone_minimum_y = ymin
            zone_maximum_y = ymax
        elif direction == "rl":
            zone_minimum_x = xmin
            zone_maximum_x = xmin + length_one_third
            zone_minimum_y = ymin
            zone_maximum_y = ymax
    elif zone == "middle_third":
        zone_minimum_x = xmin + length_one_third
        zone_maximum_x = xmax - length_one_third
        zone_minimum_y = ymin
        zone_maximum_y = ymax
    elif zone == "defensive_third":
        if direction == "lr":
            zone_minimum_x = xmin
            zone_maximum_x = xmin + length_one_third
            zone_minimum_y = ymin
            zone_maximum_y = ymax
        elif direction == "rl":
            zone_minimum_x = xmax - length_one_third
            zone_maximum_x = xmax
            zone_minimum_y = ymin
            zone_maximum_y = ymax
    elif zone == "attacking_half":
        if direction == "lr":
            zone_minimum_x = pitch.center[0]
            zone_maximum_x = xmax
            zone_minimum_y = ymin
            zone_maximum_y = ymax
        elif direction == "rl":
            zone_minimum_x = xmin
            zone_maximum_x = pitch.center[0]
            zone_minimum_y = ymin
            zone_maximum_y = ymax
    elif zone == "defensive_half":
        if direction == "lr":
            zone_minimum_x = xmin
            zone_maximum_x = pitch.center[0]
            zone_minimum_y = ymin
            zone_maximum_y = ymax
        elif direction == "rl":
            zone_minimum_x = pitch.center[0]
            zone_maximum_x = xmax
            zone_minimum_y = ymin
            zone_maximum_y = ymax
    elif zone == "green_zone":
        if direction == "lr":
            pass
        elif direction == "rl":
            pass

    else:
        raise ValueError(f"Unknown zone '{zone}'")

    if (
            (zone_minimum_x - tolerance) <= x <= (zone_maximum_x + tolerance)
    ) & (
            (zone_minimum_y - tolerance) <= y <= (zone_maximum_y + tolerance)
    ):
        in_zone = True
    else:
        in_zone = False

    return in_zone


def number_of_players_between_point_and_goal(xy, ball, t):
    if xy.direction == 'lr':
        nopbpag = sum(xy.x[t] < ball.x[t])
    elif xy.direction == 'rl':
        nopbpag = sum(xy.x[t] > ball.x[t])

    return nopbpag


def angle_between(at_x, at_y, to_x, to_y):
    """Determines the angle between a vector from (at_x, at_y) to (to_x, to_y) and the
    vector (1, 0) in degrees. Result is the (mathematical) angle in Euclidean
    coordinates (running counterclockwise from the x-axis). Angles with negative
    y-values (> 180 degrees) are negative.

    Casts the given vector into a complex number and then uses the numpy.angle() method.
    """
    x = to_x - at_x
    y = to_y - at_y
    complex = x + y * 1j
    angle = np.angle(complex, deg=True)

    return angle


def vector_in_zone(at, to, zone, direction, tolerance=0):
    """Checks whether a 2D vector (e.g. a pass) is in a specific zone.

    Parameters
    ----------
    at: Tuple(float)
        Start location of vector.
    to: Tuple(float)
        End location of vector.
    zone: str
        From ["strictly_forward"]
    direction: str
        Playing direction, "lr" or "rl"
    tolerance: float, optional
        Angular error tolerance, in degrees. Defaults to 0 (sharp boundaries).

    Returns
    -------
    in_zone: Bool,
        Returns True if point is in zone, else False.
    """
    # params
    angle = abs(angle_between(at[0], at[1], to[0], to[1]))
    zone_minimum, zone_maximum = None, None

    # cases - define angular boundaries
    if zone == "strictly_forward":
        if direction == "lr":
            zone_minimum = 0
            zone_maximum = 60
        elif direction == "rl":
            zone_minimum = 120
            zone_maximum = 180

    else:
        raise ValueError(f"Unknown zone '{zone}'")

    if (zone_minimum - tolerance) <= angle <= (zone_maximum + tolerance):
        in_zone = True
    else:
        in_zone = False

    return in_zone


