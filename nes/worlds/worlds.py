from nes.actions.actions import MoveAction
from nes.creatures.creatures import Pidgey
from nes.places.places import Fairy_Haven, Grove


class World1:
    def __init__(self):
        grove = Grove()
        fairy_haven = Fairy_Haven()
        self._places = [
            grove,
            fairy_haven
        ]
        self._me = Pidgey('Pidgey')
        grove._creatures.append(self._me)

        grove.place_links.append(fairy_haven)
        fairy_haven.place_links.append(grove)
    def update(self):
        for p in self._places:
            p.update()
    def current_place(self):
        for p in self._places:
            for c in p._creatures:
                if c == self._me:
                    return p
        raise Exception('Cannot find me.')
    def describe(self):
        return 'The world #1'
    def display(self):
        print(f'You are {self._me.name}: {self._me.describe()}')
        current_place = self.current_place()
        current_place.display()
        self._actions = current_place.actions()
        for pl in current_place.place_links:
            self._actions.append(MoveAction(self, self._me, pl))
        print('---------- POSSIBLE ACTIONS ---------------')
        for ii, a in enumerate(self._actions):
            print(f'{ii + 1}) {a.describe()}')
    def run(self):
        while True:
            print('')
            print('========================================================')
            self.display()
            ii = int(input('Your action:')) - 1
            a = self._actions[ii]
            a.execute()
            self.update()
