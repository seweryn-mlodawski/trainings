new_name = "Luke" # Definiuje nową nazwę do dodania do pliku
with open("names.txt", 'a') as write_file: # Otwiera plik names.txt w trybie do dopisywania
    write_file.write("\n" + new_name) # Dopisuje nową nazwę do pliku z nową linią przed nią
    
    
#Jeśli chcemy do niego dopisywać, to użyjemy trybu append, oznaczanego jako a:
# jeśli chcemy nadpisać zawartość pliku, to użyjemy trybu write, oznaczanego jako w:

#with open("names.txt", "w") as write_file: # Otwiera plik names.txt w trybie do zapisu (nadpisywania)
#    write_file.write("\n" + new_name) # Nadpisuje zawartość pliku nową nazwą z nową linią przed nią