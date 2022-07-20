#1110번 문제 short coding
#특히 2자리수의 문제에서는 나머지연산자를 잘 활용하면 된다는 것을 알 수 있다.
#숫자를 활용할 때에는 되도록 문자열보다 숫자의 특성을 활용하는 것이 좋다.

a=int(input())
b=a
i=0

while True:
    a=int(str(a%10)+str(((a//10)+(a%10))%10))
    i+=1
    if a==b:
        break

print(i)