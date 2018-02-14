def getFloat(fl):
    """tries to return float number from input"""
    while True:
        try:
            return float(input(fl))
        except ValueError:
            print("Give a proper value please")

def convertToKg(lbs):
    """returns given parameter (lbs) as kilograms"""
    return lbs*0.45359237

lbs = 0
while lbs != 1:
    lbs = getFloat("Give pounds(lbs) or give 1 to quit: ")
    if (lbs != 1):
        print("%.2f kg" % convertToKg(lbs))
