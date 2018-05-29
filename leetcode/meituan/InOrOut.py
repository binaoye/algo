import sys


def calc(scores, weights, n, m, k):
    weighted_scores = {i: 0.0 for i in range(n)}
    inout = [2 for i in range(n)]
    if k >= n:
        for s in range(n):
            inout[s] = 1
        return inout
    sum_weight = 0
    if len(weights) == m:
        sum_weight = sum(weights)
    else:
        for i in range(m):
            sum_weight += weights[i]
    for i in range(m):
        weight = weights[i] / sum_weight
        lst = []
        # print(scores[j])
        for j in range(n):
            lst.append(scores[j][i])
        max_score = max(lst)
        if max_score > 0:
            for x in range(n):
                weighted_scores[x] += weight * lst[x] / max_score
    ranked_result = sorted(weighted_scores.items(), key=lambda d: d[1], reverse=True)
    # 先配置前k个为出线
    for s in range(k):
        index = ranked_result[s][0]
        inout[index] = 1

    if k < n:
        threshold_score = ranked_result[k - 1][1]
        first_out_score = ranked_result[k][1]
        if threshold_score == first_out_score:
            for sh in range(n):
                if ranked_result[sh][1] == threshold_score:
                    inout[ranked_result[sh][0]] = 3
    return inout


if __name__ == "__main__":
    n, m, k, C = map(int, sys.stdin.readline().strip().split())
    weights = list(map(int, sys.stdin.readline().strip().split()))
    scores = []
    for i in range(n):
        scores.append(list(map(int, sys.stdin.readline().strip().split())))
    miss_index_x = 0
    miss_index_y = 0
    for l in range(n):
        lst = scores[l]
        for j in range(m):
            if lst[j] == -1:
                miss_index_x = l
                miss_index_y = j
    cs = []
    all_rank = []
    for x in range(C + 1):
        scores[miss_index_x][miss_index_y] = x
        answer = calc(scores, weights, n, m, k)
        all_rank.append(answer)
    final_rank = [3 for s in range(n)]
    for s in range(n):
        ranks = []
        for h in range(C + 1):
            ranks.append(all_rank[h][s])
        max_rank = max(ranks)
        min_rank = min(ranks)
        if max_rank == min_rank:
            if max_rank == 1:
                final_rank[s] = 1
            elif max_rank == 2:
                final_rank[s] = 2
    for s in final_rank:
        print(s)


