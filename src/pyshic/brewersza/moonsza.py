import math
from datetime import datetime

def moonsza(T0, LO, jday, YE):
    """
    Calculate the moon's position (right ascension and declination) based on time, longitude, Julian day, and year.

    Args:
        T0 (float): Time in minutes past midnight or MATLAB serial date number.
        LO (float): Longitude (degrees).
        jday (int): Julian day.
        YE (int): Year.

    Returns:
        RA (float): Right ascension (degrees).
        A (float): Declination (degrees).
    """
    P0 = math.pi / 180  # Degree to radian conversion factor
    

    # Calculate lunar position
    TT = (YE - 84) * 365 + int((YE - 80) / 4)
    if jday < 3 and YE % 4 == 0:
        TT -= 1

    TT = (TT - 5845.5 + jday + T0 / 1440) / 36525
    T2 = TT ** 2
    T3 = T2 * TT
    E = (84381.448 - 46.815 * TT - 0.00059 * T2 + 0.001813 * T3) / 3600
    C = fun1(36000.7701, TT)
    DT = 100.460618 + C + (0.093104 * T2 - 0.0000062 * T3) / 240 + T0 / 4
    DT %= 360
    LB = 218.32 + fun1(481267.883, TT)
    LB += 6.29 * math.sin((134.9 + fun1(477198.85, TT)) * P0)
    # Continue adding LB adjustments as in the original MATLAB code...

    # Calculate right ascension (RA) and declination (A)
    # Placeholder for these calculations; follow the MATLAB implementation
    RA = 0  # Placeholder calculation
    A = 0  # Placeholder calculation

    return RA, A

def fun1(C, TT):
    """
    Auxiliary function for lunar position calculation.

    Args:
        C (float): Constant used in the calculation.
        TT (float): Time in Julian centuries since J2000.0.

    Returns:
        float: Adjusted value based on C and TT.
    """
    return C * (TT - int(TT * C / 360) * 360 / C)

