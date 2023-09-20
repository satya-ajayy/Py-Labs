string = input('Enter characters to be stuffed : ')
sd = input('Enter Starting Delimiter : ')
ed = input('Enter Ending Delimiter : ')

stuffed_str = [sd]
for i in string:
    if i in [sd, ed]:
        stuffed_str.extend([i, i])
    else:
        stuffed_str.append(i)
stuffed_str.append(ed)
print('Stuffed String : {}'.format(''.join(stuffed_str)))
