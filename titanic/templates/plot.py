from titanic.models.dataset import Dataset
from titanic.models.service import Service
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import seaborn as sns
rc('font', family = font_manager.FontProperties(fname='C:/Windows/Fonts/H2GTRE.ttf').get_name())


class Plot(object):

    dataset: object = Dataset()
    service: object = Service()

    def __init__(self, fname):
        self.entity = self.service.new_model(fname)

    def draw_survived_dead(self):
        this = self.entity
        # print(f'The data type of Train is {type(this.train)}.')
        # print(f'Columns of Train is {this.train.columns}.')
        # print(f'The top 5 superior data are {this.train.head}.')
        # print(f'The top 5 inferior data are {this.train.tail}.')

        f, ax = plt.subplots(1, 2, figsize = (20, 8))
        this['Survived'].value_counts().plot.pie(explode=[0, 0.1], autopct='%1.1f%%', ax=ax[0], shadow=True)
        ax[0].set_title('0.사망자 vs 1.생존자')
        ax[0].set_ylabel('')
        ax[1].set_title('0.사망자 vs 1.생존자')
        sns.countplot('Survived', data=this, ax=ax[1])
        plt.show()


    def draw_pclass(self):
        this = self.entity
        this['생존결과'] = this['Survived'] \
            .replace(0, '사망자').replace(1, '생존자')
        this['Pclass'] = this['Pclass'].replace(1, '1등석').replace(2, '2등석').replace(3, '3등석')
        sns.countplot(data=this, x='좌석등급',  hue='생존결과')
        plt.show()
        # f, ax = plt.subplots(1, 2, figsize=(18, 8))
        # this['Pclass'].value_counts()
        # ax[0].set_title('0.이코노미, 1,first, 2.second')
        # ax[0].set_ylabel('')
        # ax[1].set_title('0.이코노미, 1,first, 2.second')
        # sns.countplot('Pclass', data=this, ax=ax[1])


    def draw_sex(self):
        this = self.entity
        f, ax = plt.subplots(1, 2, figsize = (18, 8))
        this['Survived'][this['Sex']=='male'].value_counts().plot.pie(explode=[0, 0.1], autopct='%1.1f%%', ax=ax[0], shadow=True)
        this['Survived'][this['Sex']=='female'].value_counts().plot.pie(explode=[0, 0.1], autopct='%1.1f%%', ax=ax[0], shadow=True)
        ##생존자 중에서 성별이 ~~인 경우에 대하여


        ax[0].set_title('남성의 생존비율[0.사망자 vs 1.사망자]')
        ax[0].set_title('여성의 생존비율[0.사망자 vs 1.사망자]')
        plt.show()


    def draw_enbarked(self):
        this = self.entity
        this['승선한구'] = this['Embarked'].replace("C", '쉘버그').replace("C", '사우스햄튼').replace("C", '퀸즈타운')

