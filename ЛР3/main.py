def greet(name):
    print(f"Привет, {name}!")


def square(number):
    return number ** 2


def max_of_two(a, b):
    if a > b:
        return a
    return b


greet("Алиса")
greet("Боб")

print(square(5))
print(square(-3))

print(max_of_two(10, 20))
print(max_of_two(-1, -5))
