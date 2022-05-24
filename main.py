# Program : main
# Description : execute the function is_prime_number
# Date : 24/05/22
# Author : Christophe LAGAILLARDE
# Version : 1.0

from is_prime_number import is_prime_number


def main():
    try:
        if is_prime_number(int(input("input a number, we will tell you if it is a prime number:"))):
            print("it's a prime number")
        else:
            print("it's not a prime number")
    except ValueError:
        print("incorect input")
    except TypeError:
        print("incorect input")
    except NameError:
        print("incorect input")


if __name__ == '__main__':
    main()