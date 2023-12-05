class EdgeServer:
    def __init__(self, SITE_ID, LONGITUDE, LATITUDE, connectedServers):
        """
        :param SITE_ID: 站点id
        :param LATITUDE: 纬度
        :param LONGITUDE: 经度
        :param connectedServers: 邻接服务器
        """
        # self.HCIS_L2 = HCIS_L2
        # self.ELEVATION = ELEVATION
        # self.SITE_PRECISION = SITE_PRECISION
        # self.POSTCODE = POSTCODE
        # self.LICENSING_AREA_ID = LICENSING_AREA_ID
        # self.STATE = STATE
        # self.NAME = NAME
        self.LONGITUDE = LONGITUDE
        self.LATITUDE = LATITUDE
        self.SITE_ID = SITE_ID
        self.data_array = []
        self.connectedServers = connectedServers

    def add_data_entry(self, data_entry):
        self.data_array.append(data_entry)

    def __str__(self):
        return f"EdgeServer ID: {self.SITE_ID}, connectedServers: {self.connectedServers} ,Data Array: {self.data_array}"
