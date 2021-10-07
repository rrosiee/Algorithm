# 5622번 문제
# 입력: 대문자 알파벳으로 구성된 문자열(길이는 2~15)
# 출력: 전화를 걸기 위해서 걸리는 최소 시간
#걸리는시간 3   4   5   6   7   8    9   10
#다이얼번호 2   3   4   5   6   7    8   9
alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphabet_sec=[3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 10, 10, 10, 10]
dial_input=input()
sum_=0
for i in dial_input:
    sum_+=alphabet_sec[alphabet.find(i)]

print(sum_)
