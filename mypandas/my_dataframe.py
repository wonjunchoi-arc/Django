class MyDataFrame(object):
    def __init__(self, column, index):
        self.column = column
        self.index = index


    @staticmethod
    def main():
        df = MyDataFrame(10, 3)