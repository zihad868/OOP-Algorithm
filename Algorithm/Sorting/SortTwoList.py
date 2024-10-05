def mergeSort(list1, list2):
    sort = []
    i, j = 0, 0

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            sort.append(list1[i])
            i += 1
        else:
            sort.append(list2[j])
            j += 1

    while i < len(list1):
        sort.append(list1[i])
        i += 1

    while j < len(list2):
        sort.append(list2[j])
        j += 1

    return sort


s = mergeSort([5, 8, 12, 15], [2, 7, 10])
print(s)
