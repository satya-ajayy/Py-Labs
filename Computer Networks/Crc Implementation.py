def xor(a, b):
    result = []
    for i in range(1, len(b)):
        result.append('0' if a[i] == b[i] else '1')
    return ''.join(result)


def crc(divident, divisor):
    pick = len(divisor)
    tmp = divident[0: pick]
    while pick < len(divident):
        if tmp[0] == '1':
            tmp = xor(divisor, tmp) + divident[pick]
        else:
            tmp = xor('0' * pick, tmp) + divident[pick]
        pick += 1

    if tmp[0] == '1':
        tmp = xor(divisor, tmp)
    else:
        tmp = xor('0' * pick, tmp)
    return tmp


def main():
    print('-----MENU-----')
    print('1.Crc-12\n2.Crc-16\n3.Crc-ccip')
    choice = int(input('Enter Choice : '))
    d = {1: '1100000001111', 2: '11000000000000101', 3: '10001000000100001'}
    divisor = d[choice]
    data = input('Enter The Data : ')
    print(f'[DATA] : {data}')
    print(f'[DIVISOR] : {divisor}')
    csum = crc(data + '0' * (len(divisor) - 1), divisor)
    print(f'[CHECK SUM] : {csum}')
    print(f'[FINAL DATA] : {data + csum}')


if __name__ == '__main__':
    main()
