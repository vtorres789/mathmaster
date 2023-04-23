import math

# Defining Functions

def distance():
    print("Welcome to the Coordinate Plane Distance Solver")
    print("Enter Your Coordinate Information: ")
    x1 = int(input("X1: "))
    y1 = int(input("Y1: "))
    x2 = int(input("X2: "))
    y2 = int(input("Y2: "))

    dist = math.sqrt((math.pow((x2-x1), 2))+(math.pow((y2-y1), 2)))

    print("Your Distance between these coordinates is:")
    print(dist)

def midpoint():
    print("Welcome to the Coordinate Plane Midpoint Solver")
    print("Enter your coordinates: ")
    a1 = int(input("X1: "))
    a2 = int(input("Y1: "))
    b1 = int(input("X2: "))
    b2 = int(input("Y2: "))

    xcoord = (a1 + b1) / 2
    ycoord = (a2 + b2) / 2

    print("Your midpoint coordinate is: ")
    print("( " + str(xcoord) + ", " + str(ycoord) + " )")

def pyth_solver():
    print("Welcome to the Triangle Sides Solver")
    print("")


def trig_solver():
    print("Welcome to the Triangle Angles and Sides Solver")


# Welcome Message and Menu

print("Hi! Welcome to MATHMASTER!")
print("Please select one of the following options to continue:")

print("[1] Coordinate Plane Distance Solver")
print("[2] Coordinate Plane Midpoint Solver")
print("[3] I want to solve for missing sides in triangles")
print("[4] I want to solve for sides and/or angles in triangles")
