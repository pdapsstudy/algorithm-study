import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000000)

def search(home, c):
    home.sort()
    start = 1
    end = home[-1]
    while start <= end:
        mid = (start + end) // 2  #mid = 가장 인접한 두 공유기 사이 거리
        current = home[0]   #현재 위치는 가장 왼쪽부터 설정
        count = 1
        for i in range(1, len(home)):
           if home[i] >= current + mid:  #현재 위치에서 다음 집과의 거리가 mid이상이면 = 
                count += 1
                current = home[i]
        if count >= c:  #공유기 설치가 완료 or 더 많이 됨 -> 간격 늘려야 됨 -> 처음으로 되는 구간이 답
            global answer
            start = mid + 1
            answer = mid 
        else:    #공유기 설치를 더 해야함 -> 간격 짧게 -> end가 점점 작아짐
            end = mid -1        
    
    return answer
if __name__ == "__main__":
    #print("입력하세요") 
    list = []
    N, C = map(int, input().split())
    for _ in range(N):
        N = int(input())
        list.append(N)
    dist = search(list, C)
    print(dist)