import networkx as nx
import matplotlib.pyplot as plt
import random

graph = nx.Graph()
#Configuração que resolve o problema de coloração tradicional.
graph.add_nodes_from([
    ("A", {"color": "green"}),
    ("B", {"color": "orange"}),
    ("C", {"color": "yellow"}),
    ("D", {"color": "blue"}),
    ("E", {"color": "orange"}),
    ("F", {"color": "red"}),
    ("G", {"color": "yellow"}),
    ("H", {"color": "red"}),
    ("I", {"color": "blue"}),
    ("J", {"color": "red"}),
    ("K", {"color": "green"}),
    ("L", {"color": "blue"}),
    ("M", {"color": "blue"}),
    ("N", {"color": "red"}),
   
   
])

graph.add_edge("A", "E")
graph.add_edge("B", "A")
graph.add_edge("C", "J")
graph.add_edge("E", "C")
graph.add_edge("E", "B")
graph.add_edge("F", "D")
graph.add_edge("G", "F")
graph.add_edge("G", "C")
graph.add_edge("F", "E")
graph.add_edge("B", "H")
graph.add_edge("I", "B")
graph.add_edge("K", "C")
graph.add_edge("A", "K")
graph.add_edge("F", "C")
graph.add_edge("L", "A")
graph.add_edge("M", "E")
graph.add_edge("N", "C")

#Configuração que resolve nosso problema
# graph.add_nodes_from([
#     ("A", {"color": "green"}),
#     ("B", {"color": "orange"}),
#     ("C", {"color": "yellow"}),
#     ("D", {"color": "red"}),
#     ("E", {"color": "orange"}),
#     ("F", {"color": "orange"}),
#     ("G", {"color": "yellow"}),
#     ("H", {"color": "red"}),
#     ("I", {"color": "green"}),
#     ("J", {"color": "red"}),
# ])

# graph.add_edge("A", "E")
# graph.add_edge("B", "F")
# graph.add_edge("C", "G")
# graph.add_edge("D", "H")
# graph.add_edge("A", "B")
# graph.add_edge("C", "D")
# graph.add_edge("G", "A")
# graph.add_edge("A", "F")
# graph.add_edge("F", "E")
# graph.add_edge("J", "I")
# graph.add_edge("I", "C")


node_colors_starter_graph = []
node_colors_final_graph = []
equal_colors = []
colors_to_change = 0
check = True

def funct():
    for i in graph.nodes:
        for j in graph[i]:
            if graph.nodes[i]['color'] == graph.nodes[j]['color'] and graph.nodes[j]['color'] != "white":
                equal_colors.append(graph.nodes[j]['color']);
                graph.nodes[j]['color'] = "white";

for i in graph.nodes(data = "color"):
    node_colors_starter_graph.append(i[1]);

funct()
random.shuffle(equal_colors, lambda: 0.1)
for i in graph.nodes:
    node_colors_final_graph.append(graph.nodes[i]['color']);
    for j in graph[i]:
        if graph.nodes[j]['color'] == "white":
            graph.nodes[j]['color'] = equal_colors[len(equal_colors) - 1];
            equal_colors.pop()
    
subax1 = plt.subplot(121)
nx.draw(graph, with_labels=True, font_weight='light', node_color= node_colors_starter_graph)
subax2 = plt.subplot(122)
nx.draw(graph, with_labels=True, font_weight='light', node_color= node_colors_final_graph)
plt.show()
