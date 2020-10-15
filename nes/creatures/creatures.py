from os import name


class Pidgey:
    def __init__(self,name):
        self.name = name
        self.HP = 25
    def update(self):
        pass
    def describe(self):
        return 'A pidgey'


class Fox:
    def __init__(self,name):
        self.name = name
        self.HP = 10
    def update(self):
        pass
    def describe(self):
        return 'A red fox'
class Doge:
    def __init__(self,name):
        self.name = name
        self.HP = 20
    def update(self):
        pass
    def describe(self):
        return '''Healthy Doge
*...BORK*'''

class Rock_Troll:
    def __init__(self):
        self.name = 'Rock Troll'
        self.HP = 30
    def update(self):
        pass
    def describe(self):
        return '''Dangerous Rock Trolls roam through the forest at night, be careful!'''

class Fairy:
    def __init__(self, name):
        self.name = name
        self.HP = 6
    def update(self):
        pass
    def describe(self):
        return '''A magical fairy flutters in the air'''

class Fairy_Goddess:
    def __init__(self, name):
        self.name = name
        self.HP = 23
    def update(self):
        pass
    def describe(self):
        return '''A mystical fairy goddess sits upon her throne'''
