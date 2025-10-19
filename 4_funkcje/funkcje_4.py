shopping_items = [
    "jajka",
    "bułka",
    "ser feta",
    "masło",
    "pomidor",
    "chusteczki",
    "papier toaletowy",
    ]

def shopping(items):
    shopping_cart = "W koszyku znajdują się:\n"
    for item in items:
        shopping_cart += f"- {item}\n"
    return shopping_cart

basket = shopping(shopping_items)
print(basket)
# ojej 

# my practice
my_fav = ["Matrix", "Incepcja", "Interstellar", "Pulp Fiction"]
def fav_movies(movies):
    movie_list = "Moje ulubione filmy to:\n"
    for movie in movies:
        movie_list += f"- {movie}\n"
    return movie_list
result = fav_movies(my_fav)
print(result)

#dodanie enumerate
def fav_movies_numbered(movies):
    movie_list = "Moje ulubione filmy (z dodanymi numerami), to:\n"
    for index, movie in enumerate(movies, start=1):
        movie_list += f"{index}. {movie}\n"
    return movie_list
    
print(fav_movies_numbered(my_fav))

# solution from lesson
print("\n--- rozwiązanie z lekcji dodanie payment i sklepu ---\n")

def shopping(items, payment='card', shop= 'Biedronka'):
    shopping_cart = f"\nW koszyku znajdują się:\n"
    for item in items:
        shopping_cart += f"- {item}\n"
    shopping_cart += f"\nSposób płatności: {payment}\n"
    shopping_cart += f"Sklep: {shop}\n"
    return shopping_cart

basket = shopping(shopping_items, shop='Supermarket',) # wciskam do wywołania funkcji argument jest to pozycyjny
print(basket)

# kolejny sposób wywołania funkcji z argumentami pozycyjnymi albo nazwanymi
print("\n--- rozwiązanie z lekcji argumenty pozycyjne albo nazwane ---\n")

def shopping(items, payment='card', shop= 'Biedronka'):
    shopping_cart = f"\nW koszyku znajdują się:\n"
    for item in items:
        shopping_cart += f"- {item}\n"
    shopping_cart += f"\nSposób płatności: {payment}\n"
    shopping_cart += f"Sklep: {shop}\n"
    return shopping_cart

basket = shopping(shopping_items, 'gotówka') # tu gotówka to argument pozycyjny
print(basket)