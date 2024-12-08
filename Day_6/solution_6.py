directions = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
turn_right = {'^': '>', '>': 'v', 'v': '<', '<': '^'}


def read_in_file(filename):

    with open(filename, "r") as file:
        data = file.read()
        for line in data.splitlines():
            grid_list.append(list(line))
    )

    return grid_list

def check_if_loop(guard_pos,guard_dir,grid,rows,columns,next_pos):

    extra_block = next_pos
    start_state = (guard_pos, guard_dir)
    guard_dir = turn_right[guard_dir]
    current_state = (guard_pos, guard_dir)
    visited_states = set()
    visited_states.add(start_state)

    while True:
        dr, dc = directions[guard_dir]
        next_pos = (guard_pos[0] + dr, guard_pos[1] + dc)

        if current_state in visited_states:
            print(current_state,visited_states)
            return 1



        if next_pos[0] < 0 or next_pos[0] >= rows or next_pos[1] < 0 or next_pos[1] >= columns:
            return 0
        elif grid[next_pos[0]][next_pos[1]] == '#' or next_pos == extra_block:
            state_placeholder =(guard_pos,guard_dir)
            visited_states.add(state_placeholder)
            guard_dir = turn_right[guard_dir]
            current_state = (guard_pos, guard_dir)
        else:
            guard_pos = next_pos
            current_state = (next_pos, guard_dir)




def part_1(grid):
    visited = set()
    rows = len(grid)
    columns =len(grid[0])
    guard_pos = None
    guard_dir = None
    blocks = set()
    summer= 0
    for r in range(rows):
        for c in range(columns):
            if grid[r][c] in directions:
                guard_pos = (r, c)
                guard_dir = grid[r][c]
                grid[r][c] = '.'  # byt för att kunna loopa med samma alltid

                break
        if guard_pos:
            break


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
            number_1 = check_if_loop(guard_pos, guard_dir, grid, rows, columns,next_pos)
            if number_1 == 1 and next_pos not in visited:
                summer += 1
                blocks.add(next_pos)


            guard_pos = next_pos
            visited.add(guard_pos)


    print(summer)
    print(len(blocks))
    return len(visited)+1, len(blocks)

def main():
    grid_list = read_in_file("input.txt")
    result, result2= part_1(grid_list)
    print(f"Part 1 results: {result}")
    print(f"Part 2 results: {result2}")


if __name__ == "__main__":
    main()