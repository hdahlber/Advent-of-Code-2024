from collections import Counter


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

    def calculate_lawn_size(row_index, col_index):
        stack = [(row_index, col_index)]
        lawn_char = data[row_index][col_index]
        lawn_size = 0
        sides = 0

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

            sides += local_sides

        return lawn_char, lawn_size, sides

    for row_index, row in enumerate(data):
        for col_index, value in enumerate(row):
            if (row_index, col_index) not in visited:
                lawn_char, lawn_size, sides = calculate_lawn_size(row_index, col_index)
                summer += lawn_size * sides

    return summer


def main():
    grid_list = read_in_file("input.txt")
    result = part_1(grid_list)
    print(f"Part 1 results: {result}")






if __name__ == "__main__":
    main()