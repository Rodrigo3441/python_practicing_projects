numbers = [17, 3, 29, 8, 14, 1, 25, 11, 30, 6, 19, 4, 27, 13, 2, 21, 9, 24, 7, 16, 28, 5, 22, 10, 18, 26, 12, 20, 15, 23]


def select_sort(arr):
    runs = 0
    comparisons = 0
    replacements = 0
    size = len(arr)

    for i in range(size):
        lower = i
        j = i+1
        for j in range(i+1,size):
            runs += 1
            if arr[j] < arr[lower]:
                comparisons += 1
                lower = j

        if lower != i:
            replacements += 1
            arr[i], arr[lower] = arr[lower], arr[i]

    return runs, comparisons, replacements, arr



            

def insertion_sort(arr):
    runs = 0
    replacements = 0
    comparisons = 0
    size = len(arr)


    for i in range(1, size):
        key = arr[i]
        j = i-1

        while j >= 0 and arr[j] > key:
            runs += 1
            arr[j+1] = arr[j]
            j -= 1
        
        arr[j+1] = key
        replacements += 1

    return runs, comparisons, replacements, arr
def bubble_sort(arr):
    pass


# runs, comparisons, replacements, arr = select_sort(numbers)
runs, comparisons, replacements, arr = insertion_sort(numbers)


print(f'Executions Number: {runs}')
print(f'Comparisons Number: {comparisons}')
print(f'Replacementes: {replacements}')
print(f'Array Organized: {arr}')