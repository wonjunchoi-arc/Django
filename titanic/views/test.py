from titanic.models.service import Service
from titanic.models.dataset import Dataset


class Test(object):

    dataset = Dataset()
    service = Service()

    def __init__(self, fname):#train.csv
        self.entity = self.service.new_model(fname)

    def plot(self):
        this =self.entity
        print(f'Train 의 type은 {type(this)}')
        print(f'Train 의 column은 {type(this.columns)}')
        print(f'Train 의 상위 5개 데이터는 {this.head()}')
        print(f'Train 의 하위 5개 데이터는 {this.tail()}')