def test():
    ary = []
    while True:
        n = int(input())
        if not n:
            return ary
        else:
            ary.append(n)


if __name__ == "__main__":
    print(test())
