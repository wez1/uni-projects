#Make a program which reads a text file, which can have any number of floating point numbers,
#which are all in their own lines. The program will calculate and display the sum
# and average (mean) of all these numbers. Make your program fool proof. 
#It should handle all common errors and ignore those lines of the input text file,
#which don't have valid numbers.

def getNumbersFromFile(fileName):
    """returns a list of all the floats from a given txt file"""
    lines = []
    with open(fileName, 'r') as f:
        for line in f:
            line = line.strip('\n')
            try:
               lines.append(float(line))
            except:
                continue
    return lines
    
def sumFloats(l):
    """returns a sum of floats from given list"""
    try:
        s = sum(l)
        return s
    except:
        print("Something went wrong while summing!")

def main():
    """ main program loop"""
    print(getNumbersFromFile("nums.txt"))
    print(sumFloats(getNumbers("nums.txt")))
    
if __name__=='__main__':
    main()
