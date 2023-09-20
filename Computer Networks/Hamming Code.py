class HammingCode:
    def __init__(self, Even=True):
        self.parity = Even

    def Helper(self, lst):
        if lst.count('1') % 2 != 0:
            return '1' if self.parity else '0'
        else:
            return '0' if self.parity else '1'

    def GetHammingCode(self, data):
        p1 = self.Helper([data[0], data[2], data[3], data[5], data[6]])
        p2 = self.Helper([data[0], data[1], data[3], data[4], data[6]])
        p4 = self.Helper([data[3], data[4], data[5]])
        p8 = self.Helper([data[0], data[1], data[2]])
        bits = ''.join(data)
        # print(p1, p2, p4, p8)
        Hcode = ''.join([*data[:3], p8, *data[3:6], p4,  data[-1], p2, p1])
        print(f'Hamming Code For {bits} is {Hcode}')

    def IsCorrect(self, Hcode):
        l = list(Hcode)
        p1 = self.Helper([l[0], l[2], l[4], l[6], l[8], l[10]])
        p2 = self.Helper([l[0], l[1], l[4], l[5], l[8], l[9]])
        p4 = self.Helper([l[4], l[5], l[6], l[7]])
        p8 = self.Helper([l[0], l[1], l[2], l[3]])
        error = eval('0b' + ''.join([p8, p4, p2, p1]))
        if error == 0:
            print('Entered Hamming Code is Correct')
        else:
            l[-error] = '0' if l[-error] == '1' else '1'
            print('Entered Hamming Code is Wrong')
            print('Corrected Code :', ''.join(l))


obj = HammingCode(Even=True)
obj.GetHammingCode('1011001')
obj.IsCorrect('10101101110')
