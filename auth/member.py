'''
회원가입 로그인, 정보수정, 마이페이지, 회원탈퇴
'''
class Member(object):
    def __init__(self, name, password, ID, mail):
        self.name = name
        self.password = password
        self.ID = ID
        self.mail = mail

    def __str__(self):
        return f'{self.name}{self.password}{self.ID}{self.AAA}'

    @staticmethod
    def main():
        ls = []
        m = Member
        while 1:
            menu = '0.Exit 1.회원가입 2.로그인 3.마이페이지 4. 정보수정 5. 회원탈퇴'
            if menu == '1':
                ls.append(m(input('이름'),input('비밀번호'), input('아이디'),input('메일')))
            elif menu == '2':
                id = input('ID를 입력해주세여')
                password = input('PassWord를 입력해주세여')






