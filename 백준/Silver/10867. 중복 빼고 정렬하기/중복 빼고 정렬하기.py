n = int(input())

list_A = input().split()

list_A = list(map(int,list_A))
list_A = list(set(list_A))
list_A = sorted(list_A)
for i in list_A:
    print(i, end = ' ')