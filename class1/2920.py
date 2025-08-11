scale = list(map(int, input().split())) #list형, 각 값을 정수로 지정

if scale == list(range(1, 9)): #1부터 8까지 1만큼 범위지정(생략됨)
    print("ascending")
elif scale == list(range(8, 0, -1)): #8부터 1까지 -1만큼 범위지정
    print("descending")
else:
    print("mixed")