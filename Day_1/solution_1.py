
def read_in_file(filename="input.txt"):
    left = []
    right =[]
    with open(filename, "r") as file:
        for line in file:
            parts = line.split()
            left.append(int(parts[0]))
            right.append(int(parts[1]))

    left = sorted(left)
    right = sorted(right)

    return left, right


def part1(left, right):
    summer = 0
    for x in range(len(left)):
        summer += abs(left[x] - right[x])
    return summer

def part2(left, right):
    left_set = set(left)
    right_counts = {}
    for num in right:
        if num in right_counts:
            right_counts[num] += 1
        else:
            right_counts[num] = 1
    summer = 0
    for num in left_set:
        if num in right_counts:
            summer += num*right_counts[num]
    return summer

def main():
    left, right = read_in_file("input.txt")
    result = part1(left, right)
    print(f"Part 1 results: {result}")
    result = part2(left, right)
    print(f"Part 2 results: {result}")


if __name__ == "__main__":
    main()
