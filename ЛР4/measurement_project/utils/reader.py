def read_numbers(file_path):
    numbers = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                if line:
                    try:
                        numbers.append(float(line))
                    except ValueError:
                        print("Not a number")
    except FileNotFoundError:
        print('File is not found')
    return numbers
