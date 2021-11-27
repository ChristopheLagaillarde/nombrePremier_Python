import sys
sys.tracebacklimit = 0

try:
    a = int(input("saisir un nombre"))
except ValueError:
    print("Saisie incorrecte!")


try:
    for i in range(2, a-1):
        temp = a % i
        if temp == 0:
            print("Ce nombre n'est pas premier")
            break
    else:
        print("Ce nombre est premier !")
except NameError:
    print()