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

    tt = 0
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

'''
genrePlays에는 장르별 총 재생수를, genrePlaysMusic에는 key : 장르, value : 넘버링 (list)을, genrePlaysMusicNum에는 key : 장르, value : 재생수 (list)를 저장하였다.

그 후 max 함수를 이용하여 maxgenre에는 genrePlays에서 가장 많은 재생수를 갖는 장르 이름을 저장하였고, maxv에는 genrePlaysMusicNum에서 가장 많은 재생수를 저장하였다. tt는 장르별 최대 2곡만 담기 위한 카운트를 하기 위한 숫자이고. tl은 장르의 종류 수이다.

while문으로 최대 리스트의 길이만큼(장르 종류 * 2곡) 반복하였고, answer list에 genrePlaysMusicNum에서 최대 곡수를 가진 인덱스를 뽑아 genrePlaysMusic에서 넘버링을 매칭시켜 저장하였다. 그 후 다음 최대 곡수를 할당하기 위해 genrePlaysMusicNum에서의 해당 인덱스를 0으로 초기화시켜주었다. answer list에 담을때마다 answerCnt와 장르카운트를 +1 해주었다.

그 후 if문을 통해 answer에 장르별 곡이 2곡 담겼을 때와, 해당 장르에 2곡 이하가 담겨있을 때를 걸러, 장르를 바꿔주었고, 최대 곡수(장르 종류 * 2곡) 만큼 담기기 전에 모든 장르가 담겼다면 while문을 빠져나오게 하였다.
'''