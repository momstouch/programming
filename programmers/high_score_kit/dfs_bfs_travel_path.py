# https://programmers.co.kr/learn/courses/30/lessons/43164

def solution(tickets):
    pass

cases = [
        ([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]],
            ["ICN", "JFK", "HND", "IAD"]),
        ([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]],
            ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"])
        ]
for tickets, answer in cases:
    assert solution(tickets) == answer
