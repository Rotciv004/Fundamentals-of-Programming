# Solve the problem from the second set here
#Luați în considerare un număr natural dat n. Determinați produsul p tuturor factorilor corespunzători ai n.

n=int(input("Introduceti un numar n: "))

p=1

for d in range(2,n+1):
    if n%d==0:
        p=p*d

print("produsul tuturor factorilor corespunzatori ai lui n este: "+str(p))

#Palindromul unui număr este numărul obținut prin inversarea ordinii cifrelor sale (de exemplu, palindrome of 237 is 732). Pentru un număr natural dat n, determinați-i palindromul.

nn=0

print("palindromul numarului "+ str(n)+" este: ")

while n!=0:
    nn=nn*10+n%10
    n=n//10

print(nn)