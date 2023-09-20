memory = [0] * 100
prompt1 = 'Enter the starting block & length of file : '
prompt2 = 'Enter the Blocks Already Allocated : '
lst = map(int, input(prompt2).split(' '))
for i in lst:
    memory[i] = 1
while True:
    start, length = map(int, input(prompt1).split())
    flag = 1 if 1 in memory[start:start + length + 1] else 0
    if flag == 0:
        memory[start:start + length + 1] = [1] * length
        for i in range(start, start + length + 1):
            print(i, '->', 1)
        print('The File is allocated to disk')
    else:
        print('Block already allocated')
    choice = input('Do u want to enter more files?(y:1/n:0) : ')
    if choice == '0':
        print('You Exited From Code Bye')
        break
