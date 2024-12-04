from contextlib import nullcontext


def check_vertical(rows):
    counter = 0
    for col in range(0, len(rows)):
        column_string = ''.join(row[col] for row in rows)
        counter += column_string.count("XMAS")
        counter += column_string.count("SAMX")
    return counter


def check_diagonal(rows):
    count = 0
    length= len(rows)-1

    for y in range(length, 2, -1):
        for x in range(length):


        #print(rows[y][length-y])
        left_up = ""
        string_right_up = ""
        #for x in range(length):

            #left_up = rows[y+x][x]

            #vänster ner up:
            #start 0,3 1,3 2,3 3,3
            #start point
            # string = rows[length][char]
            # every step
            # string += rows[length-1][+1]
    return count


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


def main():
    result = part1("test.txt")
    print(result)


if __name__ == "__main__":
    main()
