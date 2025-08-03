import numpy as np

rain_data_mm = [0.0, 5.2, 3.1, 0.0, 12.4, 0.0, 7.5]
rain = np.array(rain_data_mm)

total = np.round(np.sum(rain), 2)

average = np.round(np.mean(rain), 2)

dry_days = np.sum(rain == 0.0)

heavy_rain = np.where(rain > 5.0)

print("Weekly Rainfall (mm):", np.round(rain, 2))
print("Total rainfall:", total, "mm")
print("Average rainfall:", average, "mm")
print("Number of dry days:", dry_days)
print("Days with more than 5mm rain (index):", heavy_rain[0])
