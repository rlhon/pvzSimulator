class Zombie:
    def __init__(self, values, name, cost, jump, hp, speed, damage, tool, slow, freeze, row, col):
        self.name = name
        self.cost = cost
        self.jump = jump #int def = 1 (meaning it can't jump), 0 (it can jump once then increment)
        self.hp = hp
        self.speed = speed
        self.damage = damage 
        self.tool = tool #amount of hp of latter 
        self.slow = slow #we'll need a timer for this
        self.freeze = freeze #we'll need a timer for this
        self.row = row
        self.col = col
        self.values = values
        