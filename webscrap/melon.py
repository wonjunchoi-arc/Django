from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib.parse

class Melon(object):
    url = ''
    heador01 = {'User-Agent' : 'Mozilla/5.0'}

    def __str__(self):
        return self.url

    def scrap(self,soup):
        pass



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
                modi01 = urllib.request.Request(me.url, headers=me.heador01)
                soup = BeautifulSoup(urlopen(modi01), 'lxml')

                # print(f'Input URL:me.url')
                # print(me.scrap())
                # print('-----------------------TITLE RANK---------------------------')
                count = 0

                for i in soup.find_all(attrs="div", name=({"class": "ellipsis rank03"})):
                    count += 1
                    print(f'{str(count)}, RANKING')
                    print(f'TITLE{i.find("a").text}')
                print('-----------------------TITLE RANK---------------------------')
                count = 0
                for i in soup.find_all(attrs="div", name=({"class": "ellipsis rank02"})):
                    count += 1
                    print(f'{count}, RANKING')
                    print(f'ARTIST{i.find("a").text}')
                return 'test'




            else:
                print('잘못된 입력입니다')
                continue


Melon.main()
