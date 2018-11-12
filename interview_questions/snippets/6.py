class A:

    def __init__(self):
        print('A')
        super(A, self).__init__()


class B(A):

    def __init__(self):
        print('B')
        super(B, self).__init__()


class C:

    def __init__(self):
        print('C')
        super(C, self).__init__()


class D(B, C):

    def __init__(self):
        print('D')
        super(D, self).__init__()


D()
