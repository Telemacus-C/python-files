shortestDistance = 0.0
dimension = int(input("please enter in the dimension you are in "))
runningTotal = 0.0

if (dimension == 0):
    print ("All distances in dimension 0 are 0")
    shortestDistance = 0.0
elif(dimension < 0):
    print ("Uh oh! Negative dimensions are too spooky for me!")
    shortestDistance = 0.0

dimensionCardinalDirectionsLeft = dimension
while(dimensionCardinalDirectionsLeft > 0 ):
    nthDistance = float(input("Input the next cardinal distance: "))
    runningTotal = runningTotal + (nthDistance)**2
    dimensionCardinalDirectionsLeft -= 1
    print("Still needed " + str(dimensionCardinalDirectionsLeft))

shortestDistance = runningTotal**(1/2)

print ("The shortest distance in your dimension : " + str(shortestDistance))
