case = int(input())

for _ in range(case):
    repeat, str = input().split()
    str_list = list(str)
    result = ''
    for i in range(len(str_list)):
        for j in range(int(repeat)):
            result += str_list[i]
    print(result)