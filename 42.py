def arraySortedOrNot(arr, n):
    if (n == 0 or n == 1):
        return True
    for i in range(1, n):
        if (arr[i - 1] > arr[i]):
            return False
    return True
dd=int(input())
arr = list(map(str,(input().split())))
n = len(arr)
if (arraySortedOrNot(arr, n)):
    print("Yes")
else:
    print("No")
