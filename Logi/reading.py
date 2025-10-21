with open("names.txt", "r") as read_file: # Otwiera plik names.txt w trybie do odczytu
    for line in read_file.read().splitlines(): # Iteruje przez każdą linię w pliku, usuwając znaki nowej linii
        print(line) # Drukuje każdą linię na konsolę

        