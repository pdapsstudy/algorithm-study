import sys

input = sys.stdin.readline

def compare_str(str1, str2):
    for i in range(len(str1)):
        if str1[i] == str2[i]:
            continue
        elif str1[i] > str2[i]:
            return "big"
        else:
            return "small"
    return "same"

N, M = map(int, input().split())
words = [[] for _ in range(11)]
count = N

for _ in range(N):
    new = input().replace('\n', '')
    words[len(new)].append(new)


for _ in range(M):
    input_list = list(input().replace('\n','').split(','))
    for keyword in input_list:
        length = len(keyword)
        for word in words[length]:
            flag = compare_str(word, keyword)
            if flag == "same":
                count -= 1
                words[length].remove(word)

    print(count)