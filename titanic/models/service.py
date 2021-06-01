from titanic.models.dataset import Dataset
import pandas as pd


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
    def create_label(this):
        return this.train['Survived']

    @staticmethod
    def drop_feature(this, feature)->object:#필요없는 데이터 컬럼값은 지워버려라
        this.train = this.train.drop([feature], axis=1)
        this.test = this.test.drop([feature], axis=1)
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
            title_mapping = {'Mr': 1, 'Miss': 2, 'Mrs': 3, 'Master': 4, 'Royal': 5, 'Rare': 6}
            dataset['Title'] = dataset['Title'].fillna(0)
            dataset['Title'] = dataset['Title'].map(title_mapping)
            # dataset['Title'] = dataset['Title'].map({'Mr': 1, 'Miss': 2, 'Mrs': 3, 'Master': 4, 'Royal': 5, 'Rare': 6})
            # dataset['Title'] = dataset.fillna({'Title': 0})

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
        return this

    @staticmethod
    def create_k_fold(thois)->object:
        return