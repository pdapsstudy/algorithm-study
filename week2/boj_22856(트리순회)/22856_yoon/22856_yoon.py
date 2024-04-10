import sys
input  = sys.stdin.readline

# dfs 코드 변형 
def inorder(tree, i, visited):
    global cnt
    visited[i] = 1  # 방문처리

    for j in tree[i]:
        if visited[j] == 0 and tree[j] != -1:
            cnt += 1
            inorder(tree, j, visited)
            cnt += 1 # 수정 필요..

cnt = 0
N = int(input())
tree = [[] for _ in range(N+1)]

for j in range(N):
    a, b, c = map(int, input().split())

    tree[a].append(b)
    tree[b].append(a)
    tree[a].append(c)
    tree[c].append(a)

visited = [0] * (N+1)
inorder(tree, 1, visited)

print(cnt)