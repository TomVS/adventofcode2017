

def doubleSum(val):
    total = 0
    for i,v in enumerate(val):
        if val[i-1] == v:
            # same!
            total += int(v)
    return total


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print "Not enough args"

    with open(sys.argv[1], 'r') as f:
        val = f.read().strip()
    if val:
        print val
        print "TADAA:", doubleSum(val)
