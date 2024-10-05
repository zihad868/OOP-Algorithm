def BinarySearch(arr, left, right, target):
    if left > right:
        return -1

    mid = left + (right - left) // 2

    if arr[mid] == target:
        return  mid

    elif arr[mid] > target:
        return BinarySearch(arr, left, (mid-1), target)
    else:
        return BinarySearch(arr, (mid+1), right, target)


arr = [1, 4, 6, 9, 15, 18];
search = BinarySearch(arr, 0, len(arr)-1, 7)

print("Searh index-->",search)