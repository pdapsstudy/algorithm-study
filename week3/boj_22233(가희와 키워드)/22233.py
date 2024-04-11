import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000000)

if __name__ == "__main__":
    #print("입력하세요") 
    tmp = {}
    tmp2 = {}
    cnt = 0
    cnt2 = 0
    N, M = map(int, input().split())  #N = 메모장에 적은 키워드 M = 블로그에 쓴 글의 개수
    for _ in range(N):
        tmp[str(input().rstrip())] = 1
        cnt += 1
    for i in range(M):
        tmp2 = list(str(input().rstrip().split(',')))     
        for j in tmp2:
            if i in tmp.keys():
                if tmp[i] == 1:
                    tmp[i] = 0
                    cnt -= 1
        print(cnt)
