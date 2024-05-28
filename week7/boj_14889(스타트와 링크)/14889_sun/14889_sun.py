import sys
from itertools import combinations
input = sys.stdin.readline

N = int(input())
S = []

for _ in range(N):
    input_list = list(map(int, input().split()))
    S.append(input_list)

min_diff = sys.maxsize
students = range(N)  # 전체 학생 인덱스 (0 ~ N-1)
num_team = N//2


def cal_stat(team):
    output = 0
    for i in team:
        for j in team:
            if i != j:
                output += S[i][j]
    return output


for comb in combinations(students, num_team):
    team1 = list(comb)
    team2 = [i for i in students if i not in team1]
    team1_output = cal_stat(team1)
    team2_output = cal_stat(team2)
    diff = abs(team1_output-team2_output)
    if diff < min_diff:
        min_diff = diff
print(min_diff)
