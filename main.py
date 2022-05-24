# Program : main
# Description : execute the function is_prime_number
# Date : 24/05/22
# Author : Christophe LAGAILLARDE
# Version : 1.0

from is_prime_number import is_prime_number


def main():
    try:
        is_prime, divider = is_prime_number(int(input("input a number, we will tell you if it is a prime number:")))
        if is_prime:
            print("it's a prime number")
        else:
            print(f"it's not a prime number, it can be divided by {divider}")

    except ValueError:
        print("incorrect input")
    except TypeError:
        print("incorrect input")
    except NameError:
        print("incorrect input")


if __name__ == '__main__':
    main()