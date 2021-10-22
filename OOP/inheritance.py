class A:
    def __init__(self):
        print('init 1')

    def feature1(self):
        print('feature 1')

class B(A):
    def __init__(self):
        print('init 2')

    def feature2(self):
        print('feature 2')
        super().feature1()

a=B()
a.feature2()