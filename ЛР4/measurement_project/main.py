from utils.statistics import find_max, find_min, calculate_average
from utils.reader import read_numbers
from pathlib import Path


def main():
    file_path = Path('data') / 'measurements.txt'
    print(file_path.exists())
    print(Path.cwd())
    test_list = read_numbers(file_path)
    print(find_max(test_list))
    print(find_min(test_list))
    print(calculate_average(test_list))
    logs_dir = Path('logs')
    logs_dir.mkdir(exist_ok=True)

if __name__ == '__main__':
    main()
