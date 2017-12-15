#! /usr/bin/python
'''
'''
import sys

def findBase(data):
    parents = {}
    for line in data:
        parts = line.split('->')
        name = parts[0].split()[0]

        if name not in parents:
            # initialize with None. Base of tower will be only with None
            parents[name] = None

        if len(parts) > 1:
            # Has child information
            for child in parts[1].split(','):
                parents[child.strip()] = name


    for k,v in parents.items():
        if not v:
            return k

def main():
    if len(sys.argv) < 2:
        print("Usage: %s <input_file>" % sys.argv[0])
        sys.exit(1)

    with open(sys.argv[1]) as f:
        data = f.readlines()
        data = map(lambda x: x.strip(), data)

        print "Base is:", findBase(data)

if __name__ == '__main__':
    main()
