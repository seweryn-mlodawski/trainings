import sys # Importuje moduł sys do obsługi argumentów wiersza poleceń
import logging  # Importuje moduł logging do obsługi logowania komunikatów

#----------------------------------
#logging.basicConfig(level=logging.DEBUG) # Ustawia poziom logowania na DEBUG - bez formatu
#logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s')  # Ustawia format logowania z czasem i poziomem komunikatu
#----------------------------------

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s', filename="logfile.log") # Ustawia logowanie do pliku logfile.log - jest to kolejna opcja logowania
def print_maturity(age): # Definiuje funkcję przyjmującą wiek
    if age >= 18:
        logging.info("You are an adult")
    else:
        logging.info("You are a kiddo!")

if __name__ == "__main__": # Sprawdza, czy skrypt jest uruchamiany bezpośrednio
    logging.debug("The program was called with this parameters %s" % sys.argv[1:]) # Drukuje wszystkie argumenty wiersza poleceń przekazane do programu
    logging.debug("First parameter is %s" % sys.argv[1]) # Drukuje pierwszy argument wiersza poleceń
    age = int(sys.argv[1]) # Pobiera wiek z argumentów wiersza poleceń i konwertuje go na liczbę całkowitą
    print_maturity(age)
