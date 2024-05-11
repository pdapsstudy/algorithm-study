import sys
input = sys.stdin.readline

N = int(input())
num_list = list(map(int, input().split()))
answer = ""
if N <= 1:
    # 만일 a, b을 확정하기에 변수의 개수가 부족한 경우: A
    answer = "A"

elif N == 2:
    if num_list[0] == num_list[1]:
        answer = num_list[0]
    else:
        answer = "A"

else:
    # a, b의 값 구하기
    if (num_list[0]==num_list[1]):
        a = 0
    else:
        a = (num_list[1] - num_list[2])  / (num_list[0] - num_list[1])
    
    b = num_list[1] - a * num_list[0]

    # 만일 a나 b가 정수가 아니라면 B
    if (int(a)!=a or int(b)!=b):
        answer = "B"

    else:
        for i in range(N-1):
            if num_list[i+1] != (num_list[i] * a + b):
                # 만일 이후 범위에서 식을 만족하지 않는 경우: B
                answer = "B"

        if answer == "":
            answer = int(num_list[-1]*a+b)

print(answer)
