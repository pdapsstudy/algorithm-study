import sys
input = sys.stdin.readline
#시작하는 줄을 기준으로 정렬 끝나는 줄을 기준으로는 가장 긴 증가하는 순열 처럼(12015번) 정렬(앞 순서가 뒷 순서보다 작은 경우가 최대로 이어지는 경우)을 하면 전깃줄이 교차하지 않기 위해 있어야할 배열을 알 수 있음
#한번 풀어봤던 문제
#구현 방법만 떠올린다면 어렵지 않은 문제 처음에 그냥 구현문제인줄 알았음 구현인가? -> dp로 풀기 -> 메모리 이슈로 인한 이분탐색
#입력 처리하는게 조금 까다로울 수 있음 시작하는 줄(dictionary의 key값)을 기준으로 끝 점을 정렬해야하기 때문에 item과 lambda를 이용해 정렬 가능
dic = {}

def bi_search(arr, x):
    left, right = 0, len(arr)
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return left


def search(A):
 sq = [0]
 for i in range(len(A)):
    if sq[-1] < A[i]: # 들어온 값이 더 크면 
        sq.append(A[i]) # 바로 추가
    elif sq[-1] > A[i]: # 작다면
        idx = bi_search(sq, A[i]) 
        sq[idx] = A[i] # 더 작은 값으로 교체

 #print(sq) 
 return len(sq) - 1
  
if __name__ == "__main__":
    #print("입력하세요") 
    N = int(input())
    arr1 = []
    arr2 = []
    value = []
    number = 0
    for i in range(N):
        a, b = map(int, input().split())
        arr1.append(a)
        arr2.append(b)
        dic[a] = b
        sort_dic = dict(sorted(dic.items()))
    value = list(sort_dic.values())
    number = search(value)
    print(len(value) - number)