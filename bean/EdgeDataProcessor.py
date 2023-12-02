import pandas as pd

from bean.EdgeServer import EdgeServer
from bean.ServerGraph import ServerGraph


class EdgeDataProcessor:
    def __init__(self, csv_file):
        self.df = pd.read_csv(csv_file)
        self.edge_servers = {}

    def process_data(self):
        for index, row in self.df.iterrows():
            SITE_ID = row['SITE_ID']
            ELEVATION = row['ELEVATION']
            NAME = row['NAME']
            STATE = row['STATE']
            LICENSING_AREA_ID = row['LICENSING_AREA_ID']
            POSTCODE = row['POSTCODE']
            SITE_PRECISION = row['SITE_PRECISION']
            HCIS_L2 = row['HCIS_L2']
            LONGITUDE = row['LONGITUDE']
            LATITUDE = row['LATITUDE']
            # data_entry = row['DataEntry']
            if SITE_ID not in self.edge_servers:
                server = EdgeServer(SITE_ID, ELEVATION, LONGITUDE, NAME, STATE, LICENSING_AREA_ID, POSTCODE,
                                    SITE_PRECISION, HCIS_L2, LATITUDE, connectedServers=[])
                self.edge_servers[SITE_ID] = server

            # self.edge_servers[SITE_ID].add_data_entry(data_entry)

    def build_graph(self):
        graph = ServerGraph()
        for SITE_ID, server in self.edge_servers.items():
            graph.add_server(server)
        return graph
