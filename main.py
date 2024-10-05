def SumTwoNumbers(arr, target):
    pair = []
    for i in range(len(arr) - 1):
        for j in range(i+1, len(arr)):
            sum = arr[i] + arr[j]
            if sum == target:
                pair.append([arr[i], arr[j]])
    return pair


result = SumTwoNumbers([1, 4, 7, 10, 3, 5, 8, 2], 10)

print(result)