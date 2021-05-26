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
'''

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
