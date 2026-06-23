def second_largest(arr):
    first_largest = float('-inf')
    second = float('-inf')

    for num in arr:
        if num > first_largest:
            second = first_largest
            first_largest = num
        elif num > second and num != first_largest:
            second = num

    return second


arr = [12, 3, 5, 6, 7]
print(second_largest(arr))