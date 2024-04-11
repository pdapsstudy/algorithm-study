import sys
input = sys.stdin.readline

N, M = map(int, input().split())
words = []
keywords = []
count = N

for _ in range(N):
    words.append(input().replace('\n', ''))

words.sort()

for _ in range(M):
    input_list = list(input().replace('\n', '').split(','))
    keywords.append(input_list)

# 이분 탐색으로 진행


def compare_str(str1, str2):
    length = min(len(str1), len(str2))
    for i in range(length):
        if str1[i] == str2[i]:
            continue
        elif str1[i] > str2[i]:
            return "big"
        else:
            return "small"


def binary_search(target, words):
    low = 0
    high = len(words) - 1
    flag = False

    while low <= high:
        mid = (low + high) // 2
        compare = compare_str(target, words[mid])
        if words[mid] == target:
            flag = True
            del words[mid]
            break
        elif compare == "big":
            low = mid + 1
        else:
            high = mid - 1

    return flag, words


for i in range(M):
    for t in keywords[i]:
        flag, words = binary_search(t, words)
        if flag:
            count -= 1
    print(count)
