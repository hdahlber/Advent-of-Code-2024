import time

A, B, C = 0, 0, 0
x = 0
part1_list = []


def read_in_file(filename):
    with open(filename, "r") as file:
        lines = file.readlines()

    program = []
    global A, B, C
    for line in lines:
        line = line.strip()
        if line.startswith("Register A"):
            A = int(line.split(":")[1].strip())
        elif line.startswith("Register B"):
            B = int(line.split(":")[1].strip())
        elif line.startswith("Register C"):
            C = int(line.split(":")[1].strip())
        elif line.startswith("Program:"):
            program = [int(x.strip()) for x in line.split(":")[1].split(",")]

    return program


def adv(operation_num, literal):
    global A
    A = A // (2 ** operation_num)


def bxl(operation_num, literal):
    global B
    B = B ^ literal


def bst(operation_num, literal):
    global B
    B = operation_num % 8


def jnz(operation_num, literal):
    global A, x
    if A != 0:
        x = literal
    else:
        x += 2


def bxc(operation_num, literal):
    global B, C
    B = B ^ C


def out(operation_num, literal):
    global part1_list
    part1_list.append(operation_num % 8)


def bdv(operation_num, literal):
    global A, B
    B = A // (2 ** operation_num)


def cdv(operation_num, literal):
    global A, C
    C = A // (2 ** operation_num)


function_list = [adv, bxl, bst, jnz, bxc, out, bdv, cdv]


def get_operand_value(operand):
    if operand <= 3:
        return operand
    elif operand == 4:
        return A
    elif operand == 5:
        return B
    elif operand == 6:
        return C


def part_1(program):
    global A, B, C, x
    while 0 <= x < len(program):
        opcode = program[x]
        literal = program[x + 1]
        operand_value = get_operand_value(literal)

        function_list[opcode](operand_value, literal)
        """
        print("a ", A, "b ", B, "c ", C, "lit ", literal, "oper ", operand_value, function_list[opcode].__name__)
        if opcode == 5:
            print("----------")
        """
        if opcode != 3:
            x += 2

    return part1_list


# ADV: lit = oper so A = A// (2**lit) and A = A// (2**oper)
# BXL: lit is always 7 on first round so B= B^7 on second B = B^4
# BST: B = A % B
# JNZ: lit= oper= 0 so loop back
# BXC: B = B ^ C
# Out: B%8
# BDV: Never used
# CDV: C = A // (2**B)
# order:
# 1:           bst, bxl, cdv, bxc, bxl, out
# 2: adv, jnz, bst, bxl, cdv, bxc, bxl, out
# 3: adv, jnz, bst, bxl, cdv, bxc, bxl, out
# 4: adv, jnz, bst, bxl, cdv, bxc, bxl, out
# 5: adv, jnz, bst, bxl, cdv, bxc, bxl, out
# 6: adv, jnz, bst, bxl, cdv, bxc, bxl, out
# 7: adv, jnz, bst, bxl, cdv, bxc, bxl, out
def single_loop(A):
    B = A % 8  # Bst
    B = B ^ 7  # bxl first
    C = A // (2 ** B)  # cdv
    B = B ^ 4  # bxc
    B = B ^ C  # bxl second
    return B % 8  # out


def find_iterative(program):
    stack = [(x, 0) for x in range(8)] # loop 3 bit
    solutions = []

    while stack:
        print(stack)
        A, col = stack.pop()

        if single_loop(A) != program[-(col + 1)]:  # STOP ELSE
            continue

        if col == len(program) - 1: # needs to be 15 length
            solutions.append(A)
        else:
            for B in range(8):
                stack.append((A * 8 + B, col + 1))

    return solutions


def part_2(program):
    solutions = find_iterative(program)
    return min(solutions)


def main():
    program = read_in_file("input.txt")
    result = part_1(program)
    result = ','.join(map(str, result))
    print("part 1: ", result)
    result2 = part_2(program)
    print("part 2: ", result2)


if __name__ == "__main__":
    main()
