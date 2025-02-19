def ft_filter(function, iterable):
    """
    ft_filter(function, iterable) -> filter object

    Return an iterator yielding those items of iterable for which function(x)
    is true. If function is None, return the items that are true.
    """
    if function is None:
        return [x for x in iterable if x]
    return [x for x in iterable if function(x)]


def main():
    return


if __name__ == '__main__':
    main()

'''
list comprehension이란?
리스트를 쉽게, 짧게 한 줄로 만들 수 있는 파이썬의 문법
[ ( 변수를 활용한 값 ) for ( 사용할 변수 이름 ) in ( 순회할 수 있는 값 )]
'''
