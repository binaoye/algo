class node:
     def __init__(self, val):
         self.val = val

class one_way_route:
    def __init__(self, start, end, weight=1):
        self.start = start
        self.end = end
        self.weight = weight


class bi_direction_route:
    def __init__(self, start, end, weight=1):
        self.start = start
        self.end = end
        self.weight = weight




class graphx:
    def __init__(self, routelist=[]):
        self.route_list = routelist
        self.route_table = [[0 for i in range(len(routelist))] for j in range(len(routelist))]
        self.node_list = []

    # def __add__(self, route):

