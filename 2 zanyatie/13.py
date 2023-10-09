from math import *

x = 17.421
y = 10.365 * 10**-3
z = 0.828 * 10**5
s = ((y + ((x - 1) ** (1.0 / 3.0))) ** (1.0 / 4.0)) / (
    abs(x - y) * (sin(z) ** 2 + tan(z))
)
print(s)
