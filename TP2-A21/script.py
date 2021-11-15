import sys
result = sys.stdin.read()
result = result[1:-2].split(',')
#print(result)
print(max(list(map(int, result))))