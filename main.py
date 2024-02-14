

import random


def main():
    tenthousand_random_numbers = []
    for i in range(100):
        tenthousand_random_numbers.append(random.randrange(1, 100))
    benfords_histogram(tenthousand_random_numbers)

def benfords_histogram(numbers):
    count_dict = {
        "1": 0,
        "2": 0,
        "3": 0,
        "4": 0,
        "5": 0,
        "6": 0,
        "7": 0,
        "8": 0,
        "9": 0,
    }
    for number in numbers:
        count_dict[str(number)[0]] += 1

    max_count = 0
    for key in count_dict:
        if count_dict[key] > max_count:
            max_count = count_dict[key]
    
    for key in count_dict:
        adjusted_count = int(count_dict[key] * 40 / max_count)
        print(f"{key}: {'#' * adjusted_count}")


main()