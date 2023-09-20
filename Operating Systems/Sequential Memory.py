memory = [0]*100
prompt = 'Enter the starting block & length of file : '

while True:
    start, length = map(int, input(prompt).split())
    flag = 1 if 1 in memory[start:start+length+1] else 0
    if flag == 0:
        memory[start:start + length + 1] = [1]*length
        print('The File is allocated to disk')
    else:
        print('Block already allocated')
    choice = input('Do u want to enter more files?(y:1/n:0) : ')
    if choice == '0':
        print('You Exited From Code Bye')
        break
