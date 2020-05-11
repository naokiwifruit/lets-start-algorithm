def selection_sort(array):
    """
    :type array: List [int]
    :rtype array: List[int]
    """
    i = 0
    while i < len(array) - 1:
        indexMin = i
        k = i + 1
        while k < len(array):
            if array[k] < array[indexMin]:
                indexMin = k
            else:
                k += 1
        w = array[i]
        array[i] = array[indexMin]
        array[indexMin] = w
        
        i += 1
    return array