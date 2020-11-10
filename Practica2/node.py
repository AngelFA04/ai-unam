class Node():
    def __init__(self, child, parent=None, direction=None):
        self.child = child
        self.parent = parent
        self.direction = direction

        # distancia para llegar al destino
        self.x_dist = 0
        self.y_dist = 0
        # self.nodes = []

    @property
    def childrens(self):
        pass

    def __str__(self):
        return f'({self.child}, {self.parent})'

    def __repr__(self):
        return f'({self.child}, {self.parent})'


def find_child(child, nodes):
    for i in nodes:
        if i.child == child:
            return i


class Tree():
    def __init__(self):
        pass