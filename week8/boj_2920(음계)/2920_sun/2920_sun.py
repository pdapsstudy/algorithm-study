import sys
input = sys.stdin.readline

input_list = list(map(int, input().split()))

if input_list[0] == 1:
    type = "ascending"
    for i in range(1, len(input_list)):
        if input_list[i-1] > input_list[i]:
            type = "mixed"
elif input_list[0] == 8:
    type = "descending"
    for i in range(1, len(input_list)):
        if input_list[i-1] < input_list[i]:
            type = "mixed"
else:
    type = "mixed"

print(type)
