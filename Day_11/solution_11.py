def read_in_file(filename):
    with open(filename, 'r') as file:
        line = file.readline().strip()
    initial_stones = list(map(int, line.split()))
    return initial_stones

def process_stone(number):
    number_str = str(number)

    if number == 0:
        return [1]

    if len(number_str) % 2 == 0:
        mid = len(number_str) // 2
        left = int(number_str[:mid])
        right = int(number_str[mid:])
        return [left, right]

    return [number * 2024]

def part_1(stones, blinks):
    for x in range(blinks):
        new_stones = []
        for stone in stones:
            new_stones.extend(process_stone(stone))
        stones = new_stones
    return len(stones)


def main():
    blinks = 25
    stones_list = read_in_file("input.txt")
    result = part_1(stones_list, blinks)
    print(f"Part 1 results: {result}")

if __name__ == "__main__":
    main()