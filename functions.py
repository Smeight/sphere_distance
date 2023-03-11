import osmnx as ox
from math import radians, cos, sin, asin, sqrt


def route_distance(lat1, lon1, lat2, lon2, G):
    # define two points
    point1 = (lat1, lon1)
    point2 = (lat2, lon2)

    # get the nearest nodes to the points
    node1 = ox.distance.nearest_nodes(G, lon1=point1[1], lat1=point1[0])
    node2 = ox.distance.nearest_nodes(G, lon1=point2[1], lat1=point2[0])

    # calculate the shortest path between the nodes
    route = ox.shortest_path(G, node1, node2, weight='length')

    # calculate the length of the route
    distance = sum(ox.utils_graph.get_route_edge_attributes(G, route, 'length'))

    return distance


def distance_on_sphere(lat1, lon1, lat2, lon2, radius=6371, decimals=2):
    if not (-90 <= lat1 <= 90 and -180 <= lon1 <= 180 and -90 <= lat2 <= 90 and -180 <= lon2 <= 180):
        raise ValueError("Incorrect coordinates provided")
    # convert coordinates to radians
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])

    # calculate the distance between the points
    distance_lon = lon2 - lon1
    distance_lat = lat2 - lat1
    a = sin(distance_lat/2)**2 + cos(lat1) * cos(lat2) * sin(distance_lon/2)**2
    c = 2 * asin(sqrt(a))
    distance = c * radius
    return round(distance, decimals)
