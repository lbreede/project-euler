def main():
    i = 2

    primesFound = 0

    while True:
        if isPrime(i):
            primesFound += 1
            if primesFound == 10001:
                return i
                break
        i += 1

def isPrime(num):
    """ Function to check if incoming number is a prime number
        Copied from https://www.programiz.com/python-programming/examples/prime-number

        Arguments:
            num (int): number to check

        Returns:
            True or False

    """
    # define a flag variable
    flag = False

    # prime numbers are greater than 1
    if num > 1:
        # check for factors
        for i in range(2, num):
            if (num % i) == 0:
                # if factor is found, set flag to True
                flag = True
                # break out of loop
                break

    return not flag

if __name__ == "__main__":
    print(main())