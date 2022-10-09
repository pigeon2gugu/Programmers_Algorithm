def solution(id_list, report, k):

    aArr = {x : 0 for x in id_list}
    reports = {x : 0 for x in id_list}

    for r in set(report) :
        reports[r.split()[1]] += 1


    for i in set(report) :
        if reports[i.split()[1]] >= k :
            aArr[i.split()[0]] += 1

    answer = list(aArr.values())

    return answer

'''
aArr : key 값으로 id_list를 하였고, 추후 신고한 사람이 정지당하면 메일 받는 회수를 value로 담을 dictionay

reports : key 값으로 id_list를 하였고, 추후 신고 당한 횟수가 value로 담을 dictionary

한 사람이 다른 사람을 여러번 신고 할 수 있으니 report를 set을 통해 중복 신고를 제거하였다. 그 후 report에서 스페이스로 구분된 뒤의 이름(신고당한자)을 key값으로 가지는 reports에 신고 당한 횟수를 +1 로 하였다.

그 후, 또 set한 report에서 스페이스로 구분된 뒤의 이름(신고당한자)을 key값으로 가지는 reports에서 k횟수를 넘은 자는 정지를 당하니, 이를 if문으로 판별하였고, 이것이 true이면 신고자는 메일 받는 횟수를 +1하도록 구현하였다.
'''