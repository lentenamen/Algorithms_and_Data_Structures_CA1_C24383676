class Vehicle:
    def __init__(self,Vehicle_ID, Brand, Model, Year, Mileage, Engine_Size, Price):
        self.Vehicle_ID = Vehicle_ID
        self.Brand = Brand
        self.Model = Model
        self.Year = int(Year)
        self.Mileage = float(Mileage)
        self.Engine_Size = float(Engine_Size)
        self.Price = float(Price)
    
    def __repr__(self):
        return (f"Vehicle ID={self.Vehicle_ID}, Brand={self.Brand}, "
                f"Model={self.Model}, Year={self.Year}, "
                f"Mileage={self.Mileage}, Engine_Size={self.Engine_Size}, "
                f"Price={self.Price}")