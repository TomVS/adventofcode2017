#! /usr/bin/python

import sys

def passphraseValidCount(data):
    totalValid = 0
    totalValid2 = 0
    for line in data:

        split = line.split()
        origLength = len(split)
        setLength = len(set(split))

        if origLength == setLength:
            totalValid += 1
# now check for anagram cases (totalValid2)
            itemsMap = {}
            itemsSet = {}
            for token in split:
                l = len(token)
                if l not in itemsMap.keys():
                    itemsMap[l] = []
                    itemsSet[l] = set()
                itemsMap[l].append(token)
                orderedToken = "".join(sorted(token))
                itemsSet[l].add(orderedToken)
            allValid = True
            for k,v in itemsMap.items():
                if len(v) != len(itemsSet[k]):
                    allValid = False
            if allValid:
                totalValid2 += 1
    return totalValid, totalValid2

def main():
    if len(sys.argv) < 2:
        print("Usage: %s <input_file>" % sys.argv[0])
        sys.exit(1)

    with open(sys.argv[1]) as f:
        data = f.readlines()

    print "Total Valid (part1, part2):", passphraseValidCount(data)


if __name__ == '__main__':
    main()
