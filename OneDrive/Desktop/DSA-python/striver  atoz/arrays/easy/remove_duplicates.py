def remove_duplicates(arr):
    left=0
    for right in range(len(arr)):
        if arr[right]!=arr[left]:
            left+=1
            arr[left]=arr[right]
    return arr[:left+1]

arr=[1,1,2,3,3,4,4,5]
print(remove_duplicates(arr))