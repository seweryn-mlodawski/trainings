class Car:
    def __init__(self, make, model_name, top_speed, color): # inicjalizacja atrybutów
        self.make = make 
        self.model_name = model_name
        self.top_speed = top_speed
        self.color = color
        self._current_speed = 0 # prywatny atrybut prędkości

    def accelerate(self, step=10): # metoda przyspieszania
        self.current_speed += step # użycie właściwości current_speed

    def decelerate(self, step=10): # metoda zwalniania
        self.current_speed -= step # użycie właściwości current_speed

    @property # właściwość do pobierania i ustawiania prędkości 
    def current_speed(self): # zwraca aktualną prędkość
        return self._current_speed

    @current_speed.setter # ustawia aktualną prędkość z ograniczeniem do top_speed, .setter - definiuje metodę ustawiającą wartość właściwości
    def current_speed(self, value): #
        if value <= self.top_speed: 
            self._current_speed = value
        else:
            raise ValueError(f"Value {value} exceeds top speed of {self.top_speed}") 

    def __str__(self): # metoda do reprezentacji obiektu jako string
        return f"{self.color} {self.make} {self.model_name}"

    def __repr__(self): # oficjalna reprezentacja obiektu
        return (f"Car(make={self.make}, model={self.model_name}, "
                f"top_speed={self.top_speed}, color={self.color})")

    def __eq__(self, other): # porównanie dwóch obiektów Car
        return all(( 
            self.make == other.make,
            self.model_name == other.model_name,
            self.top_speed == other.top_speed,
            self.color == other.color
        ))

    def __gt__(self, other): # porównanie prędkości dwóch samochodów
        return self.top_speed > other.top_speed 

# Dziedziczenie – ciężarówka jako rozszerzony samochód
class Truck(Car): 
    def __init__(self, make, model_name, top_speed, color, max_load):
        super().__init__(make, model_name, top_speed, color) # wywołanie konstruktora klasy bazowej
        self.max_load = max_load # dodatkowy atrybut dla ciężarówki

    def __str__(self): # nadpisana metoda do reprezentacji obiektu jako string
        return f"{self.color} {self.make} {self.model_name} (ładowność: {self.max_load} kg)"

# Przykłady użycia:
car1 = Car("Toyota", "Corolla", 180, "niebieski")
car2 = Car("Ford", "Mustang", 250, "czerwony")
truck = Truck("Mercedes", "Actros", 90, "czarny", 1200)

print(car1)
print(repr(car2))
car1.accelerate(30)
print(car1.current_speed)
try: # ustawienie prędkości powyżej top_speed
    car1.current_speed = 300 
except ValueError as e: # obsługa wyjątku
    print(e)

print(truck)
truck.accelerate()
print(truck.current_speed)

truck = Truck(make="Mercedes", model_name="Sprinter", color="Black", top_speed=90, max_load=1200)
car = Car(make="Ford", model_name="Mustang", top_speed=250, color="red")
isinstance(car, Truck)  # False to oznacza, że obiekt car nie jest instancją klasy Truck
isinstance(truck, Car)  # True to oznacza, że obiekt truck jest instancją klasy Car, ponieważ Truck dziedziczy po Car
print(isinstance(car, Truck))  # False
print(isinstance(truck, Car))  # True
issubclass(Truck, Car)  # True to oznacza, że Truck jest podklasą Car
issubclass(Car, Truck)  # False to oznacza, że Car nie jest podklasą Truck
print(issubclass(Truck, Car))  # True 