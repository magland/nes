class AttackAction:
    def __init__(self, target_creature):
        self._target_creature = target_creature
    def describe(self):
        return f'Attack the {self._target_creature.name} ({self._target_creature.HP} HP)'
    def execute(self):
        print(f'You are attacking the {self._target_creature.name}')
        self._target_creature.HP = self._target_creature.HP + -7

class MoveAction:
    def __init__(self, world, creature, place):
        self._world = world
        self._creature = creature
        self._place = place
    def describe(self):
        return f'Go to {self._place.name}'
    def current_place(self):
        for p in self._world._places:
            for c in p._creatures:
                if c == self._creature:
                    return p
        raise Exception('Cannot find creature.')
    def execute(self):
        p = self.current_place()
        p._creatures = [c for c in p._creatures if c != self._creature]
        self._place._creatures.append(self._creature)
