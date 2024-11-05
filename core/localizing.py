import csv
import colorama
from termcolor import colored

"""
The list for valid languages.
"""
LANGS = [
    "en-us",
    "zh-cn"
]


"""
The valid color strings by termcolor.
IDK whether there is a way to add new ones like 'lime' or 'orange',
so it is currently used as-is.
"""
TERMCOLORS = [
    "black",
    "red",
    "green",
    "yellow",
    "blue",
    "magenta",
    "cyan",
    "white",
    "light_grey",
    "dark_grey",
    "light_red",
    "light_green",
    "light_yellow",
    "light_blue",
    "light_magenta",
    "light_cyan"
]


localization_dict = {}

def LoadLocalization(lang = "en-us"):
    """
    Load or Reload Localization
    lang: loaded language, only strings in LANGS are valid
    if not valid, defaulted to "en-us"
    """
    if (lang not in LANGS): 
        lang = "en-us"
    path = "localization/"+lang+".csv"
    global localization_dict
    localization_dict = {}
    with open(path, 'r', encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            localization_dict[row[0]] = row[1]
    #print(localization_dict)
    return localization_dict


class LocalizedText():
    """
    A Localized Text object
    Use a = LocalizedText(key) to create an object named "a"
    then str(a) and print(a) will automatically print the localized content
    """
    def __init__(self, key:str):
        self.key = key
    def __str__(self):
        if (self.key in localization_dict.keys()):
            return localization_dict[self.key]
        else:
            return self.key
    def __repr__(self):
        return str(self)
    

class ColoredLocalizedText(LocalizedText):
    def __init__(self, key:str, color:str):
        super().__init__(key)
        if (color in TERMCOLORS):
            self.color = color
        else:
            self.color = 'light_grey'
    def __str__(self):
        if (self.key in localization_dict.keys()):
            return colored(localization_dict[self.key], self.color)
        else:
            return colored(self.key, self.color)
    def __repr__(self):
        return str(self)
    def GetColor(self):
        return self.color
    def GetBracketed(self):
        if (self.key in localization_dict.keys()):
            return colored('['+localization_dict[self.key]+']', self.color)
        else:
            return colored('['+self.key+']', self.color)


