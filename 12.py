import matplotlib.pyplot as plt
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
temperature = [20, 22, 25, 28, 30, 32, 34, 33, 31, 28, 25, 22]
rainfall = [50, 40, 30, 20, 10, 5, 5, 10, 20, 30, 40, 50]
plt.figure(figsize=(10, 6))
plt.plot(months, temperature, marker='o', color='b', label='Temperature')
plt.title('Monthly Temperature Data')
plt.xlabel('Month')
plt.ylabel('Temperature (°C)')
plt.legend()
plt.grid(True)
plt.show()
plt.figure(figsize=(10, 6))
plt.scatter(months, rainfall, color='r', label='Rainfall')
plt.title('Monthly Rainfall Data')
plt.xlabel('Month')
plt.ylabel('Rainfall (mm)')
plt.legend()
plt.grid(True)
plt.show()
