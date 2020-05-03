def linear_search(array):
    """
    :type array: List[int]
    :rtype: str
    """
    i = 0
    while i < 5:
        if array[i] == 5:
            return '{}番目の要素が一致'.format(i)
        else:
            i += 1
    else:
        return '見つかりませんでした'