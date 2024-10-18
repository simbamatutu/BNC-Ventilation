import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm

temperature_data = np.array([[38, 40, 41], [39, 41, 42], [37, 39, 40]])

x_coords = np.array([200, 350, 350])  # Updated distance values in meters

# Updated elevation values in meters
y_coords = np.array([1100, 1170, 1200])
ax = sns.heatmap(temperature_data, annot=True,
                 cmap='inferno', square=True, vmin=37, vmax=42)
ax.set_title("Trojan Temperature Heat Map (Levels 41-45)")
ax.set_xlabel("Distance (m)")
ax.set_ylabel("Elevation (m)")
sm = cm.ScalarMappable(
    cmap='inferno', norm=plt.Normalize(vmin=37, vmax=42))
sm.set_array([])

cax = plt.gcf().add_axes([0.9, 0.2, 0.03, 0.6])
cbar = plt.colorbar(sm, cax=cax)
cbar.set_label('Temperature (°C)')
cbar.set_ticks([37, 40, 42])
plt.savefig(
    r"F:/Users/step7/343/heatMap.png", transparent=True)
