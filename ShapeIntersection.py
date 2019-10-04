import math
def isAValidPoint(x, y):
    # This function receives a tuple of two elements and checks
    # If both elements of the tuple are real numbers then
    # prints "The elements of the tuple are real and valid coordinate of a point" and returns True
    # Else raises an exception with message "The coordinates are unreal" and returns False

    P = (x, y)

    if isinstance(P[0], int):
        isinstance(P[1], int)
        print("The elements of the tuple are real and valid coordinate of a point")
        return True
    elif isinstance(P[0], int):
        isinstance(P[1], float)
        print("The elements of the tuple are real and valid coordinate of a point")
        return True
    elif isinstance(P[0], float):
        isinstance(P[1], int)
        print("The elements of the tuple are real and valid coordinate of a point")
        return True
    elif isinstance(P[0], float):
        isinstance(P[1], float)
        print("The elements of the tuple are real and valid coordinate of a point")
        return True
    else:
        print("The coordinates are unreal")
        return False
    pass


def isARectangle(Rect):
    # This function assumes Rect is a list of four tuples, each with two elements
    # Check if tuples are valid points -- calls isAValidPoint(P) function
    # It returns True if the points supplied to it form a rectangle, otherwise it returns False

    p1, p2, p3, p4 = Rect  # p1,p2,p3, and p4 are points of the rectangle
    xp1, yp1 = p1  # giving the coordinates to each point after passing stage 1
    xp2, yp2 = p2
    xp3, yp3 = p3
    xp4, yp4 = p4

    p1= Rect[0]
    p2= Rect[1]
    p3= Rect[2]
    p4= Rect[3]

    if isAValidPoint(xp1,yp1) and isAValidPoint(xp2,yp2) and isAValidPoint(xp3,yp3) and isAValidPoint(xp4,yp4):

        # creating the sides of the rectangle using the x and y values if the points
        sidep1p4 = math.sqrt(((xp1 - xp4) ** 2) + ((yp1 - yp4) ** 2))
        sidep3p2 = math.sqrt(((xp3 - xp2) ** 2) + ((yp3 - yp2) ** 2))
        sidep1p2 = math.sqrt(((xp1 - xp2) ** 2) + ((yp1 - yp2) ** 2))
        sidep3p4 = math.sqrt(((xp3 - xp4) ** 2) + ((yp3 - yp4) ** 2))

        # making sure the diagonals are equal to each other to confirm it is a rectangle
        diap1p3 = math.sqrt(((xp1 - xp3) ** 2) + ((yp1 - yp3) ** 2))
        diap2p4 = math.sqrt(((xp2 - xp4) ** 2) + ((yp2 - yp4) ** 2))

        if sidep1p4 == sidep3p2 and sidep1p2 == sidep3p4 and diap1p3 == diap2p4:  # if the opposing sides are equal and the diagonals are equal then the points create a rectangle
            return True, p1, p2, p3, p4  # points to call the function in isRectangleParalleltoAxis and doesIntersectRect
        else:
            return False
    else:
        return False

    pass  # can move on to the next stage to see if the rectangle is parallel to the x axis


def isRectangleParallelToXAxis(Rect):
    # This function assumes Rect is a list of four tuples, each with two elements
    # It assumes that the supplied set of tuples form a rectangle
    # It returns True if the rectangle is parallel to x-axis, otherwise it returns False

    p1, p2, p3, p4 = Rect  # creating the points for the rectangle

    xp4, yp4 = p4
    xp3, yp3 = p3
    xp2, yp2 = p2
# comparing the y coordinates of side p3 to p4 and p2 to check if parallel to x axis
    if yp3 == yp4 or yp3 == yp2:
        return True
    else:
        return False
    pass


