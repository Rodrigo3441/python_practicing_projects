# Filename: quick_sort.py
# Author: Rodrigo SG
# Last Modification: March 17th 2026

class Stats:
    def __init__(self):
        self.replacements = 0
        self.runs = 0
        self.comparisons = 0

stats = Stats()

def quick_sort(arr: list, start_idx: int, end_idx: int) -> list:
    """
        args:
        arr -> the array that will be sorted
        start_idx -> the first index position of the array
        end_idx -> the last index position of the array

        This function will sort an array using quick sort algorithm
    """
    middle_value = arr[(start_idx+end_idx)//2]
    i = start_idx
    j = end_idx

    # enquanto o ponteiro da direita for menor que o da esquerda, continue
    while i <= j:
        # enquanto o valor de inince i for menor que o central, avance um para i
        while arr[i] < middle_value:
            i += 1
            stats.runs += 1

        # enquanto o valor de indice j for maior que o central, diminua um para j
        while arr[j] > middle_value:
            j -= 1
            stats.runs += 1

        # no nomento que os ponteiros se encontrarem, troque
        if i <= j:
            stats.comparisons += 1
            stats.replacements += 1
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1

    # se o indice inicial for menor que o indice j (final daquele segmento do array), chame a recursao
    if start_idx < j:
        stats.comparisons += 1
        quick_sort(arr, start_idx, j)

    # se o indice i (inicio do segmento a direita do array) for menor que o inicide final daquele segmento do array, chame a recursao 
    if i < end_idx:
        stats.comparisons += 1
        quick_sort(arr, i, end_idx)

    return arr


def call_quick_sort(arr: list) -> list:
    """
        This function will return the array sorted using quick sort together some stats about the running
    """
    ordered_array = quick_sort(arr,0,len(arr)-1)
    return (stats.runs, stats.comparisons, stats.replacements, ordered_array)