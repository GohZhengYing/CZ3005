import json
import math

G_file = open('./G.json','r')
Coord_file = open('./Coord.json','r')
Cost_file = open('./Cost.json','r')
Dist_file = open('./Dist.json','r')

G = json.load(G_file)
Coord = json.load(Coord_file)
Cost = json.load(Cost_file)
Dist = json.load(Dist_file)

budget = 287932
start = '1'
end = '50'

def run(c):
    global G,Coord,Cost,Dist,budget,start,end
    path = [[start],0,0,0]#[path,total_energy_cost,total_dist,f(n)]

    deadend = []

    path_found = False
    priority_queue = [path] 
    visited = []

    while len(priority_queue) >0 and (not path_found):
        current = priority_queue[len(priority_queue)-1]
        priority_queue.remove(current)
        if len(current[0])>1:
            visited.append(current[0][-1])


        for path_node in G[current[0][-1]]:
            if path_node == end:
                current[1] += Cost[current[0][-1]+','+path_node]
                current[2] += Dist[current[0][-1] + ',' + path_node]
                current[0].append(path_node)
                path = current
                path_found = True
            elif len(G[path_node])>1 and path_node not in current[0] and current[1]+Cost[current[0][-1]+','+path_node]<=budget and path_node not in visited:
                new_path = [current[0]+[path_node],current[1]+Cost[current[0][-1]+','+path_node],current[2]+Dist[current[0][-1]+','+path_node]]
                h = math.sqrt((Coord[current[0][-1]][0] - Coord[path_node][0]) ** 2 + (Coord[current[0][-1]][1] - Coord[path_node][1]) ** 2)
                new_path.append(h*c + new_path[1] + new_path[2])# heuristics function = h*c + total_energy_cost + total_dist
                if len(priority_queue) == 0:
                    priority_queue.append(new_path)

                else:
                    for i in range(len(priority_queue)):
                        if priority_queue[i][3]<=new_path[3]:
                            priority_queue.insert(i,new_path)
                            break
                        elif i == len(priority_queue)-1:
                            priority_queue.append(new_path)

    spath = 'Shortest path: '
    for node in path[0]:
        if path[0].index(node) != len(path[0]) - 1:
            spath += (node + '->')
        else:
            spath += (node)
    print(spath)
    print('Shortest distance: ' + str(path[2]))
    print('Total energy cost: ' + str(path[1]))

#This was ran to find out the best c in the function(h * c + total_cost + total_dist)
#It is commented out as it will ~2mins to compute
# best_c = 0
# lowest = 1000000000
# for c in range(0,100):
#     result = run(c/10)[2] #total dist
#     if result<lowest and result>0:
#         best_c = c
#         lowest = result

#The best_c = 9.6
