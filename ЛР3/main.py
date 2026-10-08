numbers = [-10, 3, -2, 8, -5]
sorted_numbers = sorted(numbers)
abs_sorted_numbers = sorted(numbers, key=lambda x: abs(x))
print(sorted_numbers)
print(abs_sorted_numbers)