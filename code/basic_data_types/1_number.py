class Number(object):
    def __bool__(self):
        return False

    def __nonzero__(self):
        return self.__bool__()


print(bool(Number()))
