from collections import defaultdict

result = defaultdict(int)

for line in open('data.csv'):
    line = line.strip().split(',')
    if line[1] == 'click':
        result[line[0]] += 1
print result
