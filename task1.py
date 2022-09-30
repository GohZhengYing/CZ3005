import json
import queue
from queue import PriorityQueue


with open("Coord.json", "r") as h:
        coord = json.load(h)
        h.close()

with open("Cost.json", "r") as i:
        cost = json.load(i)
        i.close()

with open("Dist.json", "r") as j:
        dist = json.load(j)
        j.close()

with open("G.json", "r") as k:
        g = json.load(k)
        k.close()



class PathData:


    def __init__(self, path="No path found", dist=-1, energy=-1):

        self.path = path
        self.dist = dist
        self.energy = energy



def findminpath(source: str, dest: str, g: dict, dist: dict) -> PathData:
    queue = PriorityQueue()
    visited = set()
    queue.put((0, [source]))
    
    while queue.not_empty:
        
        pair = queue.get()
        
        current_path = pair[1]
        
        current = current_path[-1]
        
        distance = 0
        
        if current not in visited:
            visited.add(current)
            
            if current == dest:
                pathinformation = PathData()
                pathinformation.path = "->".join(current_path)
                for i in range(len(current_path) - 1):
                    distance += dist[f"{current_path[i]},{current_path[i+1]}"]
                pathinformation.dist = distance
                return pathinformation
            
            for neighbors in g[current]:
                new_dist = dist[f"{current},{neighbors}"]
                score = new_dist + pair[0]
                
                new_path = list(pair[1])
                new_path.append(neighbors)
                
                queue.put((score, new_path))
                
    return PathData()



def print_path(label: str, pathinformation: PathData) -> None:
    print(label)
    print(f"Shortest path: {pathinformation.path}")
    print(f"Shortest distance: {pathinformation.dist}")
    print(f"Total energy cost: {pathinformation.energy}")


