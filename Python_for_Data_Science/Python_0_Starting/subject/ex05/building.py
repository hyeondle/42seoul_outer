import sys


def text_analyzer(text):
    """
    text analyzer.
    print the count of uppercase, lowercase, punctuation, whitespace and digit

    :param text: text to analyze
    :return: None
    """

    uppercase = sum(1 for char in text if 'A' <= char <= 'Z')
    lowercase = sum(1 for char in text if 'a' <= char <= 'z')
    spaces = text.count(' ')
    punctuation = sum(1 for char in text if char in (
        "!""#$%&'()*+,-./:;<=>?@[\\]^_`{|}~")
    )
    digits = sum(1 for char in text if '0' <= char <= '9')

    print(f"The text contains {len(text)} characters:")
    print(f"{uppercase} upper letters")
    print(f"{lowercase} lower letters")
    print(f"{punctuation} punctuation marks")
    print(f"{spaces} spaces")
    print(f"{digits} digits")


def main():
    args = sys.argv

    if len(args) > 2:
        print("AssertionError: more than one argument is provided")
    elif len(args) == 1:
        print("What is the text to count?")
        text = sys.stdin.readline().replace('\n', ' ')  # carriage return을 space로 간주하기 위해 변경. input은 줄개행을 못받음
        text_analyzer(text)
    else:
        text_analyzer(args[1])


if __name__ == '__main__':
    main()
