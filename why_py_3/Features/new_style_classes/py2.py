class Base(object):

    def __init__(self):
        print('Base')


class A(Base):

    def __init__(self):
        print('A')
        super(A, self).__init__()


class B(Base):

    def __init__(self):
        print('B')
        super(B, self).__init__()


class C(A, B):
    pass


C()
