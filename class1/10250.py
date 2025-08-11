case_num = int(input())

for _ in range(case_num):
    h, w, c = map(int, input().split())
    floor = (c-1) % h + 1 #(c-1)을 하지않으면 나머지가 0으로 떨어지는 경우 호수가 100호로 지정됨
    room = (c-1) // h + 1
    if(room < 10):
        room = "0" + str(room)
    print(str(floor) + str(room))