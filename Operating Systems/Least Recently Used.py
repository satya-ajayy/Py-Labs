capacity = int(input('Enter no.of frames : '))
f, fault, st, pf = [], 0, [], 'No'
string = 'Enter the reference string : '
s = list(map(int, input(string).split()))
string = 'String '
for i in range(capacity):
    string += f' Frame{i + 1} '
print(string + ' Fault')
for i in s:
    if i not in f:
        if len(f) < capacity:
            f.append(i)
            st.append(len(f) - 1)
        else:
            ind = st.pop(0)
            f[ind] = i
            st.append(ind)
        pf = 'Yes'
        fault += 1
    else:
        st.append(st.pop(st.index(f.index(i))))
        pf = 'No'
    print(f'  {i}', end='')
    for val in f:
        print(f'\t\t{val}', end='')
    for _ in range(capacity - len(f)):
        print('\t\t ', end='')
    print(f'\t\t{pf}')
print('Total requests :', len(s))
print('Total Page Faults :', fault)
print('Fault Rate :', round(fault / len(s) * 100, 2))
