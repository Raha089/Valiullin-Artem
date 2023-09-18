# ЗАДАЧА 1
import math

x = float(14.26)
y = float(-1.22)
z = 3.5 * 10 ** (-2)
s = ((2 * math.cos(x - 2 / 3) / (1 / 2 + math.sin(y) ** 2))) * (
    1 + ((z**2) / (3 - z**2 / 5))
)
print(s)

# ЗАДАЧА 2
#import math
#
#x2 = float(-4.5)
#y2 = 0.75 * 10**-4
#z2 = -0.845 * 10**2
#s2 = (((9 + ((x2 - y2) ** 2)) ** (1.0 / 3.0)) / (x2**2 + y2**2 + 2)) - (
#    exp(abs(x2 - y2)) * tan(z2) ** 3
#)
#print(s2#)

# ЗАДАЧА 3
# import math

# x =
# y =
# z =
# s =
# print(s)
from math import *
x2 = -4.5
y2 = 0.75 * 10**-4
z2 = -0.845 * 10**2
s2 = (((9 + ((x2 - y2) ** 2)) ** (1.0 / 3.0)) / (x2**2 + y2**2 + 2)) - (
    exp(abs(x2 - y2)) * tan(z2) ** 3
)
print(s2)