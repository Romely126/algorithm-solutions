# 첫줄에 참가자 수 n
# 둘째줄에 티셔츠 사이즈별 신청자 수를 입력, 총 6사이즈, S M L XL XXL XXXL
# 셋째줄에 티셔츠와 펜의 묶음수 t와 p가 각각 부여

# 출력
# 첫줄에 티셔츠 묶음수
# 둘째줄에 펜 묶음수


n = int(input()) # 참가자 수
s, m, l, xl, xxl, xxxl = list(map(int, input().split()))
t, p = list(map(int, input().split()))

# 각 티셔츠 사이즈별 최소 주문수
if s % t != 0:
    s_sell = s // t + 1
else:
    s_sell = s // t

if m % t != 0:
    m_sell = m // t + 1
else:
    m_sell = m // t

if l % t != 0:
    l_sell = l // t + 1
else:
    l_sell = l // t

if xl % t != 0:
    xl_sell = xl // t + 1
else:
    xl_sell = xl // t

if xxl % t != 0:
    xxl_sell = xxl // t + 1
else:
    xxl_sell = xxl // t

if xxxl % t != 0:
    xxxl_sell = xxxl // t + 1
else:
    xxxl_sell = xxxl // t

# sum함수는 리스트와 튜플을 인자로 받음, 따라서 리스트로 객체들을 묶어줘야 함
t_sell = sum([s_sell, m_sell, l_sell, xl_sell, xxl_sell, xxxl_sell])
print(t_sell)

p_roll = n // p
p_each = n % p

print(p_roll, p_each)