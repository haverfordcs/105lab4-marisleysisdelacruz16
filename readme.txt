Lab 4: Shape Intersection
CS105, Haverford College
Due date: October 1, Midnight | submissions would be accepted through GitHub only unless stated otherwise. 

<replace with your name>

(1) Similar to the previous labs, you have to clone this repository into your local machine (PyCharm-> VCS-> Checkout from Git), 
if you are not sure how to do this, read the general instructions (https://bit.ly/2ZypGeY)

(2) Following are the list of tasks that you have to accomplish:

(a) Carefully read the ShapeIntersection.py file and write down all the possible test cases in ShapeIntersectionTestSuite.txt. 
    By all possible test cases, I mean after running your test cases, the messages mentioned in the functions of ShapeIntersection.py
    should get printed at least once. 

(b) Implement the functions as described in their body, and test them using the test suite you have prepared in step (a)

(c) Make sure your code is readable (well commented and have proper variable names)


FAQs
-------------------------------------------------
How to run test your code? 
Run the test suite using any of the following methods:

(1) Goto terminal in PyCharm execute the following command:
> python3 -m doctest -v ShapeIntersectionTestSuite.txt

(2) Alternatively, you can include the following piece of code in ShapeIntersection.py and run ShapeIntersection.py directly by right clicking inside the code window or green button (>) on the top-right corner. This method of testing shows output only for the failed cases.
import doctest
doctest.testfile("ShapeIntersectionTestSuite.txt")

-------------------------------------------------
How to get help on the working code?
To get help on your working code, please Commit and Push your code to GitHub and give us a link to your repository so we can just click the link, review your code, and make suggestions. 
