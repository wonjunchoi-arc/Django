from bs4 import BeautifulSoup
from urllib.request import urlopen

class Melon():
    url = ''

    def __str__(self):
        return self.url

    @staticmethod
    def main():
        m = Melon()  # 왜 여기서는 ()를 넣어주는 것일까??
        while 1:
            b = Melon()  # 왜 여기서는 ()를 넣어주는 것일까??
            menu = input('0.Exit 1.URL을 입력해 주세요 2.Get Rank URL 3. 4.')
            if menu == '0':
                break

            elif menu == '1':
                m.url = input('URL')
                print(m.url )

            elif menu == '2':
                print(m.url)   #여기서 안되는 이유는 무엇일까용??


Melon.main()
