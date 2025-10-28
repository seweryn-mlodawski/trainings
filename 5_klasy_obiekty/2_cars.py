class Car: #definicja klasy Car
    def __init__(self, make, model_name, top_speed, color): # metoda inicjalizująca z atrybutami
        self.make = make
        self.model_name = model_name
        self.top_speed = top_speed
        self.color = color

car_one = Car(make="Ford", model_name="Mustang", top_speed=250, color="Red") # tworzenie pierwszego obiektu klasy Car
car_two = Car(make="Ford", model_name="Fiesta", top_speed=200, color="Blue") # tworzenie drugiego obiektu klasy Car
car_three = Car(make="Porsche", model_name="911", top_speed=320, color="Black") # tworzenie trzeciego obiektu klasy Car
cars = [car_one, car_two, car_three] # lista obiektów klasy Car
by_speed = sorted(cars, key=lambda car: car.top_speed) # sortowanie listy obiektów według top_speed
by_make = sorted(cars, key=lambda car: car.make) # sortowanie listy obiektów według make

def get_make(car): # funkcja zwracająca atrybut make obiektu car
    return car.make
# end def
by_make_2 = sorted(cars, key=get_make) # sortowanie listy obiektów według make przy użyciu funkcji get_make
for car in by_speed:
    print(f'{car.make} {car.model_name} - Top Speed: {car.top_speed} km/h') # wypisanie posortowanej listy według top_speed
print()