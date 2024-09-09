#6
n = int(input())
a1, a2 = 0, 1

if n < 0 or n > 10**7:
    print('Err')
    exit(0)

if n == 0: print(a1)
elif n == 1: print(a2)
else:
    for i in range(n-1):
        a1, a2 = a2%10, (a1+a2)%10
    print(a2)
