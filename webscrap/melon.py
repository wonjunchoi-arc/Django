
from bs4 import BeautifulSoup
from urllib.request import urlopen

class Melon(object):
    url = ''

    def __str__(self):
        return self.url

    @staticmethod
    def main():
        me = Melon()
        while 1:
            menu = input('0.Exit 1.URL을 입력해 주세요 2.Get Rank URL 3. 4.')
            if menu == '0':
                break
            elif menu == '1':
                me.url = input('URL')

            elif menu == '2':
                print(f'Input URL:{me}')
                soup = BeautifulSoup(urlopen(me.url), 'lxml')
                print('-----------------------RANK---------------------------')
                for i in soup.find_all(attrs="div", name=({}))





Melon.main()
