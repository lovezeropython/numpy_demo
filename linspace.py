import numpy as np
x1 = np.arange(1, 11, 2)
x2 = np.linspace(1, 9, 5)

print(x2, x1)
# x2 + x1
print(np.add(x1,x2))
# x1 - x2
print(np.subtract(x1,x2))
# x1*x2
print(np.multiply(x1,x2))
# x1/x2
print(np.divide(x1,x2))
# 求余数
print(np.mod(x1,x2))



