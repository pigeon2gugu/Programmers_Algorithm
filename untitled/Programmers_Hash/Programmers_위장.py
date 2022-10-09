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

'''
defaultdict(list)를 이용하면 리스트형태로 value를 추가할 수 있다. clothes list에서 1번째 원소는 옷의 분류를 의미하므로, dictionary에 key값으로 이용하였고, 거기에 value로 그 분류에 속하는 옷들을 집어 넣었다.

그 후, dictionary에서 키 값 별로 value list 길이를 lengthDic list에 저장하였고, lengthDic list의 길이로 반복문을 돌면서 경우의 수를 각각 곱해주었다. 이때의 경우의 수들은 옷 분류의 옷 가짓수 + 1을 해주었는데, 이 이유는 그 옷 분류를 안입는 경우도 있기 때문이다. 

그 후 답에서 -1을 해주었는데, 이는 모두 안입는 경우를 제외한 것이다.
'''