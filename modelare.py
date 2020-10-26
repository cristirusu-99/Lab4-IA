from __future__ import annotations
import string


def str_list_of_nodes(list_of_nodes: list[Node]):
    return "\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n".join(map(str, list_of_nodes))


def str_pair_nodes(pair_nodes: tuple[Node, Node]):
    return ",".join(map(Node.get_region_name, pair_nodes))


def str_list_pairs(list_pairs: list[tuple[Node, Node]]):
    return " | ".join(map(str_pair_nodes, list_pairs))


def generate_queue(list_of_nodes: list[Node]):
    visited = list()
    queue = list()
    for node in list_of_nodes:
        for neigh in node.neighbours:
            if neigh not in visited:
                queue.append((node, neigh))
        visited.append(node)
    return queue


def check_arc_consistency(list_of_nodes: list[Node]):
    list_of_edges = generate_queue(list_of_nodes)
    for edge in list_of_edges:
        for color1 in edge[0].available_colors:
            consistent = False
            for color2 in edge[1].available_colors:
                if color1 != color2:
                    consistent = True
            if not consistent:
                if not edge[0].eliminate_color(color1):
                    return "Inconsistency"
                list_of_edges.extend(edge[0].get_in_edges())
    return "Consistency"


class Node:

    region_name: string
    chosen_color: string
    available_colors: list[string]
    neighbours: list[Node]

    def __init__(self, p_region_name: string, p_available_colors: list[string], p_neighbours: list[Node]):
        self.region_name = p_region_name
        self.chosen_color = ""
        self.available_colors = p_available_colors
        self.neighbours = p_neighbours

    def add_neighbours(self, p_neighbours: list[Node]):
        self.neighbours.extend(p_neighbours)

    def __str__(self) -> str:
        return "Region: " + self.region_name +\
               "\nChosen color: " + self.chosen_color +\
               "\nAvailable colors: " + str(self.available_colors) +\
               "\nNeighbours: " + str([str(item.region_name) for item in self.neighbours])

    def get_region_name(self):
        return self.region_name

    def get_in_edges(self):
        temp = list()
        for node in self.neighbours:
            temp.append((node, self))
        return temp

    def eliminate_color(self, color: string):
        self.available_colors.remove(color)
        if self.chosen_color == color:
            return self.next_color_region()

    def next_color_region(self):
        if self.available_colors:
            self.chosen_color = self.available_colors[0]
            return True
        else:
            self.chosen_color = ""
            return False

    def set_color(self, color):
        if color in self.available_colors:
            self.chosen_color = color
            return True
        else:
            return False
