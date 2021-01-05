def find_two_sum(numbers, target_sum):
    """
    :param numbers: (list of ints) The list of numbers.
    :param target_sum: (int) The required target sum.
    :returns: (a tuple of 2 ints) The indices of the two elements whose sum is equal to target_sum
    """
    dic = {}
    
    for i, n in enumerate(numbers[:-1]):
        dic[target_sum - n] = i

    for j, n in enumerate(numbers[1:], 1):
        try:
            i = dic[n]
            return (i, j)
        except KeyError:
            pass
                
    return None

if __name__ == "__main__":
    assert find_two_sum([3, 1, 5, 7, 5, 9], 10) == (4, 2)
