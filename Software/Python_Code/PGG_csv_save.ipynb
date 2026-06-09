import serial
import csv
import time

port = "COM4" # Adjust to your microcontroller por            
baud = 500000 # Adjust to your Arduino Code
filename = "Will_pgg_data.csv"  # Change output csv file name per person.
duration = 60                # seconds

ser = serial.Serial(port, baud, timeout=1)
time.sleep(2)

ser.reset_input_buffer()

start_wall_time = time.time()
first_arduino_time = None

with open(filename, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["time_s", "raw", "voltage_V"])

    print("Recording...")

    while time.time() - start_wall_time < duration:
        line = ser.readline().decode(errors="ignore").strip()

        if not line:
            continue

        try:
            t_us_str, raw_str = line.split(",")

            t_us = int(t_us_str)
            raw = int(raw_str)

            if first_arduino_time is None:
                first_arduino_time = t_us

            time_s = (t_us - first_arduino_time) / 1_000_000
            voltage = raw * 5.0 / 1023.0

            writer.writerow([time_s, raw, voltage])

        except ValueError:
            continue

print("Done recording.")
ser.close()
