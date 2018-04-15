class CustomException(Exception):
    pass


def test_exception():
    while True:
        try:
            x = int(input('Enter the first number:'))
            y = int(input('Enter the second number:'))

            print(x / y)
        except Exception as e:
            # 处理这些异常
            print(e)
        else:
            print('no exceptions')
            break
        finally:
            print("over")


if __name__ == '__main__':
    test_exception()
