# https://programmers.co.kr/learn/courses/30/lessons/17686
import re

def solution(files):
    elems = [re.split(r"([0-9]+)", s) for s in files]
    elems.sort(key = lambda x: (x[0].lower(), int(x[1])))
    return ["".join(e for e in elem) for elem in elems]


cases = [
        (
            ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"],
            ["img1.png", "IMG01.GIF", "img02.png", "img2.JPG", "img10.png", "img12.png"]
            ),
        (
            ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"],
            ["A-10 Thunderbolt II", "B-50 Superfortress", "F-5 Freedom Fighter", "F-14 Tomcat"]
            ),
        (
            ["img12", "img10", "img02", "img1", "IMG01", "img2"],
            ["img1", "IMG01", "img02", "img2", "img10", "img12"]
            ),
        ]
for files, answer in cases:
    assert solution(files) == answer
