


def function():
    a = 10
    b = 1
    num = 0
    for i in range(1, 10):
        num = num + (b + i * a)
    return num


if __name__ == '__main__':
    r = function()
    print(r)
