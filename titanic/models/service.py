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
    def crate_train(this)->object:
        return this.train.drop('Survived', axis =1)


    @staticmethod
    def create_label(this):
        return this.train['Survived']

    @staticmethod
    def drop_feature(this, feature)->object:#필요없는 데이터 컬럼값은 지워버려라
        this.train = this.train.drop([feature], axis=1)
        this.train = this.test.drop([feature], axis=1)
        return this