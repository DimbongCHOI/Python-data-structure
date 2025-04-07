# ver1.2 - Array
list1 = [3, 5, 10, 21]
list2 = [4, 6, 15, 26, 33]
list3 = []

i, j = 0, 0

# 두 리스트를 순차적으로 비교하며 병합
while(i < len(list1) and j < len(list2)):
    if(list1[i] < list2[j]):
        list3.append(list1[i])
        i += 1
    else:
        list3.append(list2[j])
        j += 1

# 남은 요소들 처리
while(i < len(list1)):
    list3.append(list1[i])
    i += 1
while(j < len(list2)):
    list3.append(list2[j])
    j += 1

print("Input:")
print("list1:", end =" ")
for i in range(len(list1)):
    print(list1[i], end = ' -> ')
print("끝")
print("list2:", end =" ")
for i in range(len(list2)):
    print(list2[i], end = ' -> ')
print("끝")

print("Output:")
for i in range(len(list3)):
    print(list3[i], end = ' -> ')
print("끝")
