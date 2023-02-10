# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 23:19:39 2023

@author: ppodl
"""

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import pylab
import pandas as pd

tracks = [['Lisboa','Madrid','pink','standard',3],\
          ['Lisboa','Cadiz','blue','standard',2],\
          ['Cadiz','Madrid','orange','standard',3],\
          ['Barcelona','Madrid','yellow','standard',2],\
          ['Barcelona','Pamplona','grey','tunnel',2],\
          ['Pamplona','Madrid','white','tunnel',3],\
          ['Pamplona','Madrid','black','tunnel',3],\
          ['Barcelona','Madrid','yellow','standard',2],\
          ['Barcelona','Pamplona','grey','tunnel',2],\
          ['Barcelona','Marseille','grey','standard',4],\
          ['Pamplona','Marseille','red','standard',4],\
          ['Pamplona','Brest','pink','standard',4],\
          ['Pamplona','Paris','blue','standard',4],\
          ['Pamplona','Paris','green','standard',4],\
          ['Paris','Marseille','grey','standard',4],\
          ['Paris','Brest','black','standard',3],\
          ['Dieppe','Brest','orange','standard',2],\
          ['Paris','Dieppe','pink','standard',1],\
          ['Dieppe','London','grey','ferry',2,1],\
          ['Dieppe','London','grey','ferry',2,1],\
          ['London','Edinburgh','black','standard',4],\
          ['London','Edinburgh','orange','standard',4],\
          ['London','Amsterdam','grey','ferry',2],\
          ['Dieppe','Bruxelles','green','standard',2],\
          ['Paris','Bruxelles','yellow','standard',2],\
          ['Paris','Bruxelles','red','standard',2],\
          ['Amsterdam','Bruxelles','black','standard',1],\
          ['Amsterdam','Essen','yellow','standard',3],\
          ['Paris','Frankfurt','white','standard',3],\
          ['Paris','Frankfurt','orange','standard',3],\
          ['Bruxelles','Frankfurt','blue','standard',2],\
          ['Amsterdam','Frankfurt','white','standard',2],\
          ['Paris','Zurich','grey','tunnel',3],\
          ['Marseille','Zurich','pink','tunnel',2],\
          ['Essen','Frankfurt','green','standard',2],\
          ['Munchen','Frankfurt','pink','standard',2],\
          ['Munchen','Zurich','yellow','tunnel',2],\
          ['Munchen','Venezia','blue','tunnel',2],\
          ['Zurich','Venezia','green','tunnel',2],\
          ['Marseille','Roma','grey','tunnel',4],\
          ['Venezia','Roma','black','standard',2],\
          ['Palermo','Roma','grey','ferry',4,1],\
          ['Palermo','Brindisi','grey','ferry',3,1],\
          ['Roma','Brindisi','white','standard',2],\
          ['Palermo','Smyrna','grey','ferry',6,2],\
          ['Athina','Smyrna','grey','ferry',2,1],\
          ['Athina','Brindisi','grey','ferry',4,1],\
          ['Essen','Kobenhavn','grey','ferry',3,1],\
          ['Essen','Kobenhavn','grey','ferry',3,1],\
          ['Stockholm','Kobenhavn','yellow','standard',3],\
          ['Stockholm','Kobenhavn','white','standard',3],\
          ['Frankfurt','Berlin','black','standard',3],\
          ['Frankfurt','Berlin','red','standard',3],\
          ['Essen','Berlin','blue','standard',2],\
          ['Danzig','Berlin','grey','standard',4],\
          ['Warszawa','Berlin','pink','standard',4],\
          ['Warszawa','Berlin','yellow','standard',4],\
          ['Warszawa','Danzig','grey','standard',2],\
          ['Warszawa','Wien','blue','standard',4],\
          ['Riga','Danzig','black','standard',3],\
          ['Stockholm','Petrograd','grey','tunnel',8],\
          ['Riga','Petrograd','grey','standard',4],\
          ['Warszawa','Wilno','red','standard',3],\
          ['Riga','Wilno','green','standard',4],\
          ['Petrograd','Wilno','blue','standard',4],\
          ['Smolensk','Wilno','yellow','standard',3],\
          ['Kyiv','Wilno','grey','standard',2],\
          ['Kyiv','Warszawa','grey','standard',4],\
          ['Moskva','Petrograd','white','standard',4],\
          ['Moskva','Smolensk','orange','standard',2],\
          ['Kyiv','Smolensk','red','standard',3],\
          ['Munchen','Wien','orange','standard',3],\
          ['Berlin','Wien','green','standard',3],\
          ['Venezia','Zagrab','grey','standard',2],\
          ['Wien','Zagrab','grey','standard',2],\
          ['Wien','Budapest','white','standard',1],\
          ['Wien','Budapest','red','standard',1],\
          ['Budapest','Zagrab','orange','standard',2],\
          ['Sarajevo','Zagrab','red','standard',3],\
          ['Sarajevo','Budapest','pink','standard',3],\
          ['Sarajevo','Athina','green','standard',4],\
          ['Sofia','Athina','pink','standard',3],\
          ['Sofia','Sarajevo','grey','tunnel',2],\
          ['Sofia','Bucaresti','grey','tunnel',2],\
          ['Budapest','Bucaresti','grey','tunnel',4],\
          ['Kyiv','Bucaresti','grey','standard',4],\
          ['Kyiv','Budapest','grey','tunnel',6],\
          ['Sofia','Constantinople','blue','standard',3],\
          ['Smyrna','Constantinople','grey','tunnel',2],\
          ['Bucaresti','Constantinople','yellow','standard',3],\
          ['Angora','Constantinople','grey','tunnel',2],\
          ['Angora','Smyrna','orange','tunnel',3],\
          ['Angora','Erzurum','black','standard',3],\
          ['Sochi','Erzurum','orange','tunnel',3],\
          ['Sochi','Sevastopol','grey','ferry',2,1],\
          ['Erzurum','Sevastopol','grey','ferry',4,2],\
          ['Constantinople','Sevastopol','grey','ferry',4,2],\
          ['Bucaresti','Sevastopol','white','standard',4],\
          ['Sochi','Rostov','grey','standard',2],\
          ['Sevastopol','Rostov','grey','standard',4],\
          ['Krarkov','Rostov','green','standard',2],\
          ['Krarkov','Kyiv','grey','standard',4],\
          ['Krarkov','Moskva','grey','standard',4],\
          ]
points_dict = {1:1,2:2,3:4,4:7,6:15,7:21}    
points_dict[7]

df_tracks = pd.DataFrame(tracks,columns = ['station1','station2','color','type','len','engines'])    
df_tracks['engines'][np.isnan(df_tracks['engines'])] = 0
df_tracks['points'] = df_tracks['len'].map(points_dict)


pos_dict = {'Lisboa':(-9.1392,38.7223),\
            'Madrid':(-3.7038,40.4168),\
            'Cadiz':(-6.29465,36.52987),\
            'Pamplona':(-1.65,42.817),\
            'Barcelona':(-2.168,41.346)\
                }    
?pd.DataFrame
# =============================================================================
# tracks = {'t01':{'start':'Lisboa','end':'Madrid','color':'pink','type':'standard','len':3}},\
#           ['Lisboa','Cadiz','blue','standard',2]\
#           ,['Cadiz','Madrid','orange','standard',3]]    
# 
# tracks['t01']['start']     
# =============================================================================


G = nx.MultiGraph()
for track in tracks:
    G.add_edge(track[0], track[1],color = track[2],type = track[3],size = track[4])

colors = nx.get_edge_attributes(G,'color').values()
#colors  = ['grey' if c == 'any' for c in colors]

nx.draw_networkx(G,arrows=False,edge_color=colors,connectionstyle='arc3, rad = 0.1')



shortest = nx.all_shortest_paths(G, 'Cadiz', 'Pampelona')
for s in shortest:
    print(s)
nx.get_edge_attributes(G,'size')


nx.shortest_path(G, 'Cadiz', 'Pampelona','size')


for s in shortest:
    print(s)

for e in G.edges:
    print(e['color'])

filtred_G = nx.MultiGraph()
selected_edges = [(u,v) for u,v,e in G.edges(data=True) if e['type'] != 'tunnel']

for edge in G.edges:
    print(edge[0])
    print(nx.get_edge_attributes(G,edge))
    #filtred_G.add_edge(edge[0],edge[1])
    

nx.get_edge_attributes(G,'size')
//12
nx.draw_networkx?
G = nx.DiGraph()

G.add_edges_from([('A', 'B'),('C','D'),('G','D')], weight=1)
G.add_edges_from([('D','A'),('D','E'),('B','D'),('D','E')], weight=2)
G.add_edges_from([('B','C'),('E','F')], weight=3)
G.add_edges_from([('C','F')], weight=4)
nx.draw_networkx(G)

G.add_edge?

G = nx.DiGraph()
G.add_edge(u_of_edge, v_of_edge, attr)
G.add_edges_from([('A', 'B'),('C','D'),('G','D')], weight=1)
G.add_edges_from([('D','A'),('D','E'),('B','D'),('D','E')], weight=2)
G.add_edges_from([('B','C'),('E','F')], weight=3)
G.add_edges_from([('C','F')], weight=4)
nx.draw_networkx(G)




val_map = {'A': 1.0,
                   'D': 0.5714285714285714,
                              'H': 0.0}

values = [val_map.get(node, 0.45) for node in G.nodes()]
edge_labels=dict([((u,v,),d['weight'])
                 for u,v,d in G.edges(data=True)])
red_edges = [('C','D'),('D','A')]
edge_colors = ['black' if not edge in red_edges else 'red' for edge in G.edges()]

pos=nx.spring_layout(G)
nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels)
nx.draw(G,pos, node_color = values, node_size=1500,edge_color=edge_colors,edge_cmap=plt.cm.Reds)
pylab.show()
