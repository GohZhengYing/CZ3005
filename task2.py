import json
from collections import defaultdict

# Open and read json files
with open('G.json') as f:
    graph_dict = json.load(f)

with open('Dist.json') as f:
    edge_dist = json.load(f)

with open('Cost.json') as f:
    edge_cost = json.load(f)

# Create a Graph class to add attributes
# Graph class contains a dictionary that maps vertex names to vertex objects.
class Graph():
    def __init__(self):
        """
        initializes a graph object
            If no dictionary or None is given,
            an empty dictionary will be used
        """
        # Initialise neighbour nodes as a list
        self.edges = defaultdict(list)

        # Edge distance between 2 nodes
        self.weights = {}

        # Energy cost between 2 nodes
        self.costs = {}

    # Function to add an edge
    # source_node = from_node, dest_node = to_node
    def add_edge(self, source_node, dest_node, weight, cost):
        self.edges[source_node].append(dest_node)
        self.edges[dest_node].append(source_node)

        self.weights[(source_node, dest_node)] = weight
        self.weights[(dest_node, source_node)] = weight

        self.costs[(source_node, dest_node)] = cost
        self.costs[(dest_node, source_node)] = cost

# Initialise a graph object
graph = Graph()

# Add attributes to the created graph object ('source_node', 'dest_node', 'weight', 'cost')
counter = len(edge_dist)
for i in edge_dist:
    # each object in dict is a pair of pair nodes, so counter is needed to avoid duplicate entries
    if counter % 2 == 0:
        # Get source and destination node (from and to)
        source_and_dest = i.split(',') # source_and_dest[0] = source, source_and_dest[1] = destination
        graph.add_edge(source_and_dest[0], source_and_dest[1], edge_dist[i], edge_cost[i])
    counter -= 1

energy_budget = 287932

def task2_search(start_node: str, end_node: str, budget: int):
    # Energy (Edge Cost) budget
    energy_cost_budget = budget

    # Stores visited nodes with unvisited neighbour nodes
    unvisited_neighbour = set()
    unvisited_neighbour.add(start_node)

    # Stores visited nodes with all neighbour nodes visited
    all_nodes_visited = set()

    # Stores accumulated path cost g(n) from start node to current node (distance)
    total_distance = {}
    total_distance[start_node] = 0

    # Stores accumulated energy cost from start node to current node
    total_energy = {}
    total_energy[start_node] = 0

    # Stores temp current node
    temp_node = {}
    temp_node[start_node] = start_node

    # Initialise Queue to pop elements
    queue = []
    # insert the starting index
    queue.append(start_node)

    while len(queue) > 0:

        selected_node = None

        for node in queue:
            if selected_node == None or total_distance[node] < total_distance[selected_node]:
                selected_node = node

        if selected_node == None:
            print("Error!")
            return

        # End Node reached
        if selected_node == end_node:
            shortest_distance_updated = total_distance[selected_node]
            total_energy_updated = total_energy[selected_node]

            shortest_path = []

            while temp_node[selected_node] != selected_node:
                shortest_path.append(selected_node)
                selected_node = temp_node[selected_node]

            shortest_path.append(start_node)
            shortest_path.reverse()

            print("Shortest path: ", end="")
            for i in shortest_path:
                if i != end_node:
                    print(i, end="->")
                else:
                    print(i)
            print("Shortest distance: ", shortest_distance_updated)
            print("Total energy cost: ", total_energy_updated)
            return

        # calculate total current energy cost and total current path cost for each neighbour node of the current node
        for connect_node in graph.edges[selected_node]:

            if connect_node not in unvisited_neighbour and connect_node not in all_nodes_visited:
                total_energy[connect_node] = total_energy[selected_node] + graph.costs[
                    connect_node, selected_node]

                # Check if total energy cost has exceeded energy budget
                if total_energy[connect_node] > energy_cost_budget:
                    continue

                queue.append(connect_node)
                unvisited_neighbour.add(connect_node)
                temp_node[connect_node] = selected_node
                total_distance[connect_node] = total_distance[selected_node] + graph.weights[connect_node, selected_node]

            # if neighbour node is in 'unvisited' or 'visited'
            else:

                if total_distance[connect_node] > total_distance[selected_node] + graph.weights[connect_node, selected_node]:
                    total_distance[connect_node] = total_distance[selected_node] + graph.weights[connect_node, selected_node]
                    total_energy[connect_node] = total_energy[selected_node] + graph.costs[
                        connect_node, selected_node]

                    # Check if total energy cost has exceeded energy budget
                    if total_energy[connect_node] > energy_cost_budget:
                        continue

                    temp_node[connect_node] = selected_node

                    if connect_node in all_nodes_visited:
                        all_nodes_visited.remove(connect_node)
                        queue.append(connect_node)
                        unvisited_neighbour.add(connect_node)

        # Pop/Remove node from queue
        queue.remove(selected_node)
        # Remove current node from 'unvisited' and add to 'visited'
        unvisited_neighbour.remove(selected_node)
        all_nodes_visited.add(selected_node)

    print("Invalid path!")
    return

#task2_search("1","50", energy_budget)






