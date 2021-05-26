# ************
# ---Data Type ----
# *********************

'''
python has Five standard types
scalar
    Number : int, float, complex
    string : str
Vector : List, Tuple, Dictionary, Set



hello = 'hello' ##본질은 다른 언어이고 학습을 위해 할당을 해주는 것이다.
print(hello)
print(hello[0])
print(hello[2:5]) # 기본적으로 str은 리스트인가보다.
print(hello[2:])


Python list

ls = ['abcd', 786, 2.23, 'john', 70.2]  #  여기 number와 str이 모여있는 것이  atomm의 단위다.. 하나의 객체가 디고 객ㅊ체는 메서드 ㄱ(기능을 갖는다)
tinylist = [123, 'john']
lu = ['ass', 'ass']

# Creat : ls에 '100'을 추가 creat
def ls_create(slef)
ls.insert(2,'100')


# Read : ls 의 목록을 출력
print(ls)

# Update : ls와 tinyls 의 결합

ls1 = ls + tinylist

# Delete : ls 에서 786을 제거
ls.remove(786)

print(ls)
ls.index('abcd')



#------------------------------------------------
 *****************
# --- Data Type ---
# *****************
'''
'''

Python has Five standard types
scalar
    Numbers : int, float, complex
    String : str
vector : List, Tuple, Dictionary, Set
hello = 'hello'
print(hello)
print(hello[0])
print(hello[2:5])
print(hello[2:])
'''
'''

# List CRUD Example
ls = ['abcd', 786, 2.23, 'john', 70.2]
tinyls = [123, 'john']
# Create: ls 에 '100'을 추가 Create
# Read: ls 의 목록을 출력
# Update: ls와 tinyls 의 결합
# Delete: ls 에서 786을 제거

c






# Tuple CRUD Example
tp = ('abcd', 786, 2.23, 'john', 70.2)
tinytp = (123, 'john')
# Create: tp 에 '100'을 추가 Create

ls = list(tp)
ls.append(100)
tp = tuple(ls)
print(tp)


# Read: tp 의 목록을 출력
print(tp)

# Update: tp와 tinytp 의 결합
tp1 = tp+ tinytp

# Delete: tp 에서 786을 제거
ls = list(tp)
ls.remove(786)
tp = tuple(ls)
print(tp)


# dictionary CRUD Example
dt = {'abcd' : 786, 'john': 70.2}
tinydt = {'홍', '30세'}
# Create: dt 에 키값으로 'tom', 밸류로 '100'을 추가 Create
dt["tom"]=100
# Read: dt 의 목록을 출력
print(dt)

# Update: dt와 tinydt 의 결합
dt.update(tinydt)
print(dt)

# Delete: dt 에서 'abcd' 제거
del dt['abcd']

print(dt)

class Dic(object):
'''

class Basic(object):
    ls = ['abcd', 786, 2.23, 'john', 70.2]
    tinyls = [123, 'john']

    tp = ('abcd', 786, 2.23, 'john', 70.2)
    tinytp = (123, 'john')

    dt = {'abcd': 786, 'john': 70.2}
    tinydt = {'홍': '30세'}


    def ls_append(self):
        self.ls.append(100)
        print(self.ls)

    def ls_read(self):
        print(self.ls)

    def ls_combine(self):
        self.ls1 = self.ls + self.tinyls
        print(self.ls1)

    def ls_del(self):
        self.ls.remove(786)
        print(self.ls)


    def tp_append(self):
        ls = list(self.tp)
        ls.append(100)
        tp = tuple(ls)
        print(self.tp)

    def tp_read(self):
        print(self.tp)

    def tp_combine(self):
        self.tp1 = self.tp + self.tinytp
        print(self.tp1)

    def tp_del(self):
        ls = list(self.tp)
        ls.remove(786)
        tp = tuple(ls)
        print(self.tp)

    def dt_append(self):
        self.dt['atom'] = 100
        print(self.dt)

    def dt_read(self):
        print(self.dt)

    def dt_combine(self):
        self.dt.update(self.tinydt)
        print(self.dt)

    def dt_del(self):
        del self.dt['abcd']
        print(self.dt)






    @staticmethod
    def main():
        b = Basic()
        while 1:
            menu = input('List: 1.Create 2.Read 3.Update 4.Delete\n'
             'Tuple: 5.Create 6. Read 7.Update 8.Delete\n'
             'Dictionary: 9.Create 10. Read 11.Update 12.Delete\n: ')
            if menu == '1':
                b.ls_append()
            elif menu == '2':
                b.ls_read()
            elif menu == '3':
                b.ls_combine()
            elif menu == '4':
                b.ls_del()
            elif menu == '5':
                b.tp_append()
            elif menu == '6':
                b.tp_read()
            elif menu == '7':
                b.tp_combine()
            elif menu == '8':
                b.tp_del()
            elif menu == '9':
                b.dt_append()
            elif menu == '10':
                b.dt_read()
            elif menu == '11':
                b.dt_combine()
            elif menu == '12':
                b.dt_del()



Basic.main()
###이거가 왜 깔끔한거지??