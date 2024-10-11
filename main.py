from turtle import *
from random import random
from zelvicka import *

# Inicializace prostředí pro želvičku
turtles()

# Nekonečná smyčka pro výběr uměleckých funkcí
while True:
    # Zobrazení možností
    print("1 - N-úhelník")
    print("2 - Kruh s želvičkami")
    print("3 - Domeček jedním tahem")
    print("4 - Jednoduchý stromeček")
    print("5 - Nevím, jak to popsat, zkus to ;)")

    # Uživatelský vstup pro výběr funkce
    state = input("Zadej 1-5 pro ZAJÍMAVÉ umělecké funkce, 0 pro vypnutí: ")

    # Ukončení programu při zadání "0"
    if state == "0":
        break

    # Volba 1 - Kreslení N-úhelníku
    elif state == "1":
        home()
        clear()
        n = int(input("Zadej počet stran: "))
        a = int(input("Zadej délku: "))
        nuhelnik(n, a)

    # Volba 2 - Kreslení kruhu s želvičkami
    elif state == "2":
        mezera = int(input("Zadej velikost mezery mezi želvičkami: "))
        zelvickovy_kruh(mezera)

    # Volba 3 - Kreslení domečku jedním tahem
    elif state == "3":
        a = int(input("Zadej velikost strany domečku: "))
        domecek_jednim_tahem(a)

    # Volba 4 - Kreslení jednoduchého stromečku
    elif state == "4":
        a = int(input("Zadej velikost strany stromečku: "))
        stromecek(a)

    # Volba 5 - Uživatelská kreativní funkce
    elif state == "5":
        pocet = int(input("Zadej počet N-úhelníků: "))
        skok = int(input(
            "Zadej číslo, kterým se bude v cyklu násobit pořadí N-úhelníků (i * toto číslo = délka strany N-úhelníku): "))
        n = int(input("Zadej počet stran N-úhelníku: "))
        uhel = int(input("Zadej úhel: "))
        nevim(pocet, skok, n, uhel)

    # Chybný vstup
    else:
        print("Špatný kód.")
