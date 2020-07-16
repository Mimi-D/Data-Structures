#Data Structures and Algorithms Assignment 1
#11922023-MIRIAM DUKE

import random
#This function takes in the array size(N) and generates two lists of random elements
def listGenerator(N):
    #Initialize listA and listB as two empty lists to hold random elements
    listA=[]
    listB=[]
    #this for loop generates random number btw 1-1000 to fill the empty lists
    for i in range(N):
        n = random.randint(1, 1000)
        listA.append(n)
    for j in range(N):
        m = random.randint(1, 1000)
        listB.append(m)
    return listA,listB

#This function calculates the dot product of two one-dimensional arrays

def DotProduct():
    #Ask the user to enter the array size
    N=int(input("Kindly enter the one dimensional array size"))

    #call the list generator function to generate random elements of the arry size given
    lA,lB=listGenerator(N)

    #Print the arrays for the user to see
    print("ListA is: ",lA)
    print("ListB is : ",lB)

    #initialize the dot ptoduct to zero
    dotProduct=0

    #loop through the arrays, multiply elements at the same index of both arrays then add to dot product
    for i in range (N):
        product=lA[i]*lB[i]
        dotProduct=dotProduct+product

    #Print the result
    print("The Dot Product is ", dotProduct)




#This class is used to create points
class Point:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y

#rectangle class
class rectangle:
    #the bottom left corner and top right corner will be accessed after using the point class
    def __init__(self,bottomLeftCorner=(0,0),topRightCorner=(1,1)):

        #The x co-ordinate of the bottom right corner is same as top right corner
        self.__bottomRight=topRightCorner.x
        # The x co-ordinate of the top left corner is same as bottom left corner
        self.__topleft=bottomLeftCorner.x

        #the length is simple the distance between the x coordinates
        self.__length=topRightCorner.x-bottomLeftCorner.x
        # the breadth is simple the distance between the y coordinates
        self.__breadth = topRightCorner.y - bottomLeftCorner.y

    #function to calculate area
    def area(self):
        #Area is the length multiplied by the breadth
       area= self.__length*self.__breadth
       return area

    #function to calculate perimeter
    def perimeter(self):
        # perimeter is twice the length and breadth
       perimeter=2*(self.__length + self.__breadth)
       return perimeter

    #To find if two rectangles intersect
    #This function takes in the coordinates of the bottom left and top right corner of the second rectangle
    def intersect(self,p1,p2):
       rect= rectangle(p1,p2)

       '''if the rectangles intersect given the illustrations, then the x coordinate of the bottom right 
       of first rectangle has to be greater than the x coordinate of the top left
       of the second rectangle'''

       #Condition for intersection
       if self.__bottomRight > rect.__topleft:
           return True
       else:
           return False

#Rectangles to test all fuctions and intersection cases
#Rectangle A
A=Point(5,5)
A0=Point(11,9)
RecA=rectangle(A,A0)

#Rectangle B
B=Point(9,4)
B0=Point(14,7)
RecB=rectangle(B,B0)

#Rectangle C
C=Point(9,6)
C0=Point(14,8)
RecC=rectangle(C,C0)

#Rectangle D
D=Point(6,6)
D0=Point(10,8)
RecD=rectangle(D,D0)

#Rectangle E
E=Point(2,3)
E0=Point(7,6)
RecE=rectangle(E,E0)

#Rectangle F
F=Point(12,3)
F0=Point(18,7)
RecF=rectangle(F,F0)

#Using the functions
print("The Area of RectangleA is: ",RecA.area())
print("The Perimeter of Rectangle A is : ",RecA.perimeter())
print(" Rectangle A and Rectangle B intersect? ",RecA.intersect(B,B0))
print(" Rectangle A and Rectangle C intersect? ",RecA.intersect(C,C0))
print(" Rectangle A and Rectangle D intersect? ",RecA.intersect(D,D0))
print(" Rectangle A and Rectangle E intersect? ",RecA.intersect(E,E0))
print(" Rectangle A and Rectangle F intersect? ",RecA.intersect(F,F0))


DotProduct()