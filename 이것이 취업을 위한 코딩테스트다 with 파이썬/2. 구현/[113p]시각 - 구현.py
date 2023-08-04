# 이코테 113쪽
'''구현 실전 문제
시각
🐾 문제 설명
정수 N이 입력되면 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램을 작성하시오.

🐾 입출력 예시
입력
5
출력
11475'''


def mine():
    N = int(input())
    result = 0
    temp = 0

    for i in range(60):
        for k in range(len(str(i))):
            if str(i)[k] == '3':
                result += 1
                break

    for i in range(N + 1):
        for k in range(len(str(i))):
            if str(i)[k] == '3':
                temp += 1
                break

    result = (N - temp + 1) * ((result * 60) + (result * (60 - result))) + temp * 60 * 60

    print(result)


def book():
    h = int(input())
    count = 0
    for i in range(h + 1):
        for j in range(60):
            for k in range(60):
                if '3' in str(i) + str(j) + str(k):
                    count += 1
    print(count)

mine()
book()