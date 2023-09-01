from random import *


def start():

    global v
    v = 3

    print("Willkommen zur Lottery")
    answerPlay = input("Möchtest du spielen? ")

    if answerPlay == "ja" or answerPlay == "Ja":
        print("Okey, dann lass und beginnen.")
        programm()
    else:
        print("Okey, dann beendet das Programm hier")

def programm():
    global z1
    global z2

    z1 = randint(1, 10)
    z2 = randint(1, 10)
    ask()

def ask():
    global v
    global z1
    global z2

    z1_vers = int(input("Gib die erste Zahl zwischen 1-10 ein: "))
    z2_vers = int(input("Gib die zweite Zahl zwischen 1-10 ein: "))

    if z1 == z1_vers and z2 == z2_vers:
        print("Du hast beide Zahlen richtig. Herzlichen Glückwunsch.")

    elif z1 == z1_vers or z2 == z2_vers:
        v = v - 1
        print("Du hast eine Zahl richtig, versuche es erneut. Du hast noch ", v, " Versuche")
        checkI()

    else:
        v = v - 1
        print("Das ist leider falsch, bitte versuche es erneut.")
        print("Du hast noch ", v, " Versuche")
        checkI()

def checkI():
    global v

    if v == 0:
        print("Leider alle Versuche aufgebraucht.")
        answerNew = input("Möchtest du ein neues spiel starten? ")
        if answerNew == "Ja" or answerNew == "ja":
            ask()

        else:
            print("Programm beendet")
    else:
        ask()


start()