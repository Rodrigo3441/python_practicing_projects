def bubble_sort(arr: list) -> tuple[int, int, int, list]:
    """
    This function sorts a list using bubble sort algorithm
    """
    runs = 0
    comparisons = 0
    replacements = 0
    size = len(arr)

    for i in range(size):
        trocou = False

        for j in range(size - 1 - i):
            runs += 1
            comparisons += 1

            if arr[j] > arr[j+1]:
                replacements += 1
                arr[j], arr[j+1] = arr[j+1], arr[j]
                trocou = True

        if not trocou:
            print('array is already sorted')
            break

    return runs, comparisons, replacements, arr