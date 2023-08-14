import pandas as pd
import numpy as np
h=pd.read_csv("house q3.csv")
arr=np.array(h)
price=h["price"]
bedroom=h['bedroom']
avg=np.mean(price[bedroom>3])
print(avg)
