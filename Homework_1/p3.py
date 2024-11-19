# Solve the problem from the third set here
#Generați cel mai mare număr perfect mai mic decât un număr natural dat n. Dacă un astfel de număr nu există, ar trebui să fie afișat un mesaj. Un număr este perfect dacă este egal cu suma divizorilor săi, cu excepția lui însuși. (de ex. 6 is a perfect number, as 6=1+2+3).

def nr_perfect(nr: int)->bool:
    s=0

    for d in range(1,nr):
        if nr%d==0:
            s=s+d

    if nr==s:
        return True
    else:
        return False


n=int(input("Introdu un numar n: "))

b=False

for nr in range(n-1,0,-1):
    if nr_perfect(nr):
        print("Cel mai mare numar perfect mai mic decat "+str(n)+" este: "+str(nr))
        b=True
        break

if b==False:
    print("Nu exista un numar perfect mai mic decat "+str(n))