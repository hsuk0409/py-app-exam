class Book:

    def printData(self):
        print('제목: ', self.title)
        print('가격: ', self.price + '원')

    def __init__(self, title, price):
        self.price = price
        self.title = title
        print('책 개체 생성!')
