from collections import defaultdict

result = defaultdict(int)
for line in open('data.csv'):
    result[line.strip()] += 1
print result
