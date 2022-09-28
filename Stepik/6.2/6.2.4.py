from math import sin, cos, tan, radians

x = float(input())

x_rad = radians(x)
print(sin(x_rad) + cos(x_rad) + tan(x_rad)**2)