num1 = 1
num2 = 2

#함수
def plus(num1, num2):
    print('더하기 모듈임', num1 + num2)
    
#클래스
class Animal:
    def __init__(self, name):
        self.name = name
    def make_sound(self, sound):
        print(f'{self.name} 이/가 {sound}소리를 냅니다')