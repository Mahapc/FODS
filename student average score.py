import pandas as pd
import numpy as np
arr=pd.read_csv("student_score.csv")
print(arr)
arr1=np.mean(arr,axis=0)
print(arr1)
h=np.argmax(arr1)
sub=["maths","science","english","history"]
print(sub[h],"=",max(arr1))
