# 1. Funkcja, która przyjmuje argumenty pozycyjne lub nazwane (domyślnie)
def fun_default(a, b):
    pass

# 2. Funkcja, która przyjmuje tylko argumenty pozycyjne
def fun_positional(a, b, /):
    pass

# 3. Funkcja, która przyjmuje tylko argumenty nazwane
def fun_keyword(*, a, b):
    pass
# 4. Funkcja, która przyjmuje dowolną liczbę argumentów pozycyjnych
def count_them_all(*args):
    positional_args_count = len(args)
    print(f"I have received {positional_args_count} positional arguments")
count_them_all(1, 2, 3, "A")

# 5. Funkcja, która przyjmuje dowolną liczbę argumentów nazwanych 
def count_them_all(*args, **kwargs):
    positional_args_count = len(args)
    keyword_args_count = len(kwargs)
    print(f"I have received {positional_args_count} positional arguments and {keyword_args_count} keyword arguments")
count_them_all(1, 2, 3, "A")

# 6. Funkcja, która przyjmuje dowolną liczbę argumentów pozycyjnych i nazwanych

def count_them_all(*args, **kwargs):
    positional_args_count = len(args)
    keyword_args_count = len(kwargs)
    print(f"I have received {positional_args_count} positional arguments and {keyword_args_count} keyword arguments")
count_them_all(1, 2, 3, "A", a=10, b=20)