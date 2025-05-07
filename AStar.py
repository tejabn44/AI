import heapq

# Heuristic values (straight-line distance to Shivajinagar)
dict_hn = {
    'Shivajinagar': 0,
    'Hinjewadi': 10,
    'Kothrud': 8,
    'Hadapsar': 6,
    'Swargate': 4,
    'Pimpri': 12,
    'Katraj': 7,
    'Viman Nagar': 5,
    'Wakad': 11
}

# Graph with actual distances
dict_gn = {
    'Shivajinagar': {'Swargate': 3, 'Kothrud': 4, 'Hinjewadi': 10},
    'Hinjewadi': {'Wakad': 2, 'Pimpri': 6, 'Shivajinagar': 10},
    'Wakad': {'Pimpri': 4, 'Hinjewadi': 2},
    'Pimpri': {'Hinjewadi': 6, 'Wakad': 4},
    'Swargate': {'Hadapsar': 7, 'Kothrud': 5, 'Shivajinagar': 3, 'Katraj': 4},
    'Hadapsar': {'Swargate': 7},
    'Kothrud': {'Swargate': 5, 'Shivajinagar': 4},
    'Katraj': {'Swargate': 4},
    'Viman Nagar': {}  # No direct connections
}

# A* Search Algorithm
def a_star_search(start, goal):
    priority_queue = []
    heapq.heappush(priority_queue, (dict_hn[start], 0, start, [start]))  # (f(n), g(n), current_city, path)
    
    visited = set()
    
    while priority_queue:
        _, cost, city, path = heapq.heappop(priority_queue)
        
        if city in visited:
            continue
        visited.add(city)

        if city == goal:
            print("\nOptimal A* Path:", " -> ".join(path))
            print("Total Cost:", cost)
            return

        for neighbor, travel_cost in dict_gn.get(city, {}).items():
            if neighbor not in visited:
                new_cost = cost + travel_cost
                f_n = new_cost + dict_hn[neighbor]
                heapq.heappush(priority_queue, (f_n, new_cost, neighbor, path + [neighbor]))

    print("\nNo valid path found from", start, "to", goal)

# Taking user input
start_city = input("Enter the start city: ")
goal_city = input("Enter the goal city: ")

# Checking if cities are valid
if start_city not in dict_gn or goal_city not in dict_hn:
    print("Invalid city name. Please enter a valid city from the list.")
else:
    a_star_search(start_city, goal_city)
