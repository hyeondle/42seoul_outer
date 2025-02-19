import sys
from ft_filter import ft_filter


def filterstring(S, N):
    """
    Returns a list of words in S that have a length greater than N.
    """
    # if special characters exist, error
    # if any(not c.isalnum() and not c.isspace() for c in S):
    #     raise AssertionError("AssertionError: special characters")

    return [word for word in ft_filter(lambda word: len(word) > N, S.split())]


def main():
    args = sys.argv[1:]

    try:
        if len(args) != 2:
            raise AssertionError("AssertionError: the arguments are bad")

        S, N = args[0], args[1]

        if not isinstance(S, str) or not N.isdigit():
            raise AssertionError("AssertionError: the arguments are bad")

        N = int(N)

        print(filterstring(S, N))

    except AssertionError as e:
        print(e)


if __name__ == '__main__':
    main()
