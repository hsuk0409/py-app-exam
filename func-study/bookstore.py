class Book:

    def setData(self, title, price):
        self.title = title
        self.price = price

    def printData(self):
        print('제목: ', self.title)
        print('가격: ', self.price + '원')

    def __init__(self):
        print('책 개체 생성!')
