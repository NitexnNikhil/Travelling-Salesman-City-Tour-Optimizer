from reader import read_csv
from distance import compute_distances
from tsp_solver import tsp, compute_total_distance
from exporter import save_geojson

def main():
    places = read_csv("places.csv")
    distance_matrix = compute_distances(places)
    route = tsp(places)
    total_distance = compute_total_distance(route, distance_matrix)
    save_geojson(places, route)

    print("\nOptimal tour (returns to start):")
    for idx, i in enumerate(route):
        print(f"{idx + 1}) {places[i][0]}")

    print(f"\nTotal distance: {total_distance:.1f} km")
    print("Route written to route.geojson")

if __name__ == "__main__":
    main()
