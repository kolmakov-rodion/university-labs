measurements = (1, 2, 3, 4, 5, 6, 7, 8, 9)

a, b = measurements[:2]
print(a, b)
measurements = list(measurements)
measurements[0] = 10
measurements = tuple(measurements)
print(measurements)