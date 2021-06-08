import pandas as pd

from titanic.models.dataset import Dataset
from titanic.models.service import Service
from sklearn.ensemble import RandomForestClassifier



class Controller(object):

    dataset = Dataset()
    service = Service()

    def modeling(self, train, test):
        service =self.service
        this = self.preprocess(train, test)
        this.label =service.create_label(this)
        this.train = service.crate_train(this)

        return this

    def learning(self, train, test) -> object:
        this = self.modeling(train, test)
        print(f'사이킷런의 SVC 알고리즘 정확도{self.service.accuracy_by_svm(this)} %')

    def submit(self,train, test):
        this = self.modeling(train,test)
        clf = RandomForestClassifier()
        clf.fit(this.train, this.label)
        prediction = clf.predict(this.test)
        pd.DataFrame({'PassengerId': this.id, 'Survived': prediction}).to_csv('./data/submission.csv', index=False)


    def preprocess(self,train, test) -> object: #train.csv
        service = self.service
        this = self.dataset
        #초기 모델 생성
        this.train =service.new_model(train) #./data/train.csv
        this.test = service.new_model(test)#./data/test.csv
        this.id =this.test['PassengerId']
        #불필요한 feature(Cabin, Ticket) 제거
        # this = service.drop_feature(this,'Ticket','Cabin')## 둘중에 하나만 날라가ㅁ

        #norminal, ordinal로 정형화
        this = service.embarked_nominal(this)
        this = service.title_norminal(this)
        this = service.gender_norminal(this)
        this = service.age_ordinal(this)
        this = service.drop_feature(this, 'Ticket','Cabin','Name', 'Sex','Age')
        this = service.fare_ordinal(this)
        #불필요한 feature (Name)제거
        self.print_this(this)
        return this

    @staticmethod
    def print_this(this):
        print('*'*100)
        print('<Type Check>')
        print(f'1.Train 의 type은\n {type(this.train)}')
        print(f'2.Train 의 column은\n {this.train.columns}')
        print(f'3.Train 의 상위 1개 행\n {this.train.head(1)}')
        print(f'4.Train 의 null 의 갯수\n {this.train.isnull().sum()}개')
        print(f'5.Test 의 type은\n {type(this.test)}')
        print(f'6.Test 의 column은\n {this.test.columns}')
        print(f'7.Test 의 상위 1개 데이터는\n {this.test.head(1)}')
        print(f'8.Test 의 null 의 갯수\n {this.test.isnull().sum()}개')
        print(f'타입체크{type(this.train["Embarked"])}-----------------------------------------')

