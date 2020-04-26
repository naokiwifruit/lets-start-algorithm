def compare_two_data(a, b):
    """
    :type a: float
    :type b: float
    :rtype: float or str
    """
    if a > b:
        return a
    else:
        if a == b:
            print('aとbは等しい')
        else:
            print(b)