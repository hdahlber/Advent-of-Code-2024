import re
def read_in_file(filename):
    first_list = []
    second_list = []
    pattern = r"mul\(\d+,\d+\)"
    pattern2 = r"mul\(\d+,\d+\)|\bdo\(\)|don't\(\)"
    with open(filename, "r") as file:

        for line in file:
            matches = re.findall(pattern, line)
            matches2 = re.findall(pattern2, line)
            first_list.extend(matches)
            second_list.extend(matches2)
    return first_list, second_list


def part1(my_list):
    summer = 0
    for match in my_list:
        numbers = re.findall(r'\d+', match)
        if len(numbers) == 2:
            try:
                num1, num2 = map(int, numbers)
                summer += num1 * num2
            except ValueError:
                print(numbers)

    return summer

def part2(second_list):
    summer = 0
    flag = True
    pattern = r"\d+|don't\(\)|do\(\)"
    for match in second_list:
        x = re.findall(pattern, match)

        if len(x) == 2 and flag == True:
            num1, num2 = map(int, x)
            summer += num1 * num2
        elif "don't()" in x:
            flag = False
        elif "do()" in x:
            flag = True

    return summer


def main():
    my_list, second_list = read_in_file("input.txt")

    result = part1(my_list)
    print(f"Part 1 results: {result}")
    result = part2(second_list)
    print(f"Part 2 results: {result}")


if __name__ == "__main__":
    main()