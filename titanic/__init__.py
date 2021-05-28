from titanic.views.controller import Contoller



if __name__ == '__main__':
    controller = Contoller()
    while 1:
        menu = input('0.Exit 1.preprocess')
        if menu == '0':
            break
        elif menu == '1':
            controller.preprocess('train.csv')
        else:
            continue





#1번에 모델 출력 컨트롤러만 가져오기