a, b, c = (int(input()) for _ in range(3)) #int(input())을 3번 반복, 각각 입력
num = a * b * c
num_list = list(map(int, str(num)))
for i in range(10):
    print(num_list.count(i))