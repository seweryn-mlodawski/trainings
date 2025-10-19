# nowy plik python.py
def greeting_from_file():
    print("Greetings from file!")

greeting_from_file()

if __name__ == "__main__":
    pass
    # here you have a place to write code that will be
    # executed after python <path_to_this_script.py>

def shopping(items, payment='card', shop='local'):          # domyślne wartości argumentów
    result = ""                                             # tworzymy pusty łańcuch znaków
    result = result + "Idę na zakupy do %s.\n" % shop       # dodajemy do łańcucha informację o sklepie
    result = result + "Kupię następujące rzeczy:\n"         # dodajemy nagłówek listy zakupów
    for item in items:                                      # iterujemy po liście zakupów
        result = result + " - %s\n" % item                  # dodajemy każdy zakup do łańcucha gdzie %s to element listy
    result = result + "By zapłacić, używam %s." % payment   # dodajemy informację o sposobie płatności
    return result                                           # zwracamy gotowy łańcuch znaków

items = ["cola", "whiskey", "lód"]                          # lista zakupów
text = shopping(items, 'card', 'small local shop')          # wywołanie funkcji z wszystkimi argumentami
print(text)