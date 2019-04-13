cube = lambda x: x ** 3


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
