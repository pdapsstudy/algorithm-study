import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
nodes = [arr[0]]  # arr의 초기 값으로 처음 값 넣음

def binary_search(nodes, target):
    start = 0
    end = len(nodes)-1
    answer = 0
    while start <= end:
        mid = (start + end) // 2
        if target > nodes[mid]:
            start = mid + 1
            answer = start
        else:
            end = mid -1
    return answer

for i in range(1, N):
    target = arr[i]
    # print(f"arr {arr} nodes {nodes}")
    if target > nodes[-1]:  # 만일 뒤에 붙을 수 있으면 뒤에 append
        nodes.append(target)
    else:
        idx = binary_search(nodes, target)
        nodes[idx] = target

print(len(nodes))