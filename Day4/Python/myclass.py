#!/usr/bin/python

class Point:
   #The function below is a special function called constructor
   #The constructor function will get invoked automatically when
   #you create an object of this class
   def __init__(self, val1=0, val2=0):
       self.x = val1
       self.y = val2

   def setValues(self, val1, val2):
       self.x = val1
       self.y = val2

   def printValues(self):
       print ( 'The value of x is ', self.x )
       print ( 'The value of y is ', self.y )

#The main function is an user-defined function in Python
#As main is not an entrypoint function in PYthon
def main():
    pointOne = Point()
    pointOne.setValues( 10, 20 )
    pointOne.printValues( )

    pointTwo= Point( 20, 30 )
    pointTwo.printValues( )

main()
