# https://programmers.co.kr/learn/courses/30/lessons/42579

def solution(genres, plays):
    genre_rank = {}
    song_rank = {}
    for idx, (gen, pl) in enumerate(zip(genres, plays)):
        genre_rank[gen] = genre_rank.get(gen, 0) + pl
        song_rank[idx] = pl

    song_rank = {k: v for k, v in sorted(
        song_rank.items(),
        key = lambda item: (item[1], -item[0]),
        reverse=True
        )}

    answer = []
    n_songs_in_album = 2
    cnt = 0
    for gen, _ in sorted(genre_rank.items(), key = lambda item: item[1], reverse=True):
        for idx in song_rank.keys():
            if gen == genres[idx]:
                answer.append(idx)
                cnt += 1
                if cnt == n_songs_in_album:
                    cnt = 0
                    break

    return answer


def solution2(genres, plays):
    genre_rank = {}
    song_rank = {}
    for idx, (gen, pl) in enumerate(zip(genres, plays)):
        genre_rank[gen] = genre_rank.get(gen, 0) + pl
        song_rank[gen] = song_rank.get(gen, []) + [[idx, pl]]

    for gen in song_rank:
        song_rank[gen] = sorted(
                song_rank[gen],
                key = lambda x: (x[1], -x[0]),
                reverse = True
                )[:2]

    answers = []
    for gen in sorted(
            genre_rank,
            key = genre_rank.get,
            reverse = True
            ):
        [answers.append(idx) for idx, _ in song_rank[gen]]

    return answers

cases = [
        [
            ["classic", "pop", "classic", "classic", "pop"],    # genres
            [500, 600, 150, 800, 2500]                          # plays
            ],                                                  # answer: [4, 1, 3, 0]
        ]

for case in cases:
    genres, plays = case
    print(solution(genres, plays)) # failed from case 9
    print(solution2(genres, plays)) # pass
