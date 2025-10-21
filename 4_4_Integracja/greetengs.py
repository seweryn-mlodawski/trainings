#def customized_hello(first_name, last_name):
#    print("Hello %s %s!" % (first_name, last_name))
#
#if __name__ == "__main__":
#    customized_hello("John", "Cleese")

#import sys # Importuje moduł sys do obsługi argumentów wiersza poleceń
#
#def customized_hello(first_name, last_name): # Definiuje funkcję przyjmującą imię i nazwisko
#    print("Hello %s %s!" % (first_name, last_name)) # Drukuje spersonalizowane powitanie
#
#if __name__ == "__main__": # Sprawdza, czy skrypt jest uruchamiany bezpośrednio
#    print("Arguments passed:", sys.argv[1:]) # Drukuje przekazane argumenty
#    customized_hello("John", "Cleese") # Wywołuje funkcję z przykładowymi danymi

import sys # Importuje moduł sys do obsługi argumentów wiersza poleceń

def customized_hello(first_name, last_name): # Definiuje funkcję przyjmującą imię i nazwisko
    print("Hello %s %s!" % (first_name, last_name)) # Drukuje spersonalizowane powitanie

if __name__ == "__main__": # Sprawdza, czy skrypt jest uruchamiany bezpośrednio
    if len(sys.argv) < 3: # Sprawdza, czy podano wystarczającą liczbę argumentów
        exit(1) # Kończy program z kodem błędu 1, jeśli argumenty są niewystarczające
    first_name = sys.argv[1] # Pobiera pierwsze imię z argumentów wiersza poleceń
    last_name = sys.argv[2] # Pobiera nazwisko z argumentów wiersza poleceń
    customized_hello(first_name, last_name)     # Wywołuje funkcję z podanymi danymi

    #Tutaj chciałem dodać jeszcze funkcjonalność, polegającą na drukowaniu komunikatow ze wpisano 
    # niewłaściwą liczbę argumentów, i zapetlić to,  -do zrobienia później.
    
    
    

        