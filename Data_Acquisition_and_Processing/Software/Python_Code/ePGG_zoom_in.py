import pandas as pd
import numpy as np

voice = pd.read_csv("Will_pgg_data.csv")

t = voice["time_s"].to_numpy()
v = voice["voltage_V"].to_numpy()

dt = np.diff(t)
print("Mean dt:", np.mean(dt))
print("Std dt:", np.std(dt))
print("fs:", 1 / np.mean(dt))

start_time = 10
window = 20
mask = (t >= start_time) & (t <= start_time + window)
plt.figure(figsize=(10,4))
plt.plot(t[mask], v_moving_avg[mask], label="voltage average")
plt.xlabel("Time (s)")
plt.ylabel("Voltage centered (V)")
plt.title("Zoomed PGG")
plt.legend()
plt.show()
