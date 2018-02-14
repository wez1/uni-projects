def getNameList():
    """returns a list of names prompted from user"""
    a = []
    while True:
        name = input("Give name or leave blank to stop: ").title().strip()
        if (name): a.append(name)
        else: return a
    
def main():
    """The main program loop"""
    l = getNameList()
    l.sort()
    print(*l, sep=', ')
    print("There were",len(l),"names in the list")
    print("There were", l.count("Jack"), "Jacks in the list")
    
if __name__=='__main__':
    main()
