class TwoLevelDirectory:
    def __init__(self):
        self.dic = {}
        Directory = input('Enter Directory Name : ')
        self.dic[Directory] = []
        print(f'Directory {Directory} Created SuccessFully')

    @staticmethod
    def showMenu():
        print('------MENU------')
        print('1) To Add a Directory')
        print('2) To Add a File')
        print('3) To Delete a File')
        print('4) To Show Files')
        print('5) Enter -1 to Exit')

    def showFiles(self):
        for dir_name in self.dic:
            print(f'Directory -> {dir_name}', end=' ')
            print('Files ->', end=' ')
            print(', '.join(self.dic[dir_name]))

    def addDirectory(self):
        dir_name = input('Enter Directory Name : ')
        if dir_name in self.dic:
            print('Directory Already Exists')
        else:
            self.dic[dir_name] = []
            print(f'Directory {dir_name} Created SuccessFully')

    def addFile(self):
        dir_name = input('Enter Directory Name : ')
        if dir_name in self.dic:
            f_name = input('Enter Filename : ')
            if f_name in self.dic[dir_name]:
                print('File Already Exists')
            else:
                self.dic[dir_name].append(f_name)
                print(f'File {f_name} Created SuccessFully')
        else:
            print('Directory not Found !!')

    def deleteFiles(self, dir_name, f_name):
        if dir_name in self.dic:
            try:
                self.dic[dir_name].remove(f_name)
                print(f'{f_name} Deleted from {dir_name}')
            except ValueError:
                print('File not Found !!')
        else:
            print('Directory not Found !!')

    def implement(self):
        self.showMenu()
        while True:
            ch = input('Enter Your Choice : ')
            if ch == '-1':
                print('You Exited From The Program Bye')
                break
            elif ch == '1':
                self.addDirectory()
            elif ch == '2':
                self.addFile()
            elif ch == '3':
                dir_name = input('Enter Directory Name : ')
                f_name = input('Enter File name to Delete : ')
                self.deleteFiles(dir_name, f_name)
            elif ch == '4':
                self.showFiles()
            else:
                print('Choose From 1-4')


if __name__ == '__main__':
    obj = TwoLevelDirectory()
    obj.implement()
