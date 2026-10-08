def analyze(numbers):
    return min(numbers), max(numbers), sum(numbers) / len(numbers)


numbers = [12, 7, 25, 3, 18, 9]
minimum, maximum, average = analyze(numbers)
print(minimum)
print(maximum)
print(average)
