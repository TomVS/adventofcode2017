
def checksum(val):
    total = 0
    for row in val.split('\n'):
        vs = row.split()
        vs = map(int, vs)
        minVal = min(vs)
        maxVal = max(vs)
        # print "->", minVal, maxVal, "=", maxVal-minVal
        total += maxVal-minVal
    return total

def evenlyDivisibleResult(val):
    total = 0
    for row in val.split('\n'):
        vs = row.split()
        vs = sorted(map(int, vs))
        ibig = len(vs)
        found = False
        while ibig > 0 and not found:
            ismall = 0
            ibig-=1
            while ismall < ibig and not found:
                if vs[ibig]%vs[ismall] == 0:
                    found = True
                else:
                    ismall+=1
                # print " ismall", ismall, "big", ibig, "found", found
        # print "Found?", found, vs[ibig], "/", vs[ismall], "=", vs[ibig]/vs[ismall]
        total += vs[ibig]/vs[ismall]

    return total


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print "Not enough args"

    with open(sys.argv[1], 'r') as f:
        val = f.read().strip()
    if val:
        print val
        print "=================="
        print "Checksum", checksum(val)
        print "=================="
        print "Evenly Divisible", evenlyDivisibleResult(val)

