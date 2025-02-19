import sys


def translator(S):
    """
    Translates a string to Morse code.
    Uses International Morse code.
    """
    NESTED_MORSE = {
        " ": "/ ",
        "A": ".- ",
        "B": "-... ",
        "C": "-.-. ",
        "D": "-.. ",
        "E": ". ",
        "F": "..-. ",
        "G": "--. ",
        "H": ".... ",
        "I": ".. ",
        "J": ".--- ",
        "K": "-.- ",
        "L": ".-.. ",
        "M": "-- ",
        "N": "-. ",
        "O": "--- ",
        "P": ".--. ",
        "Q": "--.- ",
        "R": ".-. ",
        "S": "... ",
        "T": "- ",
        "U": "..- ",
        "V": "...- ",
        "W": ".-- ",
        "X": "-..- ",
        "Y": "-.-- ",
        "Z": "--.. ",
        "1": ".---- ",
        "2": "..--- ",
        "3": "...-- ",
        "4": "....- ",
        "5": "..... ",
        "6": "-.... ",
        "7": "--... ",
        "8": "---.. ",
        "9": "----. ",
        "0": "----- ",
    }

    return "".join(NESTED_MORSE[c] for c in S.upper())


def main():
    args = sys.argv[1:]

    try:
        if len(args) != 1:
            raise AssertionError("AssertionError: the arguments are bad")

        S = args[0]

        if any(not c.isalnum() and not c.isspace() for c in S):
            raise AssertionError("AssertionError: the arguments are bad")

        print(translator(S).rstrip())

    except AssertionError as e:
        print(e)


if __name__ == '__main__':
    main()
