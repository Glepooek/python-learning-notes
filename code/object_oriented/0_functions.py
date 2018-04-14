class StoreName:
    """
    store the person's name
    """
    storage = {}

    def init(self):
        self.storage['first'] = {}
        self.storage['middle'] = {}
        self.storage['last'] = {}

    def lookup(self, label: str, name: str) -> list:
        if self.storage:
            return self.storage[label].get(name)

    def store(self, *full_names: str):
        for full_name in full_names:
            names = full_name.split()
            if len(names) == 2:
                names.insert(1, '')
            labels = 'first', 'middle', 'last'
            for label, name in zip(labels, names):
                people = self.lookup(label, name)
                if people:
                    people.append(full_name)
                else:
                    self.storage[label][name] = [full_name]


def multiplier(factor):
    temp = 5

    def multiply_by_factor(number):
        nonlocal temp
        temp += 2
        print(temp)
        return factor * number

    return multiply_by_factor


def factorial(n: int) -> int:
    """
    阶乘
    :param n:
    :return:
    """
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def power(x, n):
    """
    整数幂
    :param x:
    :param n:
    :return:
    """
    if n == 0:
        return 1
    else:
        return x * power(x, n - 1)


if __name__ == "__main__":
    store_name = StoreName()
    store_name.init()
    store_name.store('an yu', 'Robin Hood', 'Han Solo')
    print(store_name.storage)

    double = multiplier(1)
    print(double(5))
    print(double(5))

    print(factorial(5))
    print(power(0, 0))
