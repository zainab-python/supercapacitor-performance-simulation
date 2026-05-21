import numpy as np
import matplotlib.pyplot as plt

time = np.linspace(0, 10, 100)
voltage = 2.7 - 0.2 * time

plt.plot(time, voltage)
plt.xlabel("Time")
plt.ylabel("Voltage")
plt.title("Supercapacitor Discharge Curve")
plt.show()
