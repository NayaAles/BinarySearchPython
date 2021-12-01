def binary_search(numbers: [], find):

    min = 0
    max = len(numbers) - 1

    while min <= max:
        mid = int((min + max)/2)
        if find == numbers[mid]:
            return mid
        elif find > numbers[mid]:
            min = mid + 1
        elif find < numbers[mid]:
            max = mid -1

    return -1;


a = [1, 2, 3, 4, 5, 6, 7, 8]
r = binary_search(a, 5)
print(r)


a = [-8, -7, -6, -5, -4, -3, -2, -1]
r = binary_search(a, -5)
print(r)


a = [5, 10, 7, 4, 9, 8, 2, 1, 3, 6]
a.sort()
r = binary_search(a, 5)
print(r)