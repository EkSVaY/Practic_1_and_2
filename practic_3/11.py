# Task_11_Ekin_Viacheslaw


import math


a, b, c = map(float, input().split())
x_1 = int(math.acos((a ** 2 + c ** 2 - b ** 2) / (2 * a * c)) / math.radians(1))
x_2 = int(math.acos((a ** 2 + b ** 2 - c ** 2) / (2 * a * b)) / math.radians(1))
x_3 = int(math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * c * b)) / math.radians(1))

print(x_1, x_2, x_3)
