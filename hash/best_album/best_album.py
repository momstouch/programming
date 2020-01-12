# https://programmers.co.kr/learn/courses/30/lessons/42579
import operator

def solution(genres, plays):
    genre_rank = {}
    song_per_gen = {}
    for idx, (g, p) in enumerate(zip(genres, plays)):
        genre_rank[g] = genre_rank.get(g, 0) + p
        song_per_gen[g] = song_per_gen.get(g, []) + [[idx, p]]

    for key in song_per_gen.keys():
        song_per_gen[key].sort(
                reverse = True,
                key = operator.itemgetter(1)
                )
        if len(song_per_gen[key]) > 2:
            song_per_gen[key] = song_per_gen[key][:2]

    answer = []
    for genre in sorted(genre_rank, key = genre_rank.get, reverse = True):
        for song_id, play in song_per_gen[genre]:
            answer.append(song_id)

    return answer

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
# return [4, 1, 3, 0]

print(solution(genres, plays))
