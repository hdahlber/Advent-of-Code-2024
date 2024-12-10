def read_in_file(filename):
    grid_list = []
    with open(filename, "r") as file:
        data = file.read()
        for line in data.splitlines():
            grid_list.append([int(char) for char in line])
    #print(grid_list)
    return grid_list


trails = set()
trails_part2 = set()


def trail_finder(trail, number, data, row_len, col_len):
    directions = {
        "up": (-1, 0),
        "down": (1, 0),
        "right": (0, 1),
        "left": (0, -1)
    }

    current_row, current_col = trail[-1]

    for direction, (row_change, col_change) in directions.items():
        new_row = current_row + row_change
        new_col = current_col + col_change

        if 0 <= new_row < row_len and 0 <= new_col < col_len:
            neighbor_value = data[new_row][new_col]
            if neighbor_value == 9 and neighbor_value == number + 1:
                first_point = trail[0]
                last_point = (new_row, new_col)
                #print(tuple(trail + [(new_row, new_col)]))
                trails.add((first_point, last_point))
                trails_part2.add(tuple(trail + [(new_row, new_col)]))
            elif neighbor_value == number + 1:
                trail.append((new_row, new_col))
                trail_finder(trail, neighbor_value, data, row_len, col_len)
                trail.pop()


def part_1(data):
    col_len = len(data[0])
    row_len = len(data)
    for row_index, row in enumerate(data):  # Loop through rows
        for col_index, value in enumerate(row):
            if value == 0:
                #print(f"Value: {value}, Row: {row_index}, Column: {col_index}")
                trail = [(row_index, col_index)]
                trail_finder(trail, value, data, row_len, col_len)

    return len(trails), len(trails_part2)


def main():
    grid_list = read_in_file("input.txt")
    result, result2 = part_1(grid_list)
    print(f"Part 1 results: {result}")
    print(f"Part 1 results: {result2}")


if __name__ == "__main__":
    main()
