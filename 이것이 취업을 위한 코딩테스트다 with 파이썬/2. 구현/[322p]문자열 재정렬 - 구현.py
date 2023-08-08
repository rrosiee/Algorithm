s = input()
array_s = [i for i in s]
alphabet = list()
number = 0
for element in array_s:
    if element.isalpha():
        alphabet.append(element)
    else:  # 숫자
        number += int(element)


result = "".join(sorted(alphabet)) + str(number)
print(result)