import sys
from itertools import 
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
cal = list(map(int, input().split()))  # (덧셈, 뺄셈, 곱셈, 나눗셈 개수)
max_output = - sys.maxsize
min_output = sys.maxsize


def calculate(cal_item, num_list):
    num1 = num_list.pop(0)
    num2 = num_list.pop(1)

    if cal_item == 0:
        new = num1 + num2
    elif cal_item == 1:
        new = num1 - num2
    elif cal_item == 2:
        new = num1 * num2
    else:
        new = num1 // num2
    num_list.insert(0, new)
    return num_list


def process(output, cal_list):
    global max_output, min_output

    if len(output) == 1:
        num = output[0]
        if num > max_output:
            max_output = num
        if num < min_output:
            min_output = num
        return

    for i in range(5):
        output = calculate(i, output)
        process(cal_list)

