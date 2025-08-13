case = int(input())
a = []

if case == 0:
    exit()

for _ in range(case):
    a.append(input())

for i in range(case):
    mem = a[i]
    leng = int(len(mem)) / 2
    if(mem[int(leng)-1] == mem[int(leng)]):
        print("Do-it")
    else:
        print("Do-it-Not")