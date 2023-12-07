class Server:
    def __init__(self, SITE_ID, LONGITUDE, LATITUDE, data, neighbors):
        """
        :param SITE_ID: 站点id
        :param LATITUDE: 纬度
        :param LONGITUDE: 经度
        :param data: 存放数据
        :param neighbors: 邻接服务器
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
        self.data = data
        self.neighbors = neighbors

    def add_data_entry(self, data_entry):
        self.data.append(data_entry)
