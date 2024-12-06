from asyncio import wait_for


def read_in_file(filename):
    grid_list = []
    with open(filename, "r") as file:
        data = file.read()
        for line in data.splitlines():
            grid_list.append(list(line))
    print("grid_list",grid_list)

    return grid_list


def part_1(grid):
    directions = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
    turn_right = {'^': '>', '>': 'v', 'v': '<', '<': '^'}
    visited = set()
    rows = len(grid)
    columns =len(grid[0])
    guard_pos = None
    guard_dir = None

    for r in range(rows):
        for c in range(columns):
            if grid[r][c] in directions:
                guard_pos = (r, c)
                guard_dir = grid[r][c]
                grid[r][c] = '.'  # byt för att kunna loopa med samma alltid
                break
        if guard_pos:
            print(guard_pos,guard_dir)
            break
    visited.add(guard_pos)

    while True:
        dr, dc = directions[guard_dir]
        next_pos = (guard_pos[0] + dr, guard_pos[1] + dc)

        # if out of bound
        if next_pos[0] < 0 or next_pos[0] >= rows or next_pos[1] < 0 or next_pos[1] >= columns:
            break
        # elif blocked
        elif grid[next_pos[0]][next_pos[1]] == '#':
            guard_dir = turn_right[guard_dir]

        #else go forward
        else:
            guard_pos = next_pos
            print(guard_pos,guard_dir)
            visited.add(guard_pos)








    return len(visited)

def main():
    grid_list = read_in_file("input.txt")
    result = part_1(grid_list)
    print(f"Part 1 results: {result}")


if __name__ == "__main__":
    main()