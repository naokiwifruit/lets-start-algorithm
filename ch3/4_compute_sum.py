def compute_sum(array):
    """
    :type array: List[int]
    :rtype: float
    """
    sum = 0
    i = 0
    while i < 5:
        sum += array[i]
        i += 1
    else:
        return sum