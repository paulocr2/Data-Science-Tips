import numpy as np

import sys

x = np.array([34.5, 67.3, 94.5, 123.98])

x.mean()

print("min =", round(x.min(),2), "mean =", round(x.mean(),2), "\n")

print("Python version =", sys.version)

#- Zip function 

result = list(zip(["john", "carl"], [1, 3]))


print(result)


x = "1"+"2"

print(x)