import heapq
import sys
from typing import Dict, Optional, Tuple
from queue import *

class Vertex:
    """Graph vertex class"""

    def __init__(self, num):
        """Create new vertex"""
        self._num = num
        self._neighbors = {}
        self._color = "white"
        self._distance = sys.maxsize
        self._previous = None

    def __lt__(self, other):
        """Less than operator required for heapify"""
        return self._num < other.num

    def get_num(self):
        """Get vertex key"""
        return self._num

    num = property(get_num)


    def get_connections(self) -> Tuple["Vertex"]:
        return tuple(self._neighbors.keys())

    def get_neighbor(self, other):
        """Get the distance (edge weight) to an adjacent node (neighbor)"""
        return self._neighbors.get(other, None)

    def set_neighbor(self, other, weight=0):
        """Set the distance (add an edge) to an adjacent node (neighbor)"""
        self._neighbors[other] = weight

    def get_neighbors(self):
        """Get all adjacent nodes (neighbors)"""
        return self._neighbors.nums()

    def get_color(self):
        """Get vertex color"""
        return self._color

    def set_color(self, color):
        """Set vertex color"""
        self._color = color

    color = property(get_color, set_color)

    def get_distance(self):
        """Get distance"""
        return self._distance

    def set_distance(self, distance):
        """Set distance"""
        self._distance = distance

    distance = property(get_distance, set_distance)

    def get_previous(self):
        """Get previous"""
        return self._previous

    def set_previous(self, previous):
        """Set previous"""
        self._previous = previous

    previous = property(get_previous, set_previous)

    def __str__(self):
        return "{:^8}|{:^8}|{:^8}|{:^8}|{:^8}| {}".format(
            self._key,
            self._color,
            self._distance,
            self._discovery_time,
            self._closing_time,
            self._previous,
        )


class Graph:
    def __init__(self) -> None:
        self.vertices_dict: Dict[int, Vertex] = {}
        self.num_vertices = 0

    def add_vertex(self, key):
        self.num_vertices += 1
        new_vertex = Vertex(key)
        self.vertices_dict[key] = new_vertex
        return new_vertex

    def get_vertex(self, n: int) -> Optional[Vertex]:
        if n in self.vertices_dict:
            return self.vertices_dict[n]
        else:
            return None

    def __contains__(self, n):
        return n in self.vertices_dict

    def add_edge(self, f, t, weight=0) -> None:
        if f not in self.vertices_dict:
            self.add_vertex(f)
        if t not in self.vertices_dict:
            self.add_vertex(t)
        self.vertices_dict[f].set_neighbor(self.vertices_dict[t], weight)

    def get_vertices(self) -> tuple:
        return tuple(self.vertices_dict.keys())

    def __iter__(self):
        return iter(self.vertices_dict.values())



def dfs_paths(graph, start, goal):
    stack = [(start, [start])]  # (vertex, path)
    while stack:
        (vertex, path) = stack.pop()
        for next in set(graph[vertex]) - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))




def bfs(graph, start):
    visited, queue = [], deque([start])
    while queue:
        vertex = queue.pop()
        if vertex not in visited:
            visited.append(vertex)
            queue.extendleft(set(graph[vertex]) - set(visited))
    return visited


if __name__ == "__main__":
    g = Graph()
    for i in range(6):
        g.add_vertex(i)

    g.add_edge(0, 1, 5)
    g.add_edge(0, 5, 2)
    g.add_edge(1, 2, 4)
    g.add_edge(2, 3, 9)
    g.add_edge(3, 4, 7)
    g.add_edge(3, 5, 3)
    g.add_edge(4, 0, 1)
    g.add_edge(5, 4, 8)
    g.add_edge(5, 2, 1)
    for v in g:
        for w in v.get_connections():
            print("( %s , %s )" % (v.get_num(), w.get_num()))

    # print(list(dfs_paths(g, 1, 2)))
