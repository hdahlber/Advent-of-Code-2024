from collections import defaultdict

wide = 101
tall = 103


def read_in_file(filename):
    robots = []
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue  # Skip empty lines
            parts = line.split(" ")
            position = tuple(map(int, parts[0][2:].split(",")))
            velocity = tuple(map(int, parts[1][2:].split(",")))
            robots.append({"position": position, "velocity": velocity})
    return robots


def part_1(robots, seconds):
    q1 = defaultdict(int)
    q2 = defaultdict(int)
    q3 = defaultdict(int)
    q4 = defaultdict(int)
    x_line = wide // 2
    y_line = tall // 2
    grid = [["." for _ in range(wide)] for _ in range(tall)]
    for robot in robots:
        if robot["velocity"][0] >= 0:
            end_x_pos = (seconds * robot["velocity"][0] + robot["position"][0]) % wide
        else:
            end_x_pos = (robot["position"][0] + (seconds * robot["velocity"][0])) % wide
            if end_x_pos < 0:
                end_x_pos += wide

        if robot["velocity"][1] >= 0:
            end_y_pos = (seconds * robot["velocity"][1] + robot["position"][1]) % tall
        else:
            end_y_pos = (robot["position"][1] + (seconds * robot["velocity"][1])) % tall
            if end_y_pos < 0:
                end_y_pos += tall

        grid[end_y_pos][end_x_pos] = "X"

        if end_x_pos == x_line or end_y_pos == y_line:
            continue
        elif end_x_pos < x_line and end_y_pos < y_line:
            q1[robot["position"]] += 1
        elif end_x_pos > x_line and end_y_pos < y_line:
            q2[robot["position"]] += 1
        elif end_x_pos < x_line and end_y_pos > y_line:
            q3[robot["position"]] += 1
        else:
            q4[robot["position"]] += 1

    result = sum(q1.values()) * sum(q2.values()) * sum(q3.values()) * sum(q4.values())
    #print(result)
    return result, grid
def has_consecutive_robots(row, count):
    max_consecutive = 0
    consecutive = 0
    for cell in row:
        if cell == 'X':
            consecutive += 1
            max_consecutive = max(max_consecutive, consecutive)
        else:
            consecutive = 0
    return max_consecutive >= count

def part_2(robots):
    seconds = 0
    visited = {}
    with open("results.txt", "w") as file:
        while True:
            result, grid = part_1(robots, seconds)
            grid_tuple = tuple(tuple(row) for row in grid)
            if grid_tuple in visited:
                print(f"Grid repeated at time {seconds}. Exiting loop.")
                break
            for i in range(1, len(grid)):
                row = grid[i]
                prev_row = grid[i - 1]
                if has_consecutive_robots(row, 7) and has_consecutive_robots(prev_row, 5):
                    print("Grid at time:", seconds)
                    answer = seconds
                    file.write(f"Grid at time {seconds}:\n")
                    for row in grid:
                        file.write("".join(row) + "\n")
                    break
            visited[grid_tuple] = seconds
            seconds += 1
    return answer

def main():
    robots = read_in_file("input.txt")
    result, x = part_1(robots, 100)
    print(f"Part 1 results: {result}")
    result2 = part_2(robots)
    print(f"Part 2 results: {result2}")


if __name__ == "__main__":
    main()
