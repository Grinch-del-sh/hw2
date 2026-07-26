# helicopter.py
from constans import MAX_WATER_DEFAULT, BASE_HEALTH, SHOP_COST, HOSPITAL_COST, POINTS_PER_TREE

class Helicopter:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.water = 0
        self.max_water = MAX_WATER_DEFAULT
        self.health = BASE_HEALTH
        self.points = 0

    def move(self, dx, dy, field):
        nx, ny = self.x + dx, self.y + dy
        if 0 <= nx < len(field[0]) and 0 <= ny < len(field):
            self.x, self.y = nx, ny
            return True
        return False

    def take_water(self, field):
        if field[self.y][self.x].type == 'river':
            self.water = min(self.max_water, self.water + 3)
            return True
        return False

    def extinguish(self, field):
        if self.water <= 0:
            return False
        cx, cy = self.x, self.y
        # тушим клетку под вертолётом
        if field[cy][cx].on_fire:
            field[cy][cx].on_fire = False
            field[cy][cx].type = 'burnt'
            field[cy][cx].tree_alive = False
            self.water -= 1
            self.points += POINTS_PER_TREE
            return True
        # тушим соседние клетки (4 направления)
        for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            nx, ny = cx+dx, cy+dy
            if 0 <= nx < len(field[0]) and 0 <= ny < len(field):
                if field[ny][nx].on_fire:
                    field[ny][nx].on_fire = False
                    field[ny][nx].type = 'burnt'
                    field[ny][nx].tree_alive = False
                    self.water -= 1
                    self.points += POINTS_PER_TREE
                    return True
        return False

    def use_hospital(self, field):
        if field[self.y][self.x].type == 'hospital' and self.points >= HOSPITAL_COST:
            self.health = min(BASE_HEALTH, self.health + 20)
            self.points -= HOSPITAL_COST
            return True
        return False

    def use_shop(self, field):
        if field[self.y][self.x].type == 'shop' and self.points >= SHOP_COST:
            self.max_water += 1
            self.points -= SHOP_COST
            return True
        return False

    def to_dict(self):
        return {
            'x': self.x,
            'y': self.y,
            'water': self.water,
            'max_water': self.max_water,
            'health': self.health,
            'points': self.points
        }

    @classmethod
    def from_dict(cls, data):
        h = cls(data['x'], data['y'])
        h.water = data['water']
        h.max_water = data['max_water']
        h.health = data['health']
        h.points = data['points']
        return h