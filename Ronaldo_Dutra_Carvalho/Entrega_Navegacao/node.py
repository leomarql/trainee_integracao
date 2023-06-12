class Node:
    def __init__(self, x, y, g_cost, h_cost, parent=None):
        self.x = x
        self.y = y
        self.g_cost = g_cost
        self.h_cost = h_cost
        self.parent = parent

    def __lt__(self, other):
         return self.h_cost < other.h_cost

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def f_cost(self):                                                                                                           
        return (self.g_cost + self.h_cost)