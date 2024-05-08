import sys
input = sys.stdin.readline
#수식을 만드는게 어려웠음 -> 모든 경우의 수를 다 불러와야하고 depth를 깊게 가 tree를 만드는 규칙적인 구조이기 때문에 재귀를 이용
#eval함수라는 것을 처음 알게 됨

def recur(num, idx, text, result):  #모든 경우의 수를 다 불러와야 함
    if idx == num:
        if eval(text.replace(' ', '')) == 0:#공백이 있을 경우 없애주고 두 수를 합쳐주는 작업을 replace로 한 후 eval로 최종적인 값이 0이 되는 text(식)을 찾아줌
            result.append(text)
    else:
        idx = idx + 1
        recur(num, idx, text + ' ' + str(idx), result)
        recur(num, idx, text + '+' + str(idx), result)
        recur(num, idx, text + '-' + str(idx), result)
    return result

if __name__ == "__main__":
    N = int(input())
    for _ in range(N):
        result = []
        num = int(input())
        result = recur(num, 1, '1', result)
        for expression in result:
                print(expression)