class A(object):
    def m1(self, num):
        print('self:', self)

    @classmethod
    def m2(cls, num):
        print('cls:', cls)

    @staticmethod
    def m3(num):
        pass


if __name__ == '__main__':
    a = A()
    a.m1(1)
    A.m1(a, 1)
    print(A.m1)
    print(a.m1)

    A.m2(2)
    print(A.m2)
    print(a.m2)

    A.m3(3)
    print(A.m3)
    print(a.m3)
