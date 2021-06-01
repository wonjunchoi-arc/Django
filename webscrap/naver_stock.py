from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import pandas as pd

class Naver_Stock(object):
    driver_path = 'C:\Program Files\Google\Chrome\chromedriver'
    url = 'https://finance.naver.com/sise/sise_market_sum.nhn'
    title_ls = []
    code_ls = []
    dic = {}
    df =None
    real_url = []

    def set_url(self):
        for i in range(1,11):
            self.real_url.append(self.url + '?&page='+str(i))

    def scrap(self):
        driver = webdriver.Chrome(self.driver_path)
        for i in range(0,9):
            driver.get(self.real_url[i])
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            all_td = soup.find_all(name="a", attrs=({"class": "tltle"}))
            for i in all_td:
                print(i.text)
                print(i['href'].split('code=')[1])
                self.title_ls.append(i.text)
                self.code_ls.append(i['href'].split('code=')[1])

#코드를 통해서 페이지를
        driver.close

    def insert_dic(self):
        for i, j in enumerate(self.title_ls):
            self.dic[j] = self.code_ls[i]


    def dic_to_dataframe(self):
        self.df = pd.DataFrame.from_dict(self.dic, orient='index')
        print(self.df)

    def df_to_csv(self):
        path = './data/naverstock.csv'
        self.df.to_csv(path, sep=',', na_rep='NaN')





if __name__ == '__main__':
    naver = Naver_Stock()
    naver.set_url()
    naver.scrap()
    # naver.insert_dic()
    # naver.dic_to_dataframe()
    # naver.df_to_csv()




