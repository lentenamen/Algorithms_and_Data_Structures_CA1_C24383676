import csv
from models.vehicles import Vehicle

class VehicleDataLoader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.__vehicles = []
        self.load_data()

    def load_data(self):
        with open(self.file_path, newline='',encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                vehicle = Vehicle(
                Vehicle_ID=row['Vehicle_ID'],
                Brand=row['Brand'],
                Model=row['Model'],
                Year=row['Year'],
                Mileage=row['Mileage'],
                Engine_Size=row['Engine_Size'],
                Price=row['Price']
                )
                self.__vehicles.append(vehicle)


    def get_all_data(self):
        return self.__vehicles.copy()
    
    def get_data_by_size(self, size):
        if size < 0:
            raise ValueError("Size must be non-negative")
        return self.__vehicles[:size]
            
    def get_by_year(self, year):
        results = []
        for vehicle in self.__vehicles:
            if vehicle.Year == year:
                results.append(vehicle)
        return results