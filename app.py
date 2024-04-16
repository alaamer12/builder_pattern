class Car:
    def __init__(self):
        self.make = None
        self.model = None
        self.year = None
        self.color = None
        self.engine = None
        self.transmission = None

    def __str__(self):
        return f"{self.year} {self.make} {self.model} in {self.color} with a {self.engine} engine and {self.transmission} transmission"


class CarBuilder:
    def __init__(self):
        self.car = Car()

    def set_make(self, make):
        self.car.make = make
        return self

    def set_model(self, model):
        self.car.model = model
        return self

    def set_year(self, year):
        self.car.year = year
        return self

    def set_color(self, color):
        self.car.color = color
        return self

    def set_engine(self, engine):
        self.car.engine = engine
        return self

    def set_transmission(self, transmission):
        self.car.transmission = transmission
        return self

    def build(self):
        return self.car


# Usage
builder = CarBuilder()
car = builder.set_make("Toyota") \
             .set_model("Camry") \
             .set_year(2022) \
             .set_color("Blue") \
             .set_engine("V6") \
             .set_transmission("Automatic") \
             .build()

print(car)
