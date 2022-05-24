# Program : is_prime_number
# Description : tell if a number is a prime number
# Date : 24/05/22
# Author : Christophe LAGAILLARDE
# Version : 1.0

def is_prime_number(number):
    try:
        for i in range(2, number - 1):
            temp = number % i
            if temp == 0:
                return False
        else:
            return True

    except ValueError:
        print("incorect input")
    except TypeError:
        print("incorect input")
    except NameError:
        print("incorect input")
