#! /usr/bin/python
'''
'''
import sys

def processGroup(data, index=1, p_score=0):
    my_score = p_score+1
    total_score = my_score
    i = index
    isGarbage = False

    while i < len(data):
        c = data[i]
        if c == '!':
            i+=1 # skip next char
        elif not isGarbage:
            if c == '<':
                isGarbage = True
            elif c == '}': # found closing token for this group
                break
            elif c == '{':
                s, new_index = processGroup(data, i+1, my_score)
                total_score += s
                i = new_index
        else: # garbage
            if c == '>':
                isGarbage = False
        i+=1

    # print "running score", total_score
    return total_score, i

def parseInput(data):
    data = data.strip()
    finalScore, index = processGroup(data)
    print "Final Group Score:", finalScore

def main():
    if len(sys.argv) < 2:
        print("Usage: %s <input_file>" % sys.argv[0])
        sys.exit(1)

    with open(sys.argv[1]) as f:
        data = f.read()
        parseInput(data)

if __name__ == '__main__':
    main()
