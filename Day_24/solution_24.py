from collections import defaultdict


def do_operation(value1, value2, operation):
    if operation == "XOR":
        return int(value1) ^ int(value2)
    elif operation == "OR":
        return int(value1) | int(value2)
    else:
        return int(value1) & int(value2)


def read_in_file(filename):
    with open(filename, "r") as file:
        data = file.read()

    start_values, start_operations = data.split("\n\n")
    #print(start_values)
    #print(start_operations)
    values = defaultdict(set)

    for line in start_values.splitlines():
        before, after = line.split(": ")
        values[before].add(after)

    operations_list_1 = []
    operations_list_2 = []
    for line in start_operations.splitlines():
        parts = line.split()
        value1 = parts[0]
        operation = parts[1]
        value2 = parts[2]
        result = parts[4]

        if value1 in values and value2 in values:
            value1_value = list(values[value1])[0]
            value2_value = list(values[value2])[0]
            operation_result = do_operation(value1_value, value2_value, operation)
            values[result].add(operation_result)
        elif result.startswith("z"):
            operations_list_2.append({
                "value1": value1,
                "operation": operation,
                "value2": value2,
                "result": result,
            })
        else:
            operations_list_1.append({
                "value1": value1,
                "operation": operation,
                "value2": value2,
                "result": result,
            })
    #print(values)
    return values, operations_list_1, operations_list_2


def do_steps(values, operations_list):
    while operations_list:
        current_operations_list = operations_list[:]
        for operation in current_operations_list:
            value1 = operation["value1"]
            value2 = operation["value2"]
            operation_type = operation["operation"]
            result = operation["result"]
            if value1 in values and value2 in values:
                value1_value = list(values[value1])[0]
                value2_value = list(values[value2])[0]
                operation_result = do_operation(value1_value, value2_value, operation_type)
                values[result].add(operation_result)
                operations_list.remove(operation)


def part_1(values, operations_list_1, operations_list_2):
    do_steps(values, operations_list_1)
    do_steps(values, operations_list_2)
    z_keys = [key for key in values if key.startswith("z")]
    z_keys_sorted = sorted(z_keys, key=lambda key: int(key[1:]), reverse=False)
    summer = 0
    position = 0
    for key in z_keys_sorted:
        value = next(iter(values[key]))
        if value == 1:
            summer += 2 ** position
        position += 1
    return summer


def main():
    values, operations_list_1, operations_list_2 = read_in_file("input.txt")
    result = part_1(values, operations_list_1, operations_list_2)
    print(f"Part 1 results: {result}")


if __name__ == "__main__":
    main()
