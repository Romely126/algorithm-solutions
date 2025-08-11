case = int(input())

for i in range(case):
    quiz = list(input())
    count = 0
    score = 0
    for j in range(len(quiz)):
        if(quiz[j] == 'O'): #만약 결과가 O면
            count += 1  #카운트스케일을 1씩 증가
        else:
            count = 0   #이외의 경우엔 카운트스케일 초기화
        score += count #각 결과값마다 나온 점수를 합계
    print(score)