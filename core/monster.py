
#TODO

class MonStats:
    def __init__(self, values:list):
        self.hp = values[0]
        self.atk = values[1]
        self.dfc = values[2]
        self.spc = values[3]
        self.spe = values[4]
    def __str__(self):
        s = "HP: " + str(self.hp) + " ATK: " + str(self.atk) + " DEF: " + str(self.dfc) + " SPC: " + str(self.spc) + " SPE: " + str(self.spe)
        return s
    def __repr__(self):
        return self.__str__()

class MonsterDNA:
    def __init__(self, name:str):
        self.name = name
    def SetBaseStats(self, basestats:MonStats):
        self.baseStats = basestats
    def SetTypes(self, types:list):
        self.type1 = types[0]
        if (len(types)>1): 
            self.type2 = types[1]
        else:
            self.type2 = None
    def SetMovesTable(self, moves:list):
        self.moves = moves

class Monster:
    def __init__(self):
        pass

