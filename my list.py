mylist = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
index = 0
while index < len(mylist):
    if mylist[index] < 0:
        break
    if mylist[index] > 0:
        print(mylist[index])
    index += 1


