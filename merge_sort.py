# Can recursive functions have TWO recursions within them?
# How do you handle the output when it's returning BOTH parts of the array that you've just split up?

def split(arr):
    length = len(arr)
    newarr = []
    if length % 2:
        n = length // 2 - 1
    else:
        n = (length + 1) // 2
    if n == 1:
        return arr
    else:
        # split(arr[0:n])
        # split(arr[n:])


def merge_sort(arr):
    length = len(arr)
    if length == 1:
        return arr
    else:
        new = split(arr)
    return new

def sort_stage(arr):
    result = []
    if len(arr) == 1:
        result.append(arr[0])
    else:
        return arr


divide = split([4, 6, 4, 6, 7, 3])
# print(merge_sort(divide))
