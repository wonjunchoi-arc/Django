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
        return  this

    def preprocess(self,train, test) -> object: #train.csv
        service = self.service
        this = self.dataset
        #초기 모델 생성
        this.train =service.new_model(train) #./data/train.csv
        this.test = service.new_model(test)#./data/test.csv
        #불필요한 feature(Cabin, Ticket) 제거
        this = service.drop_feature(this, 'Cabin')
        this = service.drop_feature(this, 'Ticket')


        #norminal, ordinal로 정형화
        this = service.embarked_nominal(this)
        this = service.title_norminal(this)
        this = service.drop_feature(this, 'Name')
        this = service.gender_norminal(this)
        this = service.drop_feature(this, 'Sex')
        #불필요한 feature (Name)제거
        self.print_this(this)
        return this

    @staticmethod
    def print_this(this):
        print('<Type Check>')
        print(f'Train 의 type은 {type(this.train)}')
        print(f'Train 의 column은 {this.train.columns}')
        print(f'Train 의 상위 5개 데이터는 {this.train.head()}')
        print(f'Test 의 type은 {type(this.test)}')
        print(f'Test 의 column은 {this.test.columns}')
        print(f'Test 의 상위 5개 데이터는 {this.test.head()}')
        print(f'타입체크{type(this.train["Embarked"])}-----------------------------------------')

