def search_max_value(array):
    """
    :type array: List[int]
    :rtype: float
    """
    max_value = array[0]
    length = len(array)
    i = 1
    while i < 5:
        if array[i] > max:
            max_value = array[i]
        i += 1
    else:
        return max_value