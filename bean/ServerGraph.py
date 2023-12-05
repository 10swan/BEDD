class ServerGraph:
    def __init__(self):
        self.adjacency_list = {}

    # 增加服务器
    def add_server(self, server):
        if server.SITE_ID not in self.adjacency_list:
            self.adjacency_list[server.SITE_ID] = server

    # 添加邻接服务器信息
    # def add_server(self, server1, server2):
    #     if server1.SITE_ID not in self.adjacency_list:
    #         self.adjacency_list[server1.SITE_ID] = []
    #     if server2.SITE_ID not in self.adjacency_list:
    #         self.adjacency_list[server2.SITE_ID] = []
    #
    #     self.adjacency_list[server1.SITE_ID].append(server2)
    #     self.adjacency_list[server2.SITE_ID].append(server1)

    def __str__(self):
        result = []
        for SITE_ID, EdgeServers in self.adjacency_list.items():
            result.append(
                f"EdgeServer ID: {SITE_ID} -> Connected Servers: {[connectedServers.SITE_ID for connectedServers in EdgeServers.connectedServers]}")
        return "\n".join(result)
