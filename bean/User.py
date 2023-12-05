class User:
    def __init__(self, userId, latitude, longitude):
        self.userId = userId
        self.latitude = latitude
        self.longitude = longitude

    def request_data(self):
        # 在图中搜索附近的服务器
        print(f"{self.userId}正在请求数据...")
