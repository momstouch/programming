def route_exists(from_row, from_column, to_row, to_column, map_matrix):
    mem = [[False] * len(map_matrix[0])] * len(map_matrix)
    def run(fr, fc, tr, tc):
        print(fr, fc)
        if fr < 0 or fc < 0:
            return False
        if fr >= len(map_matrix) or fc >= len(map_matrix[fr]):
            return False
        if not map_matrix[fr][fc] or mem[fr][fc]:
            return False
        if fr == tr and fc == tc:
            return True

        mem[fr][fc] = True

        return run(fr-1,fc,tr,tc) + run(fr+1,fc,tr,tc) +\
                run(fr,fc-1,tr,tc) + run(fr,fc+1,tr,tc)

    return run(from_row, from_column, to_row, to_column)


if __name__ == '__main__':
    map_matrix = [
        [True, False, False],
        [True, True, False],
        [False, True, True]
    ];

    print(route_exists(0, 0, 2, 2, map_matrix))
