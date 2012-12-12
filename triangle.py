import os
import sys
import time

def parse_file(txt_file):

    """ 
        Parses file and generates list of lists. Raises exception, if the file is not in proper format. 
        List comprehension can't be used here as it is not possible to raise exception. 
    """

    ll_numbers = []
    try:
        f = open(txt_file)
        for i, l in enumerate(f):
            splitted = l.split()
            if not len(splitted) == i + 1:
                raise Exception, "Not in proper format at line: %s" % (i + 1)
            ll_numbers.append([int(n) for n in splitted])
            #ll_numbers = [[int(n) for n in l.split()] for i, l in enumerate(f) if not len(l.split()) == i+1: raise Exception]
        return ll_numbers
    except Exception, e:
        print "Exception while parsing:", e
        sys.exit(1)

def forloop(ll_numbers):

    """ Iterates through 'll_numbers' using for loop """

    num = 0
    path = []
    for l_num in ll_numbers:
        if len(l_num) == 1:
            num = l_num[0]
            path.append(num)
            index = 0
        else:
            numbers = l_num[index:index+2]
            val = numbers[0] if numbers[0] > numbers[1] else numbers[1]
            index = l_num.index(val)
            path.append(val)
            num += val
    return path, num

def using_static(l_list, index = [0]):

    """ Using static variable to remember index """
    
    if len(l_list) == 1:
        return l_list[0]
    else:
        sliced = l_list[index[-1]:index[-1]+2]
        val = sliced[0] if sliced[0] > sliced[1] else sliced[1]
        index.append(l_list.index(val))
        return val
   
index = 0
def using_global(l_list):
    
    """ Using static variable to remember index """

    global index
    if len(l_list) == 1:
        return l_list[0]
    else:
        sliced = l_list[index: index+2]
        val = sliced[0] if sliced[0] > sliced[1] else sliced[1]
        index = l_list.index(val)
        return val

if __name__ == "__main__":
    
    if len(sys.argv) != 2:
        print "Please provide filename as the argument"
        sys.exit(0)
        
    ll_numbers = parse_file(sys.argv[1])

    start = time.time()
    print "=" * 40 + " Normal method " + "=" * 40
    path, total = forloop(ll_numbers)
    print "Longest path '%s' and its weight is %s:" % ("-->".join([str(i) for i in path]), total)
    print "TIME TAKEN:", time.time() - start , "seconds"
    print "=" * 40 + " Using static " + "=" * 40
    
    start = time.time()
    path = [using_static(l) for l in ll_numbers]
    total = sum(path)
    print "longest path '%s' and its weight is %s:" % ("-->".join([str(i) for i in path]), total)
    print "time taken:", time.time() - start , "seconds"
    print "=" * 40 + " Using global " + "=" * 40

    start = time.time()
    path = [using_global(l) for l in ll_numbers]
    total = sum(path)
    print "longest path '%s' and its weight is %s:" % ("-->".join([str(i) for i in path]), total)
    print "time taken:", time.time() - start , "seconds"
    print "=" * 90

