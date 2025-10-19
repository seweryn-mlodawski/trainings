def day_times():
    return "morning", "afternoon", "evening", "night"

times = day_times()
print(times)
print(type(times))

first, second, third, fourth = day_times()
print("Trzeci element to %s" % third)

#---------------
# funkcja i jej kolejne wywołania
def add(a, b):
    print(a + b)

add(2, 2)
add(54, 64)
add(40504, 232320)

#------------

def customized_hello(first_name, last_name):
    print("Hello Mr %s %s" % (first_name, last_name))

customized_hello("John", "Cleese")

#------------------
print(f"\n gender prefix\n")

def customized_hello(first_name, last_name, gender_prefix='Mr'):
    print(f"Hello {gender_prefix} {first_name} {last_name}!")

customized_hello("Anna", "Maria", "Pani") # jesli tu nie podam gender prefiksu - to podepnie domyślny czyli Mr