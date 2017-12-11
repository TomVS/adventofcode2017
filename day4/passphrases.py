#! /usr/bin/python
'''
--- Day 4: High-Entropy Passphrases ---

A new system policy has been put in place that requires all accounts to use a passphrase instead of simply a password. A passphrase consists of a series of words (lowercase letters) separated by spaces.

To ensure security, a valid passphrase must contain no duplicate words.

For example:

    aa bb cc dd ee is valid.
    aa bb cc dd aa is not valid - the word aa appears more than once.
    aa bb cc dd aaa is valid - aa and aaa count as different words.

The system's full passphrase list is available as your puzzle input. How many passphrases are valid?

Your puzzle answer was 466.
--- Part Two ---

For added security, yet another system policy has been put in place. Now, a valid passphrase must contain no two words that are anagrams of each other - that is, a passphrase is invalid if any word's letters can be rearranged to form any other word in the passphrase.

For example:

    abcde fghij is a valid passphrase.
    abcde xyz ecdab is not valid - the letters from the third word can be rearranged to form the first word.
    a ab abc abd abf abj is a valid passphrase, because all letters need to be used when forming another word.
    iiii oiii ooii oooi oooo is valid.
    oiii ioii iioi iiio is not valid - any of these words can be rearranged to form any other word.

Under this new system policy, how many passphrases are valid?

'''
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
