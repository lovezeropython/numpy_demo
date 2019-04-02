import numpy as np
"""
a = np.array([1, 3, 4])
b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(a)
print(b)
print(a.shape, b.shape)


persontype = np.dtype({
    "names": ['name', 'age', 'china', 'math', 'english'],
    'formats': ['S32', 'i', 'i', 'i', 'f']
})

peoples = np.array([("ZhangFei", 32, 75, 100, 90), ("GuanYu", 24, 85, 96, 88.5),
                    ("ZhaoYun", 28, 85, 92, 96.5), ("HuangZhong", 29, 65, 85, 100)],
                   dtype=persontype)

ages = peoples[:]['age']

print(ages)
print(np.mean(ages))
"""
