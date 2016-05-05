'''
Created on 6 Apr 2016

@author: Federico Ressi <federico.ressi@intel.com>
'''
import sys

def is_prime(number):
    """ returns True if given number is prime
    """
    i = 2
    while i < number:
        if number % i == 0:
            return False
        i += 1

    return True


def print_primes(max_number):
    """ Prints al prime numbers that are smaller than max_number

    To iterate numbers please use while statement.
    To look if a number is prime it calls is_prime function.
    """

    i = 1
    print "Primes < %d: \n" % max_number
    while i < max_number:
        if is_prime(i) is True:
            print "%d " % i

        i += 1

    print "\n\n"


def main():
    for j in sys.argv[1:]:
        print_primes(int(j))


if __name__ == "__main__":
    main()
