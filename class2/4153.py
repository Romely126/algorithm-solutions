while(True):
    a = list(map(int, input().split()))
    for i in range(int(len(a))):
        if int(a[i]) == 0:
            exit()
    sorted_a = sorted(a, key=int)
    hypo = sorted_a.pop()
    if int((sorted_a[0]*sorted_a[0])+(sorted_a[1]*sorted_a[1])) == int(hypo*hypo):
        print("right")
    else:
        print("wrong")

# 빗변은 세 변중 언제나 가장 긴 변임
# 따라서 오름차순 정렬 후 가장 마지막에 오는 변이 빗변