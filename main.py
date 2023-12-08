# Example Usage:
from bean.ServerGraph import ServerGraph
from bean.User import User

# 数据位置
dataset_path = "./dataset/edge-servers/site-optus-melbCBD.csv"

# 初始化边缘服务器图
server_graph = ServerGraph(dataset_path)

# 初始化用户
user = User(10086, 144.97476, -37.81511)

# 获取最近服务器
nearest_server_SITE_ID = user.get_user_nearest_server_location(server_graph.adjacency_list)

print('nearest_server_SITE_ID', nearest_server_SITE_ID)

#
user.request_data(0, nearest_server_SITE_ID, server_graph.adjacency_list)
