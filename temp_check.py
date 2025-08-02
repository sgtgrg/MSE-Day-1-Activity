import numpy as np 

temp_celsius = [18.5, 19, 20, 25.0, 2, 30, 13.9]
temps = np.array(temp_celsius)

# Calculate average temperature
avg_temp = np.mean(temps)
print("The Average temperature in °C:", avg_temp)

# Find max and min temperature
max_temp = np.max(temps)
min_temp = np.min(temps)
print("Highest Temperature (°C) is:", max_temp)
print("Lowest Temperature (°C) is: ", min_temp)

# Convert to Fahrenheit
temp_fahrenheit = temps * 9/5 + 32
print("Temperature in Fahrenheit is:", temp_fahrenheit)
#print(temp_fahrenheit)

# Find indices where temperature is greater than 20°C
hotter_days = np.where(temps > 20)
print("Hot days exceeding 20°C (indices):", hotter_days[0])
#print(hotter_days[0])
