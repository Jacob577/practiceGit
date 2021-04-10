from Test1 import Test1
class Main:
    def __init__(self, name):
        self.name = str(name)

    def run(self):
        print("Your name is {}".format(self.name))


if __name__ == '__main__':
    Main(name="Jacob och Lucas").run()
    Test1().bugg123()



