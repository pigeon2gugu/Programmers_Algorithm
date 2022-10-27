#https://www.acmicpc.net/problem/2164
#난이도 하 2

#일반 list queue방법으로 하면 runtime error 발생.
from collections import deque

dq = deque([i+1 for i in range(int(input()))])

while len(dq) > 1 :
    dq.popleft()
    temp = dq.popleft()
    dq.append(temp)

print(dq[0])