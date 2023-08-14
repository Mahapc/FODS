import numpy as np
fuel_eff=np.array([25,30,20,22,28])
avg_eff=np.mean(fuel_eff)
model1=fuel_eff[1]
model2=fuel_eff[3] 
pre_imp=((model2-model1)/model1)*100
print("improved percentage",pre_imp)
