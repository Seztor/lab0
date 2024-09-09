#3
f_in = open('input.txt')
f_out = open('output.txt', 'w')
a, b = map(int, f_in.readline().split())
print(a + b, file=f_out)
f_in.close()
f_out.close()
