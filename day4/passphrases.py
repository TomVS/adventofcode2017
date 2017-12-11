#! /usr/bin/python

import sys

def passphraseValidCount(data):
    totalValid = 0
    for line in data:

        split = line.split()
        origLength = len(split)
        setLength = len(set(split))

        if origLength == setLength:
            totalValid += 1
    return totalValid

def main():
    if len(sys.argv) < 2:
        print("Usage: %s <input_file>" % sys.argv[0])
        sys.exit(1)

    with open(sys.argv[1]) as f:
        data = f.readlines()

    print "Total Valid:", passphraseValidCount(data)


if __name__ == '__main__':
    main()
