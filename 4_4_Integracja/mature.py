import sys # Importuje moduł sys do obsługi argumentów wiersza poleceń

def print_maturity(age): # Definiuje funkcję przyjmującą wiek
    if age >= 18: # Sprawdza, czy wiek jest większy lub równy 18
        print("You are an adult") # Drukuje komunikat dla dorosłych
    else:
        print("You are a kiddo!") # Drukuje komunikat dla dzieci

if __name__ == "__main__": # Sprawdza, czy skrypt jest uruchamiany bezpośrednio
    age = int(sys.argv[1]) # Pobiera wiek z argumentów wiersza poleceń i konwertuje go na liczbę całkowitą
    print_maturity(age)   # Wywołuje funkcję z podanym wiekiem

