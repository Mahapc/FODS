import pandas as pd
import numpy as np
arr=pd.read_csv("price of sold productmm.csv")
print(arr)
c=np.array(arr)
print(c)
avg=np.mean(c)
print("average of last month sales",avg)
