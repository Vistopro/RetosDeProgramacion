##
 ## Escribe un programa que, dado un número, compruebe y muestre si es primo,
 ## fibonacci y par.
 ## Ejemplos:
 ## - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 ## - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 ## 
from math import sqrt

def esPrimo(n):
    a=2
    while (a<sqrt(n)+1):
        if(n%a==0 and n!=2):
            return False
        else: return True
        a+1

def esFibonacci(n):
    


def esPar(n):
    if (n%2==0): return True
    else: return False


n=int(input("Por favor, escribe un numero: "))

print(esPrimo(n))
print(esPar(n))