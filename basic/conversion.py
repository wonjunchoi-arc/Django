# import pandas as pd
# class Conversion(object):
#     i = 0
#     f = 0.0
#     s = ''
#     ls = []
#     t = ()
#     d = {}
#
# #return 은 저장하고 버리는 값이라고 생각하면 된다.
#     def make_tp(self):
#         self.t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
#         return self.t
#
#     def conv_list(self):
#         self.ls = list(self.t)
#         return self.ls
#
#     def float_list(self):
#         self.ls = list(map(float, self.ls))
#         return self.ls
#
#     def int_list(self):
#         self.ls = list(map(int, self.ls))
#         return self.ls
#
#     def conv_dic(self):
#         self.d = {str(i+1): self.ls[i] for i in range(0, len(self.ls))}
#         return self.d
#
#     def conv_tp(self):
#         self.tp = tuple('hello')
#         return self.tp
#
#     def conv_ls(self):
#         self.ls = list(self.tp)
#         return self.ls
#     def conv_data(self):
#         df = pd.DataFrame(self.d)
#         return df
#
#
#
#
#     @staticmethod
#     def main():
#         c = Conversion()
#         while 1:
#             m = input('0-exit 1-create tuple\n'
#                       '2-convert list\n'
#                       '3-convert float-list\n'
#                       '4-convert int-list\n'
#                       '5-list convert dictionary\n'
#                       '6-str convert tuple\n'
#                       '7-str tuple convert list')
#             if m == '0':
#                 break
#             # 1부터 10까지 요소를 가진 튜플을 생성하시오 (return)
#             elif m == '1':
#                 print(c.make_tp())
#             # 1번 튜플을 리스트로 전환하시오 (return)
#             elif m == '2':
#                 print(c.conv_list())
#             # 2번 리스트를 실수(float) 리스트 바꾸시오  (return)
#             elif m == '3':
#                 print(c.float_list())
#             # 3번 실수(float) 리스트을, 정수 리스트로 바꾸시오  (return)
#             elif m == '4':
#                 print(c.int_list())
#             # 4번 리스트를 딕셔너리로 전환하시오. 단 키는 리스트의 인덱스인데 str 로 전환하시오 (return)
#             elif m == '5':
#                 print(c.conv_dic())
#             # 'hello' 를 튜플로 전환하시오
#             elif m == '6':
#                 print(c.conv_tp())
#             # 6번 튜플을 리스트로 전환하시오
#             elif m == '7':
#                 print(c.conv_ls())
#
#
#             elif m == '8':
#                 print(c.conv_data())
#
#             else:
#                 continue
# Conversion.main()
#
#
import pandas as pd
class Conversion(object):


#return 은 저장하고 버리는 값이라고 생각하면 된다.
    @staticmethod
    def make_tp() -> ():
        return (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

    @staticmethod
    def conv_list(tuple) -> []:
        return list(tuple)

    @staticmethod
    def float_list(ls) -> []:
        return [float(i) for i in ls]

    @staticmethod
    def int_list(ls) -> []:  #이 화살표는 리턴할때만 입력하는 것이다.
        return [int(i) for i in ls]

    @staticmethod
    def conv_dic(ls) -> {}:
        # return  dict([str(i) for i in zip(ls, ls)])
        return {str(i+1): [i] for i in range(0, len(ls))}    #t선생님꺼 이부분 참조하면 딕셔너리를 만들려면 리스트 두가지를 사용

    @staticmethod
    def conv_tp()-> ():
        return ('hello')

    @staticmethod
    def conv_ls(tp) -> []:
        return list(tp)


    @staticmethod
    def dictionary_to_dataframe(d):
        return pd.DataFrame.from_dict(d, orient='index')  #전환되는건가??


ls = 'hello'

    @staticmethod
    def main():
        c = Conversion()
        i = 0
        f = 0.0
        s = ''
        ls = []
        t = ()
        d = {}
        index = [1]
        while 1:
            m = input('0-exit 1-create tuple\n'
                      '2-convert list\n'
                      '3-convert float-list\n'
                      '4-convert int-list\n'
                      '5-list convert dictionary\n'
                      '6-str convert tuple\n'
                      '7-str tuple convert list')
            if m == '0':
                break
            # 1부터 10까지 요소를 가진 튜플을 생성하시오 (return)
            elif m == '1':
                t = c.make_tp()
                print(f'')
                print(t)
            # 1번 튜플을 리스트로 전환하시오 (return)
            elif m == '2':
                q = c.conv_list(t)
                print(q)
            # 2번 리스트를 실수(float) 리스트 바꾸시오  (return)
            elif m == '3':
                w = c.float_list(q)
                print(w)
            # 3번 실수(float) 리스트을, 정수 리스트로 바꾸시오  (return)
            elif m == '4':
                e = c.int_list(w)
                print(e)
            # 4번 리스트를 딕셔너리로 전환하시오. 단 키는 리스트의 인덱스인데 str 로 전환하시오 (return)
            elif m == '5':
                r = c.conv_dic(e)
                print(r)
            # 'hello' 를 튜플로 전환하시오
            elif m == '6':
                p = c.conv_tp()
                print(p)
            # 6번 튜플을 리스트로 전환하시오
            elif m == '7':
                o = c.conv_ls(r)
                print(o)


            elif m == '8':
                df = c.dictionary_to_dataframe(r)
                print(df)

            else:
                continue
Conversion.main()
##