def doesIntersectRect(Rect1, Rect2):

    # Print OR raise one of the following messages based on the values supplied to Rect1, and Rect2
    # "Points supplied for both Rect1 and Rect2 do not form rectangle"
    # "Points supplied for Rect1 form a rectangle but points supplied for Rect2 do not"
    # "Points supplied for Rect2 form a rectangle but points supplied for Rect1 do not"
    # "Points supplied for both Rect1 and Rect2 for rectangles"

    # If both Rect1 and Rect2 form two rectangles then check if they are parallel to x - axis
    # Print OR raise one of the following messages as appropriate
    # Neither Rect1 and nor Rect2 is parallel to x-axis
    # Rect1 is parallel to x-axis while Rect2 is not
    # Rect2 is parallel to x-axis while Rect1 is not
    # Both Rect1 and Rect2 are parallel to x-axis

    # If the Points supplied for both Rect1 and Rect2 form rectangles AND
    # Both Rect1 and Rect2 are parallel to x-axis THEN
    # Check if they intersect or overlap with each other
    # Print one of the following messages as appropriate as well as return True or False
    # "Rect1 and Rect2 overlap with each other"  and return True
    # "Rect1 and Rect2 do not overlap with each other" and Return False


    # Using booleans: If Rect1 is a rectangle then boolRect1 has a truth value of true, if not a rectangle then false (same for rect 2)
    if isARectangle(Rect1):
        boolRect1 = True
    else:
        boolRect1 = False

    if isARectangle(Rect2):
        boolRect2 = True
    else:
        boolRect2 = False

    if boolRect1 is False and boolRect2 is False:
        print("Points supplied for both Rect1 and Rect2 do not form rectangles")
        boolRectangles = False  # boolRectangles combines both boolRect1 and boolRect2
        return False

    elif boolRect1 is True and boolRect2 is False:
        print("Points supplied for Rect1 form a rectangle but points supplied for Rect2 do not")
        boolRectangles = False
        return False
    # can't be true unless all points supplied form two rectangles
    elif boolRect1 is False and boolRect2 is True:
        print("Points supplied for Rect2 form a rectangle but points supplied for Rect1 do not")
        boolRectangles = False
        return False

    elif boolRect1 is True and boolRect2 is True:
        print("Points supplied for both Rect1 and Rect2 for rectangles")
        boolRectangles = True


# Parallel to x axis
    if boolRectangles is True:
        if isRectangleParallelToXAxis(Rect1):
            boolRect1Parallel = True
        else:
            boolRect1Parallel = False
        if isRectangleParallelToXAxis(Rect2):
            boolRect2Parallel = True
        else:
            boolRect2Parallel = False

        if boolRect1Parallel is False and boolRect2Parallel is False:
            print("Neither Rect1 and nor Rect2 is parallel to x-axis")
            boolRectanglesParallel = False
        elif boolRect1Parallel is True and boolRect2Parallel is False:
            print("Rect1 is parallel to x - axis while Rect2 is not")
            boolRectanglesParallel = False

        elif boolRect1Parallel is False and boolRect2Parallel is True:
            print("Rect2 is parallel to x-axis while Rect1 is not")
            boolRectanglesParallel = False

        elif boolRect1Parallel is True and boolRect2Parallel is True:
            print("Both Rect1 and Rect2 are parallel to x-axis")
            boolRectanglesParallel = True
    else:
        return False

#Check if the rectangles intersect
    if isRectangleParallelToXAxis(Rect1) is True and isRectangleParallelToXAxis(Rect2) is True:
# To find minimum and maximum value of x and y in Rect1 List
        xminR1= Rect1[0][0]
        xmaxR1= Rect1[0][0]

        for point in Rect1:
            if point[0]< xminR1:
                xminR1=point[0]
            if point[0]> xmaxR1:
                xmaxR1=point[0]

        yminR1= Rect1[0][1]
        ymaxR1= Rect1[0][1]

        for point in Rect1:
            if point[1]< yminR1:
                yminR1=point[1]
            if point[1]> ymaxR1:
                ymaxR1= point[1]
# To find minimum and maximum value of x and y in Rect2 List
        xminR2 = Rect2[0][0]
        xmaxR2 = Rect2[0][0]

        for point in Rect2:
            if point[0] < xminR2:
                xminR2 = point[0]
            if point[0] > xmaxR2:
                xmaxR2 = point[0]

        yminR2 = Rect2[0][1]
        ymaxR2 = Rect2[0][1]

        for point in Rect2:
            if point[1] < yminR2:
                yminR2 = point[1]
            if point[1] > ymaxR2:
                ymaxR2 = point[1]

#Combining x and y min values and x and y max values for conditions
        min1= xminR1 and yminR1
        max1= xmaxR1 and ymaxR1
        min2= xminR2 and yminR2
        max2= xmaxR2 and xmaxR2

        if (min1 >= min2) and (max2 >= min1):
            print ("Rect1 and Rect2 overlap with each other")
            return True
        elif (min2 >= min1) and (max1 >= min2):
            print ("Rect1 and Rect2 overlap with each other")
            return True
        elif (min2 >= min1) and (max1 >= max2):
            print ("Rect1 and Rect2 overlap with each other")
            return True
        elif (min1 >= min2) and (max2 >= max1):
            print("Rect1 and Rect2 overlap with each other")
            return True
        else:
            print("Rect1 and Rect2 do not overlap with each other")
            return False

    pass

   
