class BuiltinFunctionDemo:
    """
    内置函数Demo
    """

    def __init__(self):
        self._name = None

    """
    def get_name(self):
        return self._name

    def set_name(self, value):
        self._name = value

    def del_name(self):
        del self._name

    name = property(get_name, set_name, del_name, "姓名")
    """

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @name.deleter
    def name(self):
        del self._name

test = BuiltinFunctionDemo()
test.name = 'anyu'
print(test.name)