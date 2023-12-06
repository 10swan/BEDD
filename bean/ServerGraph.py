import pandas as pd
from geopy.distance import lonlat, geodesic

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

    def add_edge(self, server, nearest_neighbors):
        SITE_ID = server.SITE_ID
        if SITE_ID in self.adjacency_list:
            self.adjacency_list[SITE_ID].neighbors = nearest_neighbors

    def compute_distance(self, server_1, server_2):
        server_1_position = lonlat(server_1.LONGITUDE, server_1.LATITUDE)
        server_2_position = lonlat(server_2.LONGITUDE, server_2.LATITUDE)
        distance_between_servers = geodesic(server_1_position, server_2_position).meters
        return distance_between_servers

    def check_distance(self, server1, server2, threshold=100):
        distance_between_servers = self.compute_distance(server1, server2)
        return distance_between_servers < threshold

    def build_graph_from_dataset(self, k=5):
        # 如果边缘服务器集合中没有该服务器，则加入(加点)
        for index, row in self.df.iterrows():
            if row.SITE_ID not in self.adjacency_list:
                self.add_server(row.SITE_ID, row.LONGITUDE, row.LATITUDE)
        # 构建边缘服务器图的邻接表
        for SITE_ID in self.adjacency_list:
            server = self.adjacency_list[SITE_ID]
            # 计算节点与所有邻接节点的距离
            distances_array = []
            for neighbor_SITE_ID in self.adjacency_list:
                if SITE_ID != neighbor_SITE_ID:
                    neighborServer = self.adjacency_list[neighbor_SITE_ID]
                    distance_between_servers = self.compute_distance(server, neighborServer)
                    distances_array.append((self.adjacency_list[neighbor_SITE_ID], distance_between_servers))

            # 按距离排序
            distances_array.sort(key=lambda x: x[1])

            # 获取最近的k个邻接节点
            nearest_neighbors = [item[0] for item in distances_array[:k]]
            # 更新邻接表
            self.add_edge(server, nearest_neighbors)

    # return nearest_neighbors

    def display(self):
        for SITE_ID, server in self.adjacency_list.items():
            print(f"Server {SITE_ID} Information:")
            print(f"  Longitude: {server.LONGITUDE}")
            print(f"  Latitude: {server.LATITUDE}")
            print(f"  Neighbors: {[neighbor.SITE_ID for neighbor in server.neighbors]}")
            print()
