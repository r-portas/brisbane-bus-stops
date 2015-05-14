"""Analyses datasets"""
from csv import reader

def parse_bus_stops(filename, suburb_filter=""):
    """Parses a csv file of bus stops
    Returns a list of bus stops
    """
    bus_stops = []

    with open(filename, "rb") as bus_stop_file:
        bus_csv_reader = reader(bus_stop_file)
        header = bus_csv_reader.next()

        # Each second line of the file is garbage
        toggle = 0

        for line in bus_csv_reader:
            if toggle:
                if suburb_filter != "":
                    if line[3] == suburb_filter:
                        bus_stops.append(BusStop(line[0], line[2], line[3], line[7], line[8]))
                else:
                    bus_stops.append(BusStop(line[0], line[2], line[3], line[7], line[8]))
                toggle = 0
            else:
                toggle = 1

    return bus_stops

"""Finds the middle location of all stops in the list, used for centering the map on the points
    Return a list of coordinates, [lat, long]
"""
def get_mid_location(bus_stops):
    max_lat = 0
    min_lat = 0

    max_long = 0
    min_long = 0

    for stop in bus_stops:
        # Find the lats
        if max_lat == 0:
            max_lat = stop.lat
        else:
            if max_lat < stop.lat:
                max_lat = stop.lat

        if min_lat == 0:
            min_lat = stop.lat
        else:
            if min_lat > stop.lat:
                min_lat = stop.lat

        # Find the longs
        if max_long == 0:
            max_long = stop.long
        else:
            if max_long < stop.long:
                max_long = stop.long

        if min_long == 0:
            min_long = stop.long
        else:
            if min_long > stop.long:
                min_long = stop.long

    mid_lat = ((max_lat - min_lat) / 2) + min_lat
    mid_long = ((max_long - min_long) / 2) + min_long

    return [mid_lat, mid_long]


"""Stores a bus stop"""
class BusStop:
    def __init__(self, stopid, road, suburb, lat, long):
        self.stopid = stopid
        self.road = road
        self.suburb = suburb
        self.lat = float(lat)
        self.long = float(long)

    def __repr__(self):
        return "{} - {}, {} - ({}, {})".format(self.stopid, self.road, self.suburb, self.long, self.lat)

    def get_location(self):
        """Returns the location of the bus stop in a list [lat, long]"""
        return [self.lat, self.long]

if __name__ == "__main__":
    stops = parse_bus_stops("datasets/dataset_bus_stops.csv")
    print(stops)