class Car:
    make: str
    model: str
    year: int
    color: str
    milage: float

    def __init__(self, make, model, year, color, milage):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.milage = milage


    def update_mileage(self, miles: float):
        self.milage += miles

    def display_info(self):
        print(self.make)
        print(self.model)
        print(self.year)
        print(self.color)
        print(self.milage)

def calculate_depreciation(car: Car, depreciation_rate: float):
    return car.milage * depreciation_rate

