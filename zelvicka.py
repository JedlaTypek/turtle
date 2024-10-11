from turtle import *


# Funkce pro kreslení N-úhelníku
def nuhelnik(n, a):
    uhel = 180 - 180 * ((n - 2) / n)  # Výpočet vnitřního úhlu N-úhelníku
    begin_fill()
    for i in range(n):
        forward(a)
        left(uhel)
    end_fill()


# Funkce pro kreslení kruhu s "želvičkami" (otisk želvy každých 20 stupňů)
def zelvickovy_kruh(mezera):
    clear()
    home()
    setheading(0)
    color("green")
    shape("turtle")
    for i in range(360):
        if i % 20 == 0:
            stamp()  # Otisk želvičky
        forward(mezera)
        left(1)


# Funkce pro kreslení domečku jedním tahem
def domecek_jednim_tahem(a):
    clear()
    home()
    uhlopricka = (a ** 2 + a ** 2) ** (1 / 2)  # Výpočet délky úhlopříčky
    setheading(45)
    forward(uhlopricka)
    left(135)
    forward(a)
    for i in range(3):
        left(90)
        forward(a)
    left(45)
    for i in range(2):
        forward(uhlopricka / 2)
        left(90)
    forward(uhlopricka)


# Funkce pro kreslení stromečku
def stromecek(a):
    clear()
    home()

    uhlopricka = (a ** 2 + a ** 2) ** (1 / 2)  # Výpočet úhlopříčky

    # Kreslení hnědého kmene
    setheading(270)
    color("brown")
    begin_fill()  # Začátek vyplňování hnědou barvou
    for i in range(3):
        forward(a)
        right(90)
    end_fill()  # Konec vyplňování

    # Kreslení zelené koruny
    home()
    setheading(180)
    begin_fill()  # Začátek vyplňování zelenou barvou
    color("green")
    forward(a + a / 2)
    for i in range(2):
        forward(a / 2)
        right(135)
        forward(uhlopricka)
        left(135)
    end_fill()  # Konec vyplňování

    # Přesun zpět na start bez kreslení čáry
    penup()
    home()
    setheading(180)
    forward(a)
    setheading(0)
    pendown()
    begin_fill()  # Další část zelené koruny
    forward(a + a / 2)
    for i in range(2):
        forward(a / 2)
        left(135)
        forward(uhlopricka)
        right(135)
    end_fill()


# Funkce pro kreslení "nevim" s více N-úhelníky
def nevim(pocet, skok, n, uhel):
    barvy = ["red", "green", "blue", "yellow", "purple", "orange", "pink", "black"]
    clear()
    setheading(0)
    for i in range(pocet, 0, -1):
        home()
        left(uhel * i)
        color(barvy[i % len(barvy)])
        nuhelnik(n, i * skok)
