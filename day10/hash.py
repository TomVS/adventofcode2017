#! /usr/bin/python
'''
'''
import sys


LIST_SIZE = 256
skip_size = 0

def reverseList(clist, curPos, length):
    ret = []
    tmp = []
    looping = False
    offset = curPos+length
    loopMod = 0
    if offset > LIST_SIZE:
        # We have some looping
        tmp = clist[curPos:]
        loopMod = offset%LIST_SIZE
        # print tmp, "mod", loopMod
        tmp += clist[:loopMod]
        looping = True
    else:
        tmp = clist[curPos:offset]

    tmp.reverse()
    # print "TMP", tmp, "looping" if looping else ""
    # print "DBG", curPos, offset, loopMod
    if not looping:
        ret = clist[:curPos] + tmp[:] + clist[offset:]
    else:
        ret = tmp[-loopMod:] + clist[loopMod:curPos] + tmp[:-loopMod]
    return ret

def processInput(data):
    global skip_size
    data = data.strip().split(',')
    clist = [x for x in range(LIST_SIZE)]
    curPos = 0
    # print clist

    for l in data:
        l = int(l.strip())
        # print "# curPos", curPos, l, curPos+l, (curPos+l)%LIST_SIZE
        clist = reverseList(clist, curPos, l)
        # print "CLIST", clist

        curPos = (curPos + l + skip_size)%LIST_SIZE
        skip_size += 1
    print "First two numbers:", clist[0:2], '=', clist[0]*clist[1]


def main():
    if len(sys.argv) < 2:
        print("Usage: %s <input_file>" % sys.argv[0])
        sys.exit(1)

    with open(sys.argv[1]) as f:
        data = f.read()
        processInput(data)

if __name__ == '__main__':
    main()
