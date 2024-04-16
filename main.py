from abc import ABC, abstractmethod

# Product
class Car:
    def __init__(self):
        self.make = None
        self.model = None
        self.color = None
        self.year = None

    def __str__(self):
        return f"{self.year} {self.color} {self.make} {self.model}"

# Builder Interface
class Builder(ABC):
    @abstractmethod
    def set_make(self):
        pass

    @abstractmethod
    def set_model(self):
        pass

    @abstractmethod
    def set_color(self):
        pass

    @abstractmethod
    def set_year(self):
        pass

    @abstractmethod
    def get_result(self) -> Car:
        pass

# Concrete Builder
class CarBuilder(Builder):
    def __init__(self):
        self.car = Car()

    def set_make(self, make):
        self.car.make = make
        return self

    def set_model(self, model):
        self.car.model = model
        return self

    def set_color(self, color):
        self.car.color = color
        return self

    def set_year(self, year):
        self.car.year = year
        return self

    def get_result(self) -> Car:
        return self.car

# Director
class CarBuildDirector:
    def __init__(self, builder: Builder):
        self.builder = builder

    def construct_sports_car(self):
        return self.builder \
            .set_make("Ferrari") \
            .set_model("488 GTB") \
            .set_color("Red") \
            .set_year(2022) \
            .get_result()

    def construct_suv(self):
        return self.builder \
            .set_make("Tesla") \
            .set_model("Model X") \
            .set_color("White") \
            .set_year(2023) \
            .get_result()

# Usage
builder = CarBuilder()
director = CarBuildDirector(builder)

sports_car = director.construct_sports_car()
suv = director.construct_suv()

print(sports_car)
print(suv)
