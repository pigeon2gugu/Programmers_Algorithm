from collections import defaultdict

def solution(clothes):
    answer = 1
    dic = defaultdict(list)

    for c in clothes:
        dic[c[1]].append(c[0])

    lengthDic = [len(v) for v in dic.values()]

    for i in range(len(lengthDic)) :
        answer = answer * (lengthDic[i] + 1)

    answer -= 1

    return answer