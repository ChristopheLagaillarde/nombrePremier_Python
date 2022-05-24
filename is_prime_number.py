# Program : is_prime_number
# Description : tell if a number is a prime number
# Date : 24/05/22
# Author : Christophe LAGAILLARDE
# Version : 1.0

def is_prime_number(number):
    try:
        i = 0
        for i in range(2, number - 1):
            temp = number % i
            if temp == 0:
                return False, i
        else:
            return True, i

    except ValueError:
        print("incorect input")
    except TypeError:
        print("incorect input")
    except NameError:
        print("incorect input")
