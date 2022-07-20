#2941번 문제

croa=['c=','c-', 'dz=', 'd-','nj', 'lj', 's=', 'z=']
example=input()
sum_=0

for i in croa:
    sum_+=example.count(i)
    example=example.replace(i, '_')
example=example.replace('_', '')
example=example.replace('-', '')
example=example.replace('=', '')
sum_+=len(example)
print(sum_)