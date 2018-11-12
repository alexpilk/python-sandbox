class A:

    def __init__(self):
        print('A')


class B(A):

    def __init__(self):
        print('B')
        super(B, self).__init__()


class C:

    def __init__(self):
        print('C')


class D(B, C):

    def __init__(self):
        print('D')
        super(D, self).__init__()


D()
