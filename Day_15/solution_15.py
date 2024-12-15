def read_in_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        grid_end_index = None
        for i, line in enumerate(lines):
            if line.strip() == "":
                grid_end_index = i
                break
        grid = [line.strip() for line in lines[:grid_end_index]]
        grid = [list(row) for row in grid]

        start_position = None
        for i, row in enumerate(grid):
            if '@' in row:
                start_position = (i, row.index('@'))
                break

        movements = list("".join(lines[grid_end_index + 1:]).strip().replace('\n', ''))
    print(grid)
    return grid, movements,  start_position

def part_1(grid, movements,  start_position):
    directions = {
        "^": (-1, 0),
        "v": (1, 0),
        ">": (0, 1),
        "<": (0, -1)
    }
    current_position = start_position
    for movement in movements:
        direction = directions[movement]
        new_position = current_position[0] + direction[0], current_position[1] + direction[1]
        if grid[new_position[0]][new_position[1]] == ".":
            grid[new_position[0]][new_position[1]] = "@"
            grid[current_position[0]][current_position[1]] = "."
            current_position = new_position

        elif grid[new_position[0]][new_position[1]] == "O":
            i = new_position[0] + direction[0]
            j = new_position[1] + direction[1]

            if grid[i][j] == ".":
                grid[new_position[0]][new_position[1]] = "@"
                grid[current_position[0]][current_position[1]] = "."
                grid[i][j] = "O"
                current_position = new_position
            else:
                while grid[i][j] == "O":
                    i += direction[0]
                    j += direction[1]
                    if grid[i][j] == ".":
                        grid[new_position[0]][new_position[1]] = "@"
                        grid[current_position[0]][current_position[1]] = "."
                        grid[i][j] = "O"
                        current_position = new_position
                        break
                    if grid[i][j] == "#":
                        break
    for line in grid:
        print("".join(line))
    print("\n")

    total_gps = 0

    for row_index, row in enumerate(grid):
        for col_index, cell in enumerate(row):
            if cell == "O":
                total_gps += (100 * row_index) + col_index

    return total_gps
def main():
    grid,movemnts,  start_position = read_in_file("input.txt")
    result = part_1(grid,movemnts,  start_position)
    print(f"Part 1 results: {result}")

if __name__ == "__main__":
    main()
