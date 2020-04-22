
#Q2

#짝수단 출력하는 함수 만들기
def gugudan_even():
    for i in range (2, 10, 2):
        for j in range(1, 10):
            answer = i*j
            print("%d * %d" % (i, j))

#홀수단 출력하는 함수 만들기
def gugudan_odd():
    for i in range (1, 10, 2):
        for j in range(1, 10):
            answer = i*j
            print("%d * %d" % (i, j))   

#gugudan_odd_or_even 함수 안에서 실행
def gugudan_odd_or_even(i):
    if i % 2 == 0:
        gugudan_even()
    else:
        gugudan_odd()

#실행
gugudan_odd_or_even(4)

#Q3 주어진 숫자에 따라 구구단 출력하는 함수 정의 및 실행

def gugudan_step(num):
    if num == 0:
        print('0으로 나눌 수 없습니다.')
    for i in range(1, num + 1):
        for j in range(1, 10):
            print("%d x %d = %d" % (i, j, i*j))

#실행
gugudan_step(5)


#만들어 놓은 FourCal 클래스에 덧셈, 뺄셈, 곱셈, 나눗셈을 연산할 때 마다
#어떠한 연산을 몇 번 수행했는지 저장하고 그 연산 횟수를 출력하는 메서드 추가

class FourCal:
    def __init__(self, name, age, university, count_add, count_subtract, count_multiply, count_divide):
        self.name = name
        self.age = age
        self.university = university
        self.count_add = count_add
        self.count_subtract = count_subtract
        self.count_multiply = count_multiply
        self.count_divide = count_divide

    def add(self, n1, n2):
        result = n1 + n2
        count_add += 1
        return result
    
    def subtract(self, n1, n2):
        result = n1 - n2
        count_subtract += 1
        return result

    def multiply(self, n1, n2):
        result = n1 * n2
        count_multiply += 1
        return result

    
    def divide(self, n1, n2):
        if(num 2 == 0):
            print('0으로 나눌 수 없습니다')
            return None
        result = n1 / n2
        count_divide += 1
        return result

    def ShowCount(self):
        print("덧셈 : %d, 뺄셈 : %d, 곱셈 : %d, 나눗셈 : %d" % (count_add, count_subtract, count_multiply, count_divide))
