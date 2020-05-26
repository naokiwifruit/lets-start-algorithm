def post_test_euclidean_algorithm(a, b):
    """
    :type a: int
    :type b: int
    :rtype a: int
    """
    while True:
        r = a % b
        a = b
        b = r
        if r != 0:
            break
    return a