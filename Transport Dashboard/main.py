# -> MySQL for bus timetable app to read w/ RESTful
# machine learning model -> linear regression
# startup function to poll SQL database 

import requests, googlemaps, time, json

headers = {"content-type": "application/JSON", "accept": "application/JSON"}
API_URL = "https://api.translink.ca/rttiapi/v1/"
API_KEY = "hg7zM8guAd8z0YAqcwmO"
house_coords = (49.23611276734657, -123.20630802759638)
GMAP_KEY = ""


def get_current_coords():
    gmaps = googlemaps.Client(key=GMAP_KEY)
    # get current location with api
    return house_coords


def local_bus_stops():
    coords = get_current_coords()
    return get_nearby_stops(
        coords[0], coords[1], 500
    )  # optionlal route number and radius specificaiton


def automatically_detect_bus_stop(bus_stops):
    while True:
        for stop in bus_stops:
            get_bus_estimates(stop)
        time.sleep(60)


# get bus routes near me to take me to destination or within x_radius of destination
# -> bus stop information gives lat and long at each stop, can use this to calculate distance to destination w/ rad
#  The API will require a unique API key to request for data.
# The API key will authorize to offer a maximum of 1,000 requests per day for use of the Data. This is to prevent malicious users from abusing our service.
# This might change and is open for discussion.
# dashboard of all bus routes added
# get current location
# get bus stops within 500m
# return list of bus stops
# google for distance to bus sotp form current location
# return list of bus stops in area w/ routes etc. supplied
# respoinse fields descriptors
# interacting with KMZ encoded location
# filter response for error codes -> 404 can include code with error message from server
# storage of data results into local database w/ SQL lite? reading the data and stored metrics and predicting results w/ linear regression after function calls and data references finished


def get_nearby_stops(lat, long, rad=200, routeNo=None):
    stops_url = (
        API_URL
        + "stops?apikey="
        + str(API_KEY)
        + "&lat="
        + str(lat)
        + "&long="
        + str(long)
        + "&radius="
        + str(rad)
    )
    print(stops_url)
    if routeNo:
        url = stops_url + "&routeNo=" + f"{routeNo:03}"
        r = requests.get(url, headers=headers).json()
    else:
        r = requests.get(stops_url, headers=headers).json()

    if r["Code"] != None:
        print(r["Code"], r["Message"])
    else:
        print(json.dumps(r, indent=4, sort_keys=True))


def get_bus_estimates(stopNo, count=3, timeframe=20, routeNo=None):
    estimates_url = (
        API_URL
        + "stops/"
        + str(stopNo)
        + "/estimates?apikey="
        + str(API_KEY)
        + "&count="
        + str(count)
        + "&timeframe="
        + str(timeframe)
    )
    if routeNo:
        url = estimates_url + "&routeNo=" + f"{routeNo:03}"
        r = requests.get(url, headers=headers).json()
    else:
        r = requests.get(estimates_url, headers=headers).json()

    print(r)

    print(json.dumps(r, indent=4, sort_keys=True))
    if r[0]["Code"] != None:
        print(r["Code"], r["Message"])
    else:
        print(json.dumps(r, indent=4, sort_keys=True))

    pass


def get_response(url):
    r = requests.get(url, headers=headers).json()
    if r["Code"] != None:
        print(r["Code"], r["Message"])
    else:
        print(json.dumps(r, indent=4, sort_keys=True))


def get_bus_locations(stopNo, routeNo=None):
    bus_locations_url = (
        API_URL + "buses?apikey=" + str(API_KEY) + "&stopNo=" + str(stopNo)
    )

    if routeNo:
        url = bus_locations_url + "&routeNo=" + f"{routeNo:03}"
        r = requests.get(url, headers=headers).json()
    else:
        r = requests.get(bus_locations_url, headers=headers).json()

    print(json.dumps(r, indent=4, sort_keys=True))


def get_bus_routes(routeNo=None, StopNo=None):
    bus_routes_url = API_URL + "routes"

    if StopNo:
        url = bus_routes_url + "?apikey=" + str(API_KEY) + "&stopNo=" + str(StopNo)
        r = requests.get(url, headers=headers).json()
    if routeNo:
        url = bus_routes_url + "/" + f"{routeNo:03}" + "?apikey=" + str(API_KEY)
        r = requests.get(url, headers=headers).json()

    print(json.dumps(r, indent=4, sort_keys=True))  # type: ignore


def get_bus_status():
    bus_status_url = API_URL + "status/all?apikey=" + str(API_KEY)
    r = requests.get(bus_status_url, headers=headers).json()
    print(json.dumps(r, indent=4, sort_keys=True))


# bus timetable w/ google maps, location services and local polling table
