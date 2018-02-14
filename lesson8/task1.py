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

#calculates the average from the already verified list of float numbers      
def getAverage(numlist):
    """calculates and returns the average from a list of floating point numbers
    """
    return sum(numlist)/len(numlist)
    
def main():
    print("average: %.2f" % getAverage(getFloatList(5)) )

if __name__=='__main__':
    main()
