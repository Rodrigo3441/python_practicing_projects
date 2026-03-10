def insertion_sort_old(arr: list) -> tuple[int, int, int, list]:
    """
    This function sorts a list using insertion sort algorithm
    """
    runs = 0
    comparisons = 0
    replacements = 0
    size = len(arr)
    
    for i in range(1,size):
        key = arr[i]
        j = i-1

        runs += 1

        while j >= 0 and arr[j] > key:
            replacements += 1
            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = key

    return runs, comparisons, replacements, arr



def insertion_sort_new(arr: list) -> tuple[int, int, int, list]:
    """
    This function sorts a list using insertion sort algorithm
    """
    runs = 0
    comparisons = 0
    replacements = 0
    size = len(arr)
    
    for i in range(1, size):
        proximo = i
        runs += 1
        while proximo > 0 and arr[proximo] < arr[proximo - 1]:
            replacements += 1
            arr[proximo], arr[proximo - 1] = arr[proximo - 1], arr[proximo]
            proximo -= 1


    return runs, comparisons, replacements, arr