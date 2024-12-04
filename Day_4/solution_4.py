

def check_vertical(rows):
    counter = 0
    for col in range(0, len(rows)):
        column_string = ''.join(row[col] for row in rows)
        counter += column_string.count("XMAS")
        counter += column_string.count("SAMX")
    return counter


def check_diagonal(rows):
    counter = 0
    length= len(rows)-1 # 9
    for y in range(length, -1, -1):
        left_up = "" #checked
        right_down = "" # checked
        left_down = ""
        right_up = ""
        for x in range(0,len(rows)):

            if y-x >= 0:
                #print("my y", y - x)
                left_up += rows[y-x][x]

            if  y-1-x >= 0:
                #print("my x", y-1-x, "my y", length-x)
                right_up += rows[length-x][y-1-x]

            if y + x <= length and y!= 0:
                #print("my x", y+x,"my y",length-x)
                left_down += rows[y+x][length-x]
            if y+x <= length:
                right_down += rows[x][y+x]


        counter += left_up.count("XMAS")
        counter += left_up.count("SAMX")
        counter += left_down.count("XMAS")
        counter += left_down.count("SAMX")
        counter += right_down.count("XMAS")
        counter += right_down.count("SAMX")
        counter += right_up.count("XMAS")
        counter += right_up.count("SAMX")



    return counter


def part1(test):
    counter = 0
    rows = []
    with open(test, "r") as file:
        for line in file:
            rows.append(line.strip())
            # horizontal
            counter += line.strip().count("XMAS")
            counter += line.strip().count("SAMX")
    #vertical
    counter += check_vertical(rows)
    # diagonal
    counter += check_diagonal(rows)

    return counter

def part2(test):
    rows = []
    counter = 0
    with open(test, "r") as file:
        for line in file:
            rows.append(line.strip())

    for row_index, row in enumerate(rows):
        for col_index, char in enumerate(row):
            my_list = []
            if char == "A" and row_index != 0 and row_index != len(rows)-1 and col_index != 0 and col_index != len(rows)-1:
                left_up = rows[row_index - 1][col_index - 1]
                left_down = rows[row_index + 1][col_index - 1]
                right_up = rows[row_index - 1][col_index + 1]
                right_down = rows[row_index + 1][col_index + 1]
                my_list.extend([left_down, left_up, right_down, right_up])
                count_m = my_list.count("M")
                count_s = my_list.count("S")
                if count_m == 2 and count_s == 2 and left_up != right_down:

                    counter += 1
    return counter


def main():
    result = part1("input.txt")
    print(f"Part 1 results: {result}")
    result = part2("input.txt")
    print(f"Part 2 results: {result}")


if __name__ == "__main__":
    main()
