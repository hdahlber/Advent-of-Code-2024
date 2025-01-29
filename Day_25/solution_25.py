def read_in_file(filename):
    with open(filename, "r") as file:
        data = file.read()
    blocks = data.strip().split("\n\n")
    keys = []
    locks = []
    for block in blocks:
        block_lines = block.split("\n")
        if block_lines[0][0] == "#":
            remaining_lines = block_lines[1:]
            heights = []
            for col_idx in range(len(block_lines[0])):
                for row_idx, line in enumerate(remaining_lines):
                    if line[col_idx] == ".":
                        heights.append(row_idx)
                        break
            locks.append(heights)
        else:
            remaining_lines = block_lines[1:]
            heights = []
            for col_idx in range(len(block_lines[0])):
                for row_idx, line in enumerate(remaining_lines):
                    if line[col_idx] == "#":
                        heights.append(len(block_lines[0])-row_idx)
                        break
            keys.append(heights)

    print(locks)
    print(keys)
    return locks,keys

def part_1(locks,keys):
    summer = 0
    for key in keys:

        for lock in locks:
            valid = True
            for k, l in zip(key, lock):
                if k + l > 5:
                    valid = False
                    break
            if valid:
                summer += 1
    return summer

def main():
    locks,keys = read_in_file("input.txt")
    result = part_1(locks,keys)
    print(f"Part 1 results: {result}")


if __name__ == "__main__":
    main()