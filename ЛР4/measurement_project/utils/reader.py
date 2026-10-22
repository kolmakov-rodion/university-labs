def read_numbers(file_path):
    numbers = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            if line:
                numbers.append(float(line))
    return numbers
