n = int(input())
marks = {}
for i in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    marks[name] = scores

query_name = input()

output = list(marks[query_name])
per = sum(output)/len(output)
print("%.2f" %per)