import pandas as pd
import numpy as np

y = [1,2,'hello','55',66.0,99]
x = []

for i in y:
	if i != str:
		x.append(i)

print("The list of only numerical items is: ", x)

