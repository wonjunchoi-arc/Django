
from bs4 import BeautifulSoup
from urllib.request import urlopen

class BugsMmusic(object):

    url = ''

    def __str__(self):
        return self.url


#https://music.bugs.co.kr/chart/track/realtime/total?wl_ref=M_contents_03_01

    @staticmethod
    def find_bugs(soup, info):
        print(f'------------{info} RANKING-----------------')
        count = 0
        for i in soup.find_all(name='p', attrs=({"class": info})):
            count += 1  # 랭크의 숫자를 만들어 내는 곳
            print(f'{str(count)} RANKING')
            print(f'{info}:{i.find("a").text}')  #
    @staticmethod
    def main():
        bugs =BugsMmusic()
        while 1:
            menu = input('0.Exit 1.URL을 입력해 주세요 2.Get Rank URL 3. 4.')
            if menu == '0':
                break
            elif menu == '1':
                bugs.url = input('Input URL')
            elif menu == '2':
                print(f'Input URL is : {bugs}')
                soup = BeautifulSoup(urlopen(bugs.url), 'lxml')
                bugs.find_bugs(soup, "artist")
                bugs.find_bugs(soup, "title")



            else:
                print('잘못된 입력입니다')
                continue
BugsMmusic.main()









