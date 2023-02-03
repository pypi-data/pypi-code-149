from enum import Enum
import random

from .regex import NameList

class NameType(Enum):
    """The types of name that a Toon could have."""
    FULL = 1
    FIRST = 2
    LAST = 3
    FIRSTLAST = 4
    TITLEFIRST = 5
    TITLELAST = 6


class Name:
    """A Name that can be given to a Toon."""
    def __init__(self,type:str=NameType.FULL,title:str="",first:str="",last1:str="",last2:str=""):
        self.type = type
        self.title = title
        match self.type:
            case NameType.FIRST:
                self.first = first.title() # This is done in the case that "Von" is the name of the toon, but this is also compatible with custom names where similar behavior is wanted.
            case NameType.FIRSTLAST:
                self.first = first.title()
            case _:
                self.first = first
        self.last1 = last1
        if self.last1 in ["O'","Mc","Mac"]: # This is done so that if one of these is selected as the first part of the last name, the second part is capitalized. There's probably an easier way to do this but WHATEVER
            self.last2 = last2.title()
        else:
            self.last2 = last2
    
    def random(list:NameList):
        """Generate a completely random name from a given list."""
        type = random.choice([NameType.FULL,NameType.FIRST,NameType.FIRSTLAST,NameType.LAST,NameType.TITLEFIRST,NameType.TITLELAST])
        return Name(type,
        title=random.choice(list.title),
        first=random.choice(list.first),
        last1=random.choice(list.last1),
        last2=random.choice(list.last2))
        
    def to_string(self):
        """Converts a Name to a String"""
        match self.type:
            case NameType.FULL:
                return self.title+" "+self.first+" "+self.last1+self.last2
            case NameType.FIRST:
                return self.first
            case NameType.LAST:
                return self.last1+self.last2
            case NameType.FIRSTLAST:
                return self.first+" "+self.last1+self.last2
            case NameType.TITLEFIRST:
                return self.title+" "+self.first
            case NameType.TITLELAST:
                return self.title+" "+self.last1+self.last2