def doesIntersectCirc(Circ1, Circ2):
    #distance between center and add radii and value has to be greater than or equal to distance

            # Check if centers of the circles are valid points --calls isAValidPoint function
            # Print one of the following, value has messages as appropriate
            # (i) "Both, center of Circ1 and center of Circ2 are valid points"
            # (ii) "Center of Circ1 is a valid point but Center of Cir2 is not"
            # (iii) "Center of Circ2 is a valid point but Center of Cir1 is not"
            # (iv) "Neither center of Circ1 is a valid point nor the Center of Cir2"

            # If (i) is the case, then check if radii of the circles are valid
            # -- think what type of values should be allowed for radius and program accordingly
            # Print one of the following messages as appropriate
            # (i) "Both, radius of Circ1 and radius of Circ2 are valid"
            # (ii) "Radius of Circ1 is a valid but Radius of Cir2 is not"
            # (ii) "Radius of Circ2 is a valid but Radius of Cir1 is not"
            # (iv) "Neither the Radius of Circ1 is a valid nor the Radius of Cir2"

            # If centers of both Circ1 and Circ2 are valid points, AND radii of Circ1 and Cir2 are valid then
            # Check if given circles intersect/overlap or not
            # Print one of the following messages and return True or False
            # "Circ1 and Cir2 intersect with each other" and return True
            # "Circ1 and Cir2 does not intersect with each other" and return False

    [(x, y), z] = Circ1
    [(a, b), c] = Circ2
    if isAValidPoint(Circ1[0][0],Circ1[0][1]) is True and isAValidPoint(Circ2[0][0],Circ2[0][1]) is True:
        print("Both, center of Circ1 and center of Circ2 are valid points")
        if Circ1[1] > 0 and Circ2[1] > 0 and isinstance(Circ1[1], int) or isinstance(Circ1[1], float) and isinstance(Circ2[1], int) or isinstance(Circ2[1], float):
            print("Both, radius of Circ1 and radius of Circ2 are valid")
            if math.sqrt((Circ2[0][0] - Circ1[0][0]) ** 2 + (Circ2[0][1] - Circ1[0][1]) ** 2) <= Circ1[1] + Circ2[1]:
                print("Circ1 and Cir2 intersect with each other")
                return True
            else:
                print("Circ1 and Cir2 does not intersect with each other")
                return False

        elif Circ1[1] > 0 and Circ2[1] < 0 and isinstance(Circ1[1], int) or isinstance(Circ1[1], float) and isinstance(Circ2[1], int) or isinstance(Circ2[1], float):
            print("Radius of Circ1 is a valid but Radius of Cir2 is not")

        elif Circ1[1] < 0 and Circ2[1] > 0 and isinstance(Circ1[1], int) or isinstance(Circ1[1], float) and isinstance(Circ2[1], int) or isinstance(Circ2[1], float):
            print("Radius of Circ2 is a valid but Radius of Cir1 is not")

        elif Circ1[1] < 0 and Circ2[1] < 0 and isinstance(Circ1[1], int) or isinstance(Circ1[1], float) and isinstance(Circ2[1], int) or isinstance(Circ2[1], float):
            print("Neither the Radius of Circ1 is a valid nor the Radius of Cir2")

    elif isAValidPoint(Circ1[0][0],Circ1[0][1]) is True and isAValidPoint(Circ2[0][0],Circ2[0][1]) is False:
        print("Center of Circ1 is a valid point but Center of Cir2 is not")

    elif isAValidPoint(Circ1[0][0],Circ1[0][1]) is False and isAValidPoint(Circ2[0][0],Circ2[0][1]) is True:
        print("Center of Circ2 is a valid point but Center of Cir1 is not")

    elif isAValidPoint(Circ1[0][0],Circ1[0][1]) is False and isAValidPoint(Circ2[0][0],Circ2[0][1]) is False:
        print("Neither center of Circ1 is a valid point nor the Center of Cir2")

    pass



# Testing for the test cases available in the test suite
import doctest
doctest.testfile("ShapeIntersectionTestSuite.txt")

# In case you want to test for particular test case locally,
# Comment the above two lines of code and uncomment the following
if __name__ == "__main__":
#     #Driver code
#     # Creating rectangles
    Rect1 = [(0,0),(0,1),(1,1),(1,0)]
    Rect2 = [(0,0),(0,2),(2,2),(2,0)]
#     # Checking whether Rect1 and Rect2 intersect
    doesIntersectRect(Rect1,Rect2)

 # Creating circles using a tuple and a non-negative real number
    Circ1 = [(0,0),4]
    Circ2 = [(1,1),3]
#     # Checking whether Rect1 and Rect2 intersect
    doesIntersectCirc(Circ1,Circ2)

# I worked on this code with Henry Moore, Raveen Green, Naomi Kalombl