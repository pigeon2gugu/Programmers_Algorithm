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