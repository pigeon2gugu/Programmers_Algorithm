from collections import defaultdict

def solution(genres, plays):
    answer = []
    answerCnt = 0

    genrePlays = {x : 0 for x in (genres)}
    genrePlaysMusic = defaultdict(list)
    genrePlaysMusicNum = defaultdict(list)

    for i in range(len(genres)) :
        genrePlays[genres[i]] += plays[i]
        genrePlaysMusic[genres[i]].append(i)
        genrePlaysMusicNum[genres[i]].append(plays[i])

    maxgenre = max(genrePlays,key=genrePlays.get)
    maxv = max(genrePlaysMusicNum[maxgenre])

    tt = 0
    tlc = 0
    tl = len(genrePlays)

    while(answerCnt < tl*2):
        maxgenre = max(genrePlays,key=genrePlays.get)
        maxv = max(genrePlaysMusicNum[maxgenre])
        answer.append(genrePlaysMusic[maxgenre][genrePlaysMusicNum[maxgenre].index(maxv)])
        genrePlaysMusicNum[maxgenre][genrePlaysMusicNum[maxgenre].index(maxv)] = 0
        answerCnt += 1
        tt+= 1

        if tt==2 or max(genrePlaysMusicNum[maxgenre]) == 0 :
            genrePlays[maxgenre] = 0
            tt = 0
            if max(genrePlays.values())== 0 :
                break;

    return answer