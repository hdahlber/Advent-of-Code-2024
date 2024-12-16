def read_in_file(filename):
    grid_list = []
    with open(filename, "r") as file:
        data = file.read()
        for line in data.splitlines():
            grid_list.append([str(char) for char in line])

    return grid_list


def part_1(data):
    directions = {
        "up": (-1, 0),
        "down": (1, 0),
        "right": (0, 1),
        "left": (0, -1)
    }

    visited = set()
    col_len = len(data[0])
    row_len = len(data)
    summer = 0
    summer2 = 0

    def calculate_lawn_size(row_index, col_index):
        stack = [(row_index, col_index)]
        lawn_char = data[row_index][col_index]
        lawn_size = 0
        sides = 0
        edges = set()
        while stack:
            r, c = stack.pop()
            if (r, c) in visited:
                continue

            visited.add((r, c))
            lawn_size += 1
            local_sides = 4

            for direction, (row_change, col_change) in directions.items():
                new_row = r + row_change
                new_col = c + col_change

                if 0 <= new_row < row_len and 0 <= new_col < col_len:
                    if data[new_row][new_col] == lawn_char:
                        if (new_row, new_col) not in visited:
                            stack.append((new_row, new_col))
                        local_sides -= 1
                    else:
                        edges.add(((r, c), direction))
                else:
                    edges.add(((r, c), direction))

            sides += local_sides
        part_2_ans = part_2(edges)
        return lawn_char, lawn_size, sides, part_2_ans

    for row_index, row in enumerate(data):
        for col_index, value in enumerate(row):
            if (row_index, col_index) not in visited:
                lawn_char, lawn_size, sides, part_2_ans = calculate_lawn_size(row_index, col_index)
                summer += lawn_size * sides
                summer2 += lawn_size * part_2_ans
    return summer, summer2


def part_2(edges):
    rows_set = set()
    cols_set = set()
    summer3 = 0
    sorted_edges = sorted(edges, key=lambda x: (x[0][0], x[0][1]))
    sorted_edges_columns = sorted(edges, key=lambda x: (x[0][1], x[0][0]))

    for edge in sorted_edges:
        ((row, column), direction) = edge
        if direction == "up":
            #print((row, column), direction)
            rows_set.add(edge)
            if ((row, column - 1), "up") not in rows_set:
                summer3 += 1
        if direction == "down":
            #print((row, column), direction)
            rows_set.add(edge)
            if ((row, column - 1), "down") not in rows_set:
                summer3 += 1


    for edge in sorted_edges_columns:
        ((row, column), direction) = edge
        if direction == "left":
            #print((row, column), direction)
            cols_set.add(edge)
            if ((row - 1, column), "left") not in cols_set:
                summer3 += 1
        if direction == "right":
            cols_set.add(edge)
            if ((row - 1, column), "right") not in cols_set:
                summer3 += 1


    print(summer3)
    return summer3


def main():
    grid_list = read_in_file("input.txt")
    result, result2 = part_1(grid_list)
    print(f"Part 1 results: {result}")
    print(f"Part 2 results: {result2}")


if __name__ == "__main__":
    main()
