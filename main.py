import psychrolib
import matplotlib.pyplot as plt
import numpy as np
from psychrochart import PsychroChart
psychrolib.SetUnitSystem(psychrolib.SI)
pressure = 101325
custom_style = {
    "figure": {
        "title": "Psychrometric Chart (sea level)",
        "x_label": "DRY-BULB TEMPERATURE, $°C$",
        "y_label": "HUMIDITY RATIO $w, g_w \ kg_{da}$",
        "x_axis": {"color": [0.0, 0.0, 0.0], "linewidth": 1.5, "linestyle": "-"},
        "x_axis_labels": {"color": [0.0, 0.0, 0.0], "fontsize": 8},
        "x_axis_ticks": {"direction": "out", "color": [1.0, 1.0, 1.0]},
        "y_axis": {"color": [0.0, 0.0, 0.0], "linewidth": 1.5, "linestyle": "-"},
        "y_axis_labels": {"color": [0.0, 0.0, 0.0], "fontsize": 8},
        "y_axis_ticks": {"direction": "out", "color": [0.7, 0.8, 1.0]},
        "partial_axis": False,
        "position": [0.025, 0.075, 0.925, 0.875]
    },
    "limits": {
        "range_temp_c": [0, 40],
        "range_humidity_g_kg": [0, 30],
        "altitude_m": 0,
        "step_temp": 1.0
    },
    "saturation": {"color": [1.0, 0.3, 1.0], "linewidth": 2, "linestyle": "-"},
    "constant_rh": {"color": [0.0, 0.6, 1.0], "linewidth": 1, "linestyle": "-"},
    "constant_v": {"color": [0.0, 0.4, 0.4], "linewidth": 0.5, "linestyle": "-"},
    "constant_h": {"color": [1, 0.4, 0.0], "linewidth": 0.75, "linestyle": "-"},
    "constant_wet_temp": {"color": [0.2, 0.8, 0.2], "linewidth": 1, "linestyle": "--"},
    "constant_dry_temp": {"color": [0.9, 0.0, 1.0], "linewidth": 0.25, "linestyle": "-"},
    "constant_humidity": {"color": [0.6, 0.0, 1.0], "linewidth": 0.25, "linestyle": "-"},
    "chart_params": {
        "with_constant_rh": True,
        "constant_rh_curves": [20, 30, 40, 50, 60, 70, 80, 90],
        "constant_rh_labels": [50, 53, 66, 70],
        "with_constant_v": False,
        "constant_v_step": 0.01,
        "range_vol_m3_kg": [0.78, 0.96],
        "with_constant_h": True,
        "constant_h_step": 10,
        "constant_h_labels": [0],
        "range_h": [40, 100],
        "with_constant_wet_temp": True,
        "constant_wet_temp_step": 1,
        "range_wet_temp": [25, 33],
        "constant_wet_temp_labels": [27, 29, 30, 33, 28],
        "with_constant_dry_temp": True,
        "constant_temp_step": 3,
        "range_dry_temp": [34, 40],
        "constant _wet_temp_labels": [34, 35.5, 36, 37, 38.5, 40],

        "with_constant_humidity": True,
        "constant_humid_step": 2,
        "with_zones": False
    }
}
fig, ax = plt.subplots(figsize=(7, 5))
chart = PsychroChart(custom_style)
chart.plot(ax)

chart.plot_legend(markerscale=.5, frameon=True, fontsize=10, labelspacing=1.2)

plt.savefig(r"F:/chart.png", transparent=True)
