def getFloat(fl):
    """tries to return float number from input"""
    while True:
        try:
            return float(input(fl))
        except ValueError:
            print("Give a proper value please")
            
def calcPosit(v, a, t):
    """returns distance(m) according to given parameters 
    velocity(m/s), acceleration(m/s**2) and time(s)"""
    
    return v*t+0.5*a*t**2

def printPositionBySeconds(v,a,t):
    """prints position after each second (meters from beginning)
    from start until the given time according to the given initial parameters
    velocity(m/s), acceleration(m/s**2) and time(s)"""
    
    for i in range(1,int(t)+1):
        print("position by %i seconds: %.2f m from beginning" % (i, calcPosit(v,a,i)) )
    print("final position at %.2f seconds: %.2f m from beginning" % (t, calcPosit(v,a,t)) )

#ask for required parameters to pass in for the function
v = getFloat("Give velocity (m/s): ")
a = getFloat("Give acceleration (m/s^2): ")
t = getFloat("Give time (s): ")
printPositionBySeconds(v,a,t)
