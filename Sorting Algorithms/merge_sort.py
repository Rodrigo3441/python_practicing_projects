numbers = [3,2,56,7,5,3,6,8,9,90,11,2,12,414,51,31,5,63,3,67,4,43,467,4,54,45,645,6]

counter = 0

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        global counter
        counter += 1
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    print(result)
    return result


def select_sort(arr):
    size = len(arr)
    for i in range(size-1):
        lower = i
        for j in range(i+1,size):
            global counter
            counter += 1
            if arr[j] < arr[lower]:
                lower = j
        if lower != i:
            arr[i], arr[lower] = arr[lower], arr[i]

    return arr

print(merge_sort(numbers))
print(counter)
