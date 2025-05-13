TSP Route Optimizer with GeoJSON Export
This project reads geographical coordinates from a CSV file, computes the shortest possible route (using a greedy TSP approach), calculates the total distance, and exports the route in GeoJSON format to visualize on a map.

##########################

#   Project Structure

Travelling Salesman City-Tour Optimizer/
│
├── main.py             # Main script to run the program
├── reader.py           # Reads coordinates from CSV
├── distance.py         # Haversine and distance matrix logic
├── tsp_solver.py       # Greedy TSP algorithm and distance calculator
├── exporter.py         # Exports the route as a GeoJSON file
└── places.csv          # Input data file with place names and coordinates




########################

# Step by Step Understanding the code

        Step 1: Read the CSV Data

                Reads a list of places with latitude and longitude from a CSV file.

                def read_csv(file_path):
                ...

        Step 2: Haversine Distance Calculation

                Calculates the great-circle distance between two geographical coordinates.

                def haversine(lat1, lon1, lat2, lon2):
                ...

        Step 3: Distance matrix

                Builds a matrix of distances between all pairs of places using the Haversine formula.

                def compute_distances(places):
                ...

        Step 4: TSP Solver (Greedy Approach)
                
                Uses a simple greedy method to find a route visiting all places starting from the first one and returning to the start.

                def tsp(places):
                ...

        Step 5: Calculate Total Route Distance
                
                Adds up the total length of the computed route.

                def compute_total_distance(route, distance_matrix):
                ...
        
        Step 6: Export to GeoJSON

                Exports the route as a .geojson file so it can be viewed on a map.

                def save_geojson(places, route, filename="route.geojson"):
                 ...

######################################

#   places.csv Format

        Name,Lat,Lon
        Eiffel Tower,48.8584,2.2945
        Louvre Museum,48.8606,2.3376
        Notre-Dame,48.8530,2.3499
        Arc de Triomphe,48.8738,2.2950
        Name: Name of the place.

        Lat: Latitude.

        Lon: Longitude.

#   Sample Output(Given sample)

        
        Optimal tour (returns to start):
        1) Eiffel Tower
        2) Notre-Dame
        3) Louvre Museum
        4) Arc de Triomphe
        5) Eiffel Tower

        Total distance: 10.5 km 
        Route written to route.geojson
        nikhilpathrabe@Nikhils-MacBook-Air Travelling Salesman City-Tour Optimizer % 



#   🛠️ Dependencies
    This project only uses Python's built-in modules:

        csv

        json

        math































