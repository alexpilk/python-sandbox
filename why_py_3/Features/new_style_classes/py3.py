class Base:

    def __init__(self):
        print('Base')


class A(Base):

    def __init__(self):
        print('A')
        super().__init__()


class B(Base):

    def __init__(self):
        print('B')
        super().__init__()


class C(A, B):
    pass


C()
