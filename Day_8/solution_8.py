from collections import defaultdict
from itertools import combinations


def read_in_file(filename):
    grid_list = []
    with open(filename, "r") as file:
        data = file.read().strip().split("\n")
        for line in data:
            grid_list.append(list(line))
    #print(grid_list)
    #print(len(grid_list))

    antenna_locations = defaultdict(list)
    # find
    for x in range(len(grid_list)):
        for y in range(len(grid_list[x])):
            if grid_list[x][y] != ".":
                antenna_locations[grid_list[x][y]].append((x, y))
    #print(antenna_locations)


    return antenna_locations, len(grid_list)





def part_1(antenna_locations,length):
    antinodes =  set()
    antinodes_part2 = set()
    for antenna in antenna_locations:
        location = antenna_locations[antenna]
        #print("dsfsdff",location)
        for a, b in combinations(location, r=2):
            antinodes_part2.add(a)
            antinodes_part2.add(b)
            #print(a,b)
            # (1,1) och (3,4)
            #row = 1 - (3-1) = 1-2 = -1
            #column = 1 -(4-1) = 1-3 = -2
            #row_2 = 3 - (1 - 3) = 3 + 2 = 5
            #column_2 = 4 - (1 - 4) = 4 + 3 = 7
            step1_x = (b[0]-a[0])
            step1_y = (b[1]-a[1])
            step2_x = (a[0]-b[0])
            step2_y = (a[1]-b[1])
            antinode_1 = a[0] - step1_x, a[1] - step1_y
            antinode_2 = b[0] - step2_x , b[1] - step2_y
            flag1= True
            flag2= True
            #print(antinode_1, antinode_2)
            if antinode_1[0] >= 0 and antinode_1[1] >= 0 and antinode_1[0] < length and antinode_1[1] < length:
                antinodes.add(antinode_1)
                antinodes_part2.add(antinode_1)
            else:
                flag1 = False

            if antinode_2[0] >= 0 and antinode_2[1] >= 0 and antinode_2[0] < length and antinode_2[1] < length:
                antinodes.add(antinode_2)
                antinodes_part2.add(antinode_2)
            else:
                flag2 = False

            while flag1 or flag2:
                antinode_1 = antinode_1[0] - step1_x, antinode_1[1] - step1_y
                antinode_2 = antinode_2[0] - step2_x, antinode_2[1] - step2_y
                #print(antinode_1, antinode_2)
                if (antinode_1[0] >= 0 and antinode_1[1] >= 0) and (antinode_1[0] < length and antinode_1[1] < length):
                    antinodes_part2.add(antinode_1)
                else:
                    #print("flag 1",flag1)
                    flag1 = False
                if (antinode_2[0] >= 0 and antinode_2[1] >= 0) and (antinode_2[0] < length and antinode_2[1] < length):
                    antinodes_part2.add(antinode_2)
                else:
                    #print("flag 2", flag2)
                    flag2 = False

    return len(antinodes), len(antinodes_part2)
def main():
    antennas,length =read_in_file("input.txt")
    result,result2 = part_1(antennas,length)
    print(f"Part 1 results: {result}")
    print(f"Part 2 results: {result2}")


if __name__ == "__main__":
    main()