from termcolor import colored
from core.localizing import TERMCOLORS, ColoredLocalizedText
import csv

class MonType:
    """
    The Type for "Type" of Monsters, like FIRE type, WATER type, etc.
    Usage: 
    Use MonType(name, color) to create a new MonType, its internal name will be [name], 
    and its translation key will be "types.[name]";
    [color] is the color of the MonType display, it has to be in TERMCOLORS to be valid.
    default/invalid will be "light_grey"
    """
    def __init__(self, name:str, color:str):
        self.name = name
        c = color.lower()
        if (c in TERMCOLORS):
            self.color = c
        else:
            self.color = "light_grey"
        self.text = ColoredLocalizedText("types."+self.name, self.color)
    def __str__(self):
        s = self.text.GetBracketed()
        return s
    def __repr__(self):
        return self.__str__()

class MonTypesRegistry:
    """
    Registration for Monster Types.
    """
    def __init__(self, types:list):
        self.types = types
        self.length = len(types)
        self.multipliers = {}
        for t in types:
            self.multipliers[t] = {}
            for j in types:
                self.multipliers[t][j] = 1.0
        pass
    def SetMultiplier(self, atk:MonType, dfc:MonType, value:float):
        if (atk in self.types and dfc in self.types):
            self.multipliers[atk][dfc] = value
    def RegisterExtraType(self, type:MonType):
        if (type not in self.types):
            self.types.append(type)
            self.multipliers[type] = {}
            for j in self.types:
                self.multipliers[type][j] = 1.0
    def LoadFromFile(self):
        #TODO
        pass









