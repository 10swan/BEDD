# Example Usage:
from bean.ServerGraph import ServerGraph

dataset_path = "./dataset/edge-servers/site-optus-melbCBD.csv"
server_graph = ServerGraph(dataset_path)
server_graph.build_graph_from_dataset()

print(server_graph)
