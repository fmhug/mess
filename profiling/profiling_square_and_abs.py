

def square(x):
    return x ** 2


def abs_foo(x):
    return abs(x)


n = 1_000_000


def foo(func):
    for i in range(n):
        v = func(i) > func(i + 1)


if __name__ == '__main__':
    import profile

    profile.run('foo(square)')
    profile.run('foo(abs_foo)')
