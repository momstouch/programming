def count_numbers(sorted_list, less_than):
    if not sorted_list:
        return 0

    cent = len(sorted_list) // 2
    if sorted_list[cent] < less_than:
        return cent + 1 + count_numbers(sorted_list[cent + 1:], less_than)
    else:
        return count_numbers(sorted_list[:cent], less_than)


def count_numbers2(sorted_list, less_than):
    ans = 0
    while sorted_list:
        cent = len(sorted_list) // 2
        if sorted_list[cent] < less_than:
            ans += cent + 1
            sorted_list = sorted_list[cent + 1:]
        else:
            sorted_list = sorted_list[:cent]

    return ans


# only count_numbers3() have passed performance test
def count_numbers3(sorted_list, less_than):
    beg = 0
    end = len(sorted_list)

    while beg + 1 <= end:
        cent = (end + beg) // 2

        if sorted_list[cent] < less_than:
            beg = cent + 1
        else:
            end = cent

    return beg 


if __name__ == "__main__":
    sorted_list = [1, 3, 5, 7]
    assert count_numbers3(sorted_list, 4) == 2
