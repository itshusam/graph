import heapq
import time
import sys

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = {}

    def add_edge(self, source, destination, weight):
        if source in self.vertices and destination in self.vertices:
            self.vertices[source][destination] = weight
            self.vertices[destination][source] = weight 

    def get_neighbors(self, vertex):
        return self.vertices[vertex] if vertex in self.vertices else {}

    def dijkstra(self, start):

        start_time = time.time()

        priority_queue = [(0, start)]  
        distances = {vertex: float('infinity') for vertex in self.vertices}
        distances[start] = 0
        previous = {vertex: None for vertex in self.vertices} 

        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)

            if current_distance > distances[current_vertex]:
                continue

            for neighbor, weight in self.get_neighbors(current_vertex).items():
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous[neighbor] = current_vertex
                    heapq.heappush(priority_queue, (distance, neighbor))

        end_time = time.time()
        elapsed_time = end_time - start_time

        space_complexity = sys.getsizeof(distances) + sys.getsizeof(priority_queue) + sys.getsizeof(previous)

        print(f"Time complexity (runtime): {elapsed_time:.6f} seconds")
        print(f"Space complexity (memory): {space_complexity} bytes")

        return distances, previous

    def get_path(self, previous, target):
        path = []
        while target is not None:
            path.insert(0, target)
            target = previous[target]
        return path



graph = Graph()
graph.add_vertex('A')
graph.add_vertex('B')
graph.add_vertex('C')
graph.add_edge('A', 'B', 5)
graph.add_edge('B', 'C', 3)
graph.add_edge('A', 'C', 10)

print(graph.vertices)

distances, previous = graph.dijkstra('A')

print("Shortest distances from 'A':")
for vertex, distance in distances.items():
    print(f"Distance to {vertex}: {distance}")