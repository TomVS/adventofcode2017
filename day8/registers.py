#! /usr/bin/python
'''

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
