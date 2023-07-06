# Coded triangle numbers

"""
Problem 42

    The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1);
    so the first ten triangle numbers are:

        1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

    By converting each letter in a word to a number corresponding to its
    alphabetical position and adding these values we form a word value.
    For example, the word value for SKY is 19 + 11 + 25 = 55 = t10.
    If the word value is a triangle number then we shall call the word
    a triangle word.

    Using words.txt (right click and 'Save Link/Target As...'), a 16K text file
    containing nearly two-thousand common English words, how many are triangle
    words?

"""

from utils.math_functions import triangle as tri

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def get_word_value(word):
    word_value = 0
    for char in word:
        word_value += ALPHABET.index(char) + 1
    return word_value


def triange_list(limit):
    tri_lst = []
    i = 1
    while True:
        t = tri(i)
        tri_lst.append(t)
        if t > limit:
            break
        i += 1
    return tri_lst


def word_value_dict(lst):
    dic = {}
    for word in lst:
        dic[word] = get_word_value(word)
    return dic


def main():
    with open("p042_words.txt") as f:
        word_list = [x.replace('"', "") for x in f.read().split(",")]

    word_dict = word_value_dict(word_list)
    limit = max(word_dict.values())
    tri_lst = triange_list(limit)

    i = 0
    for v in word_dict.values():
        if v in tri_lst:
            i += 1

    print(i, "words are triangle words.")


if __name__ == "__main__":
    main()
