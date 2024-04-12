N = int(input())
tree = {}
visited = {}
inorder_result = []
preorder_result = []
postorder_result = []

for _ in range(N):
    r, s, e = input().split()
    tree[r] = [s, e]
    visited[r] = False


def preorder(root):
    """
    전위 순회: 루트 -> 왼쪽 자식 -> 오른쪽 자식
    """
    global preorder_result
    preorder_result.append(root)
    left = tree[root][0]
    right = tree[root][1]

    if left != '.':
        preorder(left)

    if right != '.':
        preorder(right)


def inorder(root):
    """
    중위 순회: 왼쪽 자식 -> 루트 -> 오른쪽 자식
    """
    global inorder_result
    left = tree[root][0]
    right = tree[root][1]

    if left != '.':
        inorder(left)

    inorder_result.append(root)

    if right != '.':
        inorder(right)


def postorder(root):
    """
    후위 순회: 왼쪽 자식 ->  오른쪽 자식 -> 루트
    """
    global postorder_result
    left = tree[root][0]
    right = tree[root][1]

    if left != '.':
        postorder(left)

    if right != '.':
        postorder(right)

    postorder_result.append(root)


preorder('A')
inorder('A')
postorder('A')

print(*preorder_result, sep="")
print(*inorder_result, sep="")
print(*postorder_result, sep="")
