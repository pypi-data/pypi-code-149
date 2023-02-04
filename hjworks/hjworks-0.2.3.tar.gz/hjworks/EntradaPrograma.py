import time
import os
from colorama import Fore

cls=lambda:os.system("cls" if os.name in ("nt","dos") else "clear")

def entrada():
    cls()
    print("Hola, Entra con tu cuenta o Registrate !!! \n")
    print("a)Entrar ")
    print("b)Registrarme \n")
    en=input("Tu opcion: ")
    if en=="a":
        en1=input("Usuario: " )
        en2=input("Contraseña:")
        if (en1 in Users) and (en2 in Pss):
            print(Fore.GREEN+"Acces Granted")
            
        elif (en1=="Héctor") and (en2=="1983"):
            print("Root Administrator Log in ")
            for i in range(0,101):
                print(f"Loading...{i}%")
                time.sleep(0.05)
                cls()
            print(Fore.LIGHTGREEN_EX+"WELCOME MASTER ")

                
        else:
            print(Fore.RED+"Access Dennied")
            en3=input("¿Registrarse?: ")
            if (en3=="si") or (en3=="Si"):
                print(Fore.RESET)
                registro()
            else:
                exit()
    if en=="b":
        registro()
        
def registro():
    #cls
    rg=Users.append(input("Dime tu nombre: "))
    rg1=Pss.append(input("Dime tu contraseña: "))
    time.sleep(0.5)
    print("Registro Completo :D ")
    time.sleep(0.5)
    cls()
    entrada()


Users=[]
Pss=[]
entrada()
