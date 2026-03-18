# Filename: merge_sort.py
# Author: Rodrigo SG
# Last Modification: March 17th 2026


class Stats:
    def __init__(self):
        self.comparisons = 0
        self.runs = 0
        self.replacements = 0

stats = Stats()


def separate_elements(arr: list) -> list:
    """
        This function will separate all elements of an array until 
        every element becomes one single element
    """
    stats.comparisons += 1
    if len(arr) <= 1:
        return arr
    
    mid = len(arr)//2
    left = separate_elements(arr[:mid])
    right = separate_elements(arr[mid:])

    return merge_elements(left, right)


def merge_elements(left: list, right: list) -> list:
    """
        This functions will put the values together while they are being compared
        in order to find the lowest one and sort them
    """

    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        stats.runs += 1
        stats.comparisons += 1
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])    
    return result

def merge_sort(arr: list) -> tuple[int,int,int,list]:
    """
        This function will return the array sorted using merge sort together some stats about the running
    """
    result = separate_elements(arr)
    return (stats.runs, stats.comparisons, stats.replacements, result)
