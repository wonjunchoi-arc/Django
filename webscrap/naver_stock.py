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


    def scrap(self):
        driver = webdriver.Chrome(self.driver_path)
        driver.get(self.url)
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        # print(soup.tbody.find_all(name="tr"))
        all_td = soup.find_all(name="a", attrs=({"class":"tltle"}))
        for i in all_td:
            # self.date_ls.append(i.text)
            print(i.text)
            print(i['href'].split('code=')[1])
            self.title_ls.append(i.text)
            self.code_ls.append(i['href'].split('code=')[1])

        driver.close

    def insert_dic(self):
        for i, j in enumerate(self.title_ls):
            self.dic[j] = self.code_ls[i]

        print(self.dic)

    def dic_to_dataframe(self):
        self.df = pd.DataFrame.from_dict(self.dic, orient='index')
        print(self.df)

    def df_to_csv(self):
        path = './data/naverstock.csv'
        self.df.to_csv(path, sep=',', na_rep='NaN')





if __name__ == '__main__':
    naver = Naver_Stock()
    naver.scrap()
    naver.insert_dic()
    naver.dic_to_dataframe()
    naver.df_to_csv()




