import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
sales = [12000, 15000, 18000, 16000, 20000, 22000, 25000, 23000, 21000, 19000, 22000, 24000]

plt.figure(figsize=(10, 6))
plt.plot(months, sales, marker='o', color='b', label='Monthly Sales')
plt.title('Monthly Sales Data')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))  
plt.bar(months, sales, color='g', label='Monthly Sales')
plt.title('Monthly Sales Data')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.legend()
plt.grid(axis='y')  
plt.show()
