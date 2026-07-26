# cell.py
import constans

class Cell:
    def __init__(self):
        self.type = 'empty'      # empty, tree, river, burnt, hospital, shop
        self.tree_alive = False
        self.on_fire = False
        self.growth = 0          # 0..100, дерево взрослое при 100

    def __repr__(self):
        if self.type == 'river':
            return constans.RIVER
        if self.type == 'hospital':
            return constans.HOSPITAL
        if self.type == 'shop':
            return constans.SHOP
        if self.on_fire:
            return constans.FIRE
        if self.type == 'burnt':
            return constans.BURNT
        if self.type == 'tree' and self.tree_alive:
            return constans.TREE
        return constans.EMPTY

    def to_dict(self):
        return {
            'type': self.type,
            'tree_alive': self.tree_alive,
            'on_fire': self.on_fire,
            'growth': self.growth
        }

    @classmethod
    def from_dict(cls, data):
        cell = cls()
        cell.type = data['type']
        cell.tree_alive = data['tree_alive']
        cell.on_fire = data['on_fire']
        cell.growth = data['growth']
        return cell