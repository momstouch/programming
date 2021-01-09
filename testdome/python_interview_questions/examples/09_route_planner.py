def route_exists(from_row, from_column, to_row, to_column, map_matrix):
    mem = map_matrix.copy()

    def run(fr, fc, tr, tc):
        if fr == tr and fc == tc:
            return True

        mem[fr][fc] = False

        ret = False
        if fr-1 >= 0 and mem[fr-1][fc] and map_matrix[fr-1][fc]:
            ret += run(fr-1, fc, tr, tc)
        if fc-1 >= 0 and mem[fr][fc-1] and map_matrix[fr][fc-1] and not ret:
            ret += run(fr, fc-1, tr, tc)
        if fr+1 < len(map_matrix) and mem[fr+1][fc] and \
                map_matrix[fr+1][fc] and not ret:
            ret += run(fr+1, fc, tr, tc)
        if fc+1 < len(map_matrix[fr]) and mem[fr][fc+1] and \
                map_matrix[fr][fc+1] and not ret:
            ret += run(fr, fc+1, tr, tc)

        mem[fr][fc] = True

        return True if ret != 0 else False

    return run(from_row, from_column, to_row, to_column)


if __name__ == '__main__':
    map_matrix = [
        [True, False, False],
        [True, True, False],
        [False, True, True]
    ];

    assert route_exists(0, 0, 2, 2, map_matrix) == True
