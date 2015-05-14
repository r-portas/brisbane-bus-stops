__author__ = 'roy'

import folium
import analyse

def create_map(suburb=""):
    stops = analyse.parse_bus_stops("datasets/dataset_bus_stops.csv", suburb)
    location = analyse.get_mid_location(stops)
    print(location)

    map = folium.Map(location=location, tiles='Stamen Toner', zoom_start=15, width=1400, height=900)
    for stop in stops:
        map.simple_marker(stop.get_location(), popup=stop.road)

    map.create_map(path='templates/map.html')

