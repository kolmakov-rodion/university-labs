from utils.statistics import find_max, find_min, calculate_average
from utils.reader import read_numbers


def main():
    test_list = read_numbers('C:/Users/rodio/Desktop/Обучение/Лабы/ЛР4/measurement_project/data/measurements.txt')
    print(find_max(test_list))
    print(find_min(test_list))
    print(calculate_average(test_list))


if __name__ == '__main__':
    main()