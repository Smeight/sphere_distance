from functions import distance_on_sphere
from functions import route_distance

# coordinates of two points
lat1, lon1 = 55.7522, 37.6156
lat2, lon2 = 55.7536, 37.6232

# calculate distance between the two points
distance = distance_on_sphere(lat1, lon1, lat2, lon2)
print(f"Distance between the two points: {distance} km")

# calculate the shortest route distance between the two points
route_distance = route_distance(lat1, lon1, lat2, lon2)
print(f"Shortest route distance between the two points: {route_distance} meters")

