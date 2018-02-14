def getFloat(f):
    """tries to return float number from input"""
    while True:
        try:
            return float(input(f))
        except ValueError:
            print("Give a proper value please")
            
def getFloatList(size):
    """returns a list of floating point numbers with chosen size as a parameter
    """
    l = []
    for i in range(size):
        l.append(getFloat("Give a number: "))
    return list(l)
        
#returns median from already verified list of float numbers
def getMedian(l):
    """ returns the median from a list of floating point numbers (parameter: list)
    """
    #storing length in a variable -> shorter & more readable code
    ln = len(l)
    l.sort()
    #average of two middle elements if even
    if not ln % 2:
        return (l[int(ln/2)] + l[int(ln/2-1)]) / 2
    #the value of middle element if odd
    else:
        return l[int(ln/2)]

def main():
    print("Lets try getting median for list with odd amount of elements (5).")
    print("median: %.2f" % getMedian(getFloatList(5)) )
    print("Lets try getting median for list with even amount of elements (4).")
    print("median: %.2f" % getMedian(getFloatList(4)) )
    
if __name__=='__main__':
    main()
