
def genOdd(count):
    for i in range(count):
        if i == 0:
            yield 0
        elif i % 2 == 0:
            yield i
        else:
            genOdd(count - 1)



if __name__ == "__main__":
    x = genOdd(5)
    print(list(x))
