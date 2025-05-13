import json

def save_geojson(places, route, filename="route.geojson"):
    geojson = {
        "type": "FeatureCollection",
        "features": [{
            "type": "Feature",
            "geometry": {
                "type": "LineString",
                "coordinates": [[places[i][2], places[i][1]] for i in route]
            },
            "properties": {
                "name": "Optimal Route"
            }
        }]
    }
    with open(filename, "w") as f:
        json.dump(geojson, f, indent=4)
