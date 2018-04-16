class Bird:
    def __init__(self):
        self.hungry = True

    def eat(self):
        if self.hungry:
            print("aaaah...")
            self.hungry = False
        else:
            print("No, thanks...")


class SongBird(Bird):
    def __init__(self):
        # Bird.__init__(self)
        super(SongBird, self).__init__()
        self.sound = 'squawk'

    def sing(self):
        print(self.sound)


if __name__ == "__main__":
    foo = SongBird()
    foo.eat()
    foo.eat()
