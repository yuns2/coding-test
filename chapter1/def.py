# 1 
def add(a,b) :
    return a + b

print(add(2,3))

# 2 : 1 변형
# return없이 작성
# 파라미터의 변수 직접 지정
def add2(a,b):
    print('a + b =', a+b)

add2(3,4)
add2(b=2, a=4)

# 3 : 전역변수 선언 및 참조
c=1
def func():
    global c
    c += 1

for i in range(10):
    func();

print(c)

# 4 lambda Express사용
# lambda 매개변수 : 표현식
print((lambda a,b: a+b)(3,7));