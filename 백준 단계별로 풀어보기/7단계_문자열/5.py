# 1157번 문제

example=input().upper()
str_list=list(set(example))
count_list=[example.count(i) for i in str_list]

if count_list.count(max(count_list))>=2:
    print('?')

elif count_list.count(max(count_list))==1:
    print(str_list[count_list.index(max(count_list))])


#너무 어려웠다..