class Car:
   def __init__(self, make, model_name, top_speed, color, rok):
       self.make = make
       self.model_name = model_name
       self.top_speed = top_speed
       self.color = color
       self.roczek = rok #dodałem rok jako atrybut z wartością domyślną self.roczek = 2020, lub tak jak jest 
        
mustang = Car(make="Ford", model_name="Mustang", top_speed=250, color="red", rok="2020")
print(mustang.make)
print(mustang.model_name)
print(mustang.top_speed)
print(mustang.color)
print(mustang.roczek)
print()

def __str__(self):
       return f'{self.color}'
       #return f"{self.make} {self.model_name} ({self.roczek}) - {self.color}, Top Speed: {self.top_speed} km/h"
print(mustang)