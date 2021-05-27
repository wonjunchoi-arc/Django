from bs4 import BeautifulSoup
import requests
import pandas as pd

class Bmusic():
    url = 'https://music.bugs.co.kr/chart/track/realtime/total?'
    headers = {'User-Agent': 'Mozilla/5.0'}
    class_number = []
    title_ls = []
    artist_ls = []
    dic = {}
    df = None

    def set_url(self,detail):
        self.url = requests.get(f'{self.url}{detail})',headers=self.headers).text

    def get_ranking(self):
        soup = BeautifulSoup(self.url, 'lxml')
        print('-----------title----------------')
        ls = soup.find_all(name='p', attrs=({"class": self.class_number[1]}))
        for i in ls:
            print(f'{i.find("a").text}')
            self.title_ls.append(i.find("a").text)
        print('-----------artist----------------')
        ls = soup.find_all(name='p', attrs=({"class": self.class_number[0]}))
        for i in ls:
            print(f'{i.find("a").text}')
            self.artist_ls.append(i.find("a").text)




#https://music.bugs.co.kr/chart/track/realtime/total?wl_ref=M_contents_03_01
    def inser_title_dict(self):
        for i, j in enumerate(self.title_ls):
            self.dic[j] = self.artist_ls[i]

        print(self.dic)

    def dict_to_dataframe(self):
        self.df = pd.DataFrame.from_dict(self.dic, orient='index')  #dt -> df로 전환
        print(self.df)

    def df_to_csv(self):
        path = './data/bugs.csv'
        self.df.to_csv(path, sep=',' ,na_rep='NaN')





    @staticmethod
    def main():
        bm = Bmusic()
        while 1:
            menu = input('0. 1. 2. 3. 4.')
            if menu == '0':
                break
            elif menu == '1':
                bm.set_url(input('상세정보를 입력하시오'))
            elif menu == '2':
                bm.class_number.append('title')
                bm.class_number.append('artist')
                bm.get_ranking()
            elif menu == '3':
                bm.inser_title_dict()

            elif menu == '4':
                bm.dict_to_dataframe()

            elif menu == '5':
                bm.df_to_csv()



Bmusic.main()

