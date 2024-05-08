import sys
from itertools import combinations
input = sys.stdin.readline

L, C = map(int, input().split())
alphabet = list(input().split())
ja = []
mo = []
answer = []

for alph in alphabet:
    if (alph == "a") or (alph == "e") or (alph == "i") or (alph == "o") or (alph == "u"):
        ja.append(alph)
    else:
        mo.append(alph)

ja_max = min(5, L-2)
for ja_cnt in range(1, ja_max+1):
    mo_cnt = L - ja_cnt
    for i in combinations(ja, ja_cnt):
        for t in combinations(mo, mo_cnt):
            answer.append(''.join(sorted(i+t)))

print(*sorted(answer), sep="\n")

