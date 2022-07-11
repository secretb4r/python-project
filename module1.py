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
        if type([]) == type(LIST):
          self.list = LIST
        else:
            raise ValueError("Invalid Type")
        
    # representation of List object
    def __repr__(self):
        Representation = self.list
        return f"{Representation}"

    # def __str__(self):
    #   return f"{self.list}"
    
    # list _append method
    def _append(self, val1:int) -> list:
      self.list[len(self.list): ] = [val1]

  # list _index method
    def _index(self, value:any) -> int:
      # condition
      if value not in self.list:
        return f"item not in list"
      # index verifier
      location = -1
      for item in self.list:
        location += 1
        if item == value:
          return location

    # list count method
    def _count(self, value:any) -> int:
      count = 0
      for item in self.list:
        if item == value:
          count += 1
      return count

    # list _clear method
    def _clear(self):
      self.list = []
      return self.list    

    # list _copy methods
      def _copy(self,_list):
        _list = self.list
        return _list
        
    
      
