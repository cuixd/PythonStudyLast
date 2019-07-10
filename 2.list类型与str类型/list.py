list1 = [1,8,2,5,8,4,5,9,9,5,9]

while 5 in list1:
    list1.remove(5)

print(list1)

list2 = [3,8,6,4,7,7,8]
i = 0
max = 0
sec = 0
while i < len(list2):
    if list2[i] > max:
        sec = max
        max = list2[i]
    elif list2[i] == max:
        pass
    elif list2[i] > sec:
        sec = list2[i]

    i += 1
print(max, sec)

print(list2)