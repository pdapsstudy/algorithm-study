import sys
input = sys.stdin.readline
#일반 구현으로 풀면 시간초과 & 순차 탐색으로 단순 비교만 하면 문제가 틀림
#메모리 접근 -> 이분탐색 
#끝에 수보다 작다고 바로 버리지 말기 최대한 많은 수를 담아야하기 때문에(비교 대상인 수가 작으면 작을 수록 뒤에 더 많은 숫자를 담을 수 있으니까) 

def bi_search(arr, x): 
    left, right = 0, len(arr)
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
            
    print(left)        
    return left

A = list(map(int, input().split()))

sq = [0]
for i in range(len(A)):
    if sq[-1] < A[i]: # 들어온 값이 더 크다면 
        sq.append(A[i]) # 바로 추가
    elif sq[-1] > A[i]: # 작다면
        idx = bi_search(sq, A[i]) 
        sq[idx] = A[i] # 처음으로 더 리스트에서 더 큰 값이 나타나는 인덱스 찾은 후 교체

print(sq)
print(len(sq)-1)     