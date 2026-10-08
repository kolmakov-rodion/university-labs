def calculate_sum(numbers):
    total = 0
    for n in numbers:
        total += n
    return total


def find_min(numbers):
    result = numbers[0]
    for n in numbers:
        if n < result:
            result = n
    return result


def find_max(numbers):
    result = numbers[0]
    for n in numbers:
        if n > result:
            result = n
    return result


nums = [5, 3, 9, 1, 7, 2, 8]
print(calculate_sum(nums))
print(find_min(nums))
print(find_max(nums))
print(sum(nums))
print(min(nums))
print(max(nums))
