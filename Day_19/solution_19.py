from collections import defaultdict


def read_in_file(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
        separator_index = lines.index("\n")
        towel_patterns = [pattern.strip() for pattern in lines[0].split(", ")]
        designs = [design.strip() for design in lines[separator_index + 1:]]

        return towel_patterns, designs


def can_form_design(towels, design):
    if design == "":
        return True

    for pattern in towels:
        if design.startswith(pattern):
            remaining_design = design[len(pattern):]
            if can_form_design(towels, remaining_design):
                return True
    return False


def part_1(towel_patterns, designs):
    #results = {}
    summer = 0
    for design in designs:
        x = can_form_design(towel_patterns, design)
        #results[design] = x

        if x:
            summer += 1
    #print(results)
    return summer


def process_design(towels, design):
    count = 0
    design_dict = {design: 1}

    while True:
        sub_dict = {}
        for substring, current_count in design_dict.items():
            for i in range(1, len(substring) + 1):
                front_string = substring[:i]
                if front_string in towels:
                    remaining_design = substring[i:]
                    if remaining_design == "":
                        count += current_count
                    #print("remaining_design:", remaining_design, "frontstring",front_string)
                    if remaining_design in sub_dict:
                        sub_dict[remaining_design] += current_count
                    else:
                        sub_dict[remaining_design] = current_count

        if not sub_dict:
            break

        design_dict = sub_dict

    return count


def part_2(towels, designs):
    summer2 = 0
    for design in designs:
        summer2 += process_design(towels, design)
    return summer2


def main():
    towel_patterns, designs = read_in_file("input.txt")
    #print((towel_patterns, designs))
    result = part_1(towel_patterns, designs)
    print(f"Part 1 results: {result}")
    result2 = part_2(towel_patterns, designs)
    print(f"Part 2 results: {result2}")


if __name__ == "__main__":
    main()
