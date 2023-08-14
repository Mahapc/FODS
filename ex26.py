import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
area = np.array([500,1500,4000,3000,3500])
bedrooms = np.array([1,2,3,4,5])
features = np.column_stack((area, bedrooms))
prices = 10000 + 200 * area + 1000* bedrooms 
model = LinearRegression()
model.fit(features, prices)
new_area = float(input("Enter the area of the new house: "))
new_bedrooms = int(input("Enter the number of bedrooms of the new house: "))
predicted_price = model.predict([[new_area, new_bedrooms]])
print(f"Predicted price for the new house: ${predicted_price[0]:.2f}")



