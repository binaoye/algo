def chess(tr, tc, pr, pc, size):# 传入左上角的坐标，特殊点坐标，以及size
    global mark
    global table
    mark += 1
    count = mark
    if size == 1:
        return
    half = size // 2
    # 确认特殊点位置以及子问题大小，并解决另外三个子问题
    if pr < tr + half and pc < tc + half:
        chess(tr, tc, pr, pc, half)
    else:
        table[tr + half - 1][tc + half - 1] = count
        chess(tr, tc, tr + half - 1, tc + half - 1, half)
    if pr < tr + half and pc >= tc + half:
        chess(tr, tc + half, pr, pc, half)
    else:
        table[tr + half - 1][tc + half] = count
        chess(tr, tc + half, tr + half - 1, tc + half, half)
    if pr >= tr + half and pc < tc + half:
        chess(tr + half, tc, pr, pc, half)
    else:
        table[tr + half][tc + half - 1] = count
        chess(tr + half, tc, tr + half, tc + half - 1, half)
    if pr >= tr + half and pc >= tc + half:
        chess(tr + half, tc + half, pr, pc, half)
    else:
        table[tr + half][tc + half] = count
        chess(tr + half, tc + half, tr + half, tc + half, half)


def show(table):
    n = len(table)
    for i in range(n):
        for j in range(n):
            print(table[i][j], end='\t')
        print('')


if __name__ == "__main__":
    mark = 0
    n = 8
    table = [["*" for x in range(n)] for y in range(n)]
    show(table)
    chess(0, 0, 4, 2, n)
    show(table)