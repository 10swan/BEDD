from geopy.distance import lonlat, geodesic


def compute_distance(server_1, server_2):
    server_1_position = lonlat(server_1.LONGITUDE, server_1.LATITUDE)
    server_2_position = lonlat(server_2.LONGITUDE, server_2.LATITUDE)
    distance_between_servers = geodesic(server_1_position, server_2_position).meters
    return distance_between_servers
