import numpy as np 

temp_celsius = [18.5, 19, 20, 25.0, 2, 30, 13.9]
temps = np.array(temp_celsius)

avg_temp = np.mean(temps)
print("The Average temperature in °C:", avg_temp)

max_temp = np.max(temps)
min_temp = np.min(temps)
print("Highest Temperature (°C) is:", max_temp)
print("Lowest Temperature (°C) is: ", min_temp)

temp_fahrenheit = temps * 9/5 + 32
print("Temperature in Fahrenheit is:", temp_fahrenheit)

hotter_days = np.where(temps > 20)
print("Hot days exceeding 20°C (indices):", hotter_days[0])
