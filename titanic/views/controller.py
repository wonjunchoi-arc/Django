from titanic.models.dataset import Dataset
from titanic.models.service import Service


class Controller(object):

    dataset = Dataset()
    service = Service()

    def modeling(self, train, test):
        service =self.service
        this = self.preprocess(train, test)
        this.label =service.create_label(this)
        this.train = service.crate_train(this)

    def preprocess(self,train, test) -> object: #train.csv
        service = self.service
        this = self.dataset
        this.train =service.new_model(train) #./data/train.csv
        this.test = service.new_model(test)#./data/test.csv
        print(f'Train 의 type은 {type(this.train)}')
        print(f'Train 의 column은 {this.train.columns}')
        print(f'Test 의 상위 5개 데이터는 {type(this.test)}')
        print(f'Test 의 하위 5개 데이터는 {this.test.columns}')
        return this
