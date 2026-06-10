import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

filename = "Will_pgg_data.csv"
moving_avg_window = 5   # samples

voice = pd.read_csv(filename)

t = voice["time_s"].to_numpy()
v_raw = voice["voltage_V"].to_numpy()

plt.figure()
plt.plot(t, v_raw)
plt.xlabel("Time (s)")
plt.ylabel("Voltage (V)")
plt.title("Pure Raw PGG Data")
plt.show()

v_centered = v_raw - np.mean(v_raw)

plt.figure()
plt.plot(t, v_centered)
plt.xlabel("Time (s)")
plt.ylabel("Voltage Centered (V)")
plt.title("Centered Raw PGG Data")
plt.show()

kernel = np.ones(moving_avg_window) / moving_avg_window
v_moving_avg = np.convolve(v_centered, kernel, mode="same")

plt.figure()
plt.plot(t, v_moving_avg)
plt.xlabel("Time (s)")
plt.ylabel("Voltage Centered (V)")
plt.title("Moving Average PGG Data")
plt.show()

v_moving_avg_raw = np.convolve(v_raw, kernel, mode="same")

plt.figure()
plt.plot(t, v_moving_avg_raw)
plt.xlabel("Time (s)")
plt.ylabel("Voltage(V)")
plt.title("Moving Average PGG Data")
plt.show()
