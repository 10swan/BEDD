import pandas as pd
from geopy.distance import lonlat, distance

from bean.EdgeServer import EdgeServer


class ServerGraph:
    def __init__(self, dataset_path):
        self.adjacency_list = {}
        self.df = pd.read_csv(dataset_path)

    # 增加服务器
    def add_server(self, SITE_ID, LONGITUDE, LATITUDE):
        if SITE_ID not in self.adjacency_list:
            server = EdgeServer(SITE_ID, LONGITUDE, LATITUDE, [])
            self.adjacency_list[SITE_ID] = server

    def add_edge(self, server_1, server_2):
        SITE_ID_1 = server_1.SITE_ID
        SITE_ID_2 = server_2.SITE_ID
        if SITE_ID_1 in self.adjacency_list and SITE_ID_2 in self.adjacency_list:
            self.adjacency_list[SITE_ID_1].neighbors.append(server_2)
            self.adjacency_list[SITE_ID_2].neighbors.append(server_1)

    def compute_distance(self, server_1, server_2):
        server_1_position = lonlat(server_1.LONGITUDE, server_1.LATITUDE)
        server_2_position = lonlat(server_2.LONGITUDE, server_2.LATITUDE)
        distance_between_servers = distance(server_1_position, server_2_position)
        return distance_between_servers

    def check_distance(self, server1, server2, threshold=100):
        distance_between_servers = self.compute_distance(server1, server2)
        return distance_between_servers < threshold

    def build_graph_from_dataset(self):
        # 如果边缘服务器集合中没有该服务器，则加入(加点)
        for index, row in self.df.iterrows():
            if row.SITE_ID not in self.adjacency_list:
                self.add_server(row.SITE_ID, row.LONGITUDE, row.LATITUDE)
        # 构建边缘服务器图的邻接表
        for SITE_ID_1 in self.adjacency_list:
            for SITE_ID_2 in self.adjacency_list:
                server_1 = self.adjacency_list[SITE_ID_1]
                server_2 = self.adjacency_list[SITE_ID_2]
                if server_1 != server_2 and self.check_distance(server_1, server_2):
                    self.add_edge(server_1, server_2)

    def __str__(self):
        for SITE_ID, row in self.adjacency_list.items():
            for server in row.neighbors:
                return f"Server: {SITE_ID} neighbors: [{server.SITE_ID}]"
