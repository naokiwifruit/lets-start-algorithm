def pre_test_euclidean_algorithm(a, b):
    """
    :type a: int
    :type b: int
    :rtype b: int
    """
    r = a % b
    while r != 0:
        a = b
        b = r
        r = a % b
    return b