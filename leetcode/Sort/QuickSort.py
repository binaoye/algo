

def RecursiveSort(array, left, right):
    if left < right:
        mid = partion(array, left, right)
        RecursiveSort(array, left, mid - 1)
        RecursiveSort(array, mid + 1, right)
def partion(array, left, right):
    ptr = left - 1
    mat = array[right]
    for i in range(left, right):
        if array[i] < mat:
            ptr = ptr + 1
            array[ptr], array[i] = array[i], array[ptr]
    array[ptr + 1], array[right] = array[right], array[ptr + 1]
    return ptr + 1


def NoneRecursiveSort(array, l, r):
    if l >= r:
        return
    stack = []
    stack.append(l)
    stack.append(r)
    while stack:
        low = stack.pop(0)
        high = stack.pop(0)
        if high - low <= 0:
            continue
        x = array[high]
        i = low - 1
        for j in range(low, high):
            if array[j] <= x:
                i += 1
                array[i], array[j] = array[j], array[i]
        array[i + 1], array[high] = array[high], array[i + 1]
        stack.extend([low, i, i + 2, high])



if __name__ == "__main__":
    arr = [4, 8, 1, 5, 7, 2, 9, 8, 10, 12, 3]
    # RecursiveSort(arr, 0, len(arr) -1)
    NoneRecursiveSort(arr, 0, len(arr) - 1)
    print(arr)
