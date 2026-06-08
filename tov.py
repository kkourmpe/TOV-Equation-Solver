import numpy as np

from constants import (
    r_values,
    num_points,
    step
)

from eos import (
    h_crust1,
    h_crust2,
    h_crust3
)

def tov_equations(r, u, h_func):
    P, m = u
    h = h_func(P)

    # Check for division by zero
    if r == 0 or h == 0 or m == 0:
        dP_dr = 0.0
        dm_dr = 0.0
    else:
        dP_dr = -1.474 * h * m / (r**2) * (1 + P / h) * (1 + 11.2e-6 * (r**3) * P / m) * (1 - 2.948 * m / r)**(-1)
        dm_dr = 11.2e-6 * (r**2) * h

    return [dP_dr, dm_dr]

# Note: The Q flag controls the crust. Q=1 means that the code is using the crust EOS inluded in the code. If you are using e.g. a quark or a unified crust EOS then set Q=-1.

def solve_runge_kutta(P0, h_func, Q):
    m0 = 1.0e-10  #Avoid division by zero
    P = P0
    m = m0

# Runge-Kutta 4th order
    for i in range(1, num_points):
        r = r_values[i]
        u = [P, m]

        if Q<0:
            if P > 1e-11:
                k1 = np.multiply(step, tov_equations(r, u, h_func))
                k2 = np.multiply(step, tov_equations(r + 0.5 * step, np.add(u, 0.5 * k1), h_func))
                k3 = np.multiply(step, tov_equations(r + 0.5 * step, np.add(u, 0.5 * k2), h_func))
                k4 = np.multiply(step, tov_equations(r + step, np.add(u, k3), h_func))

            else:
                # Pressure is zero or negative
                return [r, m]

        if Q>0:
            if P >= 0.184:
                k1 = np.multiply(step, tov_equations(r, u, h_func))
                k2 = np.multiply(step, tov_equations(r + 0.5 * step, np.add(u, 0.5 * k1), h_func))
                k3 = np.multiply(step, tov_equations(r + 0.5 * step, np.add(u, 0.5 * k2), h_func))
                k4 = np.multiply(step, tov_equations(r + step, np.add(u, k3), h_func))

            elif P > 9.34375e-5:
                k1 = np.multiply(step, tov_equations(r, u, h_crust1))
                k2 = np.multiply(step, tov_equations(r + 0.5 * step, np.add(u, 0.5 * k1), h_crust1))
                k3 = np.multiply(step, tov_equations(r + 0.5 * step, np.add(u, 0.5 * k2), h_crust1))
                k4 = np.multiply(step, tov_equations(r + step, np.add(u, k3), h_crust1))

            elif P > 4.1725e-8:
                k1 = np.multiply(step, tov_equations(r, u, h_crust2))
                k2 = np.multiply(step, tov_equations(r + 0.5 * step, np.add(u, 0.5 * k1), h_crust2))
                k3 = np.multiply(step, tov_equations(r + 0.5 * step, np.add(u, 0.5 * k2), h_crust2))
                k4 = np.multiply(step, tov_equations(r + step, np.add(u, k3), h_crust2))

            elif P > 1e-11 :
                k1 = np.multiply(step, tov_equations(r, u, h_crust3))
                k2 = np.multiply(step, tov_equations(r + 0.5 * step, np.add(u, 0.5 * k1), h_crust3))
                k3 = np.multiply(step, tov_equations(r + 0.5 * step, np.add(u, 0.5 * k2), h_crust3))
                k4 = np.multiply(step, tov_equations(r + step, np.add(u, k3), h_crust3))

            else:
                # Pressure is zero or negative
                return [r, m]


        u_new = np.add(u, (k1 + 2.0 * k2 + 2.0 * k3 + k4) / 6.0)

        P, m = u_new

    return [r, m]

# Iterate over a range of initial central pressures

def calculate_pressure_plot(h_func, Q):
    M_values = []
    R_values = []

    samplesCount = 25
    cP = np.geomspace(1,1000,samplesCount)
    print("Calculating values")

    for i, P0 in enumerate(cP):
        rAndM = solve_runge_kutta(P0, h_func, Q)
        if rAndM != None:
            R_values.append(rAndM[0])
            M_values.append(rAndM[1])
    return [R_values, M_values]
