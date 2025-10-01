# 사용자 정의 모듈
def sum(n):
    sum = 0
    for i in range(1, n+1):
        sum = sum + i
        return sum
    
def power(x, n):
    prod = 1
    for i in range(1, n+1):
        prod = prod * x
        return prod
    
if __name__ == '__main__': # myModule.py를 직접 호출할 때만 실행됨
 print(sum(5))
 print(power(2, 3))