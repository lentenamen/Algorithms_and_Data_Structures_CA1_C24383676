class Company:
    def __init__(self, name, vehicles_list=None):
        self.name = name
        self.__vehicles = vehicles_list

    # Add a single vehicle
    def add_vehicle(self, vehicle):
        self.__vehicles.append(vehicle)

    def get_vehicles(self):
        return self.__vehicles.copy()
    
    def total_vehicles_count(self):
        return len(self.__vehicles)
    
    def sort_vehicles(self, sorter, key_function=lambda x: x):
        return sorter.sort(self.__vehicles, key=key_function)
    
    def get_top_vehicles(self, sorter, n=10):
        # Step 1: Use the sorting algorithm
        sorted_vehicles = sorter.sort(
        self.__vehicles,
        key=lambda x: x.Price
        )
        # Step 2: Collect top N using backward while loop
        top_vehicles = []
        index = len(sorted_vehicles) - 1 # Start at last element
        while index >= 0 and len(top_vehicles) < n:
            top_vehicles.append(sorted_vehicles[index])
            index -= 1 # Move backwards
        return top_vehicles