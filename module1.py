# python module for list
import itertools
import inspect
import os
import functools
import random

class List:
    
    def __init__(self, LIST:list) -> list:
        # types should be same for this object
        # object type verification
        if type([]) == type(LIST)    
            self.list = LIST
        else:
            raise ValueError("Invalid Type")
        
    # representation of List object
    def __repr__(self):
        try:
            Representation = list(self.list)
            print(Representation)
        except TypeError:
            pass
        
    
    # list _append method
    def _append(self, val1:int) -> list:
        self.list[len(self.list): ] = [val1]
        
    
      