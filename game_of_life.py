import random


class World:
    """create the dimensions of the world"""
    def __init__(self):
        self.height = 100
        self.length = 100


class Cell():
    """create a cell with a position and life criteria"""
    def __init__(self):
        self.position = (random.randint(1, 100), random.randint(1, 100))
        self.life = self.is_alive()

    def is_alive(self):
        """is current cell alive or not"""
        return True

    def get_postions(self, position, other_cells):
        """current cell learns postion of other cells"""
        for cell in other_cells:
            x, y = cell[0], cell[1]
            if self.postion[0] - x <= 1 and self.position[1] - y <= 1:
                self.is_alive = False
            else:
                pass# update_postion()

    # def update_postion(self):
    #     """move cell"""
