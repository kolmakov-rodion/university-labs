def find_element(numbers, target):
    for i in range(len(numbers)):
        if numbers[i] == target:
            return i
    return -1


nums = [4, 8, 15, 16, 23, 16, 42]
print(find_element(nums, 16))
print(find_element(nums, 100))
print(find_element(nums, 4))
print(find_element(nums, 42))
