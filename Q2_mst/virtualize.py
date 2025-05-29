import networkx as nx
import matplotlib.pyplot as plt
from kruskal import DisjointSet, kruskal

# define graph
vertices=['A','B','C','D','E','F','Z']
edges=[('A','B',2),('A','C',7),('C','D',3),('B','D',1),('B','E',5),('D','Z',6),('D','F',4),('C','F',10),('F','Z',3),('E','Z',3)]
G=nx.Graph(); G.add_weighted_edges_from(edges)
pos=nx.spring_layout(G)

# show original
plt.figure(figsize=(10,4));
plt.subplot(121);nx.draw(G,pos,with_labels=True,node_color='lightgrey');
nx.draw_networkx_edge_labels(G,pos,edge_labels={(u,v):w for u,v,w in edges});plt.title('Original Graph')

# step-by-step Kruskal
mst=[]; ds=DisjointSet(vertices)
running_graph=nx.Graph(); running_graph.add_nodes_from(vertices)
plt.subplot(122);
for u,v,w in sorted(edges,key=lambda e:e[2]):
    if ds.find(u)!=ds.find(v):
        ds.union(u,v); mst.append((u,v,w)); running_graph.add_edge(u,v,weight=w)
# draw final MST
nx.draw(running_graph,pos,with_labels=True,node_color='lightgreen')
nx.draw_networkx_edge_labels(running_graph,pos,edge_labels={(u,v):w for u,v,w in mst});plt.title('Final MST')
plt.show()
print('Selected edges step-by-step:', mst)