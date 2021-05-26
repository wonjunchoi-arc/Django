'''
구구단 프로그램은 단을 입력받아서, 입력받은 단의 1~9의 곱을 출력하는 어플이다.
단, 단은 정수이다.
'''


class Gugudan(object):
    num = 0
    dict = {}

    def gugu1(self):
        for i in range(1,10):
            print(f'{self.num} * {i}={self.num*i}')


    def all(self):
        for i in range(1,10):
            for a in range(1,10):
                print(f'{i}*{a}={i*a}')


    def print_dict_num(self):
        d = self.dict
        for i in range(1,10):
           d[i] = self.num * i  # 키는 유니크하기 떄문에 고정된 num이 아니라 숫자다
        print('딕셔너리 출력')
        print(d)
        for k in d.keys():
            print(f'{self.num}* {k} = {d.get(k)}')
    @staticmethod
    def main():
        g = Gugudan()
        while 1:
            menu = input('구구단의 단을 출력합니다.1.2.3.input dan with dict ')
            if menu == '1':
                g.num = int(input('단을 입력하시오'))
                g.gugu1()

            elif menu == '2':
                g.all()
            elif menu == '3':
                g.num = int(input('단 입력'))
                g.print_dict_num()


Gugudan.main()

