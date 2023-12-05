import pandas as pd
from geopy.distance import lonlat, distance

from bean.EdgeServer import EdgeServer
from bean.ServerGraph import ServerGraph


# 对当前节点，如果有节点的距离小于某值，则加入邻接节点

class EdgeDataProcessor:
    def __init__(self, csv_file):
        self.df = pd.read_csv(csv_file)
        self.edge_servers = {}

    def process_data(self):
        for index, row in self.df.iterrows():
            SITE_ID = row['SITE_ID']
            LONGITUDE = row['LONGITUDE']
            LATITUDE = row['LATITUDE']
            # 如果边缘服务器集合中没有该服务器，则加入
            if SITE_ID not in self.edge_servers:
                server = EdgeServer(SITE_ID, LONGITUDE, LATITUDE, [])
                self.edge_servers[SITE_ID] = server
                current_server_position = lonlat(LONGITUDE, LATITUDE)

                for neighbor_SITE_ID in self.edge_servers:
                    neighbor_server_position = lonlat(
                        self.edge_servers[neighbor_SITE_ID].LONGITUDE, self.edge_servers[neighbor_SITE_ID].LATITUDE)
                    server_distance = distance(current_server_position, neighbor_server_position).miles
                    if server_distance < 100:
                        self.edge_servers[SITE_ID].connectedServers.append(self.edge_servers[neighbor_SITE_ID])

    def build_graph(self):
        graph = ServerGraph()
        for SITE_ID, server in self.edge_servers.items():
            graph.add_server(server)
        return graph
