# LIST INDEX OUT OF RANGE...does this require a while loop instead?
# List index is *still* out of range if you use arr[0] as the pivot...
# What would a helper function be? Where would it fit?
# Can you in fact do TWO instances of recursion inside a function?

def quick_sort(arr):
    if len(arr) == 1:
        return arr
    pivot = arr[0]
    left = []
    right = []
    result = []
    for i in range((len(arr))):
        if arr[i] < pivot:
            left.append(arr[i])
        elif arr[i] > pivot:
            right.append(arr[i])
        else:
            result.append(arr[i])
    quick_sort(left)
    quick_sort(right)
    # print(b)
    return result

print(quick_sort([0,5,7,2,5,8,9]))
