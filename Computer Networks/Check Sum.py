def sendData(data):
    scheck_sum = getCheckSum(data)
    comp = getCompliment(scheck_sum)
    boolean = receiveData(data, comp)
    if boolean:
        print('Receiver Checksum is equal to 0. Therefore,')
        print('STATUS: ACCEPTED')
    else:
        print('Receiver Checksum is not equal to 0. Therefore,')
        print('STATUS: ERROR DETECTED')


def receiveData(data, scheck_sum):
    empty_bit = '00000000'
    rcheck_sum = getCheckSum([getCheckSum(data),
                              scheck_sum, empty_bit, empty_bit])
    comp = getCompliment(rcheck_sum)
    # print(comp)
    if int(comp, 2) == 0:
        return True
    return False


def getCheckSum(lst, k=8):
    s = bin(int(lst[0], 2) + int(lst[1], 2)
            + int(lst[2], 2) + int(lst[3], 2))[2:]
    # print(s)
    if len(s) > k:
        x = len(s) - k
        s = bin(int(s[0:x], 2) + int(s[x:], 2))[2:]
    if len(s) < k:
        s = '0' * (k - len(s)) + s
    # print(s)
    return s


def getCompliment(s):
    s_cmp = []
    for i in s:
        if i == '1':
            s_cmp.append('0')
        else:
            s_cmp.append('1')
    return ''.join(s_cmp)


if __name__ == '__main__':
    bits = ['10011001', '11100010', '00100100', '10000100']
    # for i in range(1, 4 + 1):
    #     bits.append(input(f'Enter Part{i} : '))
    try:
        for part in bits:
            assert len(part) == 8
        sendData(bits)
    except AssertionError:
        print('Length of All Bit Parts Must Be 8')
