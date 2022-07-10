import functools
import itertools

class Human(object):
    # python object initializer
    def __init__(self, name:str, age:str, nationality:str) -> complex:
        self.name = name
        self.age = age
        self.nationality = nationality
        

#  customized range function

def Range(first:int, second:int=None, step:int=None) -> complex:
    
    # condition for parameters
    if second is None:
        startingPoint = 0
        value = first
        Step = 1
    else:
        startingPoint = first
        value = second
        if step is None:
            Step = 1
        else:
            Step = step
    
    # iteration for creation objects 
    firstPoint = startingPoint
    while firstPoint < value:
        yield firstPoint
        firstPoint += Step
        
 # user-inputs
 
first = int(input("Enter a first number: "))
second = int(input("Enter a second number: "))
third = int(input("Enter a third number: "))
 
 
        
# prototypes
def Prototypes(val1:int, val2:int, val3:int) -> complex:
    for item in Range(val1, val2, val3):
        print(f"This is the first item: {item}")
        
Prototypes(first, second, third)
        
