def bubble_sort(array):
    """
    :type array: List [int]
    :rtype array: List[int]
    """
    length = len(array)
    k = 0
    while k < length - 1:
        i = length - 1
        while i > k:
            if array[i-1] > array[i]:
                array[i-1], array[i] = array[i], array[i-1]
            i -= 1
        k += 1
    return array