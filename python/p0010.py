from utils import math_functions as mf

def main():
    sum_ = 0
    for x in range(2000000):
        if mf.is_prime(x):
            sum_ += x

    print(sum_)

if __name__ == "__main__":
    main()