import sys

input = sys.stdin.readline
N = int(input())
K = int(input())
bam = []
apple = []

for _ in range(K):
    row, col = map(int, input().split())
    apple.append((row, col))

L = int(input())
move = []
for _ in range(L):
    time, direction = input().split()
    move.append((int(time), direction))

def is_continue(bam, now):
    flag = True
    if now in bam:
        flag = False
    if now[0] > N or now[0] < 1 or now[1] > N or now[1] < 1:
        flag = False
    return flag

# (행, 열): 행-아래, 열-오른쪽
next_move = (0, 1) # 뱀은 처음에 오른쪽을 향한다.
now = (1, 1) # 첫 위치는 맨 위 맨 좌측
bam.append(now) # 이를 뱀에 추가함
time = 0 # 시간
movement = move.pop(0)
while is_continue(bam, now):
    # 움직임을 결정하는 코드
    if movement[0] == time: # 만일 방향을 바꾼다면, 
        pass
    # 현재 위치 수정
    now[0] += movement[0]
    now[1] += movement[1]
    # 사과가 있는지 판단
    is_apple = apple.index(now)
    # 만약에 사과가 있다면 -> 뱀 길이 증가
    # 사과가 없다면 -> 뱀 길이 유지

    # 뱀 업데이트

print(time)