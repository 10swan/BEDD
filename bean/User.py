import random

from utils.compute_distance import compute_distance


class User:
    def __init__(self, userId, LONGITUDE, LATITUDE):
        self.userId = userId
        self.LONGITUDE = LONGITUDE
        self.LATITUDE = LATITUDE

    def request_data(self, dataId, serverGraph):
        nearest_server = random.choice(list(serverGraph.adjacency_list.keys()))
        nearest_distance = compute_distance(self, nearest_server)
        for SITE_ID in serverGraph.adjacency_list:
            server = serverGraph.adjacency_list[SITE_ID]
            distance_between_user_server = compute_distance(self, server)
            if distance_between_user_server < nearest_distance:
                nearest_server = SITE_ID

        # 在图中搜索附近的服务器
        print(f"{self.userId}正在请求数据: {dataId}")
