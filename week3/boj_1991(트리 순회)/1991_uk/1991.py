import sys
input = sys.stdin.readline
#재귀로 제대로 설명할 수 있는지? (메모리에 쌓여서 ~ pop할때 ~부터 꺼낸다 이런식으로)
#tree 만드는 과정이 어려웠음

def preorder(v):
    if v != '.': #자식이 있다면 
        print(v, end="") #A
        preorder(tree[v][0]) #BD
        preorder(tree[v][1]) #C(E)FG
    print()
def inorder(v):
    if v != '.':
        inorder(tree[v][0]) #BD -> DB 
        print(v, end="") #A
        inorder(tree[v][1]) #CEFG   ->   ECFG (E의 위치?)
    print()
def postorder(v):
    if v != '.':        
        postorder(tree[v][0]) #BD -> DB
        postorder(tree[v][1]) #CFGE -> EGFC
        print(v, end="") #A

if __name__ == "__main__":
     N = int(input())  
     tree ={}
     for _ in range(N):
        root, left, right = map(str, input().strip().split()) #dicitonary로 입력 받는 다는 생각이 어려움(node 클래스가 필요하다.)
        tree[root] = [left, right]

     print(tree)
     preorder('A')
     inorder('A')
     postorder('A')