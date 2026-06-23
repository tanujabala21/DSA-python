def largest_element(arr):
    largest=arr[0]
    for i in range(len(arr)):
        if arr[i]>largest:
            largest=arr[i]
    return largest
# example
arr=[1,2,3,4,5,6,7]
print(largest_element(arr))