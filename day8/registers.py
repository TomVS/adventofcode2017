#! /usr/bin/python
'''
--- Day 8: I Heard You Like Registers ---

You receive a signal directly from the CPU. Because of your recent assistance with jump instructions, it would like you to compute the result of a series of unusual register instructions.

Each instruction consists of several parts: the register to modify, whether to increase or decrease that register's value, the amount by which to increase or decrease it, and a condition. If the condition fails, skip the instruction without modifying the register. The registers all start at 0. The instructions look like this:

b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10

These instructions would be processed as follows:

    Because a starts at 0, it is not greater than 1, and so b is not modified.
    a is increased by 1 (to 1) because b is less than 5 (it is 0).
    c is decreased by -10 (to 10) because a is now greater than or equal to 1 (it is 1).
    c is increased by -20 (to -10) because c is equal to 10.

After this process, the largest value in any register is 1.

You might also encounter <= (less than or equal to) or != (not equal to). However, the CPU doesn't have the bandwidth to tell you what all the registers are named, and leaves that to you to determine.

What is the largest value in any register after completing the instructions in your puzzle input?

Your puzzle answer was 5143.

--- Part Two ---

To be safe, the CPU also needs to know the highest value held in any register during this process so that it can decide how much memory to allocate to these operations. For example, in the above instructions, the highest value ever held was 10 (in register c after the third instruction was evaluated).

'''
import sys
import operator

ops = {'<': operator.lt,
       '<=': operator.le,
       '>': operator.gt,
       '>=': operator.ge,
       '==': operator.eq,
       '!=': operator.ne,
       'inc': operator.add,
       'dec': operator.sub
}

instructions = []
conditions = []
registers = {}

def parseInput(data):
    for line in data:
        tokens = line.split('if')
        if len(tokens) > 2:
            print "We have an issue"
            sys.exit(2)
        instruction = tokens[0].strip()
        condition = tokens[1].strip()
        instructions.append(instruction)
        conditions.append(condition)
        registers[instruction.split()[0]] = 0
        registers[condition.split()[0]] = 0

def processInput():
    highestValue = 0
    for i in range(len(conditions)):
        conditionTrue = False
        r, op, val = conditions[i].split()
        op_func = ops[op]
        # print r,registers[r], op, int(val)
        if op_func(registers[r], int(val)):
            conditionTrue = True
            r2, op2, val2 = instructions[i].split()
            # print " =>", r2, registers[r2], op2, val2
            op2_func = ops[op2]
            registers[r2] = op2_func(registers[r2], int(val2))
            if registers[r2] > highestValue:
                highestValue = registers[r2]
    print "Highest value held in a register:", highestValue

def getLargestValue():
    ret = None
    for r,v in registers.items():
        if not ret:
            ret = v
        if v > ret:
            ret = v
    print "Largest value in registers:", ret

def main():
    if len(sys.argv) < 2:
        print("Usage: %s <input_file>" % sys.argv[0])
        sys.exit(1)

    with open(sys.argv[1]) as f:
        data = f.readlines()
        parseInput(data)

        processInput()

        getLargestValue()


if __name__ == '__main__':
    main()
