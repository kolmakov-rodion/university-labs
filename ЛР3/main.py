array = [10, 20, 12, 56, 12, 46, 0, 9, 8, 5, 54]

def calculate_average(measurements):
    s = 0
    for i in range(len(measurements)):
        s += measurements[i]
    return s / len(measurements)


def find_minimum(measurements):
    return sorted(measurements)[0]


def find_maximum(measurements):
    return sorted(measurements)[-1]


def count_above_average(measurements):
    count = 0
    average = calculate_average(measurements)
    for item in measurements:
        if item > average:
            count += 1
    return count


def find_value(measurements, target):
    for i in range(len(measurements)):
        if measurements[i] == target:
            return f'Элемент найден. Индекс - {i}'
    return 'Элемент не найден'


def analyze_measurements(measurements):
    return find_minimum(measurements), find_maximum(measurements), calculate_average(measurements)


print(len(array))
minimum, maximum, average = analyze_measurements(array)
print(minimum, maximum, average)
print(count_above_average(array))
print(find_value(array, 10))
