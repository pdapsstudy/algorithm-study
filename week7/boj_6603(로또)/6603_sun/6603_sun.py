import sys
from itertools import combinations
input = sys.stdin.readline

line = input()
while line.strip() != "0":  # 0 입력 받을때 까지
    line_input = list(map(int, line.split()))
    s = line_input[1:]
    for i in combinations(s, 6):
        print(*i, sep=" ")
    line = input()
    if line.strip() != "0":
        print("")
