string = input("give any text: ")

#check if string is true (empty -> false)
if string:
    print("first letter:", string[0],"\nlast letter:", string[-1], "\nlength:", len(string))
else:
    print("invalid input, try again")

    