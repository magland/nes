from os import set_blocking

from nes.actions.actions import AttackAction

from ..creatures.creatures import Doge, Fairy, Fairy_Goddess, Fox


class Grove:
    def __init__(self):
        self._creatures = [
            Fox('Fox 1'),
            Doge('Doge 1'),
            Doge('Doge 2'),
            Doge('Doge 3')
        ]
        self.name = 'Grove'
        self.place_links = []
    def update(self):
        # removes all dead creatures
        self._creatures = [c for c in self._creatures if c.HP > 0]
        for c in self._creatures:
            c.update()
    def actions(self):
        a = []
        for c in self._creatures:
            a.append(AttackAction(c))
        return a
    def describe(self):
        return 'A nice grove'
    def display(self):
        print(self.describe())
        print('-------------- CREATURES -----------')
        for c in self._creatures:
            print(f'{c.name}: {c.describe()}')
    
class Fairy_Haven:
    def __init__(self):
        self._creatures = [
            Fox('Fox 1'),
            Fairy('Fairy 1'),
            Fairy('Fairy 2'),
            Fairy_Goddess('Fairy Goddess 1')
        ]
        self.name = 'Fairy Haven'
        self.place_links = []
    def update(self):
        self._creatures = [c for c in self._creatures if c.HP > 0]
        for c in self._creatures:
            c.update()
    def actions(self):
        a = []
        for c in self._creatures:
            a.append(AttackAction(c))
        return a
    def describe(self):
        return 'A magic fairy haven'
    def display(self):
        print(self.describe())
        print('-------------- CREATURES -----------')
        for c in self._creatures:
            print(f'{c.name}: {c.describe()}')
