# from bs4 import BeautifulSoup
# import requests
#
# class BugsMusic2():
#     url = 'https://music.bugs.co.kr/chart/track/realtime/total?'
#     headers = {'User-Agent': 'Mozilla/5.0'}
#     class_name = []
#
#
#     def set_url(self,time):
#         self.url = requests.get(f'{self.url}{time}',headers=self.headers).text
#
#
#     def get_ranking(self):
#         soup = BeautifulSoup(self.url, 'lxml')
#         count = 0
#         ls = soup.find_all(name='p', attrs=({'class':self.class_name[0]}))
#         for i in ls :
#             count += 1
#             print(f'RANKING {str(count)})')
#             print(self.class_name[0],i.find('a').text)
#         print('---------Title------------------')
#         count = 0
#         for i in soup.find_all(name='p', attrs=({'class':self.class_name[0]})):   ###ls 를 주고 안주고 뒤에 들어가는 find all이 뭐 달라지는 건지 물어보자
#             count += 1
#             print(f'RANKING {str(count)})')
#             print(self.class_name[1],i.find('a').text)
#
#
#
#     @staticmethod
#     def main():
#         b = BugsMusic2()
#         while 1 :
#             menu = input('0.Exit 1.URL 2.RANKING 3. DiC')
#             if menu == '0':
#                 break
#             elif menu == '1':
#                 b.url = input('세부주소를 넣으세용')
#             elif menu == '2':
#                 b.class_name.append('artist')
#                 b.class_name.append('title')
#                 b.get_ranking()
# BugsMusic2.main()
#
#
#
from bs4 import BeautifulSoup
import requests


class Melon(object):
    url = 'https://www.melon.com/chart/index.htm?dayTime='
    headers = {'User-Agent': 'Mozilla/5.0'}
    class_name = []
    dt = {}
    lls = []
    llls = []

    def set_url(self, time):
        self.url = requests.get(f'{self.url}{time}', headers=self.headers).text

    def get_ranking(self):
        soup = BeautifulSoup(self.url, 'lxml')
        print('------- 제목 --------')
        ls = soup.find_all("div", {"class": self.class_name[0]})
        for i in ls:
            print(f' {i.find("a").text}')
            self.lls.append(i.find("a").text)
        print('------ 가수 --------')
        ls = soup.find_all("div", {"class": self.class_name[1]})
        for i in ls:
            print(f' {i.find("a").text}')
            self.llls.append(i.find("a").text)

    def insert_dict(self):
        s = self.dt
        for i in self.lls:
            for j in self.llls:
                s[i] = j

        print(self.dt)



    @staticmethod
    def main():
        melon = Melon()
        while 1:
            menu = input('0-exit, 1-input time, 2-output 3. ',)
            if menu == '0':
                break
            elif menu == '1':
                melon.set_url(input('스크래핑할 날짜 입력'))  # '2021052511'
            elif menu == '2':
                melon.class_name.append('ellipsis rank01')
                melon.class_name.append('ellipsis rank02')
                melon.get_ranking()

            elif  menu == '3':
                melon.insert_dict()

            else:
                print('Wrong number')
                continue


Melon.main()



