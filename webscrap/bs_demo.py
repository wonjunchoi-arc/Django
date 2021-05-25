from bs4 import BeautifulSoup

class Bs_Demo(object):
    html_doc = ''

    def __str__(self):
        return self.html_doc
    @staticmethod
    def main():
        bs = Bs_Demo()   #이뜻은 하드 디스크의 Bs_Demo에서 메모리라는 공간에 Self라는 공간을 만들었는데 그 중에 bs 라는 공간을 선언하겠다는 것. 노션 참조
        while 1:
            menu = input('0.Exit 1.Input 2.all Print 3.print title')
            if menu == '0':
                break
            elif menu == '1':
                bs.html_doc = """<html><head><title>The Dormouse's story</title></head>
                <body>
                <p class="title"><b>The Dormouse's story</b></p>

                <p class="story">Once upon a time there were three little sisters; and their names were
                <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
                <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
                <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
                and they lived at the bottom of a well.</p>

                <p class="story">TEST vALUE...</p>
                """



            elif menu == '2':
                soup = BeautifulSoup(bs.html_doc, 'html.parser')
                print(soup.prettify())

            elif menu =='3':
                soup = BeautifulSoup(bs.html_doc, 'html.parser')
                print(soup.title.string)  # title뒤에 왜 ()안들어 가는지 확인 하려면 a에 들어가 보자


            else:
                print('잘못된 입력입니다.')
                continue


Bs_Demo.main()
