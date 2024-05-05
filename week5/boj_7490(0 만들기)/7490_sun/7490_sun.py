import sys
from itertools import product
input = sys.stdin.readline

T = int(input()) # testcase 개수

def cal_str(str): # 입력한 수식 계산하는 함수 (eval 사용)
    str_list = str.split(" ")
    result = "".join(str_list)
    answer = eval(result)
    return answer 

def make_cal(num): # 수식 만드는 함수
    cal_tool = ["+", "-", " "]
    numbers = tuple(range(1, num+1))
    cal_combination = []
    result = []
    for i in product(cal_tool, repeat=num-1):
        cal_combination.append(i)

    for t in range(len(cal_combination)):
        tmp = ""
        cal = cal_combination[t]
        for i in range(num-1):
            tmp += str(numbers[i]) + cal[i]
        tmp += str(numbers[-1])
        result.append(tmp)
    return result

for _ in range(T):
    N = int(input())
    cal_list = make_cal(N)
    answer = []
    for cal in cal_list:
        if cal_str(cal) == 0:
            answer.append(cal)
    answer.sort()
    for ans in answer:
        print(ans)
    print()
    # print(*sorted(answer), sep="\n")
