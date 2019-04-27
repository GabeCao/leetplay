from collections import Counter
print(Counter(list(map(int, input().split(' ')))).most_common(1)[0][0])