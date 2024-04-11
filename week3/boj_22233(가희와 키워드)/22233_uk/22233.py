
if __name__ == "__main__":
    print("입력하세요") 
    N, M = map(int, input().split())
    tmp = dict()
    for _ in range(N):
        tmp[input().rstrip()] = 1
    print(tmp)    
    cnt = N
    for _ in range(M):
        entries = input().rstrip().split(',')
        print(entries)
        for i in entries:
            if i in tmp and tmp[i] == 1:
                tmp[i] -= 1
                cnt -= 1
        print(cnt)
