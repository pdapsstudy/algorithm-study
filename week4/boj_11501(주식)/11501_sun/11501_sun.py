import sys
input = sys.stdin.readline

T = int(input())


def cal_profit():
    N = int(input())
    price = list(map(int, input().split()))
    profit = 0
    stock = []
    cum_stock = [0, price[0]]

    for i in range(N):
        stock.append((i, price[i]))
        if i != 0:
            cum_stock.append(cum_stock[i] + price[i])

    stock.sort(key=lambda x: x[1])

    idx = 0
    for k in range(N):
        now = stock.pop()
        if now[0] >= idx:
            # now[0]은 현재 주가 (stock)의 기존 index, now[1]은 현재 주가 가격
            cnt = now[0] - idx
            profit += now[1] * cnt - (cum_stock[now[0]] - cum_stock[idx])
            idx = now[0] + 1
        else:
            continue

    return profit


for _ in range(T):
    print(cal_profit())
