#print("Pokażę wszystko, co wpiszesz!")
#text = input()
#print("Oto Twój tekst: ***%s***" % text)

#items_text = "cola,whiskey,lód"
#items = items_text.split(',')
#print(type(items))
#print(len(items))

def shopping(items, payment='card', shop='local shop'):
    result = ""
    result = result + "Idę na zakupy do %s.\n" % shop
    result = result + "Kupię następujące rzeczy:\n"
    for item in items:
        result = result + " - %s\n" % item
    result = result + "By zapłacić, używam %s." % payment
    return result

if __name__ == "__main__":
    items_text = input("Podaj proszę produkty rozdzielone przecinkiem: ") # pobranie tekstu od użytkownika
    items = items_text.split(',') # konwersja tekstu na listę
    shopping_result = shopping(items)
    print(shopping_result)