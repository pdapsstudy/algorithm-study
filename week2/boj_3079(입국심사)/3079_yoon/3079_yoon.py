import sys
input = sys.stdin.readline

N, M = map(int, input().split())
time = []    # 각 심사대에서 심사를 받는데 걸리는 시간 

first = int(input())
second = int(input())

for i in range(N):
    K = int(input())
    time.append(K)
    
time.sort() # 이분 탐색 전 오름차순 정렬 

start = 0
end = min(time) * M # TIME의최소값 * 사람 수
result = 0

while start <= end :
    mid = (start + end) // 2
    person = 0  # 처리한 사람 수 

    # 각 심사대에서 주어진 시간동안 처리할 수 있는 사람 수 누적적
    for t in time:
        person += mid // t

    if person >= M:
        end = mid - 1   # 더 짧은 시간에 가능하기에 end를 줄여줌줌
        result = mid
    else:
        start = mid + 1

print(result)