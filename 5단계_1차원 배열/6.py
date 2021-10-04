#8958번 문제
#입력: O와 X로 이루어진 문자열
#출력: 점수
#O가 단독으로 있으면 1점
#O가 연속되게 있으면 연속된 만큼의 점수

N=int(input())
for i in range(N):
    case=input()
    score=0
    sum_=0
    for k in case:
        if k=='O':
            score+=1
            sum_+=score
        if k=='X':
            score=0
    print(sum_)