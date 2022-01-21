# Passcode derivation

"""
Problem 79
    A common security method used for online banking is to ask the user for
    three random characters from a passcode. For example, if the passcode was
    531278, they may ask for the 2nd, 3rd, and 5th characters; the expected
    reply would be: 317.

    The text file, keylog.txt, contains fifty successful login attempts.

    Given that the three characters are always asked for in order, analyse the
    file so as to determine the shortest possible secret passcode of unknown
    length.
    """

import itertools

DIGITS = "1234567890"

with open("p079_keylog.txt") as f:
    keylog = f.read().split("\n")

nkeys = len(keylog)

i = 3
while True:
    passcodes = list(itertools.product(DIGITS, repeat=i))

    for passcode_tpl in passcodes:
        passcode = ""
        for digit in passcode_tpl:
            passcode += digit

        passed = 0
        for key in keylog:
            idx = []
            for d in key:
                if d in passcode:
                    idx.append(passcode.index(d))

            if len(idx) == 3 and idx == sorted(idx):
                passed += 1

        print(f"Iteration: {i}, Passcode: {passcode}, Passed: {passed}")
        if passed == 20:
            break
    else:
        i += 1
        continue
    break

    # print(passcodes)
