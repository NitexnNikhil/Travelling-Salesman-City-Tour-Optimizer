from distance import compute_distances
from itertools import permutations

def tsp(places):
    n = len(places)
    dist_matrix = compute_distances(places)

    best_route = []
    min_dist = float("inf")

    for perm in permutations(range(1, n)):
        route = [0] + list(perm) + [0]
        dist = sum(dist_matrix[route[i]][route[i+1]] for i in range(n))
        if dist < min_dist:
            min_dist = dist
            best_route = route

    return best_route

def compute_total_distance(route, distance_matrix):
    return sum(distance_matrix[route[i]][route[i + 1]] for i in range(len(route) - 1))
