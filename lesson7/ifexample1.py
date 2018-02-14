try:
    age = float(input("How old are you?"))
    if age<0:
        print("WTF!?")
    elif age<10:
        print("you're still a kid")
    else:
        print("you're basicly already dead")
except ValueError:
    print("You didn't give me a number")