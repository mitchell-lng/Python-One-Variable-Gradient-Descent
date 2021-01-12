import math

# starting value
start = 2.0
# Final Desired Output
end = 10

# Equation to be used
equation = "4**x"

# Gets output
def rfunc(x):
    # The actual function that is being solved for one var, x
    return eval(equation)

def getChange(x):
    # Alters the input to the equation very slightly
    return x * 0.0001

def gDescent():
    # Simple Gradient descent algorithm for single variable
    val = start
    # Get the absolute difference between current pos and goal and check to see if it's below the threshold, if not then keep going
    while (abs(rfunc(val) - end) > 0.0000001):
        # Alter the current input
        val += getChange(end - rfunc(val))
        print(val)
        
    print("\nUsing the equation: %s\nThe input should be %s to get to \n%s" % (equation, val, end))

gDescent()