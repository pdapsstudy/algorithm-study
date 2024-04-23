import sys
input = sys.stdin.readline
#일반 구현으로 풀면 시간초과 & 순차 탐색으로 단순 비교만 하면 문제가 틀림
#메모리 접근 -> 이분탐색 
#최대한 많은 수를 담아야하기 때문에 끝에 수보다 작다고 바로 버리지 말기

def binary_search(arr, x):   #작은 값을 가지고 idx를 알기 위한 함수
    left, right = 0, len(arr)
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
        return left   #작은 값을 찾기 위해 left반환   

if __name__ == "__main__":                     
  #print("입력하세요")
  n = int(input())
  memory =  list(map(int, input().split()))
  sq = [0]
  
  for i in range(len(memory)):
    if sq[-1] < memory[i]:
       sq.append(memory[i])#바로 추가 
    elif sq[-1] > memory[i]:
            idx = binary_search(sq, memory[i])
            sq[idx] = memory[i]  #더 작은 값으로 교체
  print(len(sq)-1)    