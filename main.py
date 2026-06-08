from eos import *
from tov import calculate_pressure_plot
from plotting import render_plot


def start_calc():

    finalPlotValues = []

    finalPlotValues.append(
        calculate_pressure_plot(h_MDI2_func, Q=1)
    )

    finalPlotValues.append(
        calculate_pressure_plot(h_Sk14_func, Q=1)
    )

    finalPlotValues.append(
        calculate_pressure_plot(h_SCVBB_func, Q=1)
    )

    finalPlotValues.append(
        calculate_pressure_plot(h_W_func, Q=1)
    )

    finalPlotValues.append(
        calculate_pressure_plot(h_DH_func, Q=1)
    )

    finalPlotValues.append(
        calculate_pressure_plot(h_APR1_func, Q=1)
    )

    render_plot(finalPlotValues)


if __name__ == "__main__":
    start_calc()
