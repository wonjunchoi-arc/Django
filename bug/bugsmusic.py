from bs4 import BeautifulSoup
from urllib.request import urlopen

class BugMusic(object):
    url = ''
    class_name = []

    def __str__(self):
        return self.url

    def scrap(self):
        soup = BeautifulSoup(urlopen(self.url), 'lxml')
        print('------------TITLE RANK------------')
        count = 0
        for i in soup.find_all(name='p', attrs=({'class':self.class_name[0]})):
            count += 1
            print(f'{str(count)} RANKING')
            print(f'{self.class_name[0]} : {i.find("a").text}')

        print('------------ARTIST RANK------------')
        count = 0
        for i in soup.find_all(name='p', attrs=({'class': self.class_name[1]})):
            count += 1
            print(f'{str(count)} RANKING')
            print(f'{self.class_name[1]} : {i.find("a").text}')


    def title_dict(self):
        print()




    @staticmethod
    def main():
        bugs = BugMusic()
        while 1:
            menu = input('0.Exit 1. URL 2. RANKING 3.')
            if menu == '0':
                break
            elif menu == '1':
                bugs.url = input('URL')

            elif menu == '2':
                bugs.class_name.append('title')
                bugs.class_name.append('artist')
                bugs.scrap()





            else:
                print('잘못된 입력입니다.')
                continue

BugMusic.main()











