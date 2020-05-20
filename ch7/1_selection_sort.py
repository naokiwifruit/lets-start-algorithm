def selection_sort(array):
    """
    :type array: List [int]
    :rtype array: List[int]
    """
    length = len(array)
    i = 0
    while i < length - 1:
        indexMin = i
        k = i + 1
        while k < length:
            if array[k] < array[indexMin]:
                indexMin = k
            k += 1
        array[i], array[indexMin] = array[indexMin], array[i]
        i += 1
    return array