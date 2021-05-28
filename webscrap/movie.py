from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

class NaverMove(object):
    url = 'https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=cur&date=20210527'
    classes_name = ''
    driver_path = 'C:\Program Files\Google\Chrome\chromedriver' #오브젝트의 기본값 알수 없음을  NONE로 표시
    title_ls = []
    point_ls = []
    dic = {}
    df = None

    def scrap(self):
        driver = webdriver.Chrome(self.driver_path)
        driver.get(self.url)  #이 방식은 뷰티풀숩과 다르게 코드를 가져오는 것이 아니라 url을 chrome driver에 넘긴다.
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        all_div =soup.find_all(name='div',attrs={'class':self.classes_name[0]})
        for i in all_div:
            print(i.find('a').text)
        self.title_ls.append(i.find('a').text)

        all_div = soup.find_all(name='td', attrs={'class': self.classes_name[1]})
        for i in all_div:
            print(i.find('td').float)
        self.point_ls.append(i.find('td').text)


        driver.close


    def insert_dic(self):
        for i, j in enumerate(self.title_ls):
            self.dic[j] = self.point_ls[i]

        print(self.dic)

    def dic_to_dataframe(self):
        self.df = pd.DataFrame.from_dict(self.dic, orient='index')
        print(self.df)

    def df_to_csv(self):
        path = './data/navermovie.csv'
        self.df.to_csv(path, sep=',', na_rep='NaN')








if __name__ == '__main__':
    naver = NaverMove()
    naver.classes_name = input('입력하시오'), input('입력하시오')
    naver.scrap()

    # def get_ranking(self):
    #     soup = BeautifulSoup(urlopen(self.url), 'lxml')
    #     ls = soup.find_all(name='div', attrs={'class':'tit3'})
    #     for i in ls :
    #         print(i.find('a').text)
