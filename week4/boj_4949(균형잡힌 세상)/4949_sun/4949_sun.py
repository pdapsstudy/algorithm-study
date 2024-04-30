from collections import deque

lines = []

while True:
    line = input()
    if line == '.':
        break
    lines.append(line)


def make_Q(line):
    Q = deque()
    for i in line:
        if i == "(" or i == ")" or i == "[" or i == "]":
            Q.append(i)
    return Q


def check_validate(Q: deque):
    flag = True
    tmp = deque()
    while len(Q) > 0:
        now = Q.popleft()
        if now == "(":
            tmp.append(now)

        elif now == "[":
            tmp.append(now)

        elif now == "]":
            if not tmp or tmp.pop() != "[":
                flag = False
                break

        elif now == ")":
            if not tmp or tmp.pop() != "(":
                flag = False
                break

    if len(tmp) > 0:
        flag = False

    return flag

for line in lines:
    stack = make_Q(line)
    flag = check_validate(stack)
    if flag == True:
        print("yes")
    else:
        print("no")
