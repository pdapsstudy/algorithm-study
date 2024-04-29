import sys
#그냥 스택 구현하는 문제
def push(stk, num):
   stk.append(num)

def top(stk):
    if stk:
        return stk[-1]
    else:
        return -1
   
def size(stk):
  return len(stk)

def empty(stk):
  if len(stk) == 0:
     return 1
  else:
     return 0

def pop(stk):   
  if stk:
     return stk.pop()
  elif len(stk) == 0:
     return -1
  
if __name__ == "__main__":
   N = int(input())
   stack = []
   for i in range(N):
      word = sys.stdin.readline().rstrip()
      if word.startswith('push'):   #startswitch = 특정문자로 시작하는 단어 찾기
         a, b = word.split(' ')
         push(stack, int(b))  #문자열 b를 int형으로 안바꿔줘서 런타임에러 발생했었음
      elif word == 'top':
          print(top(stack))
          
      elif word == 'size':
          print(size(stack))

      elif word == 'pop':
          print(pop(stack))

      elif word == 'empty':
          print(empty(stack))