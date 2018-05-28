def quick_sort(array, l, r):
    if l < r:
        q = partition(array, l, r)
        quick_sort(array, l, q - 1)
        quick_sort(array, q + 1, r)


def partition(array, l, r):
    print("---切分前----")
    print(array)
    x = array[r]
    i = l - 1
    for j in range(l, r):
        if array[j] <= x:
            i += 1
            array[i], array[j] = array[j], array[i]
            print(array)
    array[i + 1], array[r] = array[r], array[i + 1]
    print(array)
    print(print("---切分后----", i + 1))
    return i + 1


if __name__ == "__main__":
    arr = [4,8,1,5,7,2,9,8,10,12,3]
    quick_sort(arr, 0, arr.__len__() - 1)