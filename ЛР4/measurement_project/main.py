from utils.statistics import find_max, find_min, calculate_average

def main():
    test_list = [1, 2, 3, 4, 5]
    print(find_max(test_list))
    print(find_min(test_list))
    print(calculate_average(test_list))


if __name__ == '__main__':
    main()