def insertion_sort(array):
    """
    :type array: List [int]
    :rtype array: List[int]
    """
    length = len(array)
    i = 1
    while i < length:
        x = array[i]
        k = i
        while k > 0 and array[k-1] > x:
            array[k] = array[k-1]
            k -= 1
        array[k] = x
        i += 1
    return array