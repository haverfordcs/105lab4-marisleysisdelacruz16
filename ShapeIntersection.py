def isAValidPoint(P):
    # This function receives a tuple of two elements and checks
    # If both elements of the tuple are real numbers then
    # prints "The elements of the tuple are real and valid coordinate of a point" and returns True
    # Else raises an exception with message "The coordinates are unreal" and returns False
    pass

def isARectangle(Rect):
    # This function assumes Rect is a list of four tuples, each with two elements
    # Check is tuples are valid points -- calls isAValidPoint(P) function
    # It returns True if the points supplied to it form a rectangle, otherwise it returns False

    #<Write your logic for finding out if four given coordinates form a rectangle>
    pass


def isRectangleParallelToXAxis(Rect):
    # This function assumes Rect is a list of four tuples, each with two elements
    # It assumes that the supplied set of tuples form a rectangle
    # It returns True if the rectangle is parallel to x-axis, otherwise it returns False
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

    pass



def doesIntersectCirc(Circ1, Circ2):
    # Check if centers of the circles are valid points --calls isAValidPoint function
    # Print one of the following messages as appropriate
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
    pass


# Testing for the test cases available in the test suite
import doctest
doctest.testfile("ShapeIntersectionTestSuite.txt")



# In case you want to test for particular test case locally, 
# Comment the above two lines of code and uncomment the following
# if __name__ == "__main__":
#     #Driver code
#     # Creating rectangles
#     Rect1 = [(0,0),(0,1),(1,1),(1,0)]
#     Rect2 = [(0,0),(0,2),(2,2),(2,0)]
#     # Checking whether Rect1 and Rect2 intersect
#     doesIntersectRect(Rect1,Rect2)

#     # Creating circles using a tuple and a non-negative real number
#     Circ1 = [(0,0),4]
#     Circ2 = [(1,1),3]
#     # Checking whether Rect1 and Rect2 intersect
#     doesIntersectCirc(Circ1,Circ2)
