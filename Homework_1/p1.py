# Solve the problem from the first set here

def nr_prim(nr: int) -> bool:  # functei pentru determinarea primalitatii unui numar
    if nr == 2:
        return True
    elif nr % 2 != 0 and nr > 2:
        for d in range(3, nr, 2):
            if nr % d == 0:
                return False

        return True

    return False


# Generați primul număr prim mai mare decât un număr natural dat n.

n = input("Introdu un nr n:")

nr = int(n)

nr = nr + 1

while True:
    if nr_prim(nr):
        print("Primul numar prim mai mare decat numarul natural n este: ", nr)
        break

    nr = nr + 1

# Dat număr natural n, determinați numerele prime p1și p2astfel încât n = p1 + p2(verificați ipoteza Goldbach).

nr = int(n)
b=True

p1=1
p2=2

while b:
    for p1 in range(2, nr):
        if nr_prim(p1):
            for p2 in range(p1, nr - p1):
                if nr_prim(p2):
                    if p1 + p2 == nr:
                        print("numerele" + str(p1) + " " + str(p2) + " confirma ipoteza lui Goldbach")
                        b= False

if p1 == nr - 2 and p2 == nr - p1 - 1:  # nu inteleg de ce imi da eroarea aceasta -> This code is unreachable
    print("nu exista numerele P1 si P2 care sa confirme ipoteza lui Goldbach")

#Determinați o dată calendaristică (ca an, lună, zi) începând de la două numere întregi reprezentând anul și numărul zilei din acel an (de exemplu, ziua numărul 32 este 1 februarie). Luați în considerare anii bisecți. Nu utilizați funcțiile de dată/oră încorporate din Python.
#ianuarie 31
#februarie 28/29 -> 29 bisect
#martie 31
#aprilie 30
#mai 31
#iunie 30
#iulie 31
#august 30
#septembrie 31
#octombrie 30
#noiembrie 31
#decembrie 30

an= int(input("introduce un an calendaristic: "))
zi= int(input("introduce un numar pentru a afla luna in care te afli din anul "+ str(an)+ ": "))
pas=0

#if an%100==0 and an%400!=0: #verific daca ne aflam intr-un an bisect
   # bi= True
#else:
   #bi=False

#while



