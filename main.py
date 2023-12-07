# Example Usage:
from bean.ServerGraph import ServerGraph
from bean.User import User

# 数据位置
dataset_path = "./dataset/edge-servers/site-optus-melbCBD.csv"

# 初始化边缘服务器图
server_graph = ServerGraph(dataset_path)

# 初始化用户
user = User(10086, 144.97476, -37.81511)

user.request_data(1, server_graph)
