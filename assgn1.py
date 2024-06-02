import numpy as np

ar = np.array([[[11,22,23], [7, 21, 49]], [ [10,20,30], [25,50,75]]])

column = ar[:, 1, :]

column2 = column*2

avg = np.mean(column2, axis=1)
print(column2)
print(avg)