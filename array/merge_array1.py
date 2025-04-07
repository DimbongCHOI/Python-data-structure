# ver1.1 - Array : bubble sort -> O(n^2)..  기준 부적격
list1 = [3, 5, 10, 21]
list2 = [4, 6, 15, 26, 33]
list3 = list1 + list2

for i in range(len(list3)): # -> O(n^2)..  기준 부적격
    for j in range(len(list3) - i - 1):
        if(list3[j] > list3[j + 1]):
            tmp = list3[j]
            list3[j] = list3[j + 1]
            list3[j + 1] = tmp

print("Input:")

print("list1:", end =" ")
for i in range(len(list1)):
    print(list1[i], end = ' -> ')
print("끝")

print("list2:", end =" ")
for i in range(len(list2)):
    print(list2[i], end = ' -> ')
print("끝")

# 최종 출력
print("Output:")

for i in range(len(list3)):
    print(list3[i], end = ' -> ')
print("끝")
