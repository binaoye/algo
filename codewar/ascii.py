import math
def alphabet_position(text):
    ans = []
    for w in text:
        m = ord(w) - 65
        print(w, m)
        if (m > 0) and (m < 26):
            ans.append(str((m % 32) + 1))
        if (m > 31) and (m < 58):
            ans.append(str((m % 32) + 1))
    return ' '.join(ans)

def namelist(names):
    #your code here
    l = len(names)
    if l == 0:
        return ''
    if l == 1:
        return names[0]['name']
    if l == 2:
        return names[0]['name'] + ' & ' + names[1]['name']
    lst = [names[i]['name'] for i in range(l - 1)]
    return ', '.join(lst) + ' & ' + names[l - 1]['name']

def sum_dig_pow(a, b): # range(a, b + 1) will be studied by the function
    # your code here
    ans = []
    for i in range(a, b + 1):
        st = str(i)
        tot = 0
        for j in range(len(st)):
            tot += math.pow(int(st[j]), j + 1)
        if tot == i:
            ans.append(i)

    return ans

def decodeMorse(morse_code):
    # ToDo: Accept dots, dashes and spaces, return human-readable message
    lst = morse_code.split('   ')
    ans = []
    for l in lst:
        res = []
        for j in l.split(' '):
            if j in MORSE_CODE.keys() and j != ' ':
                res.append(MORSE_CODE[j])

        ans.append(''.join(res))
    return ' '.join(ans)

def delete_nth(order,max_e):
    d = {}
    ans = []
    for num in order:
        if num in d.keys():
            if d[str(num)] < max_e:
                ans.append(num)
                d[str(num)] = d[str(num)] + 1
        else:
            ans.append(num)
            d[str(num)] = 1
    ans.reverse()
    return ans

def dirReduc(arr):
    i = 0
    nd = {'SOUTH': 'NORTH', 'NORTH': 'SOUTH', 'WEST': 'EAST', 'EAST': 'WEST'}
    while i < len(arr) - 1:
        print(arr)
        if nd[arr[i]] == arr[i + 1]:
            arr.__delitem__(i)
            arr.__delitem__(i)
            i = 0
        else:
            i += 1
    return arr


def title_case(title, minor_words):
    d = {}
    xx = minor_words.split(' ')
    if xx:
        if len(xx) > 0:
            for wd in xx:
                d[wd.lower()] = 1
    ans = []
    tt = title.split(' ')
    if len(tt) == 0:
        return ''
    ans.append(tt[0][0].upper() + tt[0][1:].lower())
    for i in range(1, len(tt)):
        if tt[i].lower() not in d.keys():
            ans.append(tt[i][0].upper() + tt[i][1:].lower())
        else:
            ans.append(tt[i].lower())
    return ans


def find_nb(m):
    # your code
    print(type(m))
    print(m)
    upper = int(math.pow(4 * m, 0.25))
    print('upper', upper)
    print(int(0.25 * int(int(upper * upper) + upper) * int(int(upper * upper) + upper)))
    upper += 2

    for i in range(int(upper)):
        ans = int(0.25 * math.pow(math.pow(upper - i, 2) + upper - i, 2))
        if ans - m == 0:
            return upper - i
    return -1

def sum_pairs(ints, s):
    if ints == []:
        return None
    else:
        y = [s - i for i in ints]
        # x = list(1 for i in ints)
        for c in y:
            if c in ints:
                return [s - c, c]

def validSolution(board=[]):
    if len(board) != 9:
        return False
    for i in range(9):
        if len(board[:][i]) != 9:
            return False
        for j in range(9):
            if not board[:][i].__contains__(j + 1):
                print('ccccc', j + 1, i)
                print(board[:][i].__contains__(j + 1))
                return False
            if not board[i][:].__contains__(j + 1):
                print('ddddd', j + 1, i)
                return False
    for row in range(3):
        for col in range(3):
            x = []
            for i in range(3):
                for j in range(3):
                    x.append(board[3 * row + i][3 * col + j])
            print('row', row, 'col', col, x)
            for z in range(9):
                if not x.__contains__(z + 1):
                    return False
    return True


MORSE_CODE = {'....':'H', '-.--':'Y', '.':"E", '.---': 'J', '..-':'U', '-..':'D'}

if __name__ == "__main__":
    text = "azZAdu"
    # print(alphabet_position(text))
    print(len(str(bin(1234)).replace('0b','').replace('0','')))
    print(namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ]))
    print(sum_dig_pow(1, 100))
    print(decodeMorse('    . '))
    print(delete_nth([20, 37, 21], 1))
    for i in range(0):
        print("dfsafsaf")
    print(dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]))
    # x = [1,2,3,4,5]
    # x.__delitem__(3)
    # print(x)
    print(title_case('THE WIND IN THE WILLOWS', 'The In'))
    print(find_nb(3171324716232249600))
    print(sum_pairs([5, 9, 13, -3], 10))
    # x = [1, 2,3]
    # j = [s - 1 for s in x]
    # print(j)
    print(validSolution([[5, 3, 4, 6, 7, 8, 9, 1, 2],
                         [6, 7, 2, 1, 9, 5, 3, 4, 8],
                         [1, 9, 8, 3, 4, 2, 5, 6, 7],
                         [8, 5, 9, 7, 6, 1, 4, 2, 3],
                         [4, 2, 6, 8, 5, 3, 7, 9, 1],
                         [7, 1, 3, 9, 2, 4, 8, 5, 6],
                         [9, 6, 1, 5, 3, 7, 2, 8, 4],
                         [2, 8, 7, 4, 1, 9, 6, 3, 5],
                         ]))
    print(~True)