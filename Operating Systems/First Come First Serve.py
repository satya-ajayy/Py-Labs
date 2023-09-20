import tabulate as tb

n = int(input('Enter No.Of Processes (Ideal CPU): '))
brst_tyms, arrv_tyms = {}, {}
for i in range(1, n + 1):
    brst_tyms[f'P{i}'] = int(input(f'Enter Burst Time For Prc{i}   : '))
    arrv_tyms[f'P{i}'] = int(input(f'Enter Arrival Time For Prc{i} : '))
arrv_tyms = {k: v for k, v in sorted(arrv_tyms.items(), key=lambda x: x[1])}
tym = arrv_tyms[list(arrv_tyms.keys())[0]]
idle = 0
# print(tym)
cmplt_tyms = {}
for key in arrv_tyms.keys():
    if arrv_tyms[key] > tym:
        idle += arrv_tyms[key] - tym
    tym += (brst_tyms[key] + idle)
    idle = 0
    cmplt_tyms[key] = tym

trn_around_tyms, wting_tyms = {}, {}
for i in range(1, n+1):
    trn_around_tyms[f'P{i}'] = cmplt_tyms[f'P{i}'] - arrv_tyms[f'P{i}']
    wting_tyms[f'P{i}'] = trn_around_tyms[f'P{i}'] - brst_tyms[f'P{i}']


header = ['Process', 'Arrival Tym', 'Burst Tym', 'Cmpltn Tym', 'Trn Around Tym', 'Waiting Tym']
helper = []
trn_around_time = 0
waiting_time = 0
for i in range(1, n + 1):
    temp = [f'P{i}', arrv_tyms[f'P{i}'], brst_tyms[f'P{i}'], cmplt_tyms[f'P{i}'],
            trn_around_tyms[f'P{i}']]
    trn_around_time += trn_around_tyms[f'P{i}']
    temp.append(wting_tyms[f'P{i}'])
    waiting_time += wting_tyms[f'P{i}']
    helper.append(temp)
print(tb.tabulate(helper, headers=header, tablefmt='pretty'))
print('Total Turn Around Time :', trn_around_time)
print('Average Turn Around Time :', trn_around_time / n)
print('Total Waiting Time :', waiting_time)
print('Average Waiting Time :', waiting_time / n)
