from collections import deque
import sys

opi = input() # 의견의 수

cut = int(int(opi) * 0.15 + 0.5) # 제거해야 하는 의견의 수, 15%

al = deque() # 의견을 넣을 덱

for _ in range(int(opi)):
    al.append(sys.stdin.readline().strip()) # 시간복잡도 감소를 위함

sorted_list = sorted(list(al), key=int) # 덱을 리스트로 변경, 정수형으로 읽고 정렬
sorted_deque = deque(sorted_list) # 정렬된 리스트를 다시 덱으로 변경

for _ in range(int(cut)): # 덱의 좌, 우에서 절사를 진행
    sorted_deque.pop()
    sorted_deque.popleft()
cut_list = list(sorted_deque)

ins = 0
for i in range(len(cut_list)): # 덱의 총합
    ins += int(cut_list[i])

# ZeroDivisionError 핸들링
if int(len(cut_list)) == 0:
    print(0)
    exit()

result_value = int(ins / int(len(cut_list)) + 0.5)
print(result_value)

# 이 문제의 핵심은 파이썬 round()는 오사오입
# 문제의 반올림은 사사오입을 요구하기에 
# 값에 0.5를 더한 뒤 정수형으로 바꿔 소수점 아래를 날리는 데 있음
# ex. x.4이하는 0.5를 더해도 x.9, x.5이상은 0.5를 더해 x+1로