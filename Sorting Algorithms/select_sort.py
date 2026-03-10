def select_sort(arr: list) -> tuple[int, int, int, list]:
    """
    This function sorts a list using selection sort algorithm
    """
    runs = 0
    comparisons = 0
    replacements = 0
    size = len(arr)

    for i in range(size):
        lower = i
        for j in range(i+1,size):
            runs += 1
            if arr[j] < arr[lower]:
                comparisons += 1
                lower = j

        if lower != i:
            replacements += 1
            arr[i], arr[lower] = arr[lower], arr[i]

    return runs, comparisons, replacements, arr