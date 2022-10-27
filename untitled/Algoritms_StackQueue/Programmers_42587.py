#https://school.programmers.co.kr/learn/courses/30/lessons/42587#
#난이도 하 1

def solution(priorities, location):
    answer = 0
    que = []

    for i in range(len(priorities)) :
        que.append((priorities[i], i)) #우선순위는 0번째 index, 위치는 1번째 index

    while True :
        if len(que) == 1 : #maxP 오류 해결을 위한 조건문.
            answer +=1
            break
        temp = que.pop(0)
        maxP = max(que)[0]
        if temp[0] < maxP :
            que.append(temp)
        else :
            answer += 1
            if temp[1] == location :
                break

    return answer