import sys
from queue import PriorityQueue

input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))


def card_hapjae():
    global output, A
    PQ = PriorityQueue()
    order = 0

    ## 우선순위 큐에 일단 있는거 다 넣음
    for card in A:
        PQ.put(card)

    while order < M :
        x = PQ.get()
        y = PQ.get()
        new_card = x + y
        PQ.put(new_card)
        PQ.put(new_card)
        order += 1

    result = 0
    for _ in range(N):
        result += PQ.get()
    return result

result = card_hapjae()
print(result)