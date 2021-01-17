# https://programmers.co.kr/learn/courses/30/lessons/17680

from collections import OrderedDict

def solution(cacheSize, cities):
    size = 0
    cache = OrderedDict()
    time = 0

    for city in cities:
        city = city.lower()

        if cache.get(city, False): # cache hit
            cache.move_to_end(city, last = True)
            time += 1
        else: # cache miss
            time += 5
            if size < cacheSize:
                cache[city] = True
                size += 1
            elif cache: # do LRU
                cache.popitem(last = False)
                cache[city] = True

    return time


cases = [
        (3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"], 50),
        (3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"], 21),
        (2, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"], 60),
        (5, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"], 52),
        (2, ["Jeju", "Pangyo", "NewYork", "newyork"], 16),
        (0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"], 25),
        ]
for cache_size, cities, ans in cases:
    assert solution(cache_size, cities) == ans
