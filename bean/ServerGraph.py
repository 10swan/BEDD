import random

import pandas as pd

from bean.Server import Server
from utils.compute_distance import compute_distance


class ServerGraph:
    def __init__(self, dataset_path):
        self.adjacency_list = {}
        self.df = pd.read_csv(dataset_path)
        self.build_graph_from_dataset()
        self.display()

    # 增加服务器
    def add_server(self, SITE_ID, LONGITUDE, LATITUDE, data):
        if SITE_ID not in self.adjacency_list:
            server = Server(SITE_ID, LONGITUDE, LATITUDE, data, [])
            self.adjacency_list[SITE_ID] = server
            # print(server.data)

    def add_edge(self, server, nearest_neighbors):
        SITE_ID = server.SITE_ID
        if SITE_ID in self.adjacency_list:
            self.adjacency_list[SITE_ID].neighbors = nearest_neighbors

    def build_graph_from_dataset(self, k=5):
        # 如果边缘服务器集合中没有该服务器，则加入(加点)
        for index, row in self.df.iterrows():
            if row.SITE_ID not in self.adjacency_list:
                data = [random.choice([0, 1]) for _ in range(100)]
                self.add_server(row.SITE_ID, row.LONGITUDE, row.LATITUDE, data)
        # 构建边缘服务器图的邻接表
        for SITE_ID in self.adjacency_list:
            server = self.adjacency_list[SITE_ID]
            # 计算节点与所有邻接节点的距离
            distances_array = []
            for neighbor_SITE_ID in self.adjacency_list:
                if SITE_ID != neighbor_SITE_ID:
                    neighborServer = self.adjacency_list[neighbor_SITE_ID]
                    distance_between_servers = compute_distance(server, neighborServer)
                    distances_array.append((self.adjacency_list[neighbor_SITE_ID], distance_between_servers))

            # 按距离排序
            distances_array.sort(key=lambda x: x[1])

            # 获取最近的k个邻接节点
            nearest_neighbors = [item[0] for item in distances_array[:k]]
            # 更新邻接表
            self.add_edge(server, nearest_neighbors)

        return self.adjacency_list

    def display(self):
        for SITE_ID, server in self.adjacency_list.items():
            print(f"Server {SITE_ID}:\n"
                  f"data {server.data}:\n"
                  f"Neighbors: {[neighbor.SITE_ID for neighbor in server.neighbors]}\n")
