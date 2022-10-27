#https://www.acmicpc.net/problem/1874
#난이도 하 3

num = [int(input()) for i in range(int(input()))]
tempSt = []
ppST = [] #push('+') 또는 pop('-') operator
yn = 1

cc = 1

for i in range(len(num)) :
    while cc <= num[i] : #임시 list에  원하는 값이 올때까지 push해준다.
        tempSt.append(cc)
        cc += 1
        ppST.append('+')

    if tempSt[-1] == num[i] : #원하는 값이 맨 끝에 있으면 pop한다
        tempSt.pop()
        ppST.append('-')

    else : #원하는 값이 없으면 0을 표시해준다. 후에 No출력을 위한 인자.
        yn = 0
        break;

if yn == 0 :
    print("NO")
else :
    for i in range(len(ppST)) :
        print(ppST[i])