import sys
from itertools import permutations
import copy

input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
cal = list(map(int, input().split()))  # (덧셈, 뺄셈, 곱셈, 나눗셈 개수)
max_output = - sys.maxsize
min_output = sys.maxsize


def calculate(cal_item, num1, num2):
    if cal_item == "+":
        new = num1 + num2
    elif cal_item == "-":
        new = num1 - num2
    elif cal_item == "*":
        new = num1 * num2
    else:
        if num1 > 0:
            new = (num1 // num2)
        else:
            new = (-num1 // num2) * -1
    return new


def process():
    global max_output, min_output, numbers

    # 전체 가능한 모든 연산자 조합
    cal_list = ["+"] * cal[0] + ["-"] * \
        cal[1] + ["*"] * cal[2] + ["/"] * cal[3]

    for j in permutations(cal_list, N-1):
        idx = 1
        output = numbers[0]
        for cal_item in j:
            output = calculate(cal_item, output, numbers[idx])
            idx += 1
        # 최대 / 최소 계산하기
        if output > max_output:
            max_output = output
        if output < min_output:
            min_output = output


process()
print(max_output)
print(min_output)
