def read_in_file(filename):
    first_list = []
    with open(filename, "r") as file:
        for line in file:
            first_list.append([int(num) for num in line.split()])
    return first_list


def part1(my_list):
    safe = 0
    for i in range(len(my_list)):
        is_safe = True
        if my_list[i] == sorted(my_list[i]) or my_list[i] == sorted(my_list[i], reverse=True):
            for j in range(len(my_list[i]) - 1):
                absolute = abs(my_list[i][j] - my_list[i][j + 1])
                if absolute == 0 or absolute > 3:
                    is_safe = False
                    break
            if is_safe:
                safe += 1

    return safe


def pos_neg_rest(lister):
    positive_13 = 0
    negative_13 = 0
    rest_numb = 0

    for num in lister:
        if 1 <= num <= 3:
            positive_13 += 1
        elif -3 <= num <= -1:
            negative_13 += 1
        else:
            rest_numb += 1
    return positive_13, negative_13, rest_numb


def part2(my_list):
    safe = 0
    for i in range(len(my_list)):
        lister = []
        for j in range(len(my_list[i]) - 1):
            lister.append(my_list[i][j] - my_list[i][j + 1])
        positive_13, negative_13, rest_numb = pos_neg_rest(lister)
        if positive_13 + rest_numb == 0 or negative_13 + rest_numb == 0:
            safe += 1

        else:
            for j in range(len(my_list[i])):

                modified_list = my_list[i][:j] + my_list[i][j + 1:]

                if modified_list == sorted(modified_list) or modified_list == sorted(modified_list, reverse=True):

                    is_safe = True
                    absolute_list = []
                    for k in range(len(modified_list) - 1):
                        absolute_list.append(abs(modified_list[k] - modified_list[k+1]))

                    for absolute in absolute_list:
                        if absolute == 0 or absolute > 3:
                            is_safe = False
                            break

                    if is_safe:
                        print(absolute_list,i,my_list[i])
                        safe += 1
                        break




    return safe


def main():
    my_list = read_in_file("input.txt")
    result = part1(my_list)
    print(f"Part 1 results: {result}")
    result = part2(my_list)
    print(f"Part 2 results: {result}")


if __name__ == "__main__":
    main()
