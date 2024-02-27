n = int(input())
int_list = map(int,input().split())

t = tuple(int_list)

result = hash(t)

print(result)