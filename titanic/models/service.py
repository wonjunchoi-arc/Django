from titanic.models.dataset import Dataset
import pandas as pd
import  numpy as np
from sklearn.svm import SVC
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
##여기서 K는 CONUting의 의미를 지닌다.


class Service(object):

    dataset = Dataset()

    def new_model(self, payload) -> object:
        this = self.dataset
        this.context = './data/'
        this.fname = payload#train.csv
        return pd.read_csv(this.context + this.fname) #./data/train.csv

    #여기서 부터 알고리즘이다.
    @staticmethod
    def crate_train(this)->object:  #여기서 의 this
        return this.train.drop('Survived', axis =1) #여기서의 this가 다르다는 것


    @staticmethod
    def create_label(this):  # w지도학습에 대한 답을 만들어내 ㄴ것이다.
        return this.train['Survived']

    @staticmethod
    def drop_feature(this, *feature)->object:#필요없는 데이터 컬럼값은 지워버려라
        for i in feature:
            this.train = this.train.drop([i], axis=1)
            this.test = this.test.drop([i], axis=1)

        return this

    #self 에서 불러온 데이터들은 순서가 어떻든 전혀 상관없이 독립적이다. 하지만

    ##아래의 staticmethod는 전부 feature이며 이는 기존의 데이터 값과 다르게 변경할 수 있다.

    # @staticmethod
    # def embarked_nominal(this)->object :   ###
    #     this.train = this.train.fill({'Embarked':'S'})   ## 마지막에 기록을 하지 못하고 탄 사람들은 Soth햄튼 출신이라고 생각하는 것
    #
    #     # 사우스 햄튼은 1로 치환
    #     return this.train

    @staticmethod
    def embarked_nominal(this) -> object:  ###
        this.train = this.train.fillna({'Embarked': 'S'})  ## 마지막에 기록을 하지 못하고 탄 사람들은 Soth햄튼 출신이라고 생각하는 것
        this.test = this.test.fillna({'Embarked':'S'})
        this.train['Embarked'] = this.train['Embarked'].map({'S':1, 'C':2, 'Q':3})
        this.test['Embarked'] = this.test['Embarked'].map({'S': 1, 'C': 2, 'Q': 3})
        return this


    @staticmethod
    def fare_ordinal(this) -> object:
        this.test['Fare']= this.test['Fare'].fillna(1)
        print(f'Test의 null {this.test[this.test.isna().any(axis=1)]}')
        this.train['FareBand'] = pd.qcut(this.train['Fare'], 4)
        # quct 으로 bins 값 설정 {this.train["FareBand"].head(10)}
        # bins = list(pd.qcut(this.train['Fare'], 4, retbins=True))
        bins = [-1, 8, 15, 31, np.inf]
        this.train = this.train.drop(['FareBand'], axis=1)
        for these in this.train, this.test:
            these['FareBand'] = pd.cut(these['Fare'], bins=bins, labels=[1, 2, 3, 4])  # {[labels]:[bins]}
        this.test['FareBand']= this.test['FareBand'].fillna(1)

        return this

    @staticmethod
    def fare_band_ordinal(this)->object:
        return this

    @staticmethod
    def title_norminal(this)->object:
        combine = [this.train, this.test]
        for dataset in combine:
            dataset['Title'] = dataset.Name.str.extract('([A-Za-z]+)\.', expand=False)
        for dataset in combine:
            dataset['Title'] = dataset['Title'].replace(
                ['Capt', 'Col', 'Don', 'Dr', 'Major', 'Rev', 'Jonkheer', 'Dona'], 'Rare')
            dataset['Title'] = dataset['Title'].replace(['Countess', 'Lady', 'Sir'], 'Royal')
            dataset['Title'] = dataset['Title'].replace('Mlle', 'Mr')
            dataset['Title'] = dataset['Title'].replace('Ms', 'Miss')
            dataset['Title'] = dataset['Title'].replace('Mme', 'Rare')
            # title_mapping = {'Mr': 1, 'Miss': 2, 'Mrs': 3, 'Master': 4, 'Royal': 5, 'Rare': 6}
            # dataset['Title'] = dataset['Title'].fillna(0)
            # dataset['Title'] = dataset['Title'].map(title_mapping)
            dataset['Title'] = dataset['Title'].map({'Mr': 1, 'Miss': 2, 'Mrs': 3, 'Master': 4, 'Royal': 5, 'Rare': 6})
            dataset['Title'] = dataset['Title'].fillna(0) #dataset.fillna({'Title': 0})


            #위에 처럼 없는 걸 넣으면 새로운 항목이 생긴다.   ##정규표현시
        return this

    @staticmethod
    def gender_norminal(this)->object:
        combine = [this.train, this.test]
        for dataset in combine:
            dataset['Gender'] = dataset['Sex']

        for dataset in combine:
            gender_mapping = {'male':0, 'female':1}
            dataset['Gender'] = dataset['Gender'].map(gender_mapping)

        return this

    @staticmethod
    def age_ordinal(this)->object:
        combine = [this.train,this.test]
        bins = [-1, 0, 5, 12, 18, 24, 35, 60, np.inf] #값이 아니라 구간을 나타냄
        labels = ['Unknown', 'Baby', 'Child', 'Teenager', 'Student', 'Young Adult', 'Adult', 'Senior']
        age_title_mapping = { 'Unknown': 0 , 'Baby': 1, 'Child': 2, 'Teenager': 3, 'Student':4 , 'Young Adult': 5, 'Adult': 6, 'Senior' :7 }

        for i in combine:
            i['Age'] = i['Age'].fillna(-0.5)
            i['AgeGroup'] = pd.cut(i['Age'], bins=bins, labels=labels)  ## bin 과 label로 딕셔너리를 만든다는 것.
            i['AgeGroup'] = i['AgeGroup'].map(age_title_mapping)



        return this

    @staticmethod
    def create_k_fold(this)->object:
        return KFold(n_splits=10, shuffle=True, random_state=0) ##우리가 만들것을 10조각으로 ,한번 냈던것도 다시

    def accuracy_by_svm(self,this):
        score = cross_val_score(SVC(),
                                this.train,
                                this.label,
                                cv=KFold(n_splits=10,
                                         shuffle=True,
                                        random_state=0),
                                n_jobs=1,
                                scoring='accuracy')
        return round(np.mean(score)* 100, 2)