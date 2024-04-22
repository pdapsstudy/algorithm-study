import sys
input = sys.stdin.readline
#배열을 뒤집지 않으면 배열의 마지막 요소를 처리하기가 너무 까다로움 어찌됐든 수익이 나려면 배열의 마지막 요소에서는 다 팔아야되기 때문 
#그리고 buy라는 배열을 따로 만들어서 max_price가 되기 전까지의 요소들을 다 따로 저장하고 있어야 됨 - 그래야 max_price를 만났을 때 저장된 값을 모두 뺄 수 있기 때문
#배열을 뒤집지 않고 효율적으로 할 수 있는 법은 없을까 
if __name__ == "__main__":                     
  #print("입력하세요")
  buy = []
  N = int(input())
  for i in range(N):
    case = int(input())
    stock = list(map(int, input().split()))
    stock.reverse()
    buy = []
    print(stock)
    max_price = 0
    profit = 0
    cnt = 1
    for i in range(len(stock)):
      if max_price <= stock[i]:
        max_price = stock[i]
      elif max_price > stock[i]:
         profit += (max_price-stock[i])  
    print(profit)  
    
    # 배열을 뒤집지 않고 했을 때
    #  for i in range(len(stock)):
        # if max_price > stock[i]:
        #   for i in range(len(buy)):
            #  profit += (max_price-buy.pop(0))
    #    elif max_price <= stock[i]:
        #  max_price = stock[i]
        #  buy.append(stock[i])