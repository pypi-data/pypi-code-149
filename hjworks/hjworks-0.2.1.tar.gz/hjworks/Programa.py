import time
import os
import webbrowser

cls=lambda:os.system("cls" if os.name in ("nt","dos") else "clear")

def programa(en1):
    print(f"Hola {en1}, ¿qué deseas hacer hoy? \n")
    print("-Buscar Definiciones (introduce buscar) ")
    print("-Jugar a juegos (introduce jugar) \n")
    pg=input("Hoy quiero ")
    if pg=="buscar":
        cls()
        x=input("Dime la palabra que deseas buscar: ")
        webbrowser.open(f"https://dle.rae.es/{x}")
    if pg=="jugar":
        cls()
        print("Vale, tenemos estos juegos disponibles de momento: \n")
        print("Juego 1-Tres en raya (necesitas dos jugadores) ")
        print("Juego 2-Piedra,papel o tijera (Juegas contra la IA) ")
        print("Juego 3-Wordle ")


