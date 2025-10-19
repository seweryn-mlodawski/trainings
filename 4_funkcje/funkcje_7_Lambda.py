shopping_items = [
    ("ziemniak", 2.5, 0.51),
    ("cebula", 3, 1.60),
    ("ser", 0.8, 15.50)
]

def get_index_1_tuple_element(given_tuple): # Funkcja pobiera krotkę (np. ('ziemniak', 2.5, 0.51)) i zwraca jej drugi element (o indeksie 1).
# W kontekście zadania: jest to ilość kilogramów danego produktu.
    return given_tuple[1]

sorted_items = sorted(shopping_items, key=get_index_1_tuple_element) # Sortujemy listę shopping_items według ilości kilogramów, korzystając z powyższej funkcji jako klucza sortowania.
print(sorted_items)

# lub możemy użyć funkcji lambda, aby osiągnąć to samo w bardziej zwięzły sposób:
sorted_items = sorted(shopping_items, key=lambda given_tuple: given_tuple[1])
print(sorted_items)

# filtracja za pomocą funkcji lambda
print("\n--- filtracja za pomocą funkcji lambda ---\n")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers)

# Wyciągamy tylko liczby parzyste za pomocą funkcji filter i lambdy
print("\n--- wyciąganie liczb parzystych za pommocą Lambda---\n")
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(even_numbers)
