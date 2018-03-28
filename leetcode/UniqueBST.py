
def calc(num):
    if num <=1:
        return 1
    else:
        sum = 0
        for i in range(num+1):
            if i >0:
                sum = sum + calc(i -1) * calc(num - i)
        return sum




if __name__ == "__main__":
    num = int(input("input a number:"))
    print("start calculating")
    print("result:",calc(num))

