class SingleLevelDirectory:
    def __init__(self):
        self.dic = {}
        self.Directory = input('Enter Directory Name : ')
        self.dic[self.Directory] = []

    @staticmethod
    def showMenu():
        print('-----MENU-----')
        print('1) To Add a File')
        print('2) To Add Multiple Files')
        print('3) To Delete a File')
        print('4) To Show Files')
        print('5) Enter -1 to Exit')

    def showFiles(self):
        print(f'Directory -> {self.Directory}', end=' ')
        print('Files ->', end=' ')
        print(', '.join(self.dic[self.Directory]))

    def addFiles(self, n):
        for i in range(n):
            f_name = input('Enter Filename : ')
            if f_name in self.dic[self.Directory]:
                print('File Already Exists')
            else:
                self.dic[self.Directory].append(f_name)

    def deleteFiles(self, f_name):
        try:
            self.dic[self.Directory].remove(f_name)
            print(f'{f_name} Deleted from {self.Directory}')
        except ValueError:
            print('File not Found !!')

    def implement(self):
        self.showMenu()
        while True:
            ch = input('Enter Your Choice : ')
            if ch == '-1':
                print('You Exited From The Program Bye')
                break
            elif ch == '1':
                self.addFiles(1)
            elif ch == '2':
                n = int(input('Enter No.of Files : '))
                self.addFiles(n)
            elif ch == '3':
                f_name = input('Enter File name to Delete : ')
                self.deleteFiles(f_name)
            elif ch == '4':
                self.showFiles()
            else:
                print('Choose From 1-4')


if __name__ == '__main__':
    obj = SingleLevelDirectory()
    obj.implement()
