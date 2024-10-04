# Lege eine Liste mit dem Namen shoppinglist an
shoppinglist = []

# definiere eine Funktion add_item
def add_item():
    item = input("Bitte gib den Artikel ein, der zur Einkaufsliste hinzugefügt werden soll: ")
    shoppinglist.append(item)
    print("Der Artikel wurde zum Einkaufswagen hinzugefügt.")

# definiere eine Funktion show_shoppinglist
def show_shoppinglist():
    # Überprüfe, ob shoppinglist nicht leer ist
    if (shoppinglist):
        print("Deine Einkaufsliste: ")
        for item in shoppinglist:
            print(f"{item}")
    else:
        print("Die Einkaufsliste ist leer")
