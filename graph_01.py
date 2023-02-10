# -*- coding: utf-8 -*-
"""
Created on Sat Feb  4 21:46:03 2023

@author: ppodl
"""
from itertools import product

import os
os.chdir('C:\\Users\\ppodl\\Desktop\\praca\\20230124_trains')
import get_Data
import networkx as nx
import pandas as pd
df_tracks = get_Data.get_data()
track_list = get_Data.generate_tracks()


Graph = nx.MultiGraph()
for track in track_list :
    Graph.add_edge(track[0], track[1],color = track[2],type = track[3],len = track[4],engines = track[5],points = track[6],)

df_tracks.sort_values(['points'],ascending=False)




cons_list


df_cons.sort_values(['cons'],ascending = False)

cities = list(df_cons['city'])

def get_unique_neighbours(graph,node):
    neig =  nx.neighbors(graph,node)
    n_list =list(neig)
    return n_list

#get_unique_neighbours(Graph,'Barcelona')

def create_cons_df(graph):
    cons = graph.degree() # nodes with all cons
    cons_list = []
    for c in cons:
        cons_list.append(list(c))
    cons_list = [c + [len(get_unique_neighbours(graph,c[0]))] for c in cons_list] #adding nof unique cons   
    df_cons = pd.DataFrame(cons_list,columns = ['city','cons_all','cons_unique'])
    return df_cons

df_cons = create_cons_df(Graph)

paths = nx.all_simple_paths(Graph, 'Barcelona', 'Danzig')

for t in nx.all_shortest_paths(Graph, 'Barcelona', 'Danzig',weight = 'len'):
    print(t)
for t in nx.all_shortest_paths(Graph, 'Barcelona', 'Danzig'):
    print(t)


def get_best_paths(start,end):
    paths = nx.all_shortest_paths(Graph, start, end)
    paths_len = nx.all_shortest_paths(Graph, start, end,weight='len')
    best_paths = []
    for p in paths:
        best_paths.append(p)
    for p in paths_len:
        best_paths.append(p)    
    best_paths_unique = []
    for path in best_paths:
        if path not in best_paths_unique:
            best_paths_unique.append(path)
    return best_paths_unique

paths = get_best_paths('Barcelona','Danzig')

len(path)
path[5]
def path_to_steps(path):
    #### returns list with from-to steps for path, eg ['Barcelona,Pamplona','Pamplona,Paris']
    steps = []
    for i in range(1,len(path)):
        #print(i)
        step = [path[i-1],path[i]]
        step .sort()
        step = ','.join(step)
        steps.append(step)
    return steps

steps = path_to_steps(path)

def get_detailed_track(steps):
    #### returns (1) full edge (track) information (color, len etc.)
    #### if more than one track possible for step (e.g. Pamplona - Paris) returns both as a list 
    ####(2) all possible combinations of tracks, when using only one possibilty at each step
    track_detailed = []
    for step in steps:
        track_detailed.append([t for t in track_list if step in t[7]])
    track_detailed_steps_len = []
    for step in track_detailed:
        track_detailed_steps_len.append([*range(len(step))])
    track_detailed_combs = list(product(*track_detailed_steps_len))
    track_detailed_unpacked = []
    for comb in track_detailed_combs:
        track = []
        for step_number in range(len(track_detailed)):
            track.append(track_detailed[step_number][comb[step_number]])
        track_detailed_unpacked.append(track)
    return track_detailed, track_detailed_unpacked

track_detailed, track_detailed_unpacked = get_detailed_track(steps)

def get_all_tracks_detailed(paths):
    tracks_final = []
    track_no = 1
    for path in paths:
        steps = path_to_steps(path)
        track_detailed, track_detailed_unpacked = get_detailed_track(steps)
        for detailed_track in track_detailed_unpacked:
            detailed_track = [stop + [track_no] for stop in detailed_track] 
            tracks_final.append(detailed_track)
            track_no = track_no +1
    return tracks_final
        
def          
        
len(tracks_final)
len(track_detailed_unpacked)

###############################################


track_detailed_unpacked = [] 
for comb in track_detailed_combs:
    track = []
    for step_number in range(len(track_detailed)):
        track.append(track_detailed[step_number][comb[step_number]])
    track_detailed_unpacked.append(track)
    
track_detailed_unpacked[1]    
len(track_detailed_unpacked)    

print(track_detailed_unpacked[3])
print(track_detailed_unpacked[4])
track_detailde_combin
for track in track_detailed:
    
track_detailed[2][1]
    
tracks_fltr = [t for t in track_list if 'Pamplona,Paris' in t[7]]


pd.DataFrame(list(product([0,1],[2,3],[4,5])))





for t in nx.all_shortest_paths(Graph, 'Barcelona', 'Danzig')


for p in paths:
    print(p)
    
    
paths = [tuple(p) for p in nx.all_simple_paths(Graph, 'Barcelona', 'Danzig')]
paths = [tuple(p) for p in nx.all_shortest_paths(Graph, 'Barcelona', 'Danzig')]



# sort the paths according to the number of nodes in the path
print(sorted(set(paths), key=lambda x:len(x)))    

