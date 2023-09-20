string = input('Enter bits to be stuffed : ')
sd = ed = '01111110'
string = string.replace('11111', '11111O')
stuffed_str = sd + ' ' + string + ' ' + ed
print(f'Stuffed String : {stuffed_str}')